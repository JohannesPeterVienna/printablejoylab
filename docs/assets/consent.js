/* Ads and analytics – both run through Google's certified consent management (IAB TCF 2.2).
   Consent Mode v2 defaults (everything denied, wait_for_update 500 ms, ga-disable on) are set before any
   Google script – by an inline script in <head> directly before the static AdSense loader (fallback: here). Google Analytics measures only when
     – GDPR applies: TCF purpose 1 + vendor 755 (Google) consent AND Consent Mode
       analyticsStoragePurposeConsentStatus GRANTED (1);
     – GDPR does not apply (gdprApplies === false): the value is GRANTED (1) or NOT_APPLICABLE (3) AND the
       CMP explicitly reports no U.S. state opt-out (usstatesoptout DOES_NOT_APPLY 1 / NOT_OPTED_OUT 2).
   Missing, UNKNOWN (0), DENIED (2), NOT_CONFIGURED (4) or any CMP API error mean no. A clear TCF "no"
   blocks at once, before any other CMP API is called. Refusal or withdrawal sends consent "update" denied
   and sets the ga-disable flag; renewed consent switches measurement back on. A U.S. opt-out made later
   in the page view is read from the IAB GPP API (__gpp addEventListener) and blocks everything at once.
   Enum values: developers.google.com/funding-choices/fc-api-docs. Google signals/ad personalisation off.

   Interim "visitor tally" slip (since 4 Nov 2026, statistics only): Google's consent message is published
   but currently reports displayStatus "hidden", so no TCF decision arrives and analytics never starts. If,
   about 3 s after start, the CMP has given no real decision – no __tcfapi, or no "useractioncomplete" and no
   "tcloaded" with a non-empty tcString – and gdprApplies is not clearly false, our own small slip asks for
   analytics only (Accept / Decline, equal weight). Accept: analytics_storage granted + gtag.js + config as
   above. Decline or withdrawal: analytics_storage denied, ga-disable on, _ga/_ga_* cookies deleted. The slip
   never touches ad_storage, ad_user_data or ad_personalization (they stay "denied"). The choice is stored in
   localStorage "pjl-tally" ({v, choice, at}) and asked again after 12 months or a version change. As soon as
   the CMP shows its own message or gdprApplies === false, only the TCF logic above counts and the slip
   closes; on a real CMP decision the stored slip choice is deleted, and if the slip had said Accept and
   Google now says no, the _ga/_ga_* cookies are deleted too. Global Privacy Control: analytics stays
   off and the slip is never pushed. Pages without ads load this file with data-pjl-scope="settings": no ad
   code, no CMP, no Google request at all – only "Privacy settings" opening the slip, so a choice made in the
   slip can be withdrawn there too. */
(() => {
  const PUB = "ca-pub-7811071715414905";
  const GA = "G-T00HRG2YVF";
  const GOOGLE_VENDOR = 755;
  const OFF_FLAG = "ga-disable-" + GA;
  const GRANTED = 1, NOT_APPLICABLE = 3;   // googlefc.ConsentModePurposeStatusEnum
  const US_NO_OPT_OUT = [1, 2];           // usstatesoptout: DOES_NOT_APPLY, NOT_OPTED_OUT (0 UNKNOWN, 3 OPTED_OUT block)

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag(){ window.dataLayer.push(arguments); };
  window[OFF_FLAG] = true;
  // every call goes through tag(): never a ReferenceError, even if the stub above was replaced by something odd
  const tag = (...args) => { try { if (typeof window.gtag === "function") window.gtag(...args); else (function(){ window.dataLayer.push(arguments); }).apply(null, args); } catch (err) { /* ignore */ } };
  // The defaults are normally already set by the inline script in <head>, right before the static AdSense
  // loader; they are only set here as a fallback (e.g. a cached page without that script), never twice.
  if (!window.pjlConsentDefaults) {
    tag("consent", "default", {
      ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
      analytics_storage: "denied", wait_for_update: 500
    });
    window.pjlConsentDefaults = true;
  }
  window.googlefc = window.googlefc || {};
  window.googlefc.callbackQueue = window.googlefc.callbackQueue || [];

  // Ad unit IDs are added here after AdSense approval.
  // Shared AdSense units “Themen-Websites – …” (account pub-7811071715414905, created 17 Oct and 5 Nov 2026)
  const SLOTS = { billboard: "7497607759", rect: "1292301217", half: "1292301217", superbanner: "5774811012", sky: "5064364572", mbanner: "5396758258" };
  // Feste IAB-Formate: Superbanner 728×90, Wide Skyscraper 160×600. Die übrigen Plätze sind responsiv
  // (Billboard 970×250 / Leaderboard 728×90 / Mobile 320×100, Half Page 300×600, Medium Rectangle 300×250).
  const FIXED = { superbanner: [728, 90], sky: [160, 600], mbanner: [320, 100] };

  const gpc = navigator.globalPrivacyControl === true;

  // ---------- interim visitor tally: state and storage ----------
  const TALLY_KEY = "pjl-tally", TALLY_V = 1, TALLY_WAIT = 3000, TALLY_MONTHS = 12;
  const me = document.currentScript;
  const settingsOnly = !!(me && me.dataset && me.dataset.pjlScope === "settings");
  // "waiting" (first ~3 s) | "active" (slip decides analytics) | "retired" (Google's CMP decides) | "settings" (page without ads)
  // hadGrant: this browser's slip said "Accept" – needed to delete GA cookies if Google later says no
  const tally = { phase: settingsOnly ? "settings" : "waiting", pick: null, hadGrant: false };

  function readTally(now = Date.now()){
    try {
      const rec = JSON.parse(window.localStorage.getItem(TALLY_KEY) || "null");
      if (!rec || rec.v !== TALLY_V || (rec.choice !== "granted" && rec.choice !== "denied") || typeof rec.at !== "number") return null;
      const until = new Date(rec.at); until.setMonth(until.getMonth() + TALLY_MONTHS);
      return rec.at <= now && now < until.getTime() ? rec : null;
    } catch (err) { return null; }
  }
  function saveTally(choice){
    const rec = { v: TALLY_V, choice, at: Date.now() };
    try { window.localStorage.setItem(TALLY_KEY, JSON.stringify(rec)); } catch (err) { /* storage blocked: choice holds for this page view */ }
    return rec;
  }
  // Has Google's CMP spoken? A real TCF decision, its own message on screen, or GDPR clearly not applicable.
  const cmpSpoke = tc => !!tc && (tc.gdprApplies === false || tc.eventStatus === "useractioncomplete" ||
    (tc.eventStatus === "cmpuishown" && tc.displayStatus !== "hidden" && tc.displayStatus !== "disabled") ||
    tc.displayStatus === "visible" || (tc.eventStatus === "tcloaded" && typeof tc.tcString === "string" && tc.tcString !== ""));
  const cmpDecided = tc => !!tc && (tc.eventStatus === "useractioncomplete" ||
    (tc.eventStatus === "tcloaded" && typeof tc.tcString === "string" && tc.tcString !== ""));
  const tallyGranted = () => tally.phase === "active" && !!tally.pick && tally.pick.choice === "granted";

  function loadAds(){
    if (gpc) { (window.adsbygoogle = window.adsbygoogle || []).pauseAdRequests = 1; return; }   // no ad requests at all
    // The loader is in <head> as a static tag; it is only added here if it is missing – never a second copy.
    if (!document.querySelector('script[src*="pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"]')) {
      const s = document.createElement("script");
      s.async = true; s.crossOrigin = "anonymous";
      s.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${PUB}`;
      document.head.appendChild(s);
    }
    document.querySelectorAll(".ad[data-ad]").forEach(box => {
      const id = SLOTS[box.dataset.ad];
      if (!id) return;
      box.classList.add("on");
      if (box.offsetParent === null) { box.classList.remove("on"); return; }   // auf diesem Bildschirm ausgeblendet
      const ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.dataset.adClient = PUB; ins.dataset.adSlot = id;
      const fixed = FIXED[box.dataset.ad];
      if (fixed) { ins.style.cssText = `display:inline-block;width:${fixed[0]}px;height:${fixed[1]}px`; }
      else {
        ins.style.display = "block";
        ins.dataset.adFormat = box.dataset.ad === "half" ? "vertical" : "auto";
        ins.dataset.fullWidthResponsive = "true";
      }
      box.appendChild(ins);
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    });
  }

  const analytics = (() => {
    let lastTc = null;
    let mode = "pending";        // "pending" | "measuring" | "blocked"
    let tagInjected = false;
    let usOptOutConfirmed = false;   // visitor opted out in Google's U.S. dialog during this page view

    const cmpAnalyticsStatus = () => {
      try {
        const fc = window.googlefc;
        const values = fc && typeof fc.getGoogleConsentModeValues === "function" ? fc.getGoogleConsentModeValues() : null;
        const v = values ? values.analyticsStoragePurposeConsentStatus : undefined;
        return typeof v === "number" ? v : 0;
      } catch (err) { return 0; }
    };
    const has = (group, id) => Boolean(group && group.consents && group.consents[id]);

    const usOptedOut = () => {
      if (usOptOutConfirmed) return true;
      try {
        const u = window.googlefc && window.googlefc.usstatesoptout;
        return !(u && typeof u.getInitialUsStatesOptOutStatus === "function" && US_NO_OPT_OUT.includes(u.getInitialUsStatesOptOutStatus()));
      } catch (err) { return true; }
    };

    // returns "allow" | "deny" | "wait"
    const verdict = () => {
      if (gpc || usOptOutConfirmed) return "deny";
      if (tally.phase === "settings") return "wait";                 // page without ads: never measures
      if (tally.phase === "active") return tallyGranted() ? "allow" : "deny";
      if (!lastTc) return "wait";
      if (lastTc.gdprApplies === false) {
        const cm = cmpAnalyticsStatus();
        return (cm === GRANTED || cm === NOT_APPLICABLE) && !usOptedOut() ? "allow" : "deny";
      }
      if (lastTc.eventStatus !== "tcloaded" && lastTc.eventStatus !== "useractioncomplete") return "wait";
      if (!has(lastTc.purpose, 1) || !has(lastTc.vendor, GOOGLE_VENDOR)) return "deny";   // no further CMP call
      return cmpAnalyticsStatus() === GRANTED ? "allow" : "deny";
    };

    const enable = () => {
      window[OFF_FLAG] = false;
      tag("consent", "update", { analytics_storage: "granted" });
      if (!tagInjected) {
        tagInjected = true;
        tag("js", new Date());
        const s = document.createElement("script"); s.async = true;
        s.src = `https://www.googletagmanager.com/gtag/js?id=${GA}`;
        document.head.appendChild(s);
      }
      tag("config", GA, { allow_google_signals: false, allow_ad_personalization_signals: false });
      mode = "measuring";
    };

    const disable = () => {
      window[OFF_FLAG] = true;
      const update = { analytics_storage: "denied" };
      // in slip mode only analytics_storage is sent – the slip never touches ad_* (they stay at their "denied" default)
      if (usOptOutConfirmed || (tally.phase !== "active" && !has(lastTc && lastTc.purpose, 1))) {
        update.ad_storage = "denied"; update.ad_user_data = "denied"; update.ad_personalization = "denied";
      }
      tag("consent", "update", update);
      mode = "blocked";
    };

    const sync = () => {
      const v = verdict();
      if (v === "allow" && mode !== "measuring") enable();
      else if (v === "deny" && mode !== "blocked") disable();
      else if (v === "wait" && mode === "measuring") disable();   // consent record cleared by revocation
    };

    // after a U.S. opt-out: analytics and ad personalisation denied at once, whatever state we were in
    const usOptOut = () => { usOptOutConfirmed = true; disable(); };

    // a clear "no" from Google's TCF data (not a Consent Mode value that may still be on its way)
    const googleSaysNo = tc => tc.gdprApplies !== false &&
      (!has(tc.purpose, 1) || !has(tc.vendor, GOOGLE_VENDOR) || cmpAnalyticsStatus() === 2);

    const setTc = tc => {
      lastTc = tc;
      if (cmpSpoke(tc)) retireTally();
      if (cmpDecided(tc)) forgetTally();               // real Google decision: the stored slip choice is deleted
      sync();
      // measured through the slip before, now Google says no: GA cookies go as well (withdrawal, Art. 7(3) GDPR)
      if (tally.hadGrant && cmpDecided(tc) && googleSaysNo(tc)) { tally.hadGrant = false; eraseGaCookies(); }
    };

    return { sync, usOptOut, setTc, tc: () => lastTc };
  })();

  // IAB GPP (spec v1.1) pingData → U.S. opt-out? Section IDs from 6 up are U.S. (6 uspv1, 7 usnat, 8 usca,
  // 9 usva …); opt-out fields 0 = not applicable, 1 = opted out, 2 = did not opt out.
  // true = opted out, or a U.S. section applies but cannot be read (fail closed); false = no U.S. section
  // or clearly no opt-out; null = CMP not ready. Only true is acted on – this never grants anything.
  const GPP_FIELDS = ["SaleOptOut", "SharingOptOut", "TargetedAdvertisingOptOut"];
  const gppSection = sec => {        // "out" | "in" | "unclear"
    if (typeof sec === "string") return sec.length === 4 ? (sec[2] === "Y" ? "out" : "in") : "unclear";   // uspv1 "1YYN"
    let seen = false;
    for (const seg of Array.isArray(sec) ? sec : [sec]) {   // [core, gpc] segments or one object
      if (!seg || typeof seg !== "object") continue;
      if (seg.OptOutSale !== undefined) {
        if (seg.OptOutSale === "Y") return "out";
        if (seg.OptOutSale !== "N" && seg.OptOutSale !== "-") return "unclear";
        seen = true;
      }
      for (const f of GPP_FIELDS) {
        const v = seg[f];
        if (v === undefined) continue;
        if (v === 1 || v === "1") return "out";
        if (typeof v !== "number") return "unclear";
        seen = true;
      }
    }
    return seen ? "in" : "unclear";
  };
  const gppUsOptOut = pd => {
    if (!pd || typeof pd !== "object") return true;
    if (pd.signalStatus === "not ready") return null;
    const applies = Array.isArray(pd.applicableSections) ? pd.applicableSections.some(id => typeof id === "number" && id >= 6) : null;
    if (applies === false) return false;
    const parsed = pd.parsedSections;
    if (!parsed || typeof parsed !== "object") return true;
    const us = Object.keys(parsed).filter(k => k.startsWith("us"));
    if (!us.length) return true;     // a U.S. section applies (or the list is missing) but none was parsed
    return us.some(k => gppSection(parsed[k]) !== "in");
  };
  let gppWatching = false, gppOut = false;
  const onGpp = pd => {
    let out;
    try { out = gppUsOptOut(pd); } catch (err) { out = true; }
    if (out === true && !gppOut) { gppOut = true; analytics.usOptOut(); }
  };
  // missing GPP API or a failed call: nothing changes (defaults stay denied)
  function watchGpp(){
    if (gppWatching || typeof window.__gpp !== "function") return;
    try {
      window.__gpp("addEventListener", (evt, ok) => {
        if (!ok) return;
        try {
          if (evt && evt.pingData !== undefined) onGpp(evt.pingData);
          else window.__gpp("ping", (pd, pok) => { if (pok) onGpp(pd); });
        } catch (err) { onGpp(null); }
      });
      gppWatching = true;
    } catch (err) { /* GPP API not usable */ }
  }

  function watchConsent(tries = 0){
    if (typeof window.__tcfapi !== "function"){
      if (tries < 40) setTimeout(() => watchConsent(tries + 1), 250);
      return;
    }
    watchGpp();
    window.__tcfapi("addEventListener", 2, (tc, ok) => {
      if (!ok || !tc) return;
      analytics.setTc(tc);
      setTimeout(analytics.sync, 300);   // Consent Mode values may update just after the TCF event
    });
  }
  window.googlefc.callbackQueue.push({
    CONSENT_API_READY: watchGpp,
    CONSENT_MODE_DATA_READY: analytics.sync,
    INITIAL_US_STATES_OPT_OUT_DATA_READY: () => { analytics.sync(); watchGpp(); }
  });

  // "Privacy settings" link in the footer: where the CMP reports that a U.S. state privacy law applies it
  // opens Google's U.S. opt-out dialog ("Do Not Sell or Share"), everywhere else it reopens the consent dialog.
  // The U.S. dialog only for a known status NOT_OPTED_OUT (2) or OPTED_OUT (3) and only when the latest TCF data
  // does not say the GDPR applies; UNKNOWN (0) or an EU visitor gets the consent dialog to withdraw consent.
  function openPrivacyChoice(){
    const fc = window.googlefc;
    const revoke = () => { if (fc && typeof fc.showRevocationMessage === "function") fc.showRevocationMessage(); };
    try {
      const us = fc.usstatesoptout;
      if (us && typeof us.getInitialUsStatesOptOutStatus === "function" && typeof us.openConfirmationDialog === "function") {
        const E = us.InitialUsStatesOptOutStatusEnum || {};
        const notOptedOut = E.NOT_OPTED_OUT !== undefined ? E.NOT_OPTED_OUT : 2;
        const optedOut = E.OPTED_OUT !== undefined ? E.OPTED_OUT : 3;
        const tc = analytics.tc();
        const gdpr = !!(tc && tc.gdprApplies === true);
        const status = us.getInitialUsStatesOptOutStatus();
        if ((status === notOptedOut || status === optedOut) && !gdpr) {
          us.openConfirmationDialog(userDidOptOut => {
            if (userDidOptOut) analytics.usOptOut();
            else analytics.sync();
          });
          return;
        }
      }
    } catch (err) { /* U.S. opt-out API missing or failing: fall back to the consent dialog */ }
    revoke();
  }
  document.addEventListener("click", e => {
    const opener = e.target.closest("[data-privacy-settings]");
    if (!opener) return;
    if (tally.phase === "active" || tally.phase === "settings") { openSlip(opener); return; }   // interim mode: our own slip
    window.googlefc.callbackQueue.push(() => {
      try { openPrivacyChoice(); } catch (err) { /* CMP not available */ }
    });
  });

  // ---------- interim visitor tally: decision after ~3 s, the slip itself ----------
  const noteGrant = rec => { if (rec && rec.choice === "granted") tally.hadGrant = true; };
  function retireTally(){
    if (tally.phase === "retired" || tally.phase === "settings") return;
    noteGrant(tally.pick); noteGrant(readTally());
    tally.phase = "retired"; tally.pick = null;      // Google's consent management counts from now on
    closeSlip(false);
  }
  function forgetTally(){
    if (tally.phase === "settings") return;
    noteGrant(readTally());
    try { window.localStorage.removeItem(TALLY_KEY); } catch (err) { /* storage blocked: nothing stored */ }
  }
  function startTally(){
    if (tally.phase !== "waiting") return;
    if (cmpSpoke(analytics.tc())) { retireTally(); return; }
    tally.phase = "active";
    tally.pick = readTally();
    if (tally.pick && tally.pick.choice === "denied") eraseGaCookies();   // declined earlier: no GA cookie may linger
    analytics.sync();
    if (!tally.pick && !gpc) openSlip(null);         // GPC: statistics stay off, nothing is pushed
  }

  function eraseGaCookies(){
    let jar = "";
    try { jar = String(document.cookie || ""); } catch (err) { return; }
    const host = String((window.location && window.location.hostname) || "");
    const parts = host.split(".").filter(Boolean);
    const scopes = [""];
    for (let i = 0; i < parts.length - 1; i++) scopes.push("; domain=." + parts.slice(i).join("."));
    jar.split(";").forEach(c => {
      const name = c.split("=")[0].trim();
      if (!/^_ga($|_)/.test(name)) return;
      scopes.forEach(d => { try { document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; max-age=0; path=/${d}`; } catch (err) { /* ignore */ } });
    });
  }

  function choose(choice){
    tally.pick = saveTally(choice);
    if (choice === "denied") {
      window[OFF_FLAG] = true;
      tag("consent", "update", { analytics_storage: "denied" });
      eraseGaCookies();
    }
    if (tally.phase === "active") analytics.sync();
    closeSlip(true);
  }

  let slip = null, slipOpener = null;
  const longDate = ms => new Date(ms).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });

  function buildSlip(){
    const el = document.createElement("section");
    el.className = "tally";
    el.id = "pjl-tally";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-modal", "false");
    el.setAttribute("aria-labelledby", "tally-title");
    el.setAttribute("aria-describedby", "tally-text");
    el.hidden = true;
    el.innerHTML = `<div class="tally-sheet">
  <button type="button" class="tally-shut" data-tally-close aria-label="Close without deciding" title="Close without deciding"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true" focusable="false"><path d="M3 3l10 10M13 3L3 13"/></svg></button>
  <svg class="tally-marks" viewBox="0 0 44 30" width="44" height="30" aria-hidden="true" focusable="false"><path d="M6 4v22M14 4v22M22 4v22M30 4v22M2 24L36 6"/></svg>
  <div class="tally-body">
    <p class="tally-kicker">Visitor tally · statistics only</p>
    <h2 class="tally-title" id="tally-title" tabindex="-1">May we count your visit?</h2>
    <p class="tally-text" id="tally-text" data-tally-text></p>
    <p class="tally-now" data-tally-now></p>
    <div class="tally-picks" data-tally-picks>
      <button type="button" class="tally-pick" data-tally-pick="granted">Accept</button>
      <button type="button" class="tally-pick" data-tally-pick="denied">Decline</button>
    </div>
    <div class="tally-picks tally-picks--one" data-tally-gpc hidden><button type="button" class="tally-pick" data-tally-close>Close</button></div>
  </div>
</div>`;
    el.addEventListener("click", e => {
      const t = e.target;
      const pick = t && t.closest ? t.closest("[data-tally-pick]") : null;
      if (pick) { choose(pick.getAttribute("data-tally-pick")); return; }
      if (t && t.closest && t.closest("[data-tally-close]")) closeSlip(true);   // closes for now: nothing stored, no consent
    });
    el.addEventListener("keydown", e => {
      if (e.key === "Escape") { e.preventDefault(); closeSlip(true); }   // closes for now – never counts as consent
    });
    const skip = document.querySelector(".skip");    // early in the tab order, shown fixed at the bottom
    if (skip && skip.after) skip.after(el); else document.body.prepend(el);
    return el;
  }

  function fillSlip(){
    const text = slip.querySelector("[data-tally-text]");
    const now = slip.querySelector("[data-tally-now]");
    const rec = tally.phase === "settings" ? readTally() : tally.pick;
    if (gpc) {
      text.textContent = "Your browser sends a Global Privacy Control signal, so we keep Google Analytics switched off on this site and don’t ask for consent.";
      now.textContent = "";
    } else {
      text.innerHTML = "Google Analytics (Google Ireland Ltd.) would count visits and set cookies on your device; data may be processed in the USA. " +
        "Statistics only – no ads, no ad consent. Saved for 12 months; change it any time under “Privacy settings”. " +
        '<a href="/privacy.html#visitor-tally">Privacy policy</a>';
      now.textContent = rec ? `Your current choice: ${rec.choice === "granted" ? "accepted" : "declined"} on ${longDate(rec.at)}.`
        : (tally.phase === "settings" ? "No choice saved in this browser yet." : "");
      if (tally.phase === "settings") now.textContent += " Made your choice in Google’s consent message? Open “Privacy settings” on any template page to change it there.";
    }
    slip.querySelector("[data-tally-picks]").hidden = gpc;
    slip.querySelector("[data-tally-gpc]").hidden = !gpc;
  }

  function openSlip(opener){
    try {
      if (!slip) slip = buildSlip();
      slipOpener = opener;
      fillSlip();
      slip.hidden = false;
      document.body.classList.add("tally-open");
      document.body.style.setProperty("--tally-room", slip.offsetHeight + "px");   // footer stays reachable
      if (opener) slip.querySelector("#tally-title").focus();   // opened on request: move focus in; shown by itself: focus stays put
    } catch (err) { /* no DOM: nothing to show */ }
  }

  function closeSlip(returnFocus){
    if (!slip || slip.hidden) return;
    slip.hidden = true;
    try {
      document.body.classList.remove("tally-open");
      if (returnFocus && slipOpener && slipOpener.focus) slipOpener.focus();
    } catch (err) { /* ignore */ }
    slipOpener = null;
  }

  if (settingsOnly) {         // page without ads: no ad code, no CMP, no analytics – only the settings slip
    const rec = readTally();
    if (rec && rec.choice === "denied") eraseGaCookies();
    return;
  }
  loadAds();
  watchConsent();
  setTimeout(startTally, TALLY_WAIT);
})();
