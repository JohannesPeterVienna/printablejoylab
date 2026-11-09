"""Printable Joy Lab – statische Seiten bauen (GitHub Pages aus docs/)."""
import json, shutil, subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from content.tools import TOOLS, CATS, BY
from content.articles import ARTICLES

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
SITE = "https://printablejoylab.com"; V = "20261105d"
BUY_PLANNER = ""   # Lemon Squeezy checkout link – set once the product exists
UPDATED = "October 2026"
REVIEWED = "2026-11-03"; REVIEWED_TEXT = "November 3, 2026"   # last editorial review of all guides
CONTENT_UPDATED = "2026-11-04"   # last content change of template pages, home and about (sitemap lastmod)
GUIDES_UPDATED = "2026-11-03"    # last content change of the guides hub
LOADER = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7811071715414905" crossorigin="anonymous"></script>'
# Shop-Schalter: Solange False, werden shop.html und refunds.html gar nicht gebaut (404), es gibt keinen Link und
# keinen Eintrag in der Sitemap (AdSense-Prüfung 5.11.2026: keine Seite ohne funktionierenden Kauf). Erst auf True
# stellen, wenn ein echter Kauf über Lemon Squeezy durchgeht (nicht nur der Testmodus) und BUY_PLANNER gesetzt ist.
SHOP_ENABLED = False
SHOP_OPEN = SHOP_ENABLED and bool(BUY_PLANNER)
NAV = [("/", "Templates"), ("/weekly-planner.html", "Planners"), ("/monthly-calendar.html", "Calendars"), ("/habit-tracker.html", "Trackers"), ("/dot-grid.html", "Paper"), ("/guides.html", "Guides")]
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True, trim_blocks=True, lstrip_blocks=True)
PAGES = []
LEGAL_ADDR = "AdStern – Agentur für digitales Marketing<br>Seilerstätte 8/8, 1010 Wien, Österreich<br>Email: <a href='mailto:office@adstern.com'>office@adstern.com</a><br>Web: <a href='https://www.adstern.com'>www.adstern.com</a>"
ORG = {"@type": "Organization", "name": "Printable Joy Lab", "url": SITE + "/"}
AUTHOR = {"@type": "Organization", "name": "AdStern – Agentur für digitales Marketing", "url": SITE + "/about.html"}


GUIDES_INTRO = """<p>These eight guides answer the questions that come up most often once you start printing your own planners, calendars and paper. Each one has concrete measurements, a worked example, a short FAQ and the standards it relies on, and links to the templates it talks about. Here is what each guide covers, so you can go straight to the one you need.</p>
<h2>Which guide should you read?</h2>
<h3>Printing and paper</h3>
<ul><li><strong>Your grid prints too small, or the bottom of your calendar is cut off?</strong> Start with <a href="/print-at-actual-size.html">How to print at actual size</a>. It shows in numbers what “Fit to page” does (an A4 page fitted onto US Letter shrinks to about 94%), where the 100% setting hides in Chrome, Edge, Preview, Acrobat Reader and on phones, and how to check a print with a ruler.</li>
<li><strong>Not sure which paper pattern or weight to print?</strong> <a href="/choose-the-right-paper.html">Lined, grid, dot or isometric</a> compares the four patterns with line and square counts for A4 and US Letter, converts paper weights between gsm and pounds, and plans a bedroom floor plan on graph paper step by step.</li></ul>
<h3>Calendars and planning</h3>
<ul><li><strong>Printing a calendar for next year?</strong> <a href="/printable-calendar-2027.html">Printable calendar 2027</a> explains ISO week numbers (week 1 of 2027 starts on January 4), lists the US federal holidays with their observed dates, and compares yearly, monthly and weekly layouts.</li>
<li><strong>Want a weekly routine that holds?</strong> <a href="/plan-a-week-on-paper.html">How to plan a week on paper</a> walks through a 25-minute weekly review, a capacity check in hours and a fully filled example page.</li>
<li><strong>Tired of the daily “What's for dinner?”</strong> <a href="/meal-planning-one-page.html">Meal planning on one page</a> is a timed 20-minute routine with a sorted grocery list and food-safe timing for leftovers.</li>
<li><strong>Wondering whether planning on paper still makes sense?</strong> <a href="/paper-vs-digital-planning.html">Paper or app?</a> compares both honestly, summarizes what note-taking research does and does not show, and describes a hybrid routine.</li></ul>
<h3>Habits and journaling</h3>
<ul><li><strong>Starting a habit tracker?</strong> <a href="/habit-tracker-ideas.html">Habit tracker ideas that actually stick</a> turns vague goals into rows you can tick and shows how to review a finished month.</li>
<li><strong>Curious about bullet journaling?</strong> The <a href="/bullet-journal-starter.html">bullet journal starter kit</a> covers rapid logging, the core collections, migration and a complete first month, set up page by page.</li></ul>
<p>If you are new to printables, read the print guide first: the right scale setting makes the biggest difference to every template on this site.</p>"""


def write(path, template, **ctx):
    base = dict(site=SITE, v=V, updated=UPDATED, nav=NAV + ([("/shop.html", "2027 Planner")] if SHOP_OPEN else []), shop_open=SHOP_OPEN, active=ctx.get("active", "/" + path), jsonld=[], ads=True,
                robots=None, og_title=None, tools=TOOLS, cats=CATS, articles=ARTICLES)
    base.update(ctx)
    base["path"] = "/" if path == "index.html" else "/" + path
    (OUT / path).write_text(env.get_template(template).render(**base), encoding="utf-8")
    if base.get("robots") is None:
        PAGES.append((base["path"], ctx.get("priority", 0.6), ctx.get("lastmod", "2026-10-29")))


def split_first_section(html):
    """Split text after its first <h2> section, so the first ad only follows the first explanatory section."""
    first = html.find("<h2>")
    cut = html.find("<h2>", first + 1) if first >= 0 else -1
    return (html[:cut], html[cut:]) if cut > 0 else (html, "")


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + h} for i, (h, n) in enumerate(items)]}


def main():
    subprocess.run(["node", str(ROOT / "test_lab.js")], check=True)   # Vorlagen-Test: Build bricht bei Fehlern ab
    subprocess.run(["node", "--test", str(ROOT / "test_consent.js")], check=True)   # Datenschutz-Einstellungen EU/US
    subprocess.run(["node", "--test", str(ROOT / "test_tally.js")], check=True)     # Übergangs-Einwilligung Statistik
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT / "assets", OUT / "assets")

    write("index.html", "home.html", title="Printable Joy Lab: Free Customizable Planners, Calendars & Paper",
          description="Free printable planners, calendars, habit trackers, checklists and paper you customize in seconds – A4 or US Letter, your colors and dates – then download as PDF.",
          active="/", priority=1.0, lastmod=CONTENT_UPDATED,
          jsonld=[{"@context": "https://schema.org", "@type": "WebSite", "name": "Printable Joy Lab", "url": SITE + "/", "inLanguage": "en"}])

    for t in TOOLS:
        crumbs = [("/", "Templates"), ("/" + t["slug"] + ".html", t["name"])]
        related = [x for x in TOOLS if x["cat"] == t["cat"] and x["slug"] != t["slug"]][:4]
        related += [x for x in TOOLS if x not in related and x["slug"] != t["slug"]][:4 - len(related)] if len(related) < 4 else []
        ld = [crumbs_ld(crumbs),
              {"@context": "https://schema.org", "@type": "WebApplication", "name": f"{t['name']} generator – Printable Joy Lab", "url": f"{SITE}/{t['slug']}.html",
               "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "en", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}]
        guide_first, guide_rest = split_first_section(t["guide"])   # Werbung erst nach dem ersten Erklärabschnitt
        write(t["slug"] + ".html", "tool.html", title=(t["title"] + " | Printable Joy Lab" if len(t["title"]) < 46 else t["title"]), description=t["description"], h1=f"{t['name']}",
              lead=t["lead"], slug=t["slug"], cat=t["cat"], guide_first=guide_first, guide_rest=guide_rest, faq=t["faq"], related=related, crumbs=crumbs, jsonld=ld,
              active=next((h for h, l in NAV if h == "/" + t["slug"] + ".html"), ""), priority=0.9, lastmod=CONTENT_UPDATED)

    for a in ARTICLES:
        crumbs = [("/", "Templates"), ("/guides.html", "Guides"), ("/" + a["slug"] + ".html", a["title"])]
        ld = [crumbs_ld(crumbs), {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["description"],
              "inLanguage": "en", "author": AUTHOR, "publisher": ORG, "datePublished": a["published"], "dateModified": a["modified"], "mainEntityOfPage": f"{SITE}/{a['slug']}.html"}]
        links = [BY[s] for s in BY if f"/{s}.html" in a["body"]][:4]
        write(a["slug"] + ".html", "page.html", title=(a["title"] + " | Printable Joy Lab" if len(a["title"]) < 46 else a["title"]), description=a["description"], h1=a["title"],
              lead=a["teaser"], body_split=split_first_section(a["body"]), crumbs=crumbs, related=links, jsonld=ld, active="/guides.html", priority=0.7, reviewed=REVIEWED_TEXT, lastmod=a["modified"])

    guides = "".join(f'<li><a class="card" href="/{a["slug"]}.html"><strong>{a["title"]}</strong><span>{a["teaser"]}</span></a></li>' for a in ARTICLES)
    write("guides.html", "page.html", title="Guides – Printing, Planning & Paper | Printable Joy Lab",
          description="Eight practical guides: printing at actual size, paper patterns and weights, a 2027 calendar with ISO week numbers and US holidays, weekly planning, meal planning, habit trackers, bullet journaling and paper vs apps.",
          h1="Guides", lead="Practical know-how for printing, planning and paper.", active="/guides.html", priority=0.6, lastmod=GUIDES_UPDATED,
          body_split=split_first_section(GUIDES_INTRO + f'<h2>All guides</h2><ul class="cards text">{guides}</ul>'
               '<h2>About our templates</h2><p>Every template on Printable Joy Lab is generated from your settings in your own browser. The text below each template explains the ideas behind its layout – for example why college ruling is 9/32 inch or how ISO week numbers work.</p>'))

    write("about.html", "page.html", title="About Printable Joy Lab", description="Who makes Printable Joy Lab, how the templates are generated and how we check them.",
          h1="About Printable Joy Lab", lead="Customizable printables, generated in your browser.", priority=0.3, active="", lastmod=CONTENT_UPDATED,
          body="""<p>Printable Joy Lab is made by AdStern, a small digital agency in Vienna, Austria. We build free tools that are genuinely useful – and printables were a natural fit: almost everyone needs a planner page, a calendar or a sheet of graph paper now and then, but most downloads come in one fixed size and style.</p>
<h2>Who is behind it</h2><p>AdStern – Agentur für digitales Marketing, based at Seilerstätte 8/8, 1010 Wien, Österreich, develops the generator, writes the guides and is responsible for everything on the site; the full legal details are in the <a href="/imprint.html">imprint</a>. There are no accounts to create, and what you type into a template stays in your browser.</p>
<h2>What you will find here</h2><p>Twelve generators in four groups – paper (lined, graph, dot grid, isometric), calendars (monthly and yearly), planners (weekly, daily, meal) and trackers and lists (habit tracker, checklist, budget planner) – and a set of practical <a href="/guides.html">guides</a>. The guides cover printing at actual size, choosing paper patterns and weights, a 2027 calendar with ISO week numbers and US holidays, weekly and meal planning, habit tracking, bullet journaling, and an honest comparison of paper and apps.</p>
<h2>How the templates work</h2><p>Each template is described once as a set of lines, boxes and text positioned in millimeters. From that description your browser draws the live preview and creates the PDF – the same data for both, so what you see is what you print. Paper sizes follow ISO 216 (A4, A5) and the North American standards (US Letter, Half Letter). Calendars use the Gregorian calendar and ISO 8601 week numbers.</p>
<h2>How we check them</h2><p>Every time the site is updated, an automated test draws every template with many combinations of settings – all paper sizes, orientations, week starts and options – and checks that every line, box and label lands on the page. If a single check fails, the update is not published.</p>
<h2>Standards we follow</h2><p>Paper sizes are taken from their standards: A4 (210 × 297 mm) and A5 (148 × 210 mm) from ISO 216, US Letter (8.5 × 11 in) and Half Letter (5.5 × 8.5 in) from the North American sizes. The three line rulings are the US school rulings – 11/32, 9/32 and 1/4 inch. Week numbers follow ISO 8601: weeks start on Monday, and week 1 is the week with the year's first Thursday. Dates are calculated with the Gregorian calendar for every year from 1900 to 2100.</p>
<h2>How the guides are written</h2><p>The texts are written with the help of AI tools. Every template is covered by automated tests, and every text goes through a separate review against the linked sources before it is published. There is no editorial team; AdStern is responsible for all content. The measurements in the guides – how many lines fit on a page, how big a calendar box is, how many squares a grid has – are calculated from the same layout code that draws the templates, so the text and the PDF agree. Each guide shows the date of its last review, and where a guide relies on a standard, a study or an official source, it names it.</p>
<h2>Ads on this site</h2><p>The site is free and financed by ads from Google. Ad spaces are labeled “Advertisement”. Our own ad slots never appear inside a generator – not between the settings, the preview and the download buttons – so that nobody taps an ad by accident while making a page; Google may also place ads automatically on content pages. The generators work the same whether or not you consent to ads.</p>
<h2>Your data</h2><p>Your settings, habits and lists never leave your device: the PDF is created in your browser, and the last settings are remembered in your browser's local storage. Analytics and personalized ads only run with your consent. If you don't consent, Google may still show limited, non-personalized ads that use no advertising cookies; if your browser sends a Global Privacy Control signal, we pause all ad requests and fill no ad slots. Details are in the <a href="/privacy.html">privacy policy</a>.</p>
<h2>Using the printables</h2><p>You are welcome to print the pages for yourself, your family, your classroom or your own business. Please don't resell the files or offer them for download on other websites; link to the template page instead.</p>
<h2>Contact</h2><p>Ideas for a new template or found a mistake? Write to <a href="mailto:office@adstern.com">office@adstern.com</a>. If something prints wrongly, tell us the template, the paper size and your browser or PDF viewer; a share link with your settings (the “Copy link to these settings” button) lets us reproduce the exact page.</p>""")

    write("imprint.html", "page.html", title="Imprint | Printable Joy Lab", description="Legal notice for Printable Joy Lab.", h1="Imprint", ads=False, robots="noindex,follow", active="",
          body=f"""<h2>Media owner and publisher</h2><p>{LEGAL_ADDR}</p>
<h2>Company details</h2><p>Business purpose: advertising agency (Werbeagentur)<br>VAT ID: ATU54682507<br>Trade authority: Magistratisches Bezirksamt für den 1. und 8. Bezirk, Vienna<br>Chamber membership: Austrian Economic Chamber Vienna (Wirtschaftskammer Wien), advertising and market communication group<br>Professional title: advertising agency (Werbeagentur), trade licence granted in Austria<br>Applicable regulations: Austrian Trade Regulation Act (Gewerbeordnung), available at <a href="https://www.ris.bka.gv.at" rel="noopener">www.ris.bka.gv.at</a></p>
<h2>Editorial line</h2><p>Free printable templates and guides on planning, organisation and paper.</p>
<p class="small muted">Information pursuant to § 5 E-Commerce-Gesetz and § 25 Mediengesetz (Austria).</p>""")

    write("privacy.html", "page.html", title="Privacy Policy | Printable Joy Lab", description="Privacy policy of Printable Joy Lab.", h1="Privacy policy",
          lead="Last updated: 5 November 2026", ads=False, robots="noindex,follow", active="",
          body=f"""<h2>Controller</h2><p>{LEGAL_ADDR}</p>
<h2>Hosting</h2><p>This website is delivered via GitHub Pages (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, USA). When you visit, GitHub processes technically necessary connection data such as your IP address, the requested address, browser information and time to deliver the site and protect it from attacks. The legal basis is our legitimate interest in secure operation (Art. 6(1)(f) GDPR). GitHub is certified under the EU-US Data Privacy Framework. Fonts are hosted on our own server; no connection to Google Fonts is made.</p>
<h2>Templates and PDF creation</h2><p>All templates and PDFs are generated in your browser. Your settings, habits, lists and titles are not sent to us. To remember your last settings, we store them in your browser's local storage; this is necessary for the function you requested. You can delete it at any time in your browser settings. If you copy a share link, your settings are part of that link – only share it if the content is not private.</p>
<h2>Consent management</h2><p>For advertising and analytics we use Google's consent management solution “Privacy &amp; messaging” (Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland), certified under the IAB Transparency &amp; Consent Framework. On your first visit you can accept, reject or choose individual purposes and vendors. You can change or withdraw your choice at any time via “Privacy settings” in the footer.</p>
<h2 id="visitor-tally">Interim consent notice for statistics (“Visitor tally”)</h2><p>At the moment Google’s consent message is set up but is not displayed on this site. So that visits can still only be counted with your consent, we show our own small notice while this is the case. It appears about three seconds after a page has loaded if Google’s consent management has not reported a decision by then and does not report that the GDPR does not apply to your visit. It asks only about statistics with Google Analytics (Google Ireland Limited); it is not a consent to advertising, and it never switches on any advertising storage or ad personalisation – these stay “denied”. “Accept” and “Decline” are equal choices; until you choose, Google Analytics stays off.</p>
<p>What is stored: your choice is saved in your browser’s local storage under the key <code>pjl-tally</code>, with the content “granted” or “denied”, a version number and the time of your choice. This entry is necessary to respect your decision and is not sent to us or to Google. After 12 months, or if we change the notice, we ask again. If you accept, Google Analytics loads as described in the next section; it sets cookies on your device (<code>_ga</code>, <code>_ga_…</code>), and data may be transferred to the USA (Google is certified under the EU-US Data Privacy Framework). Closing the notice with “×” (or Escape) stores nothing and is not consent; we ask again on the next page. If you decline or later withdraw, measurement stops at once, Google Analytics is switched off for this site and any Google Analytics cookies (<code>_ga</code>, <code>_ga_…</code>) set for this domain are deleted.</p>
<p>Legal basis: your consent (Art. 6(1)(a) GDPR; for storing and reading information on your device § 165(3) of the Austrian Telecommunications Act 2021, TKG 2021). You can change or withdraw your choice at any time via “Privacy settings” at the bottom of every page, including this one. Priority of Google’s consent management: as soon as Google’s consent message is displayed or reports a decision, only that decision counts; our notice is then closed and no longer shown, and a choice stored in it is deleted; if you had accepted in our notice and then decline in Google’s message, the Google Analytics cookies are deleted as well. If your browser sends a Global Privacy Control signal, Google Analytics stays off and the notice is not shown. On pages without ads (such as this privacy policy and the imprint) no Google code is loaded; there “Privacy settings” opens this notice so you can change or withdraw a choice made in it.</p>
<h2>Advertising (Google AdSense)</h2><p>We show ads via Google AdSense (Google Ireland Limited). Google may use cookies and similar technologies to deliver ads, limit how often you see them and measure their performance. Personalised ads are only shown with your consent (Art. 6(1)(a) GDPR). Non-personalised ads, which are based on page content, still use cookies or similar identifiers for frequency capping, aggregated reporting and fraud prevention, so they also require your consent to storing and accessing information on your device. Without that consent Google can only show limited ads. Limited ads are not personalised and do not use cookies or local storage for personalised advertising; Google may still use technical data, and where permitted storage, for fraud prevention and frequency limits as described in its documentation. If your browser sends a Global Privacy Control signal, we don’t request any ads: Google’s ad code still loads, but ad requests stay paused, and all Google storage and measurement features stay set to “denied”. Data may be transferred to the USA; Google is certified under the EU-US Data Privacy Framework. More: <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">How Google uses information from sites or apps that use its services</a> and <a href="https://policies.google.com/technologies/ads" rel="noopener">how Google uses cookies in advertising</a>.</p>
<p>Third-party vendors, including Google, use cookies to serve ads based on your previous visits to this and other websites. Google's advertising cookies let it and its partners show ads based on those visits. You can turn off personalised advertising in <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a>, and opt out of other participating vendors at <a href="https://www.aboutads.info/choices/" rel="noopener">aboutads.info</a> or, in Europe, <a href="https://www.youronlinechoices.eu/" rel="noopener">youronlinechoices.eu</a>.</p>
<h2>Analytics (Google Analytics 4)</h2><p>With your consent we use Google Analytics 4 to understand which templates are used and how the site can be improved. Until you decide, all Google storage and measurement features in our setup are set to “denied” (Google Consent Mode). Analytics only loads once you have accepted it in our interim notice (see “Interim consent notice for statistics” above) while Google’s consent message is not displayed, or once Google’s consent message reports both your consent to “Store and/or access information on a device” for the vendor Google and your consent to analytics storage; if either is missing or unclear, it does not load. Where the consent message reports that the GDPR does not apply to your visit, analytics loads only if it reports analytics as granted or not requiring consent and confirms that you have not opted out under a U.S. state privacy law; otherwise it stays off. If you withdraw or change your consent, measurement stops immediately: Google Analytics is switched off and sends no further data until you consent again. IP addresses are not stored in full by Google Analytics 4; event data is stored for the retention period set in our Google Analytics property and then deleted; Google signals and ad personalisation are disabled. Legal basis: consent (Art. 6(1)(a) GDPR). You can withdraw consent at any time via “Privacy settings”.</p>
<h2>Your rights</h2><p>You have the right to access, rectification, erasure, restriction of processing, data portability and objection, and the right to withdraw consent at any time. You can change or withdraw your consent to ads and analytics at any time yourself via “Privacy settings” at the bottom of every page.</p><h2>Complaints to the data protection authority</h2><p>If you believe that the processing of your data breaches data protection law, you can contact the competent supervisory authority directly:<br>Österreichische Datenschutzbehörde (Austrian Data Protection Authority), Barichgasse 40–42, 1030 Vienna, Austria<br>Email: <a href="mailto:dsb@dsb.gv.at">dsb@dsb.gv.at</a> · Web: <a href="https://www.dsb.gv.at" rel="noopener">www.dsb.gv.at</a></p>""")

    if SHOP_OPEN:   # Shop und Rückgaberegeln nur bei funktionierendem Kauf (Schalter SHOP_ENABLED oben)
        pics = [("1", "Cover"), ("2", "Clickable contents"), ("3", "Year at a glance"), ("5", "Monthly calendar"), ("17", "Weekly planner"), ("70", "Habit tracker"), ("82", "Monthly budget"), ("94", "Meal planner")]
        gallery = "".join(f'<figure><img src="/assets/shop/planner-p{n}.webp" alt="{c} page of the 2027 planner" width="497" height="702" loading="lazy"><figcaption>{c}</figcaption></figure>' for n, c in pics)
        buy = (f'<a class="btn big" href="{BUY_PLANNER}" rel="noopener">Buy the 2027 Planner – €9</a>' if BUY_PLANNER else
               '<span class="btn big disabled" aria-disabled="true">Checkout opens shortly</span>')
        write("shop.html", "page.html", title="The 2027 Planner – 111-Page Printable & Digital Planner (PDF) | Printable Joy Lab",
              description="The complete 2027 planner as PDF: year, months, 53 weekly spreads, habit trackers, budget and meal pages – A4 and US Letter, Monday or Sunday start, clickable contents.",
              h1="The 2027 Planner", lead="Everything from our free templates, ready-made for the whole year in one beautifully consistent PDF – 111 pages.", ads=False, active="/shop.html", robots=None if SHOP_OPEN else "noindex,follow", priority=0.8,
              jsonld=[{"@context": "https://schema.org", "@type": "Product", "name": "The 2027 Planner (PDF)", "brand": {"@type": "Brand", "name": "Printable Joy Lab"},
                       "description": "111-page printable and digital planner for 2027 in A4 and US Letter, Monday or Sunday start.", "image": SITE + "/assets/shop/planner-p1.webp",
                       **({"offers": {"@type": "Offer", "price": "9.00", "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": SITE + "/shop.html"}} if BUY_PLANNER else {})}],
              body=f"""<div class="product">
    <div class="gallery">{gallery}</div>
    <div class="buybox">
      <p class="price">€9 <span class="small muted">incl. VAT · instant download</span></p>
      {buy}
      <ul class="ticks"><li>111 pages, crisp vector PDF</li><li>A4 and US Letter – both included</li><li>Week starts Monday or Sunday – both included</li><li>Clickable contents for tablets (GoodNotes, Notability, Xodo …)</li><li>Print as often as you like for personal use</li></ul>
      <p class="small muted">Secure checkout by Lemon Squeezy, our merchant of record. You receive the download link by email right after payment. <a href="/refunds.html">Refund policy</a></p>
    </div></div>
    <h2>What's inside</h2>
    <ul><li><strong>Cover &amp; clickable contents</strong> – jump to any section or month in one tap.</li>
    <li><strong>Year at a glance</strong> for 2027 and 2028.</li>
    <li><strong>12 monthly calendars</strong> with week numbers and a notes area.</li>
    <li><strong>53 dated weekly spreads</strong> – every week of 2027, from Dec 28, 2026 to Jan 2, 2028, with day boxes, notes and a weekly to-do list.</li>
    <li><strong>12 habit trackers</strong> with 22 rows each and a “done” counter.</li>
    <li><strong>12 monthly budget pages</strong> with planned, actual and difference columns.</li>
    <li><strong>6 meal planners</strong> with grocery lists by category.</li>
    <li><strong>Lists &amp; notes</strong>: goals, books to read, birthdays &amp; gifts, a to-do list, 4 dot grid and 4 lined pages.</li></ul>
    <h2>Print it or use it digitally</h2>
    <p>Print the whole planner and punch it for a ring binder, or print only the sections you need. On an iPad or Android tablet, import the PDF into a note-taking app and write directly on the pages – the contents page and the small “Contents” link on every page make navigation quick.</p>
    <h2>Why buy if the templates are free?</h2>
    <p>Our free generators make one page or one month at a time, exactly as you configure it. The planner saves you the work: 111 matching pages, already dated, in a consistent design, with clickable navigation that the free pages don't have. Your purchase also keeps the free templates free – thank you!</p>
    <h2>Questions</h2>
    <details><summary>Which paper size do I get?</summary><p>Both. The download contains four PDFs: A4 and US Letter, each with Monday or Sunday as the first day of the week.</p></details>
    <details><summary>Can I print it more than once?</summary><p>Yes – print as many copies as you need for yourself and your household. Please don't share or resell the files.</p></details>
    <details><summary>Is it dated?</summary><p>Yes: calendars and weekly pages are dated for 2027. Habit, meal, budget and list pages work any time.</p></details>
    <details><summary>What if something is wrong with my download?</summary><p>Write to <a href="mailto:office@adstern.com">office@adstern.com</a> and we'll fix it quickly. See our <a href="/refunds.html">refund policy</a>.</p></details>""")

        write("refunds.html", "page.html", title="Refund Policy | Printable Joy Lab", description="Refund policy for digital products from Printable Joy Lab.",
              h1="Refund policy", lead="Last updated: 29 October 2026", ads=False, robots="noindex,follow", active="",
              body="""<p>Our paid products are digital downloads (PDF files). Orders are processed by <strong>Lemon Squeezy</strong>, which acts as the merchant of record and handles payment, invoicing and sales tax.</p>
    <h2>Right of withdrawal for digital content</h2><p>If you are a consumer in the EU or UK, you normally have a 14-day right of withdrawal. For digital content delivered immediately, this right ends once the download is provided, provided you agreed at checkout to immediate delivery and acknowledged that you thereby lose your right of withdrawal.</p>
    <h2>Our promise</h2><p>If a file is damaged, incomplete or not as described, write to <a href="mailto:office@adstern.com">office@adstern.com</a> within 30 days of purchase with your order number. We will send a corrected file or refund your purchase in full. If you bought the wrong paper size or week start, don't worry – every download already contains all versions.</p>
    <h2>How refunds are paid</h2><p>Refunds are issued by Lemon Squeezy to the original payment method. Depending on your bank, it can take 5–10 business days to appear.</p>
    <h2>Contact</h2><p>AdStern – Agentur für digitales Marketing, Seilerstätte 8/8, 1010 Wien, Österreich · <a href="mailto:office@adstern.com">office@adstern.com</a></p>""")

    write("404.html", "page.html", title="Page not found | Printable Joy Lab", description="This page does not exist.", h1="This page doesn't exist", ads=False, robots="noindex,follow", active="",
          body='<p>The page may have moved. Try one of our <a href="/">free templates</a>.</p>')

    (OUT / "CNAME").write_text("printablejoylab.com\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "google9bf1079fd4bf073e.html").write_text("google-site-verification: google9bf1079fd4bf073e.html")
    (OUT / "ads.txt").write_text("google.com, pub-7811071715414905, DIRECT, f08c47fec0942fa0\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>" for p, pr, lm in PAGES)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    check_head()
    print(f"{len(PAGES)} indexable pages")


def check_head():
    """Indexable pages: consent defaults → static AdSense loader (exactly once) → consent.js. noindex pages: no loader."""
    indexed = {("/index.html" if p == "/" else p) for p, _, _ in PAGES}
    for f in OUT.glob("*.html"):
        html = f.read_text(encoding="utf-8"); head = html.split("</head>", 1)[0]
        if "/" + f.name in indexed:
            d, l, c = head.find('gtag("consent","default"'), head.find(LOADER), head.find("/assets/consent.js")
            assert html.count("adsbygoogle.js") == 1 and -1 < d < l < c, f"head order wrong: {f.name}"
        else:
            assert "adsbygoogle" not in html, f"loader on a non-indexable page: {f.name}"


if __name__ == "__main__":
    main()
