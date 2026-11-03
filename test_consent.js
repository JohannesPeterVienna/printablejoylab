// Automatischer Test: "Privacy settings" öffnet bei US-Bundesstaaten-Recht den US-Opt-out-Dialog, sonst den
// Einwilligungsdialog. assets/consent.js läuft gegen ein gestubbtes DOM und eine gestubbte Google-CMP (googlefc).
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const vm = require("vm");
const SRC = fs.readFileSync(__dirname + "/assets/consent.js", "utf8");

function page(usStatus, withEnum = true) {
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
