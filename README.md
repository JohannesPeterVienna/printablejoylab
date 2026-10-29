# Printable Joy Lab

Free customisable printables (planners, calendars, trackers, paper) – static site for GitHub Pages (`docs/`).

- `assets/lab.js` – layout engine: templates as drawing operations in mm → SVG preview + vector PDF (jsPDF, MIT, self-hosted)
- `content/` – template metadata, guides, articles (English)
- `build.py` – builds `docs/`; runs `test_lab.js` first (every template × many settings must stay on the page)
- Fonts: Instrument Serif, Manrope (SIL OFL 1.1, self-hosted)
