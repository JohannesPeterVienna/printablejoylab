/* Printable Joy Lab — one layout engine, two outputs.
   Every template describes its pages as simple drawing operations in millimetres.
   The same operations render the live SVG preview and the vector PDF (jsPDF, loaded on demand). */
(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} }
  };

  /* ------------------------------------------------------------ paper & colours */
  const PAPER = { a4: [210, 297, "A4"], letter: [215.9, 279.4, "US Letter"], a5: [148, 210, "A5"], half: [139.7, 215.9, "Half Letter"] };
  const ACCENTS = { tomato: "#E2553F", teal: "#13857D", ink: "#2B3A67", plum: "#8A4F8B", olive: "#6E7D2B", sand: "#B7894A", mono: "#3A3A3A" };
  const LINES = { light: "#C9CED6", medium: "#9AA3AF", dark: "#5B6472", blue: "#9DB8D9", accent: null };
  const PT = 0.3528; // 1 pt in mm
  const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const DOW = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  const DOWL = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  /* ------------------------------------------------------------ drawing helpers */
  function Page(o) {
    let [w, h] = PAPER[o.paper] || PAPER.a4;
    if (o.orient === "landscape") [w, h] = [h, w];
    const m = (o.paper === "a5" || o.paper === "half") ? 9 : 12;
    const ops = [];
    const accent = ACCENTS[o.accent] || ACCENTS.tomato;
    const lineC = o.lines === "accent" ? accent + "88" : (LINES[o.lines] || LINES.light);
    const P = {
      w, h, m, ops, accent, lineC, x0: m, y0: m, x1: w - m, y1: h - m - 5,
      line(x1, y1, x2, y2, c = lineC, lw = 0.2, dash) { ops.push({ t: "line", x1, y1, x2, y2, c, lw, dash }); },
      rect(x, y, rw, rh, s = { }) { ops.push({ t: "rect", x, y, w: rw, h: rh, stroke: s.stroke ?? lineC, fill: s.fill ?? null, lw: s.lw ?? 0.25, r: s.r ?? 0 }); },
      circle(cx, cy, r, s = {}) { ops.push({ t: "circle", cx, cy, r, stroke: s.stroke ?? null, fill: s.fill ?? lineC, lw: s.lw ?? 0.25 }); },
      text(x, y, txt, s = {}) { ops.push({ t: "text", x, y, txt: String(txt), size: s.size ?? 9, c: s.c ?? "#2B2B2B", align: s.align ?? "left", bold: !!s.bold, serif: !!s.serif, italic: !!s.italic }); },
      title(txt, sub) {
        let y = P.y0 + 9;
        if (txt) { P.text(P.x0, y, txt, { size: 22, serif: o.font === "serif", bold: o.font !== "serif", c: "#1F2430" }); }
        if (sub) P.text(P.x1, y, sub, { size: 10, c: accent, align: "right", bold: true });
        P.line(P.x0, y + 4, P.x1, y + 4, accent, 0.6);
        return y + 9;
      },
      label(x, y, txt) { P.text(x, y, txt.toUpperCase(), { size: 7, c: accent, bold: true }); },
      box(x, y, bw, bh, label, s = {}) {
        P.rect(x, y, bw, bh, { r: 1.6, stroke: s.stroke ?? lineC, lw: 0.3, fill: s.fill ?? null });
        if (label) P.label(x + 3, y + 5, label);
      },
      rules(x, y, rw, bottom, gap, start = 0) { for (let yy = y + start + gap; yy <= bottom + 0.01; yy += gap) P.line(x, yy, x + rw, yy); },
      check(x, y, size = 3.2, round = false) { round ? P.circle(x + size / 2, y + size / 2, size / 2, { stroke: "#8A93A0", fill: null, lw: 0.3 }) : P.rect(x, y, size, size, { stroke: "#8A93A0", lw: 0.3, r: 0.5 }); },
      footer() { if (o.brand !== false) P.text(w / 2, h - m / 2 - 1, "printablejoylab.com", { size: 6.5, c: "#A0A6AF", align: "center" }); }
    };
    return P;
  }

  // Clip an infinite line (point + direction) against a rectangle, return segment or null.
  function clipLine(px, py, dx, dy, x0, y0, x1, y1) {
    let t0 = -1e9, t1 = 1e9;
    const p = [-dx, dx, -dy, dy], q = [px - x0, x1 - px, py - y0, y1 - py];
    for (let i = 0; i < 4; i++) {
      if (Math.abs(p[i]) < 1e-12) { if (q[i] < 0) return null; continue; }
      const r = q[i] / p[i];
      if (p[i] < 0) t0 = Math.max(t0, r); else t1 = Math.min(t1, r);
    }
    return t0 > t1 ? null : [px + t0 * dx, py + t0 * dy, px + t1 * dx, py + t1 * dy];
  }

  /* ------------------------------------------------------------ dates */
  const D = (y, m, d) => new Date(Date.UTC(y, m, d));
  const addDays = (d, n) => new Date(d.getTime() + n * 864e5);
  const dowIdx = (d, ws) => (d.getUTCDay() + 7 - (ws === "sun" ? 0 : 1)) % 7; // 0 = first column
  const isoWeek = d => { const t = D(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()); const day = (t.getUTCDay() + 6) % 7; t.setUTCDate(t.getUTCDate() - day + 3); const f = D(t.getUTCFullYear(), 0, 4); return 1 + Math.round(((t - f) / 864e5 - 3 + ((f.getUTCDay() + 6) % 7)) / 7); };
  const dowNames = ws => ws === "sun" ? [DOW[6], ...DOW.slice(0, 6)] : DOW;
  const parseDate = s => { const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || ""); return m ? D(+m[1], +m[2] - 1, +m[3]) : null; };
  const fmtDay = d => `${DOWL[(d.getUTCDay() + 6) % 7]}, ${MONTHS[d.getUTCMonth()]} ${d.getUTCDate()}, ${d.getUTCFullYear()}`;
  const thisYear = new Date().getFullYear();
  const nextMonday = () => { const t = new Date(); const d = D(t.getFullYear(), t.getMonth(), t.getDate()); return addDays(d, (8 - d.getUTCDay()) % 7 || 7); };
  const iso = d => d.toISOString().slice(0, 10);

  /* ------------------------------------------------------------ common options */
  const O = {
    paper: (def = "a4") => ({ k: "paper", label: "Paper size", type: "select", def, options: [["a4", "A4 (210 × 297 mm)"], ["letter", "US Letter (8.5 × 11 in)"], ["a5", "A5 (148 × 210 mm)"], ["half", "Half Letter (5.5 × 8.5 in)"]] }),
    orient: (def = "portrait") => ({ k: "orient", label: "Orientation", type: "seg", def, options: [["portrait", "Portrait"], ["landscape", "Landscape"]] }),
    accent: () => ({ k: "accent", label: "Accent colour", type: "swatch", def: "tomato", options: Object.keys(ACCENTS) }),
    lines: (def = "light") => ({ k: "lines", label: "Line colour", type: "seg", def, options: [["light", "Light"], ["medium", "Medium"], ["dark", "Dark"], ["blue", "Blue"], ["accent", "Accent"]] }),
    title: def => ({ k: "title", label: "Title", type: "text", def, max: 40 }),
    font: () => ({ k: "font", label: "Title style", type: "seg", def: "sans", options: [["sans", "Clean"], ["serif", "Classic"]] }),
    weekstart: () => ({ k: "ws", label: "Week starts on", type: "seg", def: "mon", options: [["mon", "Monday"], ["sun", "Sunday"]] }),
    year: (def = thisYear) => ({ k: "year", label: "Year", type: "number", def, min: 1900, max: 2100 }),
    month: (allowAll = true) => ({ k: "month", label: "Month", type: "select", def: String(new Date().getMonth()), options: [...(allowAll ? [["all", "All 12 months (12 pages)"]] : []), ...MONTHS.map((m, i) => [String(i), m])] }),
    brand: () => ({ k: "brand", label: "Small site credit in footer", type: "check", def: true })
  };

  /* ------------------------------------------------------------ templates */
  const T = {};

  T["lined-paper"] = {
    opts: [O.paper(), O.orient(), { k: "ruling", label: "Line spacing", type: "select", def: "college", options: [["wide", "Wide ruled (8.7 mm / 11/32 in)"], ["college", "College ruled (7.1 mm / 9/32 in)"], ["narrow", "Narrow ruled (6.35 mm / 1/4 in)"], ["custom", "Custom"]] },
      { k: "gap", label: "Custom spacing (mm)", type: "number", def: 8, min: 3, max: 20, step: 0.5, when: o => o.ruling === "custom" },
      { k: "margin", label: "Red margin line", type: "check", def: true }, { k: "header", label: "Header line for name & date", type: "check", def: true }, O.lines(), O.brand()],
    pages(o) {
      const P = Page(o), gap = { wide: 8.73, college: 7.14, narrow: 6.35 }[o.ruling] || Math.max(3, +o.gap || 8);
      let top = P.y0 + 6;
      if (o.header) { P.text(P.x0, P.y0 + 4, "Name", { size: 7, c: "#8A93A0" }); P.line(P.x0 + 10, P.y0 + 4.5, P.w * .62, P.y0 + 4.5); P.text(P.w * .66, P.y0 + 4, "Date", { size: 7, c: "#8A93A0" }); P.line(P.w * .66 + 9, P.y0 + 4.5, P.x1, P.y0 + 4.5); top = P.y0 + 12; }
      P.rules(0, top, P.w, P.y1, gap);
      if (o.margin) { const mx = o.paper === "a5" || o.paper === "half" ? 22 : 32; P.line(mx, 0, mx, P.h, "#E8A3A3", 0.3); }
      P.footer(); return [P.ops];
    }
  };

  T["graph-paper"] = {
    opts: [O.paper(), O.orient(), { k: "grid", label: "Grid size", type: "select", def: "5", options: [["4", "4 mm"], ["5", "5 mm"], ["6.35", "1/4 inch (4 squares per inch)"], ["5.08", "1/5 inch (5 squares per inch)"], ["10", "1 cm"], ["custom", "Custom"]] },
      { k: "gap", label: "Custom grid (mm)", type: "number", def: 7, min: 2, max: 25, step: 0.5, when: o => o.grid === "custom" },
      { k: "major", label: "Bold line every … squares", type: "select", def: "5", options: [["0", "No bold lines"], ["2", "2"], ["4", "4"], ["5", "5"], ["10", "10"]] }, O.lines(), O.brand()],
    pages(o) {
      const P = Page(o), g = o.grid === "custom" ? Math.max(2, +o.gap || 7) : +o.grid, maj = +o.major;
      const cols = Math.floor((P.x1 - P.x0) / g), rows = Math.floor((P.y1 - P.y0) / g);
      const x0 = (P.w - cols * g) / 2, y0 = P.y0 + ((P.y1 - P.y0) - rows * g) / 2;
      for (let i = 0; i <= cols; i++) { const b = maj && i % maj === 0; P.line(x0 + i * g, y0, x0 + i * g, y0 + rows * g, b ? P.lineC : P.lineC, b ? 0.42 : 0.16); }
      for (let j = 0; j <= rows; j++) { const b = maj && j % maj === 0; P.line(x0, y0 + j * g, x0 + cols * g, y0 + j * g, P.lineC, b ? 0.42 : 0.16); }
      P.footer(); return [P.ops];
    }
  };

  T["dot-grid"] = {
    opts: [O.paper(), O.orient(), { k: "gap", label: "Dot spacing", type: "select", def: "5", options: [["4", "4 mm"], ["5", "5 mm (bullet journal standard)"], ["6.35", "1/4 inch"], ["7", "7 mm"], ["10", "1 cm"]] },
      { k: "size", label: "Dot size", type: "seg", def: "m", options: [["s", "Fine"], ["m", "Medium"], ["l", "Bold"]] }, O.lines("medium"), O.brand()],
    pages(o) {
      const P = Page(o), g = +o.gap, r = { s: 0.18, m: 0.26, l: 0.36 }[o.size];
      const cols = Math.floor((P.x1 - P.x0) / g), rows = Math.floor((P.y1 - P.y0) / g);
      const x0 = (P.w - cols * g) / 2, y0 = P.y0 + ((P.y1 - P.y0) - rows * g) / 2;
      for (let i = 0; i <= cols; i++) for (let j = 0; j <= rows; j++) P.circle(x0 + i * g, y0 + j * g, r, { fill: P.lineC });
      P.footer(); return [P.ops];
    }
  };

  T["isometric-paper"] = {
    opts: [O.paper(), O.orient(), { k: "gap", label: "Triangle size", type: "select", def: "5", options: [["4", "4 mm"], ["5", "5 mm"], ["7", "7 mm"], ["10", "1 cm"]] },
      { k: "style", label: "Style", type: "seg", def: "lines", options: [["lines", "Lines"], ["dots", "Dots"]] }, O.lines(), O.brand()],
    pages(o) {
      const P = Page(o), s = +o.gap, hgt = s * Math.sqrt(3) / 2, X0 = P.x0, Y0 = P.y0, X1 = P.x1, Y1 = P.y1;
      if (o.style === "dots") {
        for (let j = 0, y = Y0; y <= Y1; j++, y = Y0 + j * hgt) for (let x = X0 + (j % 2 ? s / 2 : 0); x <= X1; x += s) P.circle(x, y, 0.28, { fill: P.lineC });
      } else {
        for (let x = X0; x <= X1 + 0.01; x += hgt) P.line(x, Y0, x, Y1, P.lineC, 0.16); // vertical
        const dirs = [[Math.cos(Math.PI / 6), Math.sin(Math.PI / 6)], [Math.cos(-Math.PI / 6), Math.sin(-Math.PI / 6)]];
        const span = (X1 - X0) + (Y1 - Y0) * 2;
        for (const [dx, dy] of dirs) for (let k = -span; k <= span; k += s) {
          const seg = clipLine(X0, Y0 + k, dx, dy, X0, Y0, X1, Y1); if (seg) P.line(...seg, P.lineC, 0.16);
        }
        P.rect(X0, Y0, X1 - X0, Y1 - Y0, { stroke: P.lineC, lw: 0.2 });
      }
      P.footer(); return [P.ops];
    }
  };

  T["monthly-calendar"] = {
    opts: [O.year(), O.month(true), O.weekstart(), O.paper(), O.orient("landscape"), { k: "weeks", label: "Show week numbers", type: "check", def: true },
      { k: "notes", label: "Notes column", type: "check", def: true }, O.accent(), O.font(), O.brand()],
    pages(o) {
      const months = o.month === "all" ? [...Array(12).keys()] : [+o.month || 0], y = +o.year || thisYear;
      return months.map(mi => {
        const P = Page(o), top = P.title(MONTHS[mi], String(y));
        const notesW = o.notes ? (P.w > P.h ? 52 : 0) : 0;
        const gx = P.x0 + (o.weeks ? 7 : 0), gw = P.x1 - gx - (notesW ? notesW + 5 : 0);
        const first = D(y, mi, 1), lead = dowIdx(first, o.ws), days = new Date(Date.UTC(y, mi + 1, 0)).getUTCDate();
        const rowsN = Math.ceil((lead + days) / 7), hy = top + 2, cw = gw / 7, rh = (P.y1 - hy - 7 - (o.notes && !notesW ? 30 : 0)) / rowsN;
        dowNames(o.ws).forEach((n, i) => { P.rect(gx + i * cw, hy, cw, 6, { fill: P.accent, stroke: P.accent, lw: 0.1 }); P.text(gx + i * cw + cw / 2, hy + 4.2, n.toUpperCase(), { size: 7.5, c: "#fff", bold: true, align: "center" }); });
        for (let r = 0; r < rowsN; r++) for (let c = 0; c < 7; c++) {
          const idx = r * 7 + c - lead + 1, x = gx + c * cw, yy = hy + 6 + r * rh;
          const we = (o.ws === "sun" ? (c === 0 || c === 6) : c >= 5);
          P.rect(x, yy, cw, rh, { stroke: P.lineC, lw: 0.25, fill: we ? "#F6F4F0" : null });
          if (idx >= 1 && idx <= days) P.text(x + 2, yy + 5, idx, { size: 10, bold: true, c: we ? P.accent : "#2B2B2B" });
          if (o.weeks && c === 0) { const rowStart = addDays(first, r * 7 - lead); P.text(P.x0 + 2.5, yy + 5, isoWeek(addDays(rowStart, o.ws === "sun" ? 1 : 0)), { size: 6.5, c: "#A0A6AF", align: "center" }); }
        }
        if (notesW) { const nx = P.x1 - notesW; P.box(nx, hy, notesW, P.y1 - hy - 1, "Notes"); P.rules(nx + 3, hy + 6, notesW - 6, P.y1 - 4, 7); }
        else if (o.notes) { const ny = hy + 6 + rowsN * rh + 4; P.box(P.x0, ny, P.x1 - P.x0, P.y1 - ny - 1, "Notes"); P.rules(P.x0 + 3, ny + 6, P.x1 - P.x0 - 6, P.y1 - 4, 7); }
        P.footer(); return P.ops;
      });
    }
  };

  T["yearly-calendar"] = {
    opts: [O.year(new Date().getMonth() >= 9 ? thisYear + 1 : thisYear), O.weekstart(), O.paper(), O.orient("portrait"), { k: "fill", label: "Shade weekends", type: "check", def: true }, O.accent(), O.font(), O.brand()],
    pages(o) {
      const P = Page(o), y = +o.year || thisYear, top = P.title(String(y), "Year at a glance");
      const cols = P.w > P.h ? 4 : 3, rows = 12 / cols, gapX = 6, gapY = 5;
      const bw = (P.x1 - P.x0 - gapX * (cols - 1)) / cols, bh = (P.y1 - top - gapY * (rows - 1)) / rows, names = dowNames(o.ws);
      for (let mi = 0; mi < 12; mi++) {
        const bx = P.x0 + (mi % cols) * (bw + gapX), by = top + Math.floor(mi / cols) * (bh + gapY), cw = bw / 7, ch = (bh - 12) / 6;
        P.text(bx, by + 4.5, MONTHS[mi].toUpperCase(), { size: 8.5, bold: true, c: P.accent });
        names.forEach((n, i) => P.text(bx + i * cw + cw / 2, by + 9.5, n[0], { size: 6.5, c: "#8A93A0", align: "center", bold: true }));
        const lead = dowIdx(D(y, mi, 1), o.ws), days = new Date(Date.UTC(y, mi + 1, 0)).getUTCDate();
        for (let d = 1; d <= days; d++) {
          const k = lead + d - 1, c = k % 7, r = Math.floor(k / 7), we = o.ws === "sun" ? (c === 0 || c === 6) : c >= 5;
          if (o.fill && we) P.rect(bx + c * cw + 0.4, by + 11 + r * ch + 0.3, cw - 0.8, ch - 0.6, { fill: "#F2EFEA", stroke: "#F2EFEA", lw: 0.01, r: 0.8 });
          P.text(bx + c * cw + cw / 2, by + 11 + r * ch + ch * 0.68, d, { size: Math.min(8, ch * 1.6), align: "center", c: we ? P.accent : "#2B2B2B" });
        }
      }
      P.footer(); return [P.ops];
    }
  };

  T["weekly-planner"] = {
    opts: [{ k: "start", label: "Week starting (leave empty for undated)", type: "date", def: iso(nextMonday()) }, O.paper(), O.orient("landscape"),
      { k: "todo", label: "To-do column", type: "check", def: true }, { k: "lines", label: "Writing lines in day boxes", type: "check", def: true }, O.title("Weekly plan"), O.accent(), O.font(), O.brand()],
    pages(o) {
      const P = Page({ ...o, lines: "light" }), start = parseDate(o.start);
      const sub = start ? `${MONTHS[start.getUTCMonth()].slice(0, 3)} ${start.getUTCDate()} – ${(e => `${MONTHS[e.getUTCMonth()].slice(0, 3)} ${e.getUTCDate()}, ${e.getUTCFullYear()}`)(addDays(start, 6))}` : "Week of ____________";
      const top = P.title(o.title, sub), land = P.w > P.h, side = o.todo ? (land ? 60 : 0) : 0;
      const gx = P.x0, gw = P.x1 - P.x0 - (side ? side + 5 : 0), gap = 4;
      const cols = land ? 4 : 2, rows = 2 + (land ? 0 : 2), bw = (gw - gap * (cols - 1)) / cols, bottom = P.y1 - (o.todo && !side ? 46 : 0);
      const bh = (bottom - top - gap * (rows - 1)) / rows;
      const cells = []; for (let i = 0; i < 7; i++) cells.push(i); cells.push("notes");
      cells.forEach((c, i) => {
        const x = gx + (i % cols) * (bw + gap), y = top + Math.floor(i / cols) * (bh + gap);
        const lbl = c === "notes" ? "Notes" : (start ? `${DOWL[(addDays(start, c).getUTCDay() + 6) % 7]} ${addDays(start, c).getUTCDate()}` : DOWL[c]);
        P.box(x, y, bw, bh, lbl, { fill: c === 5 || c === 6 ? "#FBF8F3" : null });
        if (o.lines) P.rules(x + 3, y + 7, bw - 6, y + bh - 2, 6.5);
      });
      if (o.todo) {
        const x = side ? P.x1 - side : P.x0, y = side ? top : bottom + gap, w = side || (P.x1 - P.x0), h = side ? P.y1 - top : P.y1 - y;
        P.box(x, y, w, h, "To do this week");
        for (let yy = y + 10; yy < y + h - 4; yy += 7) { P.check(x + 3, yy - 2.8); P.line(x + 8.5, yy + 0.4, x + w - 3, yy + 0.4); }
      }
      P.footer(); return [P.ops];
    }
  };

  T["daily-planner"] = {
    opts: [{ k: "date", label: "Date (leave empty for undated)", type: "date", def: "" }, { k: "from", label: "Schedule from", type: "select", def: "6", options: [...Array(13).keys()].map(h => [String(h + 4), `${h + 4}:00`]) },
      { k: "to", label: "Schedule until", type: "select", def: "21", options: [...Array(12).keys()].map(h => [String(h + 13), `${h + 13}:00`]) }, { k: "half", label: "Half-hour slots", type: "check", def: false },
      { k: "water", label: "Water tracker", type: "check", def: true }, { k: "grat", label: "Gratitude & reflection", type: "check", def: true }, O.paper(), O.title("Today"), O.accent(), O.font(), O.brand()],
    pages(o) {
      const P = Page({ ...o, orient: "portrait", lines: "light" }), d = parseDate(o.date), top = P.title(o.title, d ? fmtDay(d) : "Date: ____________");
      const colW = (P.x1 - P.x0 - 5) / 2, lx = P.x0, rx = P.x0 + colW + 5;
      const from = +o.from, to = Math.max(+o.to, from + 1), slots = (to - from) * (o.half ? 2 : 1) + 1;
      const sh = (P.y1 - top - 7) / slots;
      P.box(lx, top, colW, P.y1 - top, "Schedule");
      for (let i = 0; i < slots; i++) {
        const yy = top + 7 + i * sh, hr = from + (o.half ? i / 2 : i), full = Number.isInteger(hr);
        P.line(lx + 14, yy + sh, lx + colW - 3, yy + sh, P.lineC, full ? 0.25 : 0.15, full ? null : [0.8, 0.8]);
        if (full) P.text(lx + 3, yy + sh * 0.7, `${String(hr).padStart(2, "0")}:00`, { size: 7, c: "#6B7380" });
      }
      let y = top; const H = P.y1 - top, part = (h, label, fn) => { P.box(rx, y, colW, h, label); fn && fn(y, h); y += h + 4; };
      part(H * 0.2, "Top 3 priorities", (yy, h) => { for (let i = 0; i < 3; i++) { const t = yy + 11 + i * ((h - 13) / 3); P.text(rx + 4, t, i + 1, { size: 9, bold: true, c: P.accent }); P.line(rx + 9, t + 0.6, rx + colW - 3, t + 0.6); } });
      part(H * 0.32, "To do", (yy, h) => { for (let t = yy + 10; t < yy + h - 3; t += 6.5) { P.check(rx + 3, t - 2.8); P.line(rx + 8.5, t + 0.4, rx + colW - 3, t + 0.4); } });
      const rest = P.y1 - y - (o.water ? 18 : 0) - (o.grat ? H * 0.17 + 4 : 0);
      part(rest, "Notes", (yy, h) => P.rules(rx + 3, yy + 5, colW - 6, yy + h - 2, 6.5));
      if (o.grat) part(H * 0.17, "Grateful for", (yy, h) => P.rules(rx + 3, yy + 5, colW - 6, yy + h - 2, 6.5));
      if (o.water) part(14, "Water", (yy) => { for (let i = 0; i < 8; i++) P.rect(rx + 22 + i * ((colW - 26) / 8), yy + 3, (colW - 26) / 8 - 2, 8, { r: 1.2, stroke: P.accent, lw: 0.3 }); });
      P.footer(); return [P.ops];
    }
  };

  T["habit-tracker"] = {
    opts: [O.year(), O.month(true), { k: "habits", label: "Habits (one per line, up to 15)", type: "textarea", def: "Read 20 pages\nWalk 8,000 steps\nNo phone after 10 pm\nDrink water\nStretch\nJournal\nLearn something new" },
      { k: "rows", label: "Extra empty rows", type: "number", def: 3, min: 0, max: 10 }, O.paper(), O.orient("landscape"), O.accent(), O.font(), O.brand()],
    pages(o) {
      const months = o.month === "all" ? [...Array(12).keys()] : [+o.month || 0], y = +o.year || thisYear;
      const list = String(o.habits || "").split("\n").map(s => s.trim()).filter(Boolean).slice(0, 15);
      const n = Math.min(24, list.length + Math.max(0, Math.min(24, +o.rows || 0)));
      return months.map(mi => {
        const P = Page({ ...o, lines: "light" }), top = P.title("Habit tracker", `${MONTHS[mi]} ${y}`), days = new Date(Date.UTC(y, mi + 1, 0)).getUTCDate();
        const nameW = Math.min(62, (P.x1 - P.x0) * 0.3), cw = (P.x1 - P.x0 - nameW - 12) / days, rh = Math.min(10, (P.y1 - top - 10) / Math.max(n, 1));
        for (let d = 1; d <= days; d++) { const dt = D(y, mi, d), we = dt.getUTCDay() % 6 === 0, x = P.x0 + nameW + (d - 1) * cw;
          P.text(x + cw / 2, top + 3, DOW[(dt.getUTCDay() + 6) % 7][0], { size: 6, c: "#9AA3AF", align: "center" }); P.text(x + cw / 2, top + 7.5, d, { size: 7, c: we ? P.accent : "#2B2B2B", align: "center", bold: true }); }
        P.text(P.x1 - 5, top + 7.5, "DONE", { size: 5.5, c: P.accent, align: "center", bold: true });
        for (let r = 0; r < n; r++) {
          const yy = top + 10 + r * rh;
          P.rect(P.x0, yy, P.x1 - P.x0, rh, { stroke: P.lineC, lw: 0.2, fill: r % 2 ? "#FAF8F5" : null });
          if (list[r]) P.text(P.x0 + 2.5, yy + rh * 0.65, list[r].slice(0, 32), { size: Math.min(8.5, rh * 1.5) });
          for (let d = 0; d < days; d++) P.circle(P.x0 + nameW + d * cw + cw / 2, yy + rh / 2, Math.min(cw, rh) * 0.3, { stroke: "#B8BFC9", fill: null, lw: 0.25 });
          P.rect(P.x1 - 10, yy + 1.2, 9, rh - 2.4, { stroke: "#B8BFC9", lw: 0.25, r: 1 });
        }
        P.footer(); return P.ops;
      });
    }
  };

  T["checklist"] = {
    opts: [O.title("Checklist"), { k: "items", label: "Number of lines", type: "number", def: 25, min: 5, max: 60 }, { k: "cols", label: "Columns", type: "seg", def: "1", options: [["1", "One"], ["2", "Two"]] },
      { k: "style", label: "Checkbox", type: "seg", def: "square", options: [["square", "Square"], ["round", "Round"], ["number", "Numbered"]] },
      { k: "prefill", label: "Pre-filled items (optional, one per line)", type: "textarea", def: "" }, { k: "prio", label: "Priority column", type: "check", def: false }, O.paper(), O.accent(), O.font(), O.brand()],
    pages(o) {
      const P = Page({ ...o, orient: "portrait" }), top = P.title(o.title, ""), cols = +o.cols, per = Math.ceil(Math.max(5, Math.min(60, +o.items || 25)) / cols);
      const items = String(o.prefill || "").split("\n").map(s => s.trim()).filter(Boolean);
      const cw = (P.x1 - P.x0 - (cols - 1) * 8) / cols, gap = Math.min(10, (P.y1 - top - 4) / per);
      let k = 0;
      for (let c = 0; c < cols; c++) for (let i = 0; i < per; i++, k++) {
        const x = P.x0 + c * (cw + 8), yy = top + 4 + (i + 1) * gap;
        if (o.style === "number") P.text(x + 3, yy - 0.8, `${k + 1}.`, { size: 8, c: P.accent, bold: true, align: "right" }); else P.check(x, yy - 4, 3.6, o.style === "round");
        const end = x + cw - (o.prio ? 12 : 0);
        P.line(x + 6, yy, end, yy);
        if (items[k]) P.text(x + 7, yy - 1.4, items[k].slice(0, 60), { size: 9 });
        if (o.prio) { P.text(end + 6, yy - 1.4, "· · ·", { size: 8, c: "#B8BFC9", align: "center" }); }
      }
      P.footer(); return [P.ops];
    }
  };

  T["meal-planner"] = {
    opts: [{ k: "start", label: "Week starting (optional)", type: "date", def: "" }, { k: "meals", label: "Meals", type: "select", def: "bld", options: [["bld", "Breakfast, lunch, dinner"], ["blds", "Breakfast, lunch, dinner, snacks"], ["ld", "Lunch & dinner"], ["d", "Dinner only"]] },
      O.weekstart(), { k: "grocery", label: "Grocery list", type: "check", def: true }, O.paper(), O.orient("landscape"), O.title("Meal plan"), O.accent(), O.font(), O.brand()],
    pages(o) {
      const P = Page({ ...o, lines: "light" }), s = parseDate(o.start);
      const top = P.title(o.title, s ? `Week of ${MONTHS[s.getUTCMonth()]} ${s.getUTCDate()}, ${s.getUTCFullYear()}` : "Week of ____________");
      const meals = { bld: ["Breakfast", "Lunch", "Dinner"], blds: ["Breakfast", "Lunch", "Dinner", "Snacks"], ld: ["Lunch", "Dinner"], d: ["Dinner"] }[o.meals];
      const land = P.w > P.h, gW = o.grocery ? (land ? 62 : 0) : 0, gx = P.x0 + 18, gw = P.x1 - gx - (gW ? gW + 5 : 0);
      const bottom = P.y1 - (o.grocery && !gW ? 52 : 0), cw = gw / 7, rh = (bottom - top - 7) / meals.length;
      const names = dowNames(o.ws);
      names.forEach((n, i) => { const lbl = s ? `${n} ${addDays(s, i).getUTCDate()}` : n; P.rect(gx + i * cw, top, cw, 6, { fill: P.accent, stroke: P.accent, lw: 0.1 }); P.text(gx + i * cw + cw / 2, top + 4.2, lbl.toUpperCase(), { size: 7, c: "#fff", bold: true, align: "center" }); });
      meals.forEach((m, r) => { const yy = top + 6 + r * rh; P.text(P.x0, yy + 5, m.toUpperCase(), { size: 6.5, c: P.accent, bold: true });
        for (let c = 0; c < 7; c++) P.rect(gx + c * cw, yy, cw, rh, { stroke: P.lineC, lw: 0.25 }); });
      if (o.grocery) {
        const x = gW ? P.x1 - gW : P.x0, y = gW ? top : bottom + 5, w = gW || P.x1 - P.x0, h = gW ? P.y1 - top : P.y1 - y;
        P.box(x, y, w, h, "Grocery list");
        const cats = ["Produce", "Protein", "Dairy", "Pantry", "Other"], colsN = gW ? 1 : 5, cwid = (w - 6) / colsN, per = gW ? h / 5 : h;
        cats.forEach((c, i) => { const cx = x + 3 + (gW ? 0 : i * cwid), cy = y + 8 + (gW ? i * ((h - 8) / 5) : 0);
          P.text(cx, cy + 2, c, { size: 7, bold: true, c: "#6B7380" });
          for (let t = cy + 8; t < cy + (gW ? (h - 8) / 5 : h - 10) - 1; t += 5.5) { P.check(cx, t - 2.6, 2.8); P.line(cx + 4.5, t + 0.2, cx + cwid - 3, t + 0.2); } });
      }
      P.footer(); return [P.ops];
    }
  };

  T["budget-planner"] = {
    opts: [O.year(), O.month(true), { k: "cur", label: "Currency symbol", type: "select", def: "$", options: [["$", "$"], ["€", "€"], ["£", "£"], ["", "none"]] },
      { k: "cats", label: "Expense categories (one per line)", type: "textarea", def: "Rent / mortgage\nUtilities\nGroceries\nTransport\nInsurance\nPhone & internet\nSubscriptions\nEating out\nHealth\nShopping\nGifts\nSavings\nOther" },
      O.paper(), O.title("Monthly budget"), O.accent(), O.font(), O.brand()],
    pages(o) {
      const months = o.month === "all" ? [...Array(12).keys()] : [+o.month || 0], y = +o.year || thisYear, cur = o.cur || "";
      const cats = String(o.cats || "").split("\n").map(s => s.trim()).filter(Boolean).slice(0, 18);
      return months.map(mi => {
        const P = Page({ ...o, orient: "portrait", lines: "light" }), top = P.title(o.title, `${MONTHS[mi]} ${y}`), W = P.x1 - P.x0;
        // summary strip
        const sumH = 18, sw = (W - 9) / 4;
        ["Income", "Expenses", "Saved", "Left over"].forEach((l, i) => { P.box(P.x0 + i * (sw + 3), top, sw, sumH, l, { fill: i === 3 ? "#FBF6EE" : null }); P.text(P.x0 + i * (sw + 3) + 3, top + 14, cur, { size: 11, c: "#9AA3AF" }); });
        // income table
        let yy = top + sumH + 6;
        const table = (label, rows, h) => {
          P.box(P.x0, yy, W, h, label);
          const cx = [P.x0 + W * 0.55, P.x0 + W * 0.775];
          P.text(cx[0] - 3, yy + 5, "PLANNED", { size: 6.5, c: "#9AA3AF", align: "right", bold: true }); P.text(cx[1] - 3, yy + 5, "ACTUAL", { size: 6.5, c: "#9AA3AF", align: "right", bold: true }); P.text(P.x1 - 3, yy + 5, "DIFFERENCE", { size: 6.5, c: "#9AA3AF", align: "right", bold: true });
          const rh = (h - 9) / rows.length;
          rows.forEach((r, i) => { const ty = yy + 8 + (i + 1) * rh; P.line(P.x0 + 3, ty, P.x1 - 3, ty, P.lineC, 0.2); if (r) P.text(P.x0 + 4, ty - rh * 0.3, r, { size: Math.min(8.5, rh * 1.3) });
            cx.forEach(x => P.line(x, ty - rh + 1, x, ty - 0.5, "#E4E7EC", 0.2)); });
          yy += h + 5;
        };
        table("Income", ["Salary", "Side income", "Other", "Total income"], 38);
        table("Expenses", [...cats, "Total expenses"], P.y1 - yy - 26);
        P.box(P.x0, yy, W, P.y1 - yy, "Notes & goals"); P.rules(P.x0 + 3, yy + 5, W - 6, P.y1 - 2, 6.5);
        P.footer(); return P.ops;
      });
    }
  };

  /* ------------------------------------------------------------ output: SVG */
  const esc = s => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
  function toSVG(ops, w, h) {
    let s = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}mm" height="${h}mm"><rect width="${w}" height="${h}" fill="#fff"/>`;
    for (const o of ops) {
      if (o.t === "line") s += `<line x1="${o.x1.toFixed(2)}" y1="${o.y1.toFixed(2)}" x2="${o.x2.toFixed(2)}" y2="${o.y2.toFixed(2)}" stroke="${o.c}" stroke-width="${o.lw}"${o.dash ? ` stroke-dasharray="${o.dash.join(" ")}"` : ""}/>`;
      else if (o.t === "rect") s += `<rect x="${o.x.toFixed(2)}" y="${o.y.toFixed(2)}" width="${o.w.toFixed(2)}" height="${o.h.toFixed(2)}" rx="${o.r}" fill="${o.fill || "none"}" stroke="${o.stroke || "none"}" stroke-width="${o.lw}"/>`;
      else if (o.t === "circle") s += `<circle cx="${o.cx.toFixed(2)}" cy="${o.cy.toFixed(2)}" r="${o.r.toFixed(2)}" fill="${o.fill || "none"}" stroke="${o.stroke || "none"}" stroke-width="${o.lw}"/>`;
      else if (o.t === "text") s += `<text x="${o.x.toFixed(2)}" y="${o.y.toFixed(2)}" font-size="${(o.size * PT).toFixed(2)}" fill="${o.c}" text-anchor="${o.align === "center" ? "middle" : o.align === "right" ? "end" : "start"}" font-family="${o.serif ? "Times New Roman, Times, serif" : "Helvetica, Arial, sans-serif"}"${o.bold ? ' font-weight="700"' : ""}${o.italic ? ' font-style="italic"' : ""}>${esc(o.txt)}</text>`;
    }
    return s + "</svg>";
  }

  /* ------------------------------------------------------------ output: PDF */
  let jsPDFLoading;
  const loadPDF = () => jsPDFLoading ||= new Promise((res, rej) => { if (window.jspdf) return res(window.jspdf.jsPDF); const s = document.createElement("script"); s.src = "/assets/jspdf.umd.min.js"; s.onload = () => res(window.jspdf.jsPDF); s.onerror = rej; document.head.appendChild(s); });
  const hex = c => { let h = c.replace("#", ""); if (h.length === 3 || h.length === 4) h = h.slice(0, 3).split("").map(x => x + x).join(""); h = h.slice(0, 6); return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)]; };
  const alphaMix = c => { const h = c.replace("#", ""); if (h.length < 8) return hex(c); const a = parseInt(h.slice(6, 8), 16) / 255; return hex(c).map(v => Math.round(v * a + 255 * (1 - a))); };
  function drawInto(doc, pages, w, h, first = true) {
    pages.forEach((ops, i) => {
      if (i || !first) doc.addPage([w, h], w > h ? "landscape" : "portrait");
      for (const o of ops) {
        if (o.t === "line") { doc.setDrawColor(...alphaMix(o.c)); doc.setLineWidth(o.lw); doc.setLineDashPattern(o.dash || [], 0); doc.line(o.x1, o.y1, o.x2, o.y2); doc.setLineDashPattern([], 0); }
        else if (o.t === "rect") { const st = o.fill && o.stroke ? "FD" : o.fill ? "F" : "S"; if (o.fill) doc.setFillColor(...alphaMix(o.fill)); if (o.stroke) { doc.setDrawColor(...alphaMix(o.stroke)); doc.setLineWidth(o.lw); } if (!o.fill && !o.stroke) continue; o.r ? doc.roundedRect(o.x, o.y, o.w, o.h, o.r, o.r, st) : doc.rect(o.x, o.y, o.w, o.h, st); }
        else if (o.t === "circle") { const st = o.fill && o.stroke ? "FD" : o.fill ? "F" : "S"; if (o.fill) doc.setFillColor(...alphaMix(o.fill)); if (o.stroke) { doc.setDrawColor(...alphaMix(o.stroke)); doc.setLineWidth(o.lw); } doc.circle(o.cx, o.cy, o.r, st); }
        else if (o.t === "text") { doc.setFont(o.serif ? "times" : "helvetica", o.bold ? (o.italic ? "bolditalic" : "bold") : (o.italic ? "italic" : "normal")); doc.setFontSize(o.size); doc.setTextColor(...hex(o.c)); doc.text(o.txt, o.x, o.y, { align: o.align }); }
      }
    });
  }
  async function toPDF(pages, w, h, name) {
    const jsPDF = await loadPDF();
    const doc = new jsPDF({ unit: "mm", format: [w, h], orientation: w > h ? "landscape" : "portrait", compress: true });
    doc.setProperties({ title: name, creator: "Printable Joy Lab – printablejoylab.com" });
    drawInto(doc, pages, w, h);
    doc.save(name);
  }

  /* ------------------------------------------------------------ UI */
  function readOpts(form, tpl) {
    const o = {};
    for (const d of tpl.opts) {
      const el = form.elements[d.k]; if (!el) { o[d.k] = d.def; continue; }
      o[d.k] = d.type === "check" ? el.checked : (el.value ?? d.def);
    }
    return o;
  }
  function controlHTML(d, v) {
    const id = `opt-${d.k}`;
    if (d.type === "select") return `<label class="f" for="${id}"><span>${d.label}</span><select id="${id}" name="${d.k}">${d.options.map(([val, t]) => `<option value="${val}"${String(v) === val ? " selected" : ""}>${t}</option>`).join("")}</select></label>`;
    if (d.type === "seg") return `<fieldset class="f seg"><legend>${d.label}</legend><div>${d.options.map(([val, t]) => `<label><input type="radio" name="${d.k}" value="${val}"${String(v) === val ? " checked" : ""}><span>${t}</span></label>`).join("")}</div></fieldset>`;
    if (d.type === "swatch") return `<fieldset class="f sw"><legend>${d.label}</legend><div>${d.options.map(val => `<label title="${val}"><input type="radio" name="${d.k}" value="${val}"${v === val ? " checked" : ""}><span style="--c:${ACCENTS[val]}"></span><b class="sr">${val}</b></label>`).join("")}</div></fieldset>`;
    if (d.type === "check") return `<label class="f chk"><input type="checkbox" name="${d.k}"${v ? " checked" : ""}><span>${d.label}</span></label>`;
    if (d.type === "textarea") return `<label class="f" for="${id}"><span>${d.label}</span><textarea id="${id}" name="${d.k}" rows="5">${esc(String(v ?? ""))}</textarea></label>`;
    const extra = d.type === "number" ? ` inputmode="decimal" min="${d.min ?? ""}" max="${d.max ?? ""}" step="${d.step ?? 1}"` : d.type === "text" ? ` maxlength="${d.max || 60}"` : "";
    return `<label class="f" for="${id}"><span>${d.label}</span><input id="${id}" type="${d.type}" name="${d.k}" value="${esc(String(v ?? ""))}"${extra}></label>`;
  }

  function initLab(root) {
    const key = root.dataset.lab, tpl = T[key]; if (!tpl) return;
    const form = $("[data-controls]", root), stage = $("[data-stage]", root), info = $("[data-info]", root);
    const q = new URLSearchParams(location.search), saved = store.get(`pjl-${key}`, {});
    const val = d => q.has(d.k) ? (d.type === "check" ? q.get(d.k) === "1" : q.get(d.k)) : (d.k in saved ? saved[d.k] : d.def);
    form.innerHTML = tpl.opts.map(d => `<div class="ctl" data-k="${d.k}">${controlHTML(d, val(d))}</div>`).join("");
    let page = 0, pages = [], dims = [210, 297];
    function render() {
      const o = readOpts(form, tpl);
      tpl.opts.forEach(d => { if (d.when) $(`.ctl[data-k="${d.k}"]`, form).hidden = !d.when(o); });
      try { pages = tpl.pages(o); } catch (e) { console.error(e); stage.innerHTML = `<p class="err">This combination could not be drawn. Try other settings.</p>`; return; }
      const P = Page(o); dims = [P.w, P.h];
      page = Math.min(page, pages.length - 1);
      stage.innerHTML = `<div class="sheet" style="aspect-ratio:${P.w}/${P.h};--ar:${(P.w / P.h).toFixed(3)}">${toSVG(pages[page], P.w, P.h)}</div>`;
      info.innerHTML = `${(PAPER[o.paper] || PAPER.a4)[2]} · ${P.w > P.h ? "landscape" : "portrait"} · ${pages.length} page${pages.length > 1 ? "s" : ""}` +
        (pages.length > 1 ? ` <span class="pager"><button type="button" data-prev aria-label="Previous page">‹</button> ${page + 1} / ${pages.length} <button type="button" data-next aria-label="Next page">›</button></span>` : "");
      store.set(`pjl-${key}`, o);
    }
    form.addEventListener("input", render); form.addEventListener("change", render);
    info.addEventListener("click", e => { if (e.target.closest("[data-prev]")) { page = (page - 1 + pages.length) % pages.length; render(); } if (e.target.closest("[data-next]")) { page = (page + 1) % pages.length; render(); } });
    $("[data-pdf]", root).addEventListener("click", async e => {
      const b = e.currentTarget, t = b.textContent; b.disabled = true; b.textContent = "Creating PDF …";
      try { await toPDF(pages, dims[0], dims[1], `${key}-${readOpts(form, tpl).paper}.pdf`); if (window.gtag) gtag("event", "pdf_download", { template: key }); }
      catch (err) { console.error(err); info.insertAdjacentHTML("beforeend", ` <span class="err">PDF could not be created – please try again or use Print.</span>`); }
      b.disabled = false; b.textContent = t;
    });
    $("[data-print]", root).addEventListener("click", () => {
      let st = $("#pjl-print"); if (!st) { st = document.createElement("style"); st.id = "pjl-print"; document.head.appendChild(st); }
      st.textContent = `@page{size:${dims[0]}mm ${dims[1]}mm;margin:0}`;
      let box = $("#print-pages"); if (!box) { box = document.createElement("div"); box.id = "print-pages"; document.body.appendChild(box); }
      box.innerHTML = pages.map(p => `<div class="pp">${toSVG(p, dims[0], dims[1])}</div>`).join("");
      window.print();
    });
    $("[data-share]", root).addEventListener("click", async e => {
      const o = readOpts(form, tpl), qs = new URLSearchParams();
      tpl.opts.forEach(d => { const v = o[d.k]; if (String(v) !== String(d.def)) qs.set(d.k, d.type === "check" ? (v ? "1" : "0") : v); });
      const url = `${location.origin}${location.pathname}${qs.toString() ? "?" + qs : ""}`;
      try { await navigator.clipboard.writeText(url); e.currentTarget.textContent = "Link copied ✓"; } catch { history.replaceState(null, "", url); e.currentTarget.textContent = "Link is in the address bar"; }
    });
    $("[data-reset]", root).addEventListener("click", () => { store.set(`pjl-${key}`, {}); location.href = location.pathname; });
    render();
  }

  // Thumbnails on overview pages
  function thumbs() {
    $$("[data-thumb]").forEach(el => {
      const tpl = T[el.dataset.thumb]; if (!tpl) return;
      const o = {}; tpl.opts.forEach(d => o[d.k] = d.def); if (el.dataset.accent) o.accent = el.dataset.accent;
      if (typeof o.lines === "string") o.lines = "dark"; // thumbnails are tiny – make lines visible
      const P = Page(o); el.innerHTML = toSVG(tpl.pages(o)[0], P.w, P.h);
    });
  }

  window.PJL = { T, Page, toSVG, PAPER, drawInto }; // used by tests
  const init = () => { $$("[data-lab]").forEach(initLab); thumbs(); };
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", init) : init();
})();
