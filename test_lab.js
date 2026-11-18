// Automatischer Test: jede Vorlage mit Standardwerten und Varianten zeichnen; alles muss auf der Seite liegen.
const fs = require("fs");
global.localStorage = { getItem: () => null, setItem() {} };
global.document = { readyState: "complete", querySelectorAll: () => [], querySelector: () => null, addEventListener() {} };
global.window = global; global.location = { search: "" };
eval(fs.readFileSync(__dirname + "/assets/lab.js", "utf8"));
const { T, Page, LANG, edgeRulerLength } = window.PJL;
let n = 0, bad = 0;
const variants = [{}, { paper: "a4" }, { paper: "letter" }, { ws: "mon" }, { paper: "a5" }, { paper: "half" }, { orient: "landscape" }, { orient: "portrait" }, { ws: "sun" }, { month: "all" }, { ruling: "custom", gap: "5" }, { style: "dots" }, { cols: "2" }, { style: "number" }, { half: true }, { meals: "blds" }, { grocery: false }, { notes: false }, { start: "" }, { date: "2027-03-14" }, { year: "2028", month: "1" },
  { lang: "de" }, { lang: "fr", start: "2027-09-27", paper: "a5", orient: "portrait" }, { lang: "pt", month: "all" }, { lang: "nb", ws: "sun" }, { lang: "xx" }, { inch: false }, { frames: false, paper: "half" }];
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

// Sprachen: Monats- und Wochentagsnamen gegen die CLDR-Daten von Node (Intl) prüfen; nur Zeichen, die die PDF-Standardschrift kennt.
let names = 0;
const norm = x => x.toLowerCase().replace(/\./g, "");
for (const [code, lg] of Object.entries(LANG)) {
  const all = [...lg.m, ...lg.d, ...lg.s, lg.notes, lg.year, lg.todo, lg.weekof, lg.habit, lg.done, lg.day ? lg.day(1, lg.m[2]) : ""];
  if (lg.m.length !== 12 || lg.d.length !== 7 || lg.s.length !== 7) { console.error("SPRACHE unvollständig", code); bad++; }
  for (const t of all) if ([...t].some(ch => ch.codePointAt(0) > 255)) { console.error("SPRACHE Zeichen außerhalb Latin-1", code, t); bad++; }
  if (new Intl.DateTimeFormat(code).resolvedOptions().locale.slice(0, 2) !== code) continue;   // Node ohne diese Sprachdaten
  const f = opt => new Intl.DateTimeFormat(code, { timeZone: "UTC", ...opt });
  for (let i = 0; i < 12; i++, names++) { const want = f({ month: "long" }).format(new Date(Date.UTC(2027, i, 15))); if (norm(want) !== norm(lg.m[i])) { console.error("SPRACHE Monat", code, lg.m[i], "≠", want); bad++; } }
  for (let i = 0; i < 7; i++, names += 2) {   // 4 January 2027 is a Monday
    const day = new Date(Date.UTC(2027, 0, 4 + i)), long = f({ weekday: "long" }).format(day), short = f({ weekday: "short" }).format(day);
    if (norm(long) !== norm(lg.d[i])) { console.error("SPRACHE Wochentag", code, lg.d[i], "≠", long); bad++; }
    if (norm(short) !== norm(lg.s[i])) { console.error("SPRACHE Kurzform", code, lg.s[i], "≠", short); bad++; }
  }
}
// Testseite: das Quadrat misst genau 100 mm, die Randlineale beginnen an der Papierkante und bleiben vor dem Inhalt.
for (const paper of ["a4", "letter", "a5", "half"]) {
  const ops = T["print-test-page"].pages({ paper, inch: true, frames: true, brand: true })[0], P = Page({ paper });
  const sq = ops.filter(op => op.t === "rect");
  if (sq.length !== 1 || Math.abs(sq[0].w - 100) > 1e-9 || Math.abs(sq[0].h - 100) > 1e-9) { console.error("TESTSEITE Quadrat", paper); bad++; }
  const n = edgeRulerLength(P.m), spines = ops.filter(op => op.t === "line" && [op.x1, op.y1, op.x2, op.y2].some((v, i) => v === [0, 0, 0, 0][i] || v === [P.w, P.h, P.w, P.h][i]) && Math.abs(Math.hypot(op.x2 - op.x1, op.y2 - op.y1) - n) < 1e-9);
  if (spines.length !== 4 || n >= P.m) { console.error("TESTSEITE Randlineale", paper, spines.length, n); bad++; }
}
if (bad) { console.error(bad, "Probleme"); process.exit(1); }
console.log(`Sprachen: ${Object.keys(LANG).length} Sprachen, ${names} Namen mit Intl verglichen`);
console.log(`Vorlagen-Test: ${Object.keys(T).length} Vorlagen, ${n} Zeichenbefehle OK`);
