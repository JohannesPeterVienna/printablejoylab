/* Printable Joy Lab — paper size table, print scale calculator and ruler check.
   The arithmetic lives in pure functions (window.PJLSizes) that test_sizes.js runs in Node; the page only wires them
   to forms. Sizes come from the table in the page itself (data-size rows), so text, table and calculator agree. */
(() => {
  "use strict";
  const round = (x, d = 1) => { const f = 10 ** d; return Math.round(x * f) / f; };
  const num = v => { const n = parseFloat(String(v ?? "").trim().replace(",", ".")); return Number.isFinite(n) ? n : NaN; };
  const clamp = (n, lo, hi, def) => Number.isFinite(n) ? Math.min(hi, Math.max(lo, n)) : def;
  const MODES = ["actual", "fit", "shrink", "custom"];

  /* A page of doc = [w, h] mm printed on a sheet = [w, h] mm whose printer leaves `border` mm blank on every side.
     actual: 100%.  fit: as large as fits into the printable area (up or down).  shrink: like fit, but never above 100%.
     custom: the percentage given. Same orientation for page and sheet; the page is centred. */
  function printScale(doc, sheet, border, mode, percent) {
    const availW = Math.max(1, sheet[0] - 2 * border), availH = Math.max(1, sheet[1] - 2 * border);
    const fit = Math.min(availW / doc[0], availH / doc[1]);
    const scale = mode === "fit" ? fit : mode === "shrink" ? Math.min(1, fit) : mode === "custom" ? percent / 100 : 1;
    const w = doc[0] * scale, h = doc[1] * scale;
    return { scale, fit, w, h, availW, availH,
      lostW: Math.max(0, w - availW), lostH: Math.max(0, h - availH),          // falls outside the printable area (both sides together)
      spareW: Math.max(0, sheet[0] - w), spareH: Math.max(0, sheet[1] - h) };   // blank paper left over (both sides together)
  }

  // The four sizes our generators offer – used to explain a measured scale.
  const OURS = { a4: ["A4", 210, 297], letter: ["US Letter", 215.9, 279.4], a5: ["A5", 148, 210], half: ["Half Letter", 139.7, 215.9] };

  /* Ruler check: the 100 mm square measured `across` and `down` millimeters. */
  function diagnose(across, down, nominal = 100) {
    const sx = across / nominal, sy = down / nominal, s = (sx + sy) / 2;
    const out = { sx, sy, scale: s, kind: "", matches: [], border: null };
    if (Math.abs(across - down) > 1) { out.kind = "uneven"; return out; }
    if (Math.abs(s - 1) <= 0.005) { out.kind = "ok"; return out; }
    out.kind = s < 1 ? "small" : "large";
    for (const [dk, d] of Object.entries(OURS)) for (const [sk, sh] of Object.entries(OURS)) {
      if (dk === sk) continue;
      const f = printScale([d[1], d[2]], [sh[1], sh[2]], 0, "fit").scale;
      if (Math.abs(f - s) <= 0.006) out.matches.push({ doc: dk, sheet: sk, docName: d[0], sheetName: sh[0], scale: f });
    }
    // same paper, fitted into the printable area: which border on each side gives this scale?
    if (s < 1) out.border = { a4: Math.max((1 - s) * 210 / 2, (1 - s) * 297 / 2), letter: Math.max((1 - s) * 215.9 / 2, (1 - s) * 279.4 / 2) };
    return out;
  }

  // Spreadsheet programs run cells that start with = + - @ (or tab / carriage return) as formulas: prefix them with '.
  const csvCell = v => { let s = String(v ?? ""); if (/^[=+\-@\t\r]/.test(s)) s = "'" + s; return /[",\n\r;]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; };
  const toCSV = rows => rows.map(r => r.map(csvCell).join(",")).join("\r\n") + "\r\n";

  const API = { printScale, diagnose, csvCell, toCSV, round, num, OURS };
  if (typeof window !== "undefined") window.PJLSizes = API;
  if (typeof document === "undefined" || !document.querySelector) return;

  /* ------------------------------------------------------------ page wiring */
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const el = (tag, text, cls) => { const e = document.createElement(tag); if (text != null) e.textContent = text; if (cls) e.className = cls; return e; };
  const fill = (box, parts) => { box.replaceChildren(...parts.filter(Boolean)); };
  const pct = s => `${round(s * 100, 1)}%`;
  const mm = x => `${round(x, 1)} mm`;
  async function copy(btn, text, done) {
    const old = btn.dataset.label || (btn.dataset.label = btn.textContent);
    try { await navigator.clipboard.writeText(text); btn.textContent = done; } catch { btn.textContent = "Copying is blocked in this browser"; }
    setTimeout(() => { btn.textContent = old; }, 2500);
  }
  const link = (href, text) => { const a = el("a", text); a.href = href; return a; };

  function sizes() {   // from the reference table; without it, the four sizes of our generators
    const rows = $$("tr[data-size]").map(tr => ({ id: tr.dataset.size, name: tr.dataset.name, w: +tr.dataset.w, h: +tr.dataset.h, ours: tr.dataset.ours || "" }));
    return rows.length ? rows : Object.entries(OURS).map(([k, v]) => ({ id: k, name: v[0], w: v[1], h: v[2], ours: k }));
  }

  function initCalc(root) {
    const list = sizes(), by = Object.fromEntries(list.map(s => [s.id, s])), form = $("form", root), out = $("[data-out]", root), fig = $("[data-fig]", root);
    for (const name of ["doc", "sheet"]) {
      const sel = form.elements[name], keep = sel.dataset.def;
      sel.replaceChildren(...list.map(s => { const o = el("option", `${s.name} (${round(s.w, 1)} × ${round(s.h, 1)} mm)`); o.value = s.id; return o; }));
      sel.value = by[keep] ? keep : list[0].id;
    }
    const state = () => ({ doc: form.elements.doc.value, sheet: form.elements.sheet.value, mode: form.elements.mode.value,
      border: clamp(num(form.elements.border.value), 0, 30, 0), percent: clamp(num(form.elements.percent.value), 10, 400, 100), feature: clamp(num(form.elements.feature.value), 0.1, 500, 5) });
    function apply(v) {
      if (by[v.doc]) form.elements.doc.value = v.doc;
      if (by[v.sheet]) form.elements.sheet.value = v.sheet;
      if (MODES.includes(v.mode)) form.elements.mode.value = v.mode;
      for (const k of ["border", "percent", "feature"]) if (v[k] != null && Number.isFinite(num(v[k]))) form.elements[k].value = num(v[k]);
      render();
    }
    function shareURL() { const s = state(), q = new URLSearchParams({ doc: s.doc, sheet: s.sheet, mode: s.mode, border: s.border, feature: s.feature }); if (s.mode === "custom") q.set("percent", s.percent); return `${location.origin}${location.pathname}?${q}#scale`; }
    let summary = "";
    function render() {
      const s = state(), d = by[s.doc], p = by[s.sheet];
      $("[data-percent]", root).hidden = s.mode !== "custom";
      const r = printScale([d.w, d.h], [p.w, p.h], s.border, s.mode, s.percent);
      const lost = r.lostW > 0.05 || r.lostH > 0.05, exact = Math.abs(r.scale - 1) < 0.0005;
      const head = el("p", null, "calc-big"); head.append(el("strong", pct(r.scale)), document.createTextNode(` · the ${d.name} page prints ${round(r.w, 1)} × ${round(r.h, 1)} mm on ${p.name}`));
      const facts = el("ul");
      facts.append(el("li", `A ${round(s.feature, 2)} mm grid or line spacing prints as ${round(s.feature * r.scale, 2)} mm; a 100 mm line measures ${mm(100 * r.scale)}.`));
      if (lost) facts.append(el("li", `Cut off: ${r.lostW > 0.05 ? mm(r.lostW) + " of the width" : ""}${r.lostW > 0.05 && r.lostH > 0.05 ? " and " : ""}${r.lostH > 0.05 ? mm(r.lostH) + " of the height" : ""} fall outside the printable area (${round(r.availW, 1)} × ${round(r.availH, 1)} mm), split between the two opposite edges.`));
      else facts.append(el("li", `Nothing is cut off. Blank paper around the page: ${mm(r.spareW / 2)} left and right, ${mm(r.spareH / 2)} top and bottom.`));
      const why = el("p");
      if (exact && !lost) why.textContent = "Result: true to size. Measurements on the page are the measurements in the PDF.";
      else if (exact && lost) why.textContent = "Result: true to size, but the page is larger than the area this printer can reach. Lines stop where the printable area ends.";
      else why.textContent = `Result: everything on the page is ${r.scale < 1 ? "reduced" : "enlarged"} by the same factor (${r.scale < 1 ? "smaller" : "larger"} of ${round(r.availW, 1)} ÷ ${round(d.w, 1)} = ${round(r.availW / d.w, 4)} and ${round(r.availH, 1)} ÷ ${round(d.h, 1)} = ${round(r.availH / d.h, 4)} is the fit factor ${round(r.fit, 4)}).`;
      const next = el("p");
      if (p.ours && d.id !== p.id) { next.append("Next step: make the page in the size of your paper instead – for example ", link(`/graph-paper.html?paper=${p.ours}`, `graph paper in ${p.name}`), " – and print it at 100%."); }
      else if (!exact) { next.append("Next step: choose 100% / “Actual size” in the print dialog. To see whether it worked, print the ", link(`/print-test-page.html${p.ours ? "?paper=" + p.ours : ""}`, "test page"), " and measure its 100 mm square."); }
      else if (lost) { next.append("Next step: check how far your printer really reaches with the edge rulers on the ", link(`/print-test-page.html${p.ours ? "?paper=" + p.ours : ""}`, "print test page"), "."); }
      else next.textContent = "Next step: print. A ruler on the first sheet confirms the result.";
      fill(out, [head, facts, why, next]);
      summary = `${d.name} page on ${p.name}, ${form.elements.mode.selectedOptions[0].textContent.trim()}, printer border ${s.border} mm: scale ${pct(r.scale)}, printed ${round(r.w, 1)} × ${round(r.h, 1)} mm; ${round(s.feature, 2)} mm prints as ${round(s.feature * r.scale, 2)} mm. ${shareURL()}`;
      // drawing: sheet, printable area, printed page (all to one scale)
      const k = 150 / Math.max(p.h, r.h, p.w), W = Math.max(p.w, r.w) * k + 20, H = Math.max(p.h, r.h) * k + 20, cx = W / 2, cy = H / 2;
      const box = (w, h, cls) => `<rect x="${(cx - w * k / 2).toFixed(1)}" y="${(cy - h * k / 2).toFixed(1)}" width="${(w * k).toFixed(1)}" height="${(h * k).toFixed(1)}" class="${cls}"/>`;
      fig.innerHTML = `<svg viewBox="0 0 ${W.toFixed(0)} ${H.toFixed(0)}" role="img" aria-label="Sheet, printable area and printed page drawn to scale">${box(p.w, p.h, "fig-sheet")}${box(r.availW, r.availH, "fig-area")}${box(r.w, r.h, "fig-page")}</svg>`;
    }
    form.addEventListener("input", render); form.addEventListener("change", render);
    $$("[data-example]", root).forEach(b => b.addEventListener("click", () => apply(Object.fromEntries(new URLSearchParams(b.dataset.example)))));
    $("[data-copy]", root).addEventListener("click", e => copy(e.currentTarget, summary, "Result copied ✓"));
    $("[data-share]", root).addEventListener("click", e => copy(e.currentTarget, shareURL(), "Link copied ✓"));
    const q = new URLSearchParams(location.search);
    apply(q.has("doc") || q.has("sheet") || q.has("mode") ? Object.fromEntries(q) : {});
  }

  function initMeasure(root) {
    const form = $("form", root), out = $("[data-out]", root);
    const shareURL = () => `${location.origin}${location.pathname}?across=${num(form.elements.across.value)}&down=${num(form.elements.down.value)}#check`;
    let summary = "";
    function render() {
      const a = num(form.elements.across.value), d = num(form.elements.down.value);
      if (!(a > 0) || !(d > 0)) { fill(out, [el("p", "Enter both measurements in millimeters, for example 94 and 94.", "muted")]); summary = ""; return; }
      if (a < 20 || a > 300 || d < 20 || d > 300) { fill(out, [el("p", "That is outside what a 100 mm square can measure on a printed sheet (20–300 mm). Please check the numbers; they must be millimeters, not inches.", "err")]); summary = ""; return; }
      const r = diagnose(a, d), parts = [];
      const head = el("p", null, "calc-big");
      if (r.kind === "uneven") {
        head.append(el("strong", `${pct(r.sx)} across, ${pct(r.sy)} down`));
        parts.push(head, el("p", "The two directions differ by more than 1 mm. A scale setting in the print dialog changes both directions by the same factor, so it cannot be the only cause. Measure again from line to line; if the difference stays, it is not a scaling setting."));
      } else if (r.kind === "ok") {
        head.append(el("strong", pct(r.scale)), document.createTextNode(" · true to size"));
        parts.push(head, el("p", "Both directions are within half a millimeter of 100 mm. A 5 mm grid prints as 5 mm. Next step: print your pages with exactly these settings."));
      } else {
        head.append(el("strong", pct(r.scale)), document.createTextNode(r.kind === "small" ? " · the print is reduced" : " · the print is enlarged"));
        parts.push(head, el("p", `A 5 mm grid prints as ${round(5 * r.scale, 2)} mm, a 7.1 mm ruling as ${round(7.1 * r.scale, 2)} mm.`));
        const ul = el("ul");
        r.matches.forEach(m => ul.append(el("li", `${pct(m.scale)} is what “Fit” produces when a ${m.docName} page is printed on ${m.sheetName} paper. If that is your paper, make the page in ${m.sheetName} instead.`)));
        if (r.border) ul.append(el("li", `With matching paper, “Fit to printable area” gives this scale when the printer's border is about ${round(r.border.a4, 1)} mm on A4 or ${round(r.border.letter, 1)} mm on US Letter.`));
        if (r.kind === "large" && !r.matches.length) ul.append(el("li", "An enlargement comes from a “Fit” option with a page smaller than the sheet, or from a custom scale above 100."));
        parts.push(ul);
        const next = el("p"); next.append("Next step: set the scale to 100% / “Actual size”, print the test page again and measure. The ", link("/paper-sizes.html#scale", "print scale calculator"), " shows the result for any pair of page and paper.");
        parts.push(next);
      }
      fill(out, parts);
      summary = `100 mm square measured ${a} × ${d} mm: ${r.kind === "uneven" ? `${pct(r.sx)} across, ${pct(r.sy)} down` : pct(r.scale)}. ${shareURL()}`;
    }
    form.addEventListener("input", render);
    $$("[data-example]", root).forEach(b => b.addEventListener("click", () => { const [a, d] = b.dataset.example.split(","); form.elements.across.value = a; form.elements.down.value = d; render(); }));
    $("[data-copy]", root).addEventListener("click", e => summary && copy(e.currentTarget, summary, "Result copied ✓"));
    $("[data-share]", root).addEventListener("click", e => summary && copy(e.currentTarget, shareURL(), "Link copied ✓"));
    const q = new URLSearchParams(location.search);
    if (q.has("across")) { const a = num(q.get("across")), d = num(q.get("down") ?? q.get("across")); if (Number.isFinite(a)) form.elements.across.value = a; if (Number.isFinite(d)) form.elements.down.value = d; }
    render();
  }

  function initTable(root) {
    const rows = $$("tr[data-size]", root), search = $("[data-search]", root), group = $("[data-group]", root), count = $("[data-count]", root);
    function render() {
      const words = search.value.toLowerCase().replace(/[×*]/g, "x").split(/\s+/).filter(Boolean), g = group.value;
      let n = 0;
      rows.forEach(tr => { const hay = tr.dataset.hay, show = (!g || tr.dataset.g === g) && words.every(w => hay.includes(w)); tr.hidden = !show; if (show) n++; });
      count.textContent = n ? `Showing ${n} of ${rows.length} sizes` : `No size matches. Try a name (“legal”), a group or a number such as 210.`;
    }
    search.addEventListener("input", render); group.addEventListener("change", render);
    $("[data-clear]", root).addEventListener("click", () => { search.value = ""; group.value = ""; render(); search.focus(); });
    $("[data-csv]", root).addEventListener("click", () => {
      const head = $$("thead th", root).map(th => th.textContent.trim());
      const data = rows.filter(tr => !tr.hidden).map(tr => [...tr.cells].map(td => td.textContent.trim()));
      const a = el("a"); a.href = URL.createObjectURL(new Blob(["﻿" + toCSV([head, ...data])], { type: "text/csv;charset=utf-8" })); a.download = "paper-sizes.csv";
      document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
    });
    const q = new URLSearchParams(location.search);
    if (q.has("q")) search.value = q.get("q").slice(0, 40);
    if (q.has("group") && [...group.options].some(o => o.value === q.get("group"))) group.value = q.get("group");
    render();
  }

  const init = () => { $$("[data-sizetable]").forEach(initTable); $$("[data-scalecalc]").forEach(initCalc); $$("[data-measure]").forEach(initMeasure); };
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", init) : init();
})();
