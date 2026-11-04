// Automatischer Test: Übergangs-Einwilligung "Visitor tally" (nur Statistik) in assets/consent.js.
// Läuft gegen ein gestubbtes DOM, eine gestubbte Uhr (setTimeout) und eine wahlweise fehlende oder
// gestubbte Google-CMP (__tcfapi). Geprüft: kein __tcfapi, displayStatus "hidden", CMP-Entscheidung
// schlägt eigene Wahl, GPC, Ablauf nach 12 Monaten, Widerruf löscht _ga-Cookies, Seiten ohne Werbung.
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const vm = require("vm");
const SRC = fs.readFileSync(__dirname + "/assets/consent.js", "utf8");
const KEY = "pjl-tally", OFF = "ga-disable-G-T00HRG2YVF";
const DAY = 864e5;

// tiny element stub: enough for createElement / querySelector / events / hidden / focus
function el(tag) {
  const e = {
    tagName: tag, dataset: {}, style: { setProperty(k, v) { this[k] = v; } }, attrs: {}, hidden: false, children: {}, handlers: {}, focused: 0, offsetHeight: 180,
    classList: { set: new Set(), add(c) { this.set.add(c); }, remove(c) { this.set.delete(c); }, contains(c) { return this.set.has(c); } },
    setAttribute(k, v) { this.attrs[k] = String(v); }, getAttribute(k) { return this.attrs[k]; },
    addEventListener(ev, fn) { this.handlers[ev] = fn; },
    focus() { this.focused++; },
    querySelector(sel) { return this.children[sel] || (this.children[sel] = el("child:" + sel)); },
    after(x) { this.next = x; }, prepend(x) { this.first = x; }
  };
  return e;
}

function site({ tcf = "none", tc = null, stored, gpc = false, scope, cookies = [] } = {}) {
  const timers = []; let clock = 0;
  const commands = [], updates = [], scripts = [], cookieWrites = [];
  const store = new Map(stored === undefined ? [] : [[KEY, typeof stored === "string" ? stored : JSON.stringify(stored)]]);
  let onClick = null, tcfListener = null;
  const body = el("body"); const skip = el("a.skip");
  let jar = cookies.slice();
  const document = {
    head: { appendChild: s => scripts.push(s) }, body,
    currentScript: scope ? { dataset: { pjlScope: scope } } : null,
    createElement: t => el(t),
    querySelector: sel => (sel === ".skip" ? skip : null),
    querySelectorAll: () => [],
    addEventListener: (ev, fn) => { if (ev === "click") onClick = fn; },
    get cookie() { return jar.join("; "); },
    set cookie(v) {
      cookieWrites.push(v);
      const name = v.split("=")[0];
      if (/expires=Thu, 01 Jan 1970/.test(v)) jar = jar.filter(c => c.split("=")[0] !== name);
    }
  };
  const window = {
    document, navigator: gpc ? { globalPrivacyControl: true } : {}, Date, JSON,
    location: { hostname: "www.printablejoylab.com" },
    localStorage: { getItem: k => (store.has(k) ? store.get(k) : null), setItem: (k, v) => store.set(k, String(v)), removeItem: k => store.delete(k) },
    setTimeout: (fn, ms) => { timers.push({ at: clock + (ms || 0), fn }); return timers.length; },
    gtag: (...a) => { commands.push(a); if (a[0] === "consent" && a[1] === "update") updates.push(a[2]); }
  };
  if (tcf !== "none") window.__tcfapi = (cmd, v, cb) => { if (cmd === "addEventListener") { tcfListener = cb; if (tc) cb(tc, true); } };
  window.window = window;
  vm.runInContext(SRC, vm.createContext(window));
  const advance = ms => {
    const until = clock + ms;
    for (;;) {
      timers.sort((a, b) => a.at - b.at);
      const t = timers[0];
      if (!t || t.at > until) break;
      timers.shift(); clock = t.at; t.fn();
    }
    clock = until;
  };
  const slip = () => skip.next || null;
  const gtm = () => scripts.filter(s => /googletagmanager\.com\/gtag\/js/.test(s.src || ""));
  const opener = el("button");
  const clickSettings = () => onClick({ target: { closest: sel => (sel === "[data-privacy-settings]" ? opener : null) } });
  const shut = () => slip().handlers.click({ target: { closest: sel => (sel === "[data-tally-close]" ? {} : null) } });
  const pick = choice => slip().handlers.click({ target: { closest: sel => (sel === "[data-tally-pick]" ? { getAttribute: () => choice } : null) } });
  return { shut, window, body, commands, updates, scripts, store, advance, slip, gtm, clickSettings, pick, opener, cookieWrites,
    jar: () => jar, fire: t => tcfListener(t, true), last: () => updates[updates.length - 1],
    saved: () => (store.has(KEY) ? JSON.parse(store.get(KEY)) : null) };
}
const shown = p => !!p.slip() && p.slip().hidden === false;
const hiddenTc = { gdprApplies: true, eventStatus: "tcloaded", displayStatus: "hidden", tcString: "", purpose: { consents: {} }, vendor: { consents: {} } };
const adKeys = ["ad_storage", "ad_user_data", "ad_personalization"];
const noAdGrant = p => p.updates.every(u => adKeys.every(k => u[k] === undefined || u[k] === "denied"));

test("no __tcfapi: nothing before ~3 s, then the slip; nothing measured until a choice", () => {
  const p = site();
  p.advance(2900);
  assert.equal(shown(p), false);
  p.advance(200);
  assert.equal(shown(p), true);
  assert.equal(p.slip().attrs.role, "dialog");
  assert.equal(p.slip().attrs["aria-labelledby"], "tally-title");
  assert.equal(p.slip().querySelector("#tally-title").focused, 0, "shown by itself: focus is not stolen");
  assert.equal(p.gtm().length, 0);
  assert.equal(p.window[OFF], true);
});

test("Accept: analytics granted, exactly one gtag.js, config without signals; ad storage never granted; saved with version + time", () => {
  const p = site();
  p.advance(3000 + 10000);   // incl. the 10 s of __tcfapi polling
  p.pick("granted");
  assert.equal(shown(p), false);
  assert.equal(p.last().analytics_storage, "granted");
  assert.equal(p.gtm().length, 1);
  assert.equal(p.window[OFF], false);
  const cfg = p.commands.find(a => a[0] === "config");
  assert.deepEqual({ ...cfg[2] }, { allow_google_signals: false, allow_ad_personalization_signals: false });
  assert.ok(noAdGrant(p));
  const rec = p.saved();
  assert.equal(rec.v, 1); assert.equal(rec.choice, "granted"); assert.ok(Math.abs(rec.at - Date.now()) < 5000);
  p.clickSettings(); p.pick("granted");          // accepting again loads nothing a second time
  assert.equal(p.gtm().length, 1);
});

test("Decline: no gtag.js, analytics denied, ga-disable on; reload respects the stored choice", () => {
  const p = site();
  p.advance(3000);
  p.pick("denied");
  assert.equal(p.gtm().length, 0);
  assert.equal(p.last().analytics_storage, "denied");
  assert.equal(p.window[OFF], true);
  const q = site({ stored: p.saved() });
  q.advance(5000);
  assert.equal(shown(q), false);
  assert.equal(q.gtm().length, 0);
});

test("stored Accept: measured after ~3 s without asking again", () => {
  const p = site({ stored: { v: 1, choice: "granted", at: Date.now() - 30 * DAY } });
  p.advance(2900);
  assert.equal(p.gtm().length, 0, "not before the CMP had its chance");
  p.advance(200);
  assert.equal(shown(p), false);
  assert.equal(p.gtm().length, 1);
});

test("CMP displayStatus hidden without a decision (tcloaded, empty tcString): the slip appears", () => {
  const p = site({ tcf: "stub", tc: hiddenTc });
  p.advance(3000);
  assert.equal(shown(p), true);
  p.pick("granted");
  assert.equal(p.gtm().length, 1);
  p.fire(hiddenTc);                              // further hidden events keep the slip's choice
  p.advance(400);
  assert.equal(p.window[OFF], false);
});

test("a real CMP decision beats the slip: before 3 s, no slip and the stored choice is ignored", () => {
  const deny = { gdprApplies: true, eventStatus: "useractioncomplete", tcString: "CQ-deny", purpose: { consents: {} }, vendor: { consents: {} } };
  const p = site({ tcf: "stub", tc: deny, stored: { v: 1, choice: "granted", at: Date.now() - DAY } });
  p.advance(5000);
  assert.equal(shown(p), false);
  assert.equal(p.gtm().length, 0);
  assert.equal(p.last().analytics_storage, "denied");
  // tcloaded with a non-empty tcString (earlier decision) counts as well
  const q = site({ tcf: "stub", tc: { ...deny, eventStatus: "tcloaded" }, stored: { v: 1, choice: "granted", at: Date.now() - DAY } });
  q.advance(5000);
  assert.equal(shown(q), false);
  assert.equal(q.gtm().length, 0);
});

test("CMP decision after the slip appeared: slip closes, stored slip choice no longer counts", () => {
  const p = site({ tcf: "stub", tc: hiddenTc });
  p.advance(3000);
  p.pick("granted");
  assert.equal(p.gtm().length, 1);
  p.fire({ gdprApplies: true, eventStatus: "useractioncomplete", tcString: "CQ-no", purpose: { consents: {} }, vendor: { consents: {} } });
  assert.equal(p.last().analytics_storage, "denied");
  assert.equal(p.window[OFF], true);
  // and an open slip is closed by the CMP's own message
  const q = site({ tcf: "stub", tc: hiddenTc });
  q.advance(3000);
  assert.equal(shown(q), true);
  q.fire({ ...hiddenTc, eventStatus: "cmpuishown", displayStatus: "visible" });
  assert.equal(shown(q), false);
  q.clickSettings();                             // from now on Google's dialog, not the slip
  assert.equal(shown(q), false);
});

test("gdprApplies === false: no slip", () => {
  const p = site({ tcf: "stub", tc: { gdprApplies: false, eventStatus: "tcloaded", tcString: "" } });
  p.advance(5000);
  assert.equal(shown(p), false);
});

test("Global Privacy Control: no slip pushed, nothing measured even with a stored Accept; settings show a notice only", () => {
  const p = site({ gpc: true, stored: { v: 1, choice: "granted", at: Date.now() - DAY } });
  p.advance(13000);
  assert.equal(shown(p), false);
  assert.equal(p.gtm().length, 0);
  assert.equal(p.window[OFF], true);
  p.clickSettings();
  assert.equal(shown(p), true);
  assert.equal(p.slip().querySelector("[data-tally-picks]").hidden, true);
  assert.equal(p.slip().querySelector("[data-tally-gpc]").hidden, false);
});

test("12 months: an older choice, a future time stamp, another version or garbage → asked again", () => {
  const now = new Date();
  const old = new Date(now); old.setMonth(old.getMonth() - 12); old.setDate(old.getDate() - 1);
  const young = new Date(now); young.setMonth(young.getMonth() - 11);
  for (const stored of [{ v: 1, choice: "granted", at: old.getTime() }, { v: 1, choice: "granted", at: Date.now() + 10 * DAY },
    { v: 0, choice: "granted", at: Date.now() }, { v: 1, choice: "yes", at: Date.now() }, "{broken"]) {
    const p = site({ stored });
    p.advance(3000);
    assert.equal(shown(p), true, JSON.stringify(stored));
    assert.equal(p.gtm().length, 0);
  }
  const q = site({ stored: { v: 1, choice: "granted", at: young.getTime() } });
  q.advance(3000);
  assert.equal(shown(q), false);
  assert.equal(q.gtm().length, 1);
});

test("withdrawal via Privacy settings: slip with the current state, Decline deletes _ga cookies on every domain level", () => {
  const p = site({ stored: { v: 1, choice: "granted", at: Date.now() - DAY }, cookies: ["_ga=GA1.1.1", "_ga_T00HRG2YVF=GS1.1", "pjl=1", "_gat=1", "_gallery=keep"] });
  p.advance(3000);
  assert.equal(p.gtm().length, 1);
  p.clickSettings();
  assert.equal(shown(p), true);
  assert.match(p.slip().querySelector("[data-tally-now]").textContent, /accepted on/);
  assert.equal(p.slip().querySelector("#tally-title").focused, 1, "opened on request: focus moves into the slip");
  p.pick("denied");
  assert.equal(p.last().analytics_storage, "denied");
  assert.equal(p.window[OFF], true);
  assert.deepEqual(p.jar(), ["pjl=1", "_gat=1", "_gallery=keep"]);
  for (const d of ["", "; domain=.www.printablejoylab.com", "; domain=.printablejoylab.com"])
    assert.ok(p.cookieWrites.some(w => w.startsWith("_ga_T00HRG2YVF=;") && w.endsWith("path=/" + d)), d);
  assert.equal(p.saved().choice, "denied");
  assert.ok(p.opener.focused >= 1, "focus returns to the Privacy settings button");
  assert.ok(noAdGrant(p));
});

test("Escape closes the slip without saving and without consent", () => {
  const p = site();
  p.advance(3000);
  let prevented = false;
  p.slip().handlers.keydown({ key: "Escape", preventDefault() { prevented = true; } });
  assert.ok(prevented);
  assert.equal(shown(p), false);
  assert.equal(p.saved(), null);
  assert.equal(p.gtm().length, 0);
});

test("page without ads (data-pjl-scope=settings): no ad code, no Google request, no slip by itself; settings open the slip", () => {
  const p = site({ scope: "settings", stored: { v: 1, choice: "granted", at: Date.now() - DAY }, cookies: ["_ga=GA1.1.1"] });
  p.advance(15000);
  assert.equal(p.scripts.length, 0, "no AdSense loader, no gtag.js");
  assert.equal(shown(p), false);
  p.clickSettings();
  assert.equal(shown(p), true);
  assert.match(p.slip().querySelector("[data-tally-now]").textContent, /accepted on/);
  p.pick("denied");
  assert.equal(p.saved().choice, "denied");
  assert.deepEqual(p.jar(), []);
  p.clickSettings(); p.pick("granted");
  assert.equal(p.scripts.length, 0, "Accept on a page without ads loads nothing there");
});

test("localStorage blocked: slip still works for the page view", () => {
  const p = site();
  p.window.localStorage.getItem = () => { throw new Error("blocked"); };
  p.window.localStorage.setItem = () => { throw new Error("blocked"); };
  p.advance(3000);
  assert.equal(shown(p), true);
  p.pick("granted");
  assert.equal(p.gtm().length, 1);
});

test("V1/V2: own Accept → Google says no → stored slip choice and _ga cookies deleted; reload without tcString asks again, measures nothing", () => {
  const no = { gdprApplies: true, eventStatus: "useractioncomplete", tcString: "CQ-no", purpose: { consents: {} }, vendor: { consents: {} } };
  const p = site({ tcf: "stub", tc: hiddenTc, cookies: ["_ga=GA1.1.1", "_ga_T00HRG2YVF=GS1", "pjl=1"] });
  p.advance(3000);
  p.pick("granted");
  assert.equal(p.gtm().length, 1);
  p.fire(no);
  assert.equal(p.window[OFF], true);
  assert.equal(p.saved(), null, "slip choice deleted on a real Google decision");
  assert.deepEqual(p.jar(), ["pjl=1"], "GA cookies deleted on Google's no");
  const q = site({ tcf: "stub", tc: hiddenTc });            // reload: CMP again only tcloaded with empty tcString
  q.advance(13000);
  assert.equal(q.gtm().length, 0);
  assert.equal(q.window[OFF], true);
  assert.equal(shown(q), true, "the slip asks again");
});

test("V1: Google no on a later page view (slip choice only stored) also deletes choice and cookies; Google yes keeps cookies", () => {
  const no = { gdprApplies: true, eventStatus: "useractioncomplete", tcString: "CQ-no", purpose: { consents: {} }, vendor: { consents: {} } };
  const p = site({ tcf: "stub", tc: no, stored: { v: 1, choice: "granted", at: Date.now() - DAY }, cookies: ["_ga=GA1.1.1"] });
  p.advance(5000);
  assert.equal(p.saved(), null);
  assert.deepEqual(p.jar(), []);
  assert.equal(p.gtm().length, 0);
  const yes = { gdprApplies: true, eventStatus: "useractioncomplete", tcString: "CQ-yes", purpose: { consents: { 1: true } }, vendor: { consents: { 755: true } } };
  const q = site({ tcf: "stub", tc: yes, stored: { v: 1, choice: "granted", at: Date.now() - DAY }, cookies: ["_ga=GA1.1.1"] });
  q.advance(5000);
  assert.equal(q.saved(), null, "stored slip choice deleted on any real decision");
  assert.deepEqual(q.jar(), ["_ga=GA1.1.1"]);
});

test("slip mode: consent updates carry analytics_storage only – no ad_* key at all", () => {
  const p = site({ tcf: "stub", tc: hiddenTc });
  const before = p.updates.length;
  p.advance(3000);
  p.pick("granted"); p.clickSettings(); p.pick("denied");
  p.fire(hiddenTc); p.advance(400);
  const slipUpdates = p.updates.slice(before);
  assert.ok(slipUpdates.length >= 2);
  for (const u of slipUpdates) assert.deepEqual(Object.keys(u), ["analytics_storage"], JSON.stringify(u));
});

test("× closes without deciding: nothing stored, nothing measured, asked again next time", () => {
  const p = site();
  p.advance(3000);
  p.shut();
  assert.equal(shown(p), false);
  assert.equal(p.saved(), null);
  assert.equal(p.gtm().length, 0);
  const q = site();
  q.advance(3000);
  assert.equal(shown(q), true);
});
