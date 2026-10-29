// Erzeugt den "Complete 2027 Planner" (Premium-Produkt) mit der Engine der Website.
// node products/planner2027.js  -> products/out/*.pdf
const fs = require("fs"), path = require("path");
global.localStorage = { getItem: () => null, setItem() {} };
global.document = { readyState: "complete", querySelectorAll: () => [], querySelector: () => null, addEventListener() {} };
global.window = global; global.location = { search: "" };
eval(fs.readFileSync(path.join(__dirname, "../assets/lab.js"), "utf8"));
const { jsPDF } = require("/tmp/npmx/node_modules/jspdf/dist/jspdf.node.min.js");
const { T, Page, drawInto } = window.PJL;
const YEAR = 2027, MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function defaults(key, over) { const o = {}; T[key].opts.forEach(d => o[d.k] = d.def); return Object.assign(o, over); }
const iso = d => d.toISOString().slice(0, 10);

function build(paper, ws, accent) {
  const base = { paper, ws, accent, orient: "portrait", brand: true, font: "serif" };
  const sections = []; // [title, pages(ops[]), landmarks]
  const P0 = Page(base), W = P0.w, H = P0.h;
  // Cover
  const C = Page(base);
  C.rect(0, 0, W, H, { fill: "#FBF7F0", stroke: "#FBF7F0", lw: 0.01 });
  C.rect(C.x0, C.y0, W - 2 * C.x0, H - 2 * C.y0, { stroke: C.accent, lw: 0.8, r: 4 });
  C.text(W / 2, H * 0.36, "The", { size: 30, serif: true, italic: true, align: "center", c: "#1F2430" });
  C.text(W / 2, H * 0.36 + 26, String(YEAR), { size: 96, serif: true, align: "center", c: C.accent });
  C.text(W / 2, H * 0.36 + 44, "Planner", { size: 40, serif: true, align: "center", c: "#1F2430" });
  C.line(W / 2 - 25, H * 0.36 + 54, W / 2 + 25, H * 0.36 + 54, C.accent, 0.6);
  C.text(W / 2, H * 0.36 + 64, "Year · Months · Weeks · Habits · Budget · Meals", { size: 10, align: "center", c: "#5E6573" });
  C.text(W / 2, H - 30, "This planner belongs to", { size: 9, align: "center", c: "#8A93A0" });
  C.line(W / 2 - 45, H - 20, W / 2 + 45, H - 20, "#C9CED6", 0.3);
  C.text(W / 2, H - C.y0 - 4, "Printable Joy Lab · printablejoylab.com", { size: 7, align: "center", c: "#A0A6AF" });
  sections.push(["Cover", [C.ops]]);
  sections.push(["Contents", [[]]]); // placeholder, drawn later with links
  sections.push(["Year at a glance", [...T["yearly-calendar"].pages(defaults("yearly-calendar", { ...base, year: YEAR })), ...T["yearly-calendar"].pages(defaults("yearly-calendar", { ...base, year: YEAR + 1 }))]]);
  sections.push(["Monthly calendars", T["monthly-calendar"].pages(defaults("monthly-calendar", { ...base, year: YEAR, month: "all", weeks: true, notes: true }))]);
  // Weeks: from the week containing Jan 1 to the week containing Dec 31
  const jan1 = new Date(Date.UTC(YEAR, 0, 1)), back = ws === "sun" ? jan1.getUTCDay() : (jan1.getUTCDay() + 6) % 7;
  let d = new Date(jan1.getTime() - back * 864e5); const weeks = [];
  while (d.getUTCFullYear() <= YEAR) { weeks.push(...T["weekly-planner"].pages(defaults("weekly-planner", { ...base, start: iso(d), title: "Weekly plan", lines: true, todo: true }))); d = new Date(d.getTime() + 7 * 864e5); if (d.getUTCFullYear() > YEAR) break; }
  sections.push(["Weekly planners", weeks]);
  sections.push(["Habit trackers", T["habit-tracker"].pages(defaults("habit-tracker", { ...base, year: YEAR, month: "all", habits: "", rows: 22 }))]);
  sections.push(["Monthly budget", T["budget-planner"].pages(defaults("budget-planner", { ...base, year: YEAR, month: "all", cur: paper === "letter" ? "$" : "€" }))]);
  sections.push(["Meal planners", Array(6).fill(0).flatMap(() => T["meal-planner"].pages(defaults("meal-planner", { ...base, start: "", grocery: true })))]);
  sections.push(["Lists & notes", [
    ...T["checklist"].pages(defaults("checklist", { ...base, title: "Goals for " + YEAR, style: "number", items: 20 })),
    ...T["checklist"].pages(defaults("checklist", { ...base, title: "Books to read", items: 30, cols: "2" })),
    ...T["checklist"].pages(defaults("checklist", { ...base, title: "Birthdays & gifts", items: 30 })),
    ...T["checklist"].pages(defaults("checklist", { ...base, title: "To do", items: 30, prio: true })),
    ...[1, 2, 3, 4].flatMap(() => T["dot-grid"].pages(defaults("dot-grid", { ...base, lines: "medium" }))),
    ...[1, 2, 3, 4].flatMap(() => T["lined-paper"].pages(defaults("lined-paper", { ...base, header: false, margin: false })))]]);
  // page numbers
  let n = 1; const starts = sections.map(([t, pg]) => { const s = n; n += pg.length; return [t, s, pg.length]; });
  // Contents page with links
  const K = Page(base); let y = K.title("Contents", String(YEAR));
  const ink = "#1F2430";
  starts.slice(2).forEach(([t, s], i) => { y += 11; K.text(K.x0, y, t, { size: 14, serif: true, c: ink }); K.text(K.x1, y, `p. ${s}`, { size: 10, c: K.accent, align: "right", bold: true }); K.line(K.x0, y + 3, K.x1, y + 3, "#E6DFD3", 0.2); });
  y += 16; K.text(K.x0, y, "Months", { size: 8, bold: true, c: K.accent });
  const mStart = starts.find(s => s[0] === "Monthly calendars")[1];
  MONTHS.forEach((m, i) => { const cx = K.x0 + (i % 4) * ((K.x1 - K.x0) / 4), cy = y + 8 + Math.floor(i / 4) * 9; K.rect(cx, cy - 5, (K.x1 - K.x0) / 4 - 3, 7, { r: 1.5, stroke: "#E6DFD3", lw: 0.3 }); K.text(cx + 3, cy, m, { size: 9, c: ink }); });
  K.footer(); sections[1][1] = [K.ops];
  const all = sections.flatMap(s => s[1]);
  const doc = new jsPDF({ unit: "mm", format: [W, H], orientation: "portrait", compress: true });
  doc.setProperties({ title: `The ${YEAR} Planner – Printable Joy Lab`, author: "Printable Joy Lab", creator: "printablejoylab.com", subject: `${YEAR} planner, ${paper === "letter" ? "US Letter" : "A4"}, week starts ${ws === "sun" ? "Sunday" : "Monday"}` });
  drawInto(doc, all, W, H);
  // hyperlinks: contents -> sections & months; every page -> contents
  doc.setPage(2);
  let yy = Page(base).y0 + 9 + 9;
  starts.slice(2).forEach(([t, s]) => { yy += 11; doc.link(Page(base).x0, yy - 6, W - 2 * Page(base).x0, 9, { pageNumber: s }); });
  yy += 16;
  MONTHS.forEach((m, i) => { const x0 = Page(base).x0, x1 = W - x0, cx = x0 + (i % 4) * ((x1 - x0) / 4), cy = yy + 8 + Math.floor(i / 4) * 9; doc.link(cx, cy - 5, (x1 - x0) / 4 - 3, 7, { pageNumber: mStart + i }); });
  for (let p = 3; p <= all.length; p++) { doc.setPage(p); doc.setFont("helvetica", "normal"); doc.setFontSize(6.5); doc.setTextColor(160, 166, 175); doc.text("Contents", W - Page(base).m, H - Page(base).m / 2 - 1, { align: "right" }); doc.link(W - Page(base).m - 12, H - Page(base).m / 2 - 4, 12, 5, { pageNumber: 2 }); }
  return { doc, pages: all.length, starts };
}

const out = path.join(__dirname, "out"); fs.mkdirSync(out, { recursive: true });
for (const [paper, label] of [["a4", "A4"], ["letter", "US-Letter"]]) for (const ws of ["mon", "sun"]) {
  const { doc, pages, starts } = build(paper, ws, "tomato");
  const f = path.join(out, `Planner-${YEAR}-${label}-${ws === "sun" ? "Sunday" : "Monday"}-start.pdf`);
  fs.writeFileSync(f, Buffer.from(doc.output("arraybuffer")));
  console.log(path.basename(f), pages, "pages", Math.round(fs.statSync(f).size / 1024), "KB", JSON.stringify(starts.map(s => s[0] + ":" + s[1])));
}
