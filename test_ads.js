// Ad slots in a real browser (Playwright + Chromium). Run after building: node test_ads.js
// adsbygoogle.js is replaced by a stub that never fills anything.
//  - Without data-ad-status="filled": no ad slot is visible – no height, no margins, no “Advertisement” label.
//  - With data-ad-status="filled": the slot shows, label included, and keeps its 150 px gap to controls.
"use strict";
const http = require("http");
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const DOCS = path.join(__dirname, "docs");
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".webp": "image/webp", ".png": "image/png" };

const results = [];
const expect = (cond, label) => results.push({ ok: !!cond, label });

const slots = page => page.$$eval(".ad", boxes => boxes.map(b => {
  const cs = getComputedStyle(b);
  if (cs.display === "none") return null;                       // slot not meant for this screen width
  const height = b.getBoundingClientRect().height;
  return { kind: b.dataset.ad, height, top: parseFloat(cs.marginTop), bottom: parseFloat(cs.marginBottom),
           label: height > 0 && getComputedStyle(b, "::before").display !== "none" };
}).filter(s => s && (s.height > 0 || s.top > 0 || s.bottom > 0 || s.label)));

(async () => {
  const server = http.createServer((req, res) => {
    let file = path.join(DOCS, decodeURIComponent(req.url.split("?")[0]));
    if (file.endsWith(path.sep)) file += "index.html";
    if (!file.startsWith(DOCS) || !fs.existsSync(file)) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { "content-type": TYPES[path.extname(file)] || "application/octet-stream" });
    res.end(fs.readFileSync(file));
  });
  await new Promise(r => server.listen(0, "127.0.0.1", r));
  const origin = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch();

  const open = async (width, url) => {
    const context = await browser.newContext({ viewport: { width, height: 900 } });
    await context.route(/^https?:\/\/(?!127\.0\.0\.1)/, route => route.fulfill({ status: 200, contentType: "text/javascript", body: "/* stub: no ad */" }));
    const page = await context.newPage();
    const errors = [];
    page.on("pageerror", e => errors.push(e.message));
    await page.goto(origin + url);
    await page.waitForFunction(() => document.querySelector(".ad.on ins.adsbygoogle"));
    return { context, page, errors };
  };

  for (const width of [390, 1366]) {
    for (const url of ["/", "/weekly-planner.html", "/print-at-actual-size.html"]) {
      const { context, page, errors } = await open(width, url);
      const visible = await slots(page);
      expect(visible.length === 0, `${width}px ${url}: no empty ad slot visible ${visible.length ? JSON.stringify(visible) : ""}`);
      expect(errors.length === 0, `${width}px ${url}: no JS errors ${errors.join(" | ")}`);
      await context.close();
    }
  }

  {
    const { context, page } = await open(1366, "/weekly-planner.html");
    await page.$$eval(".ad.on ins.adsbygoogle", list => list.forEach(i => i.setAttribute("data-ad-status", "filled")));
    const shown = Object.fromEntries((await slots(page)).map(s => [s.kind, s]));
    expect(shown.rect && shown.rect.height >= 250 && shown.rect.label, "filled: rectangle shows with its label");
    expect(shown.rect && shown.rect.top === 150 && shown.rect.bottom === 120, "filled: rectangle keeps the 150 px gap");
    expect(shown.superbanner && shown.superbanner.height >= 90 && shown.superbanner.bottom === 28, "filled: superbanner shows with its normal margin");
    expect(await page.$$eval(".ad.on", list => list.every(b => b.classList.contains("ad--served"))), "filled: fallback class .ad--served set");
    await context.close();
  }
  {
    const { context, page } = await open(390, "/weekly-planner.html");
    await page.$$eval(".ad.on ins.adsbygoogle", list => list.forEach(i => i.setAttribute("data-ad-status", "unfilled")));
    expect((await slots(page)).length === 0, "390px unfilled: everything stays collapsed");
    await page.$eval('.ad.on[data-ad="rect"] ins.adsbygoogle', i => i.setAttribute("data-ad-status", "filled"));
    const shown = await slots(page);
    expect(shown.length === 1 && shown[0].kind === "rect", "390px: only the filled slot appears");
    await context.close();
  }

  await browser.close();
  server.close();
  for (const r of results) console.log(`${r.ok ? "ok  " : "FAIL"} ${r.label}`);
  const failed = results.filter(r => !r.ok).length;
  console.log(failed ? `Ad slot test: ${failed} failed` : `Ad slot test: ${results.length} checks OK`);
  process.exit(failed ? 1 : 0);
})();
