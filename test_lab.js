// Automatischer Test: jede Vorlage mit Standardwerten und Varianten zeichnen; alles muss auf der Seite liegen.
const fs = require("fs");
global.localStorage = { getItem: () => null, setItem() {} };
global.document = { readyState: "complete", querySelectorAll: () => [], querySelector: () => null, addEventListener() {} };
global.window = global; global.location = { search: "" };
eval(fs.readFileSync(__dirname + "/assets/lab.js", "utf8"));
const { T, Page } = window.PJL;
let n = 0, bad = 0;
const variants = [{}, { paper: "letter" }, { paper: "a5" }, { paper: "half" }, { orient: "landscape" }, { orient: "portrait" }, { ws: "sun" }, { month: "all" }, { ruling: "custom", gap: "5" }, { style: "dots" }, { cols: "2" }, { style: "number" }, { half: true }, { meals: "blds" }, { grocery: false }, { notes: false }, { start: "" }, { date: "2027-03-14" }, { year: "2028", month: "1" }];
for (const [key, tpl] of Object.entries(T)) {
  for (const v of variants) {
    const o = {}; tpl.opts.forEach(d => o[d.k] = d.def); for (const [k, val] of Object.entries(v)) if (k in o) o[k] = val;
    let pages; try { pages = tpl.pages(o); } catch (e) { console.error("FEHLER", key, v, e.message); bad++; continue; }
    const P = Page(o);
    for (const ops of pages) for (const op of ops) {
      n++;
      const xs = op.t === "line" ? [op.x1, op.x2] : op.t === "rect" ? [op.x, op.x + op.w] : op.t === "circle" ? [op.cx] : [op.x];
      const ys = op.t === "line" ? [op.y1, op.y2] : op.t === "rect" ? [op.y, op.y + op.h] : op.t === "circle" ? [op.cy] : [op.y];
      const vals = [...xs, ...ys];
      if (vals.some(z => !Number.isFinite(z)) || xs.some(x => x < -0.01 || x > P.w + 0.01) || ys.some(y => y < -0.01 || y > P.h + 0.01) || (op.t === "rect" && (op.w < 0 || op.h < 0))) {
        if (bad < 12) console.error("AUSSERHALB", key, JSON.stringify(v), JSON.stringify(op).slice(0, 140)); bad++;
      }
    }
  }
}
if (bad) { console.error(bad, "Probleme"); process.exit(1); }
console.log(`Vorlagen-Test: ${Object.keys(T).length} Vorlagen, ${n} Zeichenbefehle OK`);
