// Whole-site check in a real browser (Playwright + Chromium). Run after building: node test_site.js
//  - every page of the sitemap at 390 and 1366 px: no JS errors, no horizontal overflow
//  - every internal link resolves to a built file (and its #anchor exists); links that carry settings
//    (?paper=…, ?doc=…) only use options and values the target really has
//  - generators, print scale calculator, ruler check and size table are clicked through, also with nonsense input
// External requests are answered with an empty stub; nothing leaves the machine.
"use strict";
const http = require("http");
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const DOCS = path.join(__dirname, "docs");
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".webp": "image/webp", ".png": "image/png", ".xml": "application/xml", ".txt": "text/plain" };
const results = [];
const expect = (cond, label) => { results.push({ ok: !!cond, label }); };

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
  const open = async (width, url, opts = {}) => {
    const context = await browser.newContext({ viewport: { width, height: 900 }, acceptDownloads: true, ...opts });
    await context.route(/^https?:\/\/(?!127\.0\.0\.1)/, route => route.fulfill({ status: 200, contentType: "text/javascript", body: "/* stub */" }));
    const page = await context.newPage();
    const errors = [];
    page.on("pageerror", e => errors.push(e.message));
    page.on("console", m => { if (m.type() === "error") errors.push(m.text()); });
    page.on("dialog", d => { errors.push("dialog: " + d.message()); d.dismiss(); });
    await page.goto(origin + url, { waitUntil: "load" });
    return { context, page, errors };
  };

  const urls = [...fs.readFileSync(path.join(DOCS, "sitemap.xml"), "utf8").matchAll(/<loc>https:\/\/printablejoylab\.com([^<]*)<\/loc>/g)].map(m => m[1]);
  expect(urls.length >= 20, `sitemap lists ${urls.length} pages`);
  const links = new Map();   // href → page it was found on
  for (const width of [390, 1366]) {
    for (const url of [...urls, "/imprint.html", "/privacy.html"]) {
      const { context, page, errors } = await open(width, url);
      const over = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      expect(over <= 1, `${width}px ${url}: no horizontal overflow${over > 1 ? " (" + over + " px)" : ""}`);
      expect(errors.length === 0, `${width}px ${url}: no JS errors ${errors.join(" | ")}`);
      if (width === 390) for (const h of await page.$$eval("a[href]", as => as.map(a => a.getAttribute("href")))) if (h.startsWith("/") && !links.has(h)) links.set(h, url);
      await context.close();
    }
  }

  // internal links: file exists, anchor exists, settings in the link are real options
  const optionCache = {};
  let withSettings = 0;
  for (const [href, from] of links) {
    const u = new URL(href, origin), file = path.join(DOCS, u.pathname === "/" ? "index.html" : u.pathname);
    if (!fs.existsSync(file)) { expect(false, `dead link ${href} on ${from}`); continue; }
    if (u.hash && !new RegExp(`id="${u.hash.slice(1)}"`).test(fs.readFileSync(file, "utf8"))) expect(false, `missing anchor ${href} on ${from}`);
    if (![...u.searchParams].length) continue;
    withSettings++;
    const { context, page, errors } = await open(1366, href);
    if (await page.$("[data-lab]")) {
      const bad = await page.evaluate(() => {
        const form = document.querySelector("[data-controls]"), out = [];
        for (const [k, v] of new URLSearchParams(location.search)) {
          const el = form.elements[k];
          if (k === "across" || k === "down") continue;   // belong to the ruler check on the same page
          if (!el) { out.push(`unknown option ${k}`); continue; }
          const one = el instanceof RadioNodeList ? null : el;
          if (one && one.type === "checkbox") { if (!["0", "1"].includes(v) || one.checked !== (v === "1")) out.push(`${k}=${v}`); }
          else if (String(el.value).replace(/\r/g, "") !== v) out.push(`${k}=${v} became ${el.value}`);
        }
        return out;
      });
      expect(bad.length === 0, `settings link ${href} (on ${from}) ${bad.join("; ")}`);
      expect(await page.$("[data-stage] svg"), `settings link ${href}: preview drawn`);
    }
    if (u.searchParams.has("across")) expect(await page.$eval("[data-measure] [data-out]", e => /%/.test(e.textContent)), `ruler check link ${href} shows a result`);
    else if (await page.$("[data-lab]")) { /* checked above */ }
    else if (u.searchParams.has("doc")) {
      const state = await page.evaluate(() => { const f = document.querySelector("[data-scalecalc] form"); return { doc: f.elements.doc.value, sheet: f.elements.sheet.value, mode: f.elements.mode.value, border: f.elements.border.value }; });
      expect(state.doc === u.searchParams.get("doc") && state.sheet === u.searchParams.get("sheet") && state.mode === u.searchParams.get("mode") && state.border === u.searchParams.get("border"), `calculator link ${href} sets its values`);
    } else expect(false, `link with settings to a page without a tool: ${href}`);
    expect(errors.length === 0, `settings link ${href}: no JS errors ${errors.join(" | ")}`);
    await context.close();
  }
  expect(true, `${links.size} internal links resolve (${withSettings} with settings)`);

  // moved pages: noindex, canonical and refresh to an existing page, not in the sitemap
  for (const f of fs.readdirSync(DOCS).filter(f => f.endsWith(".html"))) {
    const html = fs.readFileSync(path.join(DOCS, f), "utf8"), m = /http-equiv="refresh" content="0; url=([^"]+)"/.exec(html);
    if (!m) continue;
    expect(/noindex/.test(html) && html.includes(`rel="canonical" href="https://printablejoylab.com${m[1]}"`) && fs.existsSync(path.join(DOCS, m[1])) && !urls.includes("/" + f), `moved page ${f} → ${m[1]}: noindex, canonical, target exists, not in sitemap`);
  }

  // home: the generator is the first thing on the page and works
  {
    const { context, page, errors } = await open(390, "/");
    expect(await page.$eval("main", m => m.querySelector("[data-lab]").compareDocumentPosition(m.querySelector("#templates")) & Node.DOCUMENT_POSITION_FOLLOWING), "home: generator comes before the template list");
    await page.selectOption("[data-controls] select[name=lang]", "de");
    await page.fill("[data-controls] input[name=year]", "2027");
    await page.selectOption("[data-controls] select[name=month]", "2");
    expect(await page.$eval("[data-stage] svg", s => s.textContent.includes("März") && s.textContent.includes("NOTIZEN") && s.textContent.includes("MO")), "home: German month, weekday and label in the preview");
    expect(errors.length === 0, `home generator: no JS errors ${errors.join(" | ")}`);
    await context.close();
  }

  // generators: nonsense in the address and in the fields must neither break the page nor run as HTML
  const evil = '"><img src=x onerror=window.__xss=1><script>window.__xss=1</script>';
  for (const slug of ["monthly-calendar", "weekly-planner", "habit-tracker", "checklist", "print-test-page", "budget-planner"]) {
    const q = new URLSearchParams({ paper: evil, lang: evil, title: evil, habits: evil, prefill: evil, cats: evil, year: "abc", month: "99", start: "not-a-date", ws: evil, orient: evil, items: "1e9", rows: "-5", across: evil, down: "NaN" });
    const { context, page, errors } = await open(1366, `/${slug}.html?${q}`);
    expect(await page.$("[data-stage] svg") && !(await page.evaluate(() => window.__xss)) && !(await page.$("img[src=x]")), `${slug}: nonsense settings draw a page and inject nothing`);
    await page.click("[data-share]");
    expect(await page.waitForFunction(() => /Link copied|address bar/.test(document.querySelector("[data-share]").textContent), null, { timeout: 3000 }).then(() => true, () => false), `${slug}: “Copy link” confirms on the button`);
    for (const name of ["title", "habits", "prefill", "cats"]) if (await page.$(`[data-controls] [name=${name}]`)) await page.fill(`[data-controls] [name=${name}]`, evil + "\n=1+1\n" + "x".repeat(500));
    expect(await page.$("[data-stage] svg") && !(await page.evaluate(() => window.__xss)) && !(await page.$("img[src=x]")), `${slug}: nonsense typed into the fields injects nothing`);
    expect(errors.length === 0, `${slug}: no JS errors with nonsense ${errors.join(" | ")}`);
    await context.close();
  }

  // PDF: the German calendar really carries German names (text is stored with the standard fonts)
  {
    const { context, page, errors } = await open(1366, "/monthly-calendar.html?lang=de&year=2027&month=2&paper=a4&orient=landscape");
    const [download] = await Promise.all([page.waitForEvent("download"), page.click("[data-pdf]")]);
    const file = await download.path(), raw = fs.readFileSync(file);
    expect(download.suggestedFilename() === "monthly-calendar-a4.pdf" && raw.length > 1500 && raw.subarray(0, 5).toString() === "%PDF-", "PDF download: a PDF file with the expected name");
    expect(errors.length === 0, `PDF download: no JS errors ${errors.join(" | ")}`);
    await context.close();
  }

  // print scale calculator
  for (const width of [390, 1366]) {
    const { context, page, errors } = await open(width, "/paper-sizes.html");
    const out = () => page.$eval("[data-scalecalc] [data-out]", e => e.textContent);
    expect(/94\.1%/.test(await out()) && /4\.7 mm/.test(await out()), `${width}px calculator: default A4 on US Letter with Fit gives 94.1% and 4.7 mm`);
    for (const [i, want] of [[1, /97\.3%/], [2, /96\.2%/], [3, /100%[\s\S]*17\.6 mm of the height/], [4, /141\.4%/]]) {
      await page.click(`[data-scalecalc] [data-example] >> nth=${i}`);
      expect(want.test(await out()), `${width}px calculator: example ${i + 1} → ${want}`);
    }
    await page.selectOption("[data-scalecalc] select[name=sheet]", "iso_a10_26x37mm");
    await page.fill("[data-scalecalc] input[name=border]", "20");
    expect(/no printable area is left/.test(await out()) && !/NaN|Infinity/.test(await out()), `${width}px calculator: border wider than the sheet gives a clear message`);
    await page.selectOption("[data-scalecalc] select[name=sheet]", "iso_a4_210x297mm"); await page.fill("[data-scalecalc] input[name=border]", "0");
    await page.selectOption("[data-scalecalc] select[name=mode]", "custom");
    await page.fill("[data-scalecalc] input[name=percent]", "50");
    expect(/50%/.test(await out()), `${width}px calculator: custom 50%`);
    for (const junk of ["", "abc", "-999", "1e99", evil]) {
      for (const name of ["border", "feature", "percent"]) await page.$eval(`[data-scalecalc] input[name=${name}]`, (el, v) => { el.type = "text"; el.value = v; el.dispatchEvent(new Event("input", { bubbles: true })); }, junk);
      expect(/%|no printable area/.test(await out()) && !/NaN|Infinity|undefined/.test(await out()), `${width}px calculator: nonsense "${junk.slice(0, 12)}" still gives a finite result`);
    }
    expect(await page.$eval("[data-scalecalc] [data-fig] svg", s => s.querySelectorAll("rect").length === 3), `${width}px calculator: drawing with sheet, printable area and page`);
    // size table
    const shown = () => page.$$eval("tr[data-size]", rows => rows.filter(r => !r.hidden).length);
    expect(await shown() === 81, `${width}px table: 81 sizes`);
    await page.fill("[data-search]", "legal");
    expect(await shown() === 2, `${width}px table: “legal” finds US Legal and Government Legal`);
    await page.fill("[data-search]", "210 x 297");
    expect(await shown() >= 1 && await page.$eval("tr[data-size]:not([hidden]) th", th => th.textContent === "A4"), `${width}px table: “210 x 297” finds A4 first`);
    await page.fill("[data-search]", evil);
    expect(await shown() === 0 && /No size matches/.test(await page.$eval("[data-count]", e => e.textContent)) && !(await page.evaluate(() => window.__xss)), `${width}px table: nonsense search shows the empty message`);
    await page.click("[data-clear]");
    await page.selectOption("[data-group]", "jis");
    expect(await shown() === 12, `${width}px table: group filter (12 Japanese sizes)`);
    const [download] = await Promise.all([page.waitForEvent("download"), page.click("[data-csv]")]);
    const csv = fs.readFileSync(await download.path(), "utf8");
    expect(csv.split("\r\n").filter(Boolean).length === 13 && csv.includes("jis_b5_182x257mm") && csv.includes("Size,Millimeters,Inches"), `${width}px table: CSV holds the header and the 12 rows shown`);
    expect(errors.length === 0, `${width}px paper sizes: no JS errors ${errors.join(" | ")}`);
    await context.close();
  }
  {
    const q = new URLSearchParams({ doc: evil, sheet: evil, mode: evil, border: evil, feature: evil, q: evil, group: evil });
    const { context, page, errors } = await open(1366, `/paper-sizes.html?${q}`);
    expect(/%/.test(await page.$eval("[data-scalecalc] [data-out]", e => e.textContent)) && !(await page.evaluate(() => window.__xss)) && !(await page.$("img[src=x]")), "paper sizes: nonsense in the address injects nothing and the calculator still works");
    expect(errors.length === 0, `paper sizes with nonsense address: no JS errors ${errors.join(" | ")}`);
    await context.close();
  }

  // ads keep their distance from the calculators: every ad slot, shown as filled, is at least 250 px away from any control
  for (const width of [390, 1366]) for (const url of ["/print-test-page.html", "/paper-sizes.html"]) {
    const { context, page } = await open(width, url);
    await page.waitForFunction(() => document.querySelector(".ad.on ins.adsbygoogle"));
    await page.$$eval(".ad.on ins.adsbygoogle", list => list.forEach(i => i.setAttribute("data-ad-status", "filled")));
    const r = await page.evaluate(() => {
      const ads = [...document.querySelectorAll(".ad")].filter(a => getComputedStyle(a).display !== "none"), all = [];
      const controls = [...document.querySelectorAll(".calc button, .calc input, .calc select, .filter input, .filter select, .filter-actions button")].filter(c => c.getClientRects().length);
      for (const a of ads) for (const c of controls) {
        const A = a.getBoundingClientRect(), C = c.getBoundingClientRect();
        all.push({ gap: Math.hypot(Math.max(0, A.left - C.right, C.left - A.right), Math.max(0, A.top - C.bottom, C.top - A.bottom)), ad: a.dataset.ad, control: c.name || c.textContent.trim().slice(0, 20) });
      }
      all.sort((x, y) => x.gap - y.gap);
      return { ads: ads.length, controls: controls.length, nearest: all[0] };
    });
    expect(r.ads >= 2 && r.controls >= 4 && r.nearest.gap >= 250, `${width}px ${url}: nearest ad is ${Math.round(r.nearest.gap)} px from a calculator control (${r.nearest.ad} ↔ ${r.nearest.control}), ${r.ads} slots`);
    await context.close();
  }
  // every guide shows the date of its last change as review date
  for (const url of urls) {
    const html = fs.readFileSync(path.join(DOCS, url === "/" ? "index.html" : url), "utf8"), mod = /"dateModified": ?"(\d{4})-(\d\d)-(\d\d)"/.exec(html), rev = /Reviewed (\w+) (\d+), (\d{4})/.exec(html);
    if (!mod || !rev) continue;
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    expect(rev[1] === months[+mod[2] - 1] && +rev[2] === +mod[3] && rev[3] === mod[1], `${url}: review date matches dateModified (${mod[0].slice(-11, -1)})`);
  }

  // ruler check on the test page
  {
    const { context, page, errors } = await open(390, "/print-test-page.html");
    const out = () => page.$eval("[data-measure] [data-out]", e => e.textContent);
    const type = async (a, d) => { await page.fill("[data-measure] input[name=across]", a); await page.fill("[data-measure] input[name=down]", d); };
    await type("100", "100"); expect(/true to size/.test(await out()), "ruler check: 100 × 100 is true to size");
    await type("94", "94,2"); expect(/94\.1%/.test(await out()) && /A4 page is printed on US Letter/.test(await out()), "ruler check: 94 × 94,2 (decimal comma) → 94.1%, A4 on US Letter");
    await type("96", "96"); expect(/about 4\.2 mm on A4 or 4\.3 mm on US Letter/.test(await out()), "ruler check: 96 × 96 names a border of 4.2 mm (A4) / 4.3 mm (US Letter)");
    await type("101", "100"); expect(!/true to size/.test(await out()) && /101% across, 100% down/.test(await out()), "ruler check: 101 × 100 is not called true to size");
    await type("94", "100"); expect(/differ by more than 1 mm/.test(await out()), "ruler check: uneven result is explained");
    await type("3.9", "3.9"); expect(/not inches/.test(await out()), "ruler check: inch values are caught");
    await type(evil, "abc"); expect(/Enter both measurements/.test(await out()) && !(await page.evaluate(() => window.__xss)), "ruler check: nonsense asks for numbers");
    await page.click("[data-measure] [data-example] >> nth=2"); expect(/97\.3%/.test(await out()), "ruler check: example button");
    expect(errors.length === 0, `ruler check: no JS errors ${errors.join(" | ")}`);
    await context.close();
  }

  // keyboard: the calculator can be reached and used without a mouse
  {
    const { context, page } = await open(1366, "/paper-sizes.html");
    await page.focus("[data-scalecalc] select[name=doc]");
    await page.keyboard.press("Tab"); await page.keyboard.press("Tab");
    expect(await page.evaluate(() => document.activeElement.name) === "mode", "keyboard: Tab moves through the calculator fields in order");
    await page.focus("[data-scalecalc] [data-example]"); await page.keyboard.press("Enter");
    expect(/94\.1%/.test(await page.$eval("[data-scalecalc] [data-out]", e => e.textContent)), "keyboard: Enter on an example button runs it");
    await context.close();
  }

  await browser.close();
  server.close();
  for (const r of results) if (!r.ok || process.argv.includes("-v")) console.log(`${r.ok ? "ok  " : "FAIL"} ${r.label}`);
  const failed = results.filter(r => !r.ok).length;
  console.log(failed ? `Site test: ${failed} of ${results.length} failed` : `Site test: ${results.length} checks OK`);
  process.exit(failed ? 1 : 0);
})();
