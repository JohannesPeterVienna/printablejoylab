// Automatischer Test: "Privacy settings" öffnet bei US-Bundesstaaten-Recht den US-Opt-out-Dialog, sonst den
// Einwilligungsdialog. assets/consent.js läuft gegen ein gestubbtes DOM und eine gestubbte Google-CMP (googlefc).
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const vm = require("vm");
const SRC = fs.readFileSync(__dirname + "/assets/consent.js", "utf8");

function page(usStatus, withEnum = true, gpp) {
  const calls = [], updates = [];
  let onClick = null, tcfListener = null;
  const us = {
    status: usStatus,
    getInitialUsStatesOptOutStatus: () => us.status,
    openConfirmationDialog: cb => { calls.push("usDialog"); us.answer = cb; }
  };
  if (withEnum) us.InitialUsStatesOptOutStatusEnum = { UNKNOWN: 0, DOES_NOT_APPLY: 1, NOT_OPTED_OUT: 2, OPTED_OUT: 3 };
  const googlefc = {
    callbackQueue: [], usstatesoptout: us,
    showRevocationMessage: () => calls.push("revocation"),
    getGoogleConsentModeValues: () => ({ analyticsStoragePurposeConsentStatus: 3 })
  };
  const scripts = [];
  const window = {
    document: null, navigator: {}, setTimeout: () => 0, Date,
    googlefc,
    gtag: (...a) => { if (a[0] === "consent" && a[1] === "update") updates.push(a[2]); },
    __tcfapi: (cmd, v, cb) => { if (cmd === "addEventListener") tcfListener = cb; }
  };
  const document = {
    head: { appendChild: s => scripts.push(s) },
    createElement: () => ({ dataset: {}, style: {} }),
    querySelectorAll: () => [],
    addEventListener: (ev, fn) => { if (ev === "click") onClick = fn; }
  };
  if (gpp) window.__gpp = gpp;
  window.document = document; window.window = window;   // as in a browser, window is the global object
  vm.runInContext(SRC, vm.createContext(window));
  const runQueue = () => {
    for (const item of googlefc.callbackQueue.splice(0)) {
      if (typeof item === "function") item();
      else for (const k of ["CONSENT_API_READY", "CONSENT_MODE_DATA_READY", "INITIAL_US_STATES_OPT_OUT_DATA_READY"]) if (item[k]) item[k]();
    }
  };
  runQueue();
  tcfListener({ gdprApplies: false, eventStatus: "tcloaded", purpose: { consents: {} }, vendor: { consents: {} } }, true);
  const click = () => onClick({ target: { closest: sel => (sel === "[data-privacy-settings]" ? {} : null) } });
  return { calls, us, scripts, window, runQueue, click, last: () => updates[updates.length - 1] };
}

test("U.S. state law applies: opt-out dialog instead of the consent dialog; opting out denies analytics and ad personalisation", () => {
  const p = page(2);
  assert.equal(p.last().analytics_storage, "granted");
  assert.ok(p.scripts.some(s => /adsbygoogle\.js/.test(s.src)), "ad/CMP script loaded");
  p.click(); p.runQueue();
  assert.deepEqual(p.calls, ["usDialog"]);
  p.us.answer(true);   // the initial status is not updated by the CMP within the page view
  assert.equal(p.last().analytics_storage, "denied");
  assert.equal(p.last().ad_personalization, "denied");
  assert.equal(p.window["ga-disable-G-T00HRG2YVF"], true);
});

test("U.S. dialog closed without opting out: measuring stays as it was", () => {
  const p = page(2, false);   // no enum object: DOES_NOT_APPLY falls back to 1
  p.click(); p.runQueue();
  assert.deepEqual(p.calls, ["usDialog"]);
  p.us.answer(false);
  assert.equal(p.last().analytics_storage, "granted");
  assert.equal(p.window["ga-disable-G-T00HRG2YVF"], false);
});

test("U.S. state law does not apply: the consent (revocation) dialog opens", () => {
  for (const withEnum of [true, false]) {
    const p = page(1, withEnum);
    p.click(); p.runQueue();
    assert.deepEqual(p.calls, ["revocation"]);
  }
});

test("CMP without the U.S. opt-out API: the consent dialog opens", () => {
  const p = page(1);
  delete p.us.getInitialUsStatesOptOutStatus;
  p.click(); p.runQueue();
  assert.deepEqual(p.calls, ["revocation"]);
});

// ---------- later U.S. opt-out through the IAB GPP API (stubbed __gpp) ----------
function gppStub() {
  const g = (cmd, cb) => {
    if (cmd === "addEventListener") { g.listener = cb; cb({ eventName: "listenerRegistered", listenerId: 1, data: true, pingData: g.ping }, true); }
    else if (cmd === "ping") cb(g.ping, true);
  };
  g.ping = { gppVersion: "1.1", cmpStatus: "loaded", signalStatus: "ready", applicableSections: [7], parsedSections: { usnat: [{ Version: 1, SaleOptOut: 2, SharingOptOut: 2, TargetedAdvertisingOptOut: 2 }] } };
  g.fire = pingData => g.listener({ eventName: "signalStatus", listenerId: 1, data: "ready", pingData }, true);
  g.fireNoPing = () => g.listener({ eventName: "sectionChange", listenerId: 1, data: "usnat" }, true);
  return g;
}
const OFF = "ga-disable-G-T00HRG2YVF";
const allDenied = u => u.analytics_storage === "denied" && u.ad_storage === "denied" && u.ad_user_data === "denied" && u.ad_personalization === "denied";

test("GPP: opt-out after an initial NOT_OPTED_OUT blocks analytics and ad signals at once", () => {
  const g = gppStub();
  const p = page(2, true, g);
  assert.ok(g.listener, "GPP listener registered");
  assert.equal(p.last().analytics_storage, "granted");
  assert.equal(p.window[OFF], false);
  g.fire({ signalStatus: "ready", applicableSections: [7], parsedSections: { usnat: [{ SaleOptOut: 1, SharingOptOut: 1, TargetedAdvertisingOptOut: 1 }, { Gpc: false }] } });
  assert.ok(allDenied(p.last()), JSON.stringify(p.last()));
  assert.equal(p.window[OFF], true);
  g.fire(g.ping);                       // a later "no opt-out" grants nothing again
  p.runQueue();
  assert.equal(p.window[OFF], true);
  assert.equal(p.last().analytics_storage, "denied");
});

test("GPP: event without pingData is read through ping; a state section (usca) counts too", () => {
  const g = gppStub();
  const p = page(2, true, g);
  g.ping = { signalStatus: "ready", applicableSections: [8], parsedSections: { usca: { SaleOptOut: 2, SharingOptOut: 1 } } };
  g.fireNoPing();
  assert.ok(allDenied(p.last()));
  assert.equal(p.window[OFF], true);
});

test("GPP: no opt-out, no U.S. section or not ready leaves the state unchanged", () => {
  const g = gppStub();
  const p = page(2, true, g);
  g.fire({ signalStatus: "ready", applicableSections: [7], parsedSections: { usnat: { SaleOptOut: 0, SharingOptOut: 2, TargetedAdvertisingOptOut: 2 } } });
  g.fire({ signalStatus: "ready", applicableSections: [-1], parsedSections: {} });
  g.fire({ signalStatus: "not ready" });
  assert.equal(p.last().analytics_storage, "granted");
  assert.equal(p.window[OFF], false);
});

test("no GPP API: nothing changes; GPP never grants anything", () => {
  const p = page(2);
  assert.equal(p.last().analytics_storage, "granted");
  const q = page(0);                    // UNKNOWN initial status: stays blocked
  assert.equal(q.last().analytics_storage, "denied");
  const g = gppStub();
  const r = page(0, true, g);
  g.fire(g.ping);
  assert.equal(r.last().analytics_storage, "denied");
  assert.equal(r.window[OFF], true);
});

test("GPP: malformed or unreadable data → denied", () => {
  const bad = ["garbage", null,
    { signalStatus: "ready", applicableSections: [7], parsedSections: { usnat: "xx" } },
    { signalStatus: "ready", applicableSections: [7], parsedSections: { usnat: [{ SaleOptOut: "no" }] } },
    { signalStatus: "ready", applicableSections: [7] },
    { signalStatus: "ready", parsedSections: { tcfeuv2: {} } }];
  for (const pd of bad) {
    const g = gppStub();
    const p = page(2, true, g);
    assert.equal(p.last().analytics_storage, "granted");
    g.fire(pd);
    assert.ok(allDenied(p.last()), JSON.stringify(pd));
    assert.equal(p.window[OFF], true);
  }
  const p = page(0, true, () => { throw new Error("boom"); });   // throwing API: page keeps working
  assert.equal(p.last().analytics_storage, "denied");
});
