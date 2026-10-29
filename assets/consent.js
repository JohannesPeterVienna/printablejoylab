/* Ads and analytics – both run through Google's certified consent management (IAB TCF 2.2).
   Google Analytics loads only after storage (purpose 1) and Google as a vendor are allowed.
   Google signals and ad personalisation are disabled in Analytics. */
(() => {
  const PUB = "ca-pub-7811071715414905";
  const GA = "G-T00HRG2YVF";
  const GOOGLE_VENDOR = 755;

  // Ad unit IDs are added here after AdSense approval.
  const SLOTS = { billboard: "", rect: "", half: "" };

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
      const ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.style.display = "block";
      ins.dataset.adClient = PUB; ins.dataset.adSlot = id;
      ins.dataset.adFormat = box.dataset.ad === "half" ? "vertical" : "auto";
      ins.dataset.fullWidthResponsive = "true";
      box.appendChild(ins);
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    });
  }

  let gaLoaded = false;
  function loadGA(){
    if (gaLoaded || gpc) return; gaLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ dataLayer.push(arguments); };
    gtag("consent", "default", { ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "granted" });
    gtag("js", new Date());
    gtag("config", GA, { allow_google_signals: false, allow_ad_personalization_signals: false });
    const s = document.createElement("script"); s.async = true;
    s.src = `https://www.googletagmanager.com/gtag/js?id=${GA}`;
    document.head.appendChild(s);
  }

  function watchConsent(tries = 0){
    if (typeof window.__tcfapi !== "function"){
      if (tries < 40) setTimeout(() => watchConsent(tries + 1), 250);
      return;
    }
    window.__tcfapi("addEventListener", 2, (tc, ok) => {
      if (!ok || !tc) return;
      if (tc.eventStatus !== "tcloaded" && tc.eventStatus !== "useractioncomplete") return;
      const p1 = tc.purpose && tc.purpose.consents && tc.purpose.consents[1];
      const v = tc.vendor && tc.vendor.consents && tc.vendor.consents[GOOGLE_VENDOR];
      if (p1 && v) loadGA();
    });
  }

  // "Privacy settings" link in the footer reopens the Google consent dialog
  document.addEventListener("click", e => {
    if (!e.target.closest("[data-privacy-settings]")) return;
    window.googlefc = window.googlefc || {}; window.googlefc.callbackQueue = window.googlefc.callbackQueue || [];
    window.googlefc.callbackQueue.push(() => window.googlefc.showRevocationMessage());
  });

  loadAds();
  watchConsent();
})();
