/* Ads and analytics – both run through Google's certified consent management (IAB TCF 2.2).
   Consent Mode v2 defaults (everything denied, wait_for_update 500 ms) are set before any Google script.
   Google Analytics measures only when the Google CMP reports BOTH
     – TCF purpose 1 + vendor 755 (Google) consent, and
     – Consent Mode analytics_storage GRANTED (googlefc.getGoogleConsentModeValues()).
   UNKNOWN/missing values mean no. Outside GDPR scope (gdprApplies === false) analytics may run unless
   the CMP reports a refusal. Refusal or withdrawal sends consent "update" denied and sets the
   ga-disable flag, so no further hits are sent; renewed consent switches measurement back on.
   Google signals and ad personalisation are disabled in Analytics. */
(() => {
  const PUB = "ca-pub-7811071715414905";
  const GA = "G-T00HRG2YVF";
  const GOOGLE_VENDOR = 755;
  const OFF_FLAG = "ga-disable-" + GA;
  const GRANTED = 1, DENIED = 2;          // googlefc.ConsentModePurposeStatusEnum

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag(){ window.dataLayer.push(arguments); };
  window[OFF_FLAG] = true;
  window.gtag("consent", "default", {
    ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
    analytics_storage: "denied", wait_for_update: 500
  });
  window.googlefc = window.googlefc || {};
  window.googlefc.callbackQueue = window.googlefc.callbackQueue || [];

  // Ad unit IDs are added here after AdSense approval.
  const SLOTS = { billboard: "", rect: "", half: "", superbanner: "", sky: "" };
  // Feste IAB-Formate: Superbanner 728×90, Wide Skyscraper 160×600. Die übrigen Plätze sind responsiv
  // (Billboard 970×250 / Leaderboard 728×90 / Mobile 320×100, Half Page 300×600, Medium Rectangle 300×250).
  const FIXED = { superbanner: [728, 90], sky: [160, 600] };

  const gpc = navigator.globalPrivacyControl === true;

  function loadAds(){
    if (gpc) return;
    const s = document.createElement("script");
    s.async = true; s.crossOrigin = "anonymous";
    s.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${PUB}`;
    document.head.appendChild(s);
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

    const cmpAnalyticsStatus = () => {
      try {
        const fc = window.googlefc;
        const values = fc && typeof fc.getGoogleConsentModeValues === "function" ? fc.getGoogleConsentModeValues() : null;
        const v = values ? values.analyticsStoragePurposeConsentStatus : undefined;
        return typeof v === "number" ? v : 0;
      } catch (err) { return 0; }
    };
    const has = (group, id) => Boolean(group && group.consents && group.consents[id]);

    // returns "allow" | "deny" | "wait"
    const verdict = () => {
      const cm = cmpAnalyticsStatus();
      if (gpc || cm === DENIED) return "deny";
      if (!lastTc) return "wait";
      if (lastTc.gdprApplies === false) return "allow";
      if (lastTc.eventStatus !== "tcloaded" && lastTc.eventStatus !== "useractioncomplete") return "wait";
      return has(lastTc.purpose, 1) && has(lastTc.vendor, GOOGLE_VENDOR) && cm === GRANTED ? "allow" : "deny";
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
      if (!has(lastTc && lastTc.purpose, 1)) {
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

    return { sync, setTc(tc){ lastTc = tc; sync(); } };
  })();

  function watchConsent(tries = 0){
    if (typeof window.__tcfapi !== "function"){
      if (tries < 40) setTimeout(() => watchConsent(tries + 1), 250);
      return;
    }
    window.__tcfapi("addEventListener", 2, (tc, ok) => {
      if (!ok || !tc) return;
      analytics.setTc(tc);
      setTimeout(analytics.sync, 300);   // Consent Mode values may update just after the TCF event
    });
  }
  window.googlefc.callbackQueue.push({ CONSENT_MODE_DATA_READY: analytics.sync });

  // "Privacy settings" link in the footer reopens the Google consent dialog
  document.addEventListener("click", e => {
    if (!e.target.closest("[data-privacy-settings]")) return;
    window.googlefc.callbackQueue.push(() => {
      if (typeof window.googlefc.showRevocationMessage === "function") window.googlefc.showRevocationMessage();
    });
  });

  loadAds();
  watchConsent();
})();
