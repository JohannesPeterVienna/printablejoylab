// Arithmetic behind the print scale calculator, the ruler check and the CSV export (node --test test_sizes.js).
"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
global.window = global;
eval(fs.readFileSync(__dirname + "/assets/sizes.js", "utf8"));
const { printScale, diagnose, csvCell, toCSV, num } = window.PJLSizes;
const A4 = [210, 297], LETTER = [215.9, 279.4], A5 = [148, 210];
const near = (a, b, eps = 1e-4) => assert.ok(Math.abs(a - b) <= eps, `${a} ≉ ${b}`);

test("actual size keeps 100% and reports what does not fit", () => {
  const r = printScale(A4, LETTER, 0, "actual");
  assert.equal(r.scale, 1); near(r.lostH, 17.6); assert.equal(r.lostW, 0); near(r.spareW, 5.9);
});
test("fit uses the smaller of the two ratios", () => {
  near(printScale(A4, LETTER, 0, "fit").scale, 279.4 / 297);
  near(printScale(LETTER, A4, 0, "fit").scale, 210 / 215.9);
  near(printScale(A4, A4, 4, "fit").scale, 202 / 210);
  const r = printScale(A4, LETTER, 0, "fit"); assert.equal(r.lostW, 0); assert.equal(r.lostH, 0);
});
test("fit enlarges a small page, shrink never does", () => {
  near(printScale(A5, A4, 0, "fit").scale, 297 / 210);
  assert.equal(printScale(A5, A4, 0, "shrink").scale, 1);
  near(printScale(A4, A5, 0, "shrink").scale, 148 / 210);
});
test("custom percentage and absurd borders stay finite", () => {
  assert.equal(printScale(A4, A4, 0, "custom", 50).w, 105);
  assert.equal(printScale(A4, A4, 500, "fit").impossible, true);
  assert.equal(printScale([26, 37], [26, 37], 13, "fit").impossible, true);
  assert.ok(printScale([26, 37], [26, 37], 12.5, "fit").scale > 0);
});
test("ruler check: fine, reduced, enlarged, uneven", () => {
  assert.equal(diagnose(100, 100).kind, "ok");
  assert.equal(diagnose(99.6, 100.3).kind, "ok");
  assert.equal(diagnose(101, 100).kind, "large");   // one direction off by 1 mm is not "true to size"
  assert.equal(diagnose(100, 99.4).kind, "small");
  const a = diagnose(94, 94); assert.equal(a.kind, "small");
  assert.deepEqual(a.matches.map(m => m.doc + ">" + m.sheet), ["a4>letter", "a5>half"]);   // 279.4 ÷ 297 = 0.941, 139.7 ÷ 148 = 0.944
  near(a.border.a4, 0.06 * 210 / 2, 1e-9); near(a.border.letter, 0.06 * 215.9 / 2, 1e-9);
  // the border the check names must reproduce the measured scale when it is put back into the calculator
  for (const m of [96, 94, 98.5, 90]) { const d = diagnose(m, m); near(printScale(A4, A4, d.border.a4, "fit").scale, m / 100, 1e-9); near(printScale(LETTER, LETTER, d.border.letter, "fit").scale, m / 100, 1e-9); }
  near(diagnose(96, 96).border.a4, 4.2, 1e-9); near(diagnose(96, 96).border.letter, 4.318, 1e-9);
  const b = diagnose(97.3, 97.3); assert.deepEqual(b.matches.map(m => m.doc + ">" + m.sheet), ["letter>a4", "half>a5"]);
  assert.equal(diagnose(141.4, 141.4).kind, "large");
  assert.ok(diagnose(141.4, 141.4).matches.some(m => m.doc === "a5" && m.sheet === "a4"));
  assert.equal(diagnose(94, 100).kind, "uneven");
});
test("numbers: decimal comma, rubbish", () => {
  assert.equal(num("94,5"), 94.5); assert.ok(Number.isNaN(num("<script>"))); assert.ok(Number.isNaN(num("")));
});
test("CSV cells that look like formulas are neutralised", () => {
  for (const bad of ["=1+1", "+1", "-1", "@SUM(A1)", "\tx", "\rx"]) assert.ok(csvCell(bad).replace(/^"/, "").startsWith("'"), bad);
  assert.equal(csvCell("A4"), "A4");
  assert.equal(csvCell('8.5 "x" 11'), '"8.5 ""x"" 11"');
  assert.equal(csvCell("a,b"), '"a,b"');
  assert.equal(toCSV([["Name", "mm"], ["=HYPERLINK(1)", "210 × 297"]]), "Name,mm\r\n'=HYPERLINK(1),210 × 297\r\n");
});
