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
   Enum values: developers.google.com/funding-choices/fc-api-docs. Google signals/ad personalisation off. */
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
  // The defaults are normally already set by the inline script in <head>, right before the static AdSense
  // loader; they are only set here as a fallback (e.g. a cached page without that script), never twice.
  if (!window.pjlConsentDefaults) {
    window.gtag("consent", "default", {
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
      gtag("consent", "update", { analytics_storage: "granted" });
      if (!tagInjected) {
        tagInjected = true;
        gtag("js", new Date());
        const s = document.createElement("script"); s.async = true;
        s.src = `https://www.googletagmanager.com/gtag/js?id=${GA}`;
        document.head.appendChild(s);
      }
      gtag("config", GA, { allow_google_signals: false, allow_ad_personalization_signals: false });
      mode = "measuring";
    };

    const disable = () => {
      window[OFF_FLAG] = true;
      const update = { analytics_storage: "denied" };
      if (usOptOutConfirmed || !has(lastTc && lastTc.purpose, 1)) {
        update.ad_storage = "denied"; update.ad_user_data = "denied"; update.ad_personalization = "denied";
      }
      gtag("consent", "update", update);
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

    return { sync, usOptOut, setTc(tc){ lastTc = tc; sync(); }, tc: () => lastTc };
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
    if (!e.target.closest("[data-privacy-settings]")) return;
    window.googlefc.callbackQueue.push(() => {
      try { openPrivacyChoice(); } catch (err) { /* CMP not available */ }
    });
  });

  loadAds();
  watchConsent();
})();
