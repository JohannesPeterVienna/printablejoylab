# Printable Joy Lab

Free customisable printables (planners, calendars, trackers, paper) – static site for GitHub Pages (`docs/`).

- `assets/lab.js` – layout engine: templates as drawing operations in mm → SVG preview + vector PDF (jsPDF, MIT, self-hosted)
- `content/` – template metadata, guides, articles (English)
- `build.py` – builds `docs/`; runs `test_lab.js` first (every template × many settings must stay on the page)
- Fonts: Instrument Serif, Manrope (SIL OFL 1.1, self-hosted)
- `assets/sizes.js` + `content/sizes.py` + `content/reference.py` – paper size reference (81 sizes from PWG 5101.1), print scale calculator and the ruler check of the print test page; `test_sizes.js` covers the arithmetic and the CSV export
- `test_ads.js` – after building: Playwright check that unfilled ad slots stay invisible and filled ones appear (with their gap to controls)
- `test_site.js` – after building: Playwright walk over the sitemap at 390 and 1366 px (JS errors, overflow, dead links, links that carry settings) and through the tools with nonsense input
- Shop: `SHOP_ENABLED = False` in `build.py` – `shop.html` and `refunds.html` are not built until a real purchase works
