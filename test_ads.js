// Ad slots in a real browser (Playwright + Chromium). Run after building: node test_ads.js
// adsbygoogle.js is replaced by a stub that never fills anything.
//  - Without data-ad-status: the <ins class="adsbygoogle"> stays visible and unclipped (AdSense help 10762946),
//    width > 0, no overflow:hidden – but no “Advertisement” label, no min-height, no margins.
//  - "unfilled": the ins is display:none (Google's pattern), no extras.
//  - "filled" / "unfill-optimized": the slot shows, label included, and keeps its 150 px gap to controls.
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

const units = page => page.$$eval(".ad.on ins.adsbygoogle", list => list.map(i => {
  const b = i.parentElement, ci = getComputedStyle(i), cb = getComputedStyle(b), ri = i.getBoundingClientRect();
  return { kind: b.dataset.ad, display: ci.display, vis: ci.visibility, width: ri.width, insH: ri.height,
           boxH: b.getBoundingClientRect().height, overflow: cb.overflowX + "/" + cb.overflowY, boxVis: cb.visibility,
           label: getComputedStyle(b, "::before").display !== "none", gap: parseFloat(cb.marginTop) + parseFloat(cb.marginBottom), minH: cb.minHeight };
}));
const unclipped = l => l.length > 0 && l.every(u => u.display !== "none" && u.vis === "visible" && u.boxVis === "visible" && u.width > 0 && u.overflow === "visible/visible" && u.boxH >= u.insH);

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
      const l = await units(page);
      expect(unclipped(l), `${width}px ${url}: without status the ins stays visible and unclipped ${unclipped(l) ? "" : JSON.stringify(l)}`);
      expect(l.every(u => !u.label && u.gap === 0 && u.minH === "0px"), `${width}px ${url}: without status no label, no margins, no min-height`);
      const visible = await slots(page);
      expect(visible.every(s => !s.label && s.top === 0 && s.bottom === 0), `${width}px ${url}: no extras visible`);
      expect(errors.length === 0, `${width}px ${url}: no JS errors ${errors.join(" | ")}`);
      await context.close();
    }
  }

  for (const status of ["filled", "unfill-optimized"]) {
    const { context, page } = await open(1366, "/weekly-planner.html");
    await page.$$eval(".ad.on ins.adsbygoogle", (list, st) => list.forEach(i => i.setAttribute("data-ad-status", st)), status);
    const shown = Object.fromEntries((await slots(page)).map(s => [s.kind, s]));
    expect(shown.rect && shown.rect.height >= 250 && shown.rect.label, `${status}: rectangle shows with its label`);
    expect(shown.rect && shown.rect.top === 150 && shown.rect.bottom === 120, `${status}: rectangle keeps the 150 px gap`);
    expect(shown.superbanner && shown.superbanner.height >= 90 && shown.superbanner.bottom === 28 && shown.superbanner.label, `${status}: superbanner shows with label and its normal margin`);
    expect(await page.$$eval(".ad.on", list => list.every(b => b.classList.contains("ad--served"))), `${status}: fallback class .ad--served set`);
    await context.close();
  }
  {
    const { context, page } = await open(390, "/weekly-planner.html");
    await page.$$eval(".ad.on ins.adsbygoogle", list => list.forEach(i => i.setAttribute("data-ad-status", "unfilled")));
    expect((await units(page)).every(u => u.display === "none" && !u.label && u.boxH === 0), "390px unfilled: ins display:none, no label, no height");
    expect((await slots(page)).length === 0, "390px unfilled: nothing visible");
    await page.$eval('.ad.on[data-ad="rect"] ins.adsbygoogle', i => i.setAttribute("data-ad-status", "filled"));
    const shown = await slots(page);
    expect(shown.length === 1 && shown[0].kind === "rect" && shown[0].label, "390px: only the filled slot appears, with label");
    await context.close();
  }
  {
    // browser without :has(): drop the :has() rules, force the fallback class on <html>
    const { context, page } = await open(1366, "/weekly-planner.html");
    await page.evaluate(() => {
      for (const sh of document.styleSheets) { try { for (let k = sh.cssRules.length - 1; k >= 0; k--) if (sh.cssRules[k].cssText.includes(":has(")) sh.deleteRule(k); } catch (e) {} }
      document.documentElement.classList.add("no-has");
    });
    let l = await units(page);
    expect(unclipped(l) && l.every(u => !u.label && u.gap === 0), "no :has(): empty → ins visible, no extras");
    await page.$$eval(".ad.on ins.adsbygoogle", list => list.forEach(i => i.setAttribute("data-ad-status", "unfill-optimized")));
    l = await units(page);
    expect(l.every(u => u.label), "no :has(): unfill-optimized → label visible");
    await context.close();
  }

  await browser.close();
  server.close();
  for (const r of results) console.log(`${r.ok ? "ok  " : "FAIL"} ${r.label}`);
  const failed = results.filter(r => !r.ok).length;
  console.log(failed ? `Ad slot test: ${failed} failed` : `Ad slot test: ${results.length} checks OK`);
  process.exit(failed ? 1 : 0);
})();
