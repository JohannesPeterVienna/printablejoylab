"""Printable Joy Lab – statische Seiten bauen (GitHub Pages aus docs/)."""
import json, shutil, subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from content.tools import TOOLS, CATS, BY
from content.articles import ARTICLES

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
SITE = "https://printablejoylab.com"; V = "20261029"; UPDATED = "October 2026"
NAV = [("/", "Templates"), ("/weekly-planner.html", "Planners"), ("/monthly-calendar.html", "Calendars"), ("/habit-tracker.html", "Trackers"), ("/dot-grid.html", "Paper"), ("/guides.html", "Guides")]
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True, trim_blocks=True, lstrip_blocks=True)
PAGES = []
LEGAL_ADDR = "AdStern :: Agentur für digitales Marketing<br>Seilerstätte 8, 1010 Vienna, Austria<br>Email: <a href='mailto:office@adstern.com'>office@adstern.com</a><br>Web: <a href='https://www.adstern.com'>www.adstern.com</a>"
ORG = {"@type": "Organization", "name": "Printable Joy Lab", "url": SITE + "/"}


def write(path, template, **ctx):
    base = dict(site=SITE, v=V, updated=UPDATED, nav=NAV, active=ctx.get("active", "/" + path), jsonld=[], ads=True,
                robots=None, og_title=None, tools=TOOLS, cats=CATS, articles=ARTICLES)
    base.update(ctx)
    base["path"] = "/" if path == "index.html" else "/" + path
    (OUT / path).write_text(env.get_template(template).render(**base), encoding="utf-8")
    if base.get("robots") is None:
        PAGES.append((base["path"], ctx.get("priority", 0.6)))


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + h} for i, (h, n) in enumerate(items)]}


def main():
    subprocess.run(["node", str(ROOT / "test_lab.js")], check=True)   # Vorlagen-Test: Build bricht bei Fehlern ab
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for f in (ROOT / "assets").iterdir(): shutil.copy(f, OUT / "assets" / f.name)

    write("index.html", "home.html", title="Printable Joy Lab – Free Customisable Printables: Planners, Calendars & Paper",
          description="Free printable planners, calendars, habit trackers, checklists and paper you customise in seconds – A4 or US Letter, your colours and dates – then download as PDF.",
          active="/", priority=1.0,
          jsonld=[{"@context": "https://schema.org", "@type": "WebSite", "name": "Printable Joy Lab", "url": SITE + "/", "inLanguage": "en"}])

    for t in TOOLS:
        crumbs = [("/", "Templates"), ("/" + t["slug"] + ".html", t["name"])]
        related = [x for x in TOOLS if x["cat"] == t["cat"] and x["slug"] != t["slug"]][:4]
        related += [x for x in TOOLS if x not in related and x["slug"] != t["slug"]][:4 - len(related)] if len(related) < 4 else []
        ld = [crumbs_ld(crumbs),
              {"@context": "https://schema.org", "@type": "WebApplication", "name": f"{t['name']} generator – Printable Joy Lab", "url": f"{SITE}/{t['slug']}.html",
               "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "en", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}]
        write(t["slug"] + ".html", "tool.html", title=t["title"] + " | Printable Joy Lab", description=t["description"], h1=f"{t['name']}",
              lead=t["lead"], slug=t["slug"], guide=t["guide"], faq=t["faq"], related=related, crumbs=crumbs, jsonld=ld,
              active=next((h for h, l in NAV if h == "/" + t["slug"] + ".html"), ""), priority=0.9)

    for a in ARTICLES:
        crumbs = [("/", "Templates"), ("/guides.html", "Guides"), ("/" + a["slug"] + ".html", a["title"])]
        ld = [crumbs_ld(crumbs), {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["description"],
              "inLanguage": "en", "author": ORG, "publisher": ORG, "datePublished": "2026-10-29", "dateModified": "2026-10-29", "mainEntityOfPage": f"{SITE}/{a['slug']}.html"}]
        links = [BY[s] for s in BY if f"/{s}.html" in a["body"]][:4]
        write(a["slug"] + ".html", "page.html", title=a["title"] + " | Printable Joy Lab", description=a["description"], h1=a["title"],
              lead=a["teaser"], body=a["body"], crumbs=crumbs, related=links, jsonld=ld, active="/guides.html", priority=0.7)

    guides = "".join(f'<li><a class="card" href="/{a["slug"]}.html"><strong>{a["title"]}</strong><span>{a["teaser"]}</span></a></li>' for a in ARTICLES)
    write("guides.html", "page.html", title="Guides – Printing, Planning & Paper | Printable Joy Lab",
          description="Guides on printing at actual size, choosing the right paper, bullet journaling and planning on paper.",
          h1="Guides", lead="Practical know-how for printing, planning and paper.", active="/guides.html", priority=0.6,
          body=f'<p>Short, practical guides to get the most out of printable planners and paper – from exact print settings to building a planning routine that lasts.</p><ul class="cards text">{guides}</ul>'
               '<h2>About our templates</h2><p>Every template on Printable Joy Lab is generated from your settings in your own browser. The guides explain the ideas behind the layouts – why college ruling is 9/32 inch, how ISO week numbers work and why a habit tracker helps.</p>')

    write("about.html", "page.html", title="About Printable Joy Lab", description="Who makes Printable Joy Lab, how the templates are generated and how we check them.",
          h1="About Printable Joy Lab", lead="Customisable printables, generated in your browser.", priority=0.3, active="",
          body="""<p>Printable Joy Lab is made by AdStern, a small digital agency in Vienna, Austria. We build free tools that are genuinely useful – and printables were a natural fit: almost everyone needs a planner page, a calendar or a sheet of graph paper now and then, but most downloads come in one fixed size and style.</p>
<h2>How the templates work</h2><p>Each template is described once as a set of lines, boxes and text positioned in millimetres. From that description your browser draws the live preview and creates the PDF – the same data for both, so what you see is what you print. Paper sizes follow ISO 216 (A4, A5) and the North American standards (US Letter, Half Letter). Calendars use the Gregorian calendar and ISO 8601 week numbers.</p>
<h2>How we check them</h2><p>Every time the site is updated, an automated test draws every template with many combinations of settings – all paper sizes, orientations, week starts and options – and checks that every line, box and label lands on the page. If a single check fails, the update is not published. We also print sample pages and measure them with a ruler.</p>
<h2>Your data</h2><p>Your settings, habits and lists never leave your device: the PDF is created in your browser, and the last settings are remembered in your browser's local storage. Ads and analytics only run with your consent – see the <a href="/privacy.html">privacy policy</a>.</p>
<h2>Using the printables</h2><p>You are welcome to print the pages for yourself, your family, your classroom or your own business. Please don't resell the files or offer them for download on other websites; link to the template page instead.</p>
<h2>Contact</h2><p>Ideas for a new template or found a mistake? Write to <a href="mailto:office@adstern.com">office@adstern.com</a>.</p>""")

    write("imprint.html", "page.html", title="Imprint | Printable Joy Lab", description="Legal notice for Printable Joy Lab.", h1="Imprint", ads=False, robots="noindex,follow", active="",
          body=f"""<h2>Media owner and publisher</h2><p>{LEGAL_ADDR}</p>
<h2>Company details</h2><p>Business purpose: advertising agency (Werbeagentur)<br>VAT ID: ATU54682507<br>Trade authority: Magistratisches Bezirksamt für den 1. Bezirk, Vienna</p>
<h2>Editorial line</h2><p>Free printable templates and guides on planning, organisation and paper.</p>
<p class="small muted">Information pursuant to § 5 E-Commerce-Gesetz and § 25 Mediengesetz (Austria).</p>""")

    write("privacy.html", "page.html", title="Privacy Policy | Printable Joy Lab", description="Privacy policy of Printable Joy Lab.", h1="Privacy policy",
          lead="Last updated: 29 October 2026", ads=False, robots="noindex,follow", active="",
          body=f"""<h2>Controller</h2><p>{LEGAL_ADDR}</p>
<h2>Hosting</h2><p>This website is delivered via GitHub Pages (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, USA). When you visit, GitHub processes technically necessary connection data such as your IP address, the requested address, browser information and time to deliver the site and protect it from attacks. The legal basis is our legitimate interest in secure operation (Art. 6(1)(f) GDPR). GitHub is certified under the EU-US Data Privacy Framework. Fonts are hosted on our own server; no connection to Google Fonts is made.</p>
<h2>Templates and PDF creation</h2><p>All templates and PDFs are generated in your browser. Your settings, habits, lists and titles are not sent to us. To remember your last settings, we store them in your browser's local storage; this is necessary for the function you requested. You can delete it at any time in your browser settings. If you copy a share link, your settings are part of that link – only share it if the content is not private.</p>
<h2>Consent management</h2><p>For advertising and analytics we use Google's consent management solution “Privacy &amp; messaging” (Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland), certified under the IAB Transparency &amp; Consent Framework. On your first visit you can accept, reject or choose individual purposes and vendors. You can change or withdraw your choice at any time via “Privacy settings” in the footer.</p>
<h2>Advertising (Google AdSense)</h2><p>We show ads via Google AdSense (Google Ireland Limited). Google may use cookies and similar technologies to deliver ads, limit how often you see them and measure their performance. Personalised ads are only shown with your consent (Art. 6(1)(a) GDPR); without consent, Google may show non-personalised or limited ads. Data may be transferred to the USA; Google is certified under the EU-US Data Privacy Framework. More: <a href="https://policies.google.com/technologies/ads" rel="noopener">How Google uses information from sites that use its services</a>.</p>
<h2>Analytics (Google Analytics 4)</h2><p>With your consent we use Google Analytics 4 to understand which templates are used and how the site can be improved. IP addresses are not stored in full by Google Analytics 4; Google signals and ad personalisation are disabled. Legal basis: consent (Art. 6(1)(a) GDPR). You can withdraw consent at any time via “Privacy settings”.</p>
<h2>Your rights</h2><p>You have the right to access, rectification, erasure, restriction of processing, data portability and objection, and the right to withdraw consent at any time. You may lodge a complaint with a supervisory authority; in Austria this is the Datenschutzbehörde (dsb.gv.at). Contact: <a href="mailto:office@adstern.com">office@adstern.com</a>.</p>""")

    write("404.html", "page.html", title="Page not found | Printable Joy Lab", description="This page does not exist.", h1="This page doesn't exist", ads=False, robots="noindex,follow", active="",
          body='<p>The page may have moved. Try one of our <a href="/">free templates</a>.</p>')
    (OUT / "advertise.html").write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/"><link rel="canonical" href="https://printablejoylab.com/"><title>Printable Joy Lab</title>', encoding="utf-8")
    (OUT / "parents.html").write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/"><link rel="canonical" href="https://printablejoylab.com/"><title>Printable Joy Lab</title>', encoding="utf-8")

    (OUT / "CNAME").write_text("printablejoylab.com\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "google9bf1079fd4bf073e.html").write_text("google-site-verification: google9bf1079fd4bf073e.html")
    (OUT / "ads.txt").write_text("google.com, pub-7811071715414905, DIRECT, f08c47fec0942fa0\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>2026-10-29</lastmod><priority>{pr}</priority></url>" for p, pr in PAGES)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    print(f"{len(PAGES)} indexable pages")


if __name__ == "__main__":
    main()
