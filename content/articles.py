"""Guides – longer articles that support the templates.

Each guide: concrete numbers, a worked example, an FAQ and a sources section (standards are named, no invented links).
"published" is the first publication date, "modified" the date of the last content change (dateModified + sitemap).
"""

ARTICLES = [
{
"slug": "print-at-actual-size",
"published": "2026-10-29", "modified": "2026-11-18",
"title": "How to print at actual size (and why your grid comes out wrong)",
"teaser": "A4 vs US Letter, “Fit to page” and the settings that keep 5 mm at 5 mm.",
"description": "Why printed grids and calendars come out slightly too small, how A4 and US Letter differ, what “Fit” does in numbers, and the exact print settings for Windows, Mac, Acrobat, iPhone and Android.",
"body": """
<p>You download a 5 mm grid, print it, and the squares measure 4.7 mm. Or the last row of your monthly calendar disappears at the bottom of the sheet. In almost every case the PDF is fine and a single setting in the print dialog is responsible. This guide explains what happens in numbers, which option to pick, and how to check the result with a ruler.</p>

<h2>Why printed grids come out too small</h2>
<p>A PDF stores its page size exactly. When you print, the program compares that page with the sheet in the tray and with the area the printer can physically reach. If you have chosen an option such as <em>Fit</em>, <em>Fit to page</em>, <em>Fit to printable area</em> or <em>Shrink oversized pages</em>, the program shrinks the whole page until it fits inside that area. A 3–6% reduction is invisible on a letter but obvious on graph paper, dot grid or a calendar, where the spacing is the whole point of the page.</p>
<p>Two different problems usually hide behind “it prints wrong”:</p>
<ul><li><strong>Paper size mismatch:</strong> the PDF is A4 but the printer holds US Letter (or the other way round). The program either cuts off part of the page or scales it.</li>
<li><strong>Scaling to the printable area:</strong> the sizes match, but the program still shrinks the page a little so that it fits inside the printer's unprintable border.</li></ul>
<p>Both are solved in the same two steps: generate the template in the paper size you really have, and print at 100%.</p>

<h2>A4 and US Letter in numbers</h2>
<p>A4 belongs to the international A series (ISO 216). US Letter is the North American office size; the Printer Working Group's media list also carries it under the aliases “a” and “engineering-a”. They look similar, but they are different shapes:</p>
<div class="table-wrap"><table>
<thead><tr><th>Size</th><th>Millimeters</th><th>Inches</th><th>Where it is standard</th></tr></thead>
<tbody>
<tr><td>A4</td><td>210 × 297</td><td>8.27 × 11.69</td><td>Most countries outside North America</td></tr>
<tr><td>US Letter</td><td>215.9 × 279.4</td><td>8.5 × 11</td><td>USA, Canada, Mexico, parts of Latin America</td></tr>
<tr><td>A5</td><td>148 × 210</td><td>5.83 × 8.27</td><td>Half of A4; common planner and notebook size</td></tr>
<tr><td>Half Letter</td><td>139.7 × 215.9</td><td>5.5 × 8.5</td><td>Half of Letter; US planner inserts</td></tr>
</tbody></table></div>
<p>US Letter is 5.9 mm wider than A4 but 17.6 mm shorter. That height difference is why an A4 calendar printed on Letter paper loses its bottom edge, or gets shrunk. Every template on this site lets you choose A4, US Letter, A5 or Half Letter, so the PDF can match the sheet before you even open the print dialog. Sizes beyond these four – Legal, A3, B5, envelopes and more – are in our <a href="/paper-sizes.html#table">paper size reference</a>.</p>
<figure class="figure"><svg viewBox="0 0 340 176" role="img" aria-label="A4 and US Letter drawn to the same scale with their top left corners aligned">
<rect x="10" y="12" width="105" height="148.5" class="fig-page"/><rect x="10" y="12" width="107.95" height="139.7" class="fig-b"/>
<text x="132" y="30" class="fig-t">A4 (red): 210 × 297 mm</text><text x="132" y="46" class="fig-t">US Letter (black): 215.9 × 279.4 mm</text>
<text x="132" y="70" class="fig-tm">Letter is 5.9 mm wider</text><text x="132" y="83" class="fig-tm">and 17.6 mm shorter.</text>
<text x="132" y="159" class="fig-tm">← 17.6 mm of an A4 page do not fit on Letter</text>
</svg><figcaption>A4 and US Letter drawn to the same scale, top left corners aligned. The strip at the bottom is what gets cut off – or what “Fit” removes by shrinking the whole page to 94.1%.</figcaption></figure>

<h2>What “Fit” does to your page</h2>
<p>Scaling is simple arithmetic: the program divides the available width and height by the page width and height and uses the smaller ratio. The table shows typical results for a page that contains a 5 mm grid.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Scale</th><th>5 mm grid prints as</th><th>10 cm measures</th></tr></thead>
<tbody>
<tr><td>Matching paper, printed at 100% / Actual size</td><td>100%</td><td>5.00 mm</td><td>10.0 cm</td></tr>
<tr><td>A4 PDF fitted onto US Letter (279.4 ÷ 297)</td><td>about 94%</td><td>about 4.70 mm</td><td>about 9.4 cm</td></tr>
<tr><td>US Letter PDF fitted onto A4 (210 ÷ 215.9)</td><td>about 97%</td><td>about 4.86 mm</td><td>about 9.7 cm</td></tr>
<tr><td>Matching A4, fitted inside a 4 mm border on every side (202 ÷ 210)</td><td>about 96%</td><td>about 4.81 mm</td><td>about 9.6 cm</td></tr>
</tbody></table></div>
<p>The last row is the sneaky one: even with the correct paper, “Fit to printable area” shrinks the page because the printer cannot reach the outermost few millimeters. The real border depends on the printer model; the 4 mm in the table is an example.</p>
<p><strong>Try it with your own values.</strong> These links open the print scale calculator with the rows of the table: <a href="/paper-sizes.html?doc=iso_a4_210x297mm&amp;sheet=na_letter_8.5x11in&amp;mode=fit&amp;border=0&amp;feature=5#scale">A4 page on US Letter</a>, <a href="/paper-sizes.html?doc=na_letter_8.5x11in&amp;sheet=iso_a4_210x297mm&amp;mode=fit&amp;border=0&amp;feature=5#scale">US Letter page on A4</a>, <a href="/paper-sizes.html?doc=iso_a4_210x297mm&amp;sheet=iso_a4_210x297mm&amp;mode=fit&amp;border=4&amp;feature=5#scale">A4 inside a 4 mm border</a>. There you can change the paper, the border and the spacing you care about, for example 7.1 mm for college-ruled lines.</p>

<h2>Where to find the setting</h2>
<p>Program menus change between versions, but the wording is usually close to the following. The goal is always the same: <strong>100%</strong>, <strong>Actual size</strong>, <strong>Default</strong> or <strong>None</strong> – never a “fit” or “shrink” option.</p>
<ul><li><strong>Chrome and Edge (Windows, Mac, ChromeOS):</strong> open <em>More settings</em> and look at <em>Scale</em>. Choose <em>Default</em>, <em>Actual size</em> or <em>Custom</em> with 100. Avoid <em>Fit to page</em> or <em>Fit to printable area</em>. Also check that <em>Paper size</em> matches the PDF.</li>
<li><strong>Preview on a Mac:</strong> in the print dialog, set <em>Scale</em> to 100% and make sure <em>Scale to Fit</em> is not selected. Check the paper size in the same dialog.</li>
<li><strong>Adobe Acrobat Reader:</strong> under <em>Page Sizing &amp; Handling</em>, choose <em>Actual size</em>. Both <em>Fit</em> and <em>Shrink oversized pages</em> can reduce a full-size page.</li>
<li><strong>Firefox:</strong> under <em>Scale</em>, pick 100 instead of <em>Fit to page width</em>.</li>
<li><strong>iPhone and iPad (AirPrint):</strong> there is usually no scale control. Generate the PDF in the size that is loaded in the printer, then choose the matching paper size in the print options if they are offered.</li>
<li><strong>Android:</strong> in the print preview, select the paper size first; if the printer plugin offers a scaling or “fit” option, switch it off or set it to 100%.</li></ul>

<h2>Why every template keeps a white border</h2>
<p>A printer cannot mark a sheet reliably right up to its edges. The W3C specification for paged media calls this strip the non-printable area and notes that its size depends on the printer. You can measure yours: the <a href="/print-test-page.html">print test page</a> has a short ruler on each side that starts at the paper edge, and the first tick you can see is the border on that side. Our templates keep 12 mm free at the top and sides on A4 and US Letter and 9 mm on A5 and Half Letter. At the bottom the border is 5 mm larger, because the optional site credit sits there. Because nothing important lies in the outer few millimeters, you can print at 100% without losing a line – there is no need to let the printer shrink anything.</p>

<h2>Worked example: checking a print with a ruler</h2>
<p>Suppose you want to be sure your 5 mm dot grid really prints at 5 mm before you print a 50-sheet stack.</p>
<ol><li>Open the <a href="/print-test-page.html">print test page</a> and choose the paper that is in your printer.</li>
<li>Print it with the scale set to 100% (see the list above).</li>
<li>Measure the square across and down. It is drawn exactly 100 mm wide and 100 mm high, so the millimeters you read are the scale in percent.</li>
<li>Type both numbers into the ruler check below the generator, or open an example: <a href="/print-test-page.html?across=94&amp;down=94#check">94 × 94 mm</a> is 94%, which is what “Fit” produces when an A4 page lands on US Letter paper; <a href="/print-test-page.html?across=97.3&amp;down=97.3#check">97.3 mm</a> means a Letter page on A4; <a href="/print-test-page.html?across=96&amp;down=96#check">about 96 mm</a> on matching paper means the page was fitted inside the printer's border.</li>
<li>Fix the setting, print once more and measure again. Only then print the rest of the stack in the pattern you actually wanted.</li></ol>
<p>A difference of half a millimeter over 10 cm is hard to see on the finished page and usually not worth chasing; a difference of several millimeters is always a scaling setting.</p>

<h2>Small pages, booklets and two-sided printing</h2>
<p>If you want A5 pages, the cleanest result is to create the A5 version of the template and print it on A5 paper. Printing an A4 page “2 pages per sheet” also works, but the printer then reduces each page to about 71% (1 ÷ √2) – a 5 mm grid becomes roughly 3.5 mm. For which paper weight to load, see <a href="/choose-the-right-paper.html">our paper guide</a>, which has a gsm to pound conversion table.</p>

<h2>FAQ</h2>
<h3>Why is the bottom of my calendar missing?</h3>
<p>The PDF is taller than the sheet, which happens when an A4 page is printed on US Letter without scaling. Generate the calendar in US Letter instead, or print the A4 version on A4 paper.</p>
<h3>Is “Default” the same as 100%?</h3>
<p>In most browsers, yes: <em>Default</em> prints the page at its stored size. If a ruler check shows a reduction, choose <em>Custom</em> and type 100.</p>
<h3>Can I print edge to edge?</h3>
<p>Only some printers support borderless printing, mostly for photo paper. It is not needed here, because the templates already keep a safe border.</p>

<h2>Sources and standards</h2>
<ul><li><strong>The Printer Working Group, PWG 5101.1-2023, “PWG Media Standardized Names v2.1”</strong>: <a href="https://ftp.pwg.org/pub/pwg/candidates/cs-pwgmsn21-20230915-5101.1.pdf" rel="noopener">ftp.pwg.org/pub/pwg/candidates/cs-pwgmsn21-20230915-5101.1.pdf</a> – dimensions of A4, A5, US Letter and Half Letter (media names <code>iso_a4_210x297mm</code>, <code>iso_a5_148x210mm</code>, <code>na_letter_8.5x11in</code>, <code>na_invoice_5.5x8.5in</code>). Accessed 18 November 2026.</li>
<li><strong>NIST, “SI Units – Length”</strong>: <a href="https://www.nist.gov/pml/owm/si-units-length" rel="noopener">nist.gov/pml/owm/si-units-length</a> – 1 inch = 25.4 mm exactly. Accessed 18 November 2026.</li>
<li><strong>W3C, “CSS Paged Media Module Level 3”</strong> (Working Draft, 14 September 2023): <a href="https://www.w3.org/TR/css-page-3/" rel="noopener">w3.org/TR/css-page-3</a> – printable and non-printable area. Accessed 18 November 2026.</li>
<li>ISO 216 is the standard usually named for the A series. We did not read it and quote the dimensions from the Printer Working Group list instead.</li>
<li>Scaling figures are calculated from these dimensions. The names of the print dialog options reflect common program versions at the time of the review on November 3, 2026; we did not test them on specific devices.</li></ul>

""",
},
{
"slug": "choose-the-right-paper",
"published": "2026-10-29", "modified": "2026-11-18",
"title": "Lined, grid, dot or isometric: which paper for which job?",
"teaser": "Rulings, grid sizes and paper weights compared – with gsm to pound conversions.",
"description": "Compare lined, graph, dot grid and isometric paper: standard spacings, how many lines or squares fit on A4 and US Letter, paper weights in gsm and pounds, and a worked floor-plan example.",
"body": """
<p>Lines, squares, dots and triangles are not just a matter of taste. Each pattern makes one kind of work easier and another slightly harder. This guide compares the four patterns with real measurements, shows how much fits on a page, explains paper weights in both grams per square meter and US pounds, and walks through one practical example from start to finish.</p>

<h2>The four patterns at a glance</h2>
<p>All four patterns can be printed on A4, US Letter, A5 or Half Letter. The first question is what you will mostly do on the page: write sentences, line up numbers, mix text with boxes and sketches, or draw objects in three dimensions.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Typical spacing</th><th>Best for</th><th>Less suited for</th></tr></thead>
<tbody>
<tr><td><a href="/lined-paper.html">Lined</a></td><td>6.35–8.73 mm (1/4–11/32 in)</td><td>Running text, letters, essays, lecture notes</td><td>Tables, diagrams</td></tr>
<tr><td><a href="/graph-paper.html">Graph</a></td><td>5 mm, 1 cm, 1/4 in, 1/5 in</td><td>Math, charts, floor plans, pixel and stitch patterns</td><td>Long handwritten text (busy background)</td></tr>
<tr><td><a href="/dot-grid.html">Dot grid</a></td><td>5 mm (most common), 4–10 mm</td><td>Journaling, planning layouts, mixed notes and sketches</td><td>Precise technical drawing</td></tr>
<tr><td><a href="/isometric-paper.html">Isometric</a></td><td>5–10 mm triangle side</td><td>3D sketches, product ideas, game maps</td><td>Writing</td></tr>
</tbody></table></div>

<h2>Lined paper: the three rulings in numbers</h2>
<p>US school rulings are defined in fractions of an inch. Wide ruling is 11/32 in (8.73 mm), college ruling 9/32 in (7.14 mm) and narrow ruling 1/4 in (6.35 mm). The table shows how many writing lines our generator fits on a portrait page with the name and date header switched on.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ruling</th><th>Spacing</th><th>Lines on A4</th><th>Lines on US Letter</th></tr></thead>
<tbody>
<tr><td>Wide</td><td>8.73 mm (11/32 in)</td><td>29</td><td>27</td></tr>
<tr><td>College</td><td>7.14 mm (9/32 in)</td><td>35</td><td>33</td></tr>
<tr><td>Narrow</td><td>6.35 mm (1/4 in)</td><td>40</td><td>37</td></tr>
</tbody></table></div>
<p>A practical way to choose: write one sentence in your normal handwriting on scrap paper and measure the height of a capital letter. If capitals are taller than about half the spacing, the lines will feel cramped; go one ruling wider.</p>

<h2>Graph paper and dot grid: how many squares or dots fit</h2>
<p>Grid paper is named after the side of one square. A 1/4 in grid has four squares per inch (6.35 mm) and is the classic US quad ruling; a 1/5 in grid (5.08 mm) is common on engineering pads. Dot grid uses the same idea but prints only the corners. With our margins, a portrait page holds:</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>A4 portrait</th><th>US Letter portrait</th></tr></thead>
<tbody>
<tr><td>5 mm graph paper</td><td>37 × 53 squares</td><td>38 × 50 squares</td></tr>
<tr><td>1/4 in graph paper</td><td>29 × 42 squares</td><td>30 × 39 squares</td></tr>
<tr><td>1 cm graph paper</td><td>18 × 26 squares</td><td>19 × 25 squares</td></tr>
<tr><td>5 mm dot grid</td><td>38 × 54 dots</td><td>39 × 51 dots</td></tr>
</tbody></table></div>
<p>On dot grid, the dot size matters as much as the spacing. Our fine, medium and bold dots are about 0.36, 0.52 and 0.72 mm across. Fine dots almost disappear under ink; bold dots survive faint printers and photocopies. On isometric paper, a 5 mm triangle has a height of about 4.33 mm (5 × √3 ÷ 2), so rows are slightly closer together than the triangle side suggests.</p>

<h2>Paper weight: gsm and pounds</h2>
<p>Outside the US, paper weight is given as grammage in grams per square meter (g/m² or gsm). In the US it is given in pounds: the weight of 500 sheets in the paper grade's “basis size”. Because bond, text and cover paper have different basis sizes, the same pound number means different paper. That is why a 65 lb cover stock is much heavier than 24 lb bond. The conversions below use the standard basis sizes (bond 17 × 22 in, text 25 × 38 in, cover 20 × 26 in) and are rounded.</p>
<div class="table-wrap"><table>
<thead><tr><th>US label</th><th>Approx. gsm</th><th>Typical use for printables</th></tr></thead>
<tbody>
<tr><td>20 lb bond</td><td>75 g/m²</td><td>Everyday copy paper; fine for lists and test prints</td></tr>
<tr><td>24 lb bond (≈ 60 lb text)</td><td>90 g/m²</td><td>Planner pages written on both sides with ballpoint or gel pen</td></tr>
<tr><td>28 lb bond (≈ 70 lb text)</td><td>105 g/m²</td><td>Less show-through with fineliners and light markers</td></tr>
<tr><td>32 lb bond (≈ 80 lb text)</td><td>120 g/m²</td><td>Notebook feel; good for dot grid journals</td></tr>
<tr><td>65 lb cover</td><td>176 g/m²</td><td>Covers, dividers, calendars on a wall</td></tr>
</tbody></table></div>
<p>The common European office paper of 80 g/m² sits between the first two rows, at roughly 21 lb bond. Before you load heavier paper, check the maximum weight in your printer's specifications; many home printers handle 120 g/m² from the main tray but need the rear or manual feed for card stock.</p>

<h2>Worked example: a floor plan on graph paper</h2>
<p>You want to sketch a bedroom of 4.2 m × 3.6 m and try out furniture positions.</p>
<ol><li><strong>Pick the grid:</strong> 5 mm graph paper, landscape. On A4 landscape the page holds 54 × 36 squares; on US Letter landscape 51 × 37.</li>
<li><strong>Pick the scale:</strong> with 1 square = 10 cm, the room needs 42 × 36 squares. That fits on both sizes, with 9–12 squares to spare for labels on the long side.</li>
<li><strong>Use bold lines:</strong> set a bold line every 10 squares, so each bold square equals exactly 1 m. Counting becomes much faster. <a href="/graph-paper.html?grid=5&amp;major=10&amp;orient=landscape">Open this exact sheet</a> (5 mm grid, bold every 10, landscape) and pick your paper size.</li>
<li><strong>Draw the furniture to the same scale:</strong> a 90 × 200 cm bed is 9 × 20 squares. Cut the pieces out of a second sheet and move them around before you move anything heavy.</li></ol>
<p>Working in feet? Choose the 1/4 in grid and let one square stand for 6 in: a 14 × 12 ft room then needs 28 × 24 squares, which fits on a Letter page in either orientation.</p>

<h2>Quick recommendations</h2>
<p>Each link opens the generator with that setting already chosen; your paper size stays as you last used it.</p>
<ul><li><strong>Lecture notes:</strong> <a href="/lined-paper.html?ruling=college">college-ruled lines</a>, or a <a href="/dot-grid.html?gap=5&amp;size=m">5 mm dot grid</a> if you draw diagrams.</li>
<li><strong>Math homework:</strong> <a href="/graph-paper.html?grid=5&amp;major=5">5 mm</a> or <a href="/graph-paper.html?grid=6.35&amp;major=4">1/4 in graph paper</a>.</li>
<li><strong>Handwriting practice for children:</strong> <a href="/lined-paper.html?ruling=wide">wide ruling</a> or a <a href="/graph-paper.html?grid=10&amp;major=0">1 cm grid</a>.</li>
<li><strong>Journaling and planning:</strong> <a href="/dot-grid.html?gap=5&amp;size=m">5 mm dot grid, medium dots</a>.</li>
<li><strong>Product and room sketches:</strong> <a href="/isometric-paper.html?gap=7&amp;style=lines">isometric paper with 7 mm triangles</a>.</li>
<li><strong>Not sure the grid will print at its real size?</strong> Print the <a href="/print-test-page.html">test page</a> first.</li></ul>

<h2>FAQ</h2>
<h3>Is college ruled the same as 7 mm?</h3>
<p>Nearly: 9/32 in is 7.14 mm. Over a whole page the difference adds up to only a few millimeters.</p>
<h3>Why is 65 lb cover heavier than 80 lb text paper?</h3>
<p>Because the pound figure is the weight of 500 sheets in each grade's own basis size, and those sizes differ: cover is weighed at 20 × 26 in, text at 25 × 38 in and bond at 17 × 22 in. The text sheet is much larger, so the same pounds are spread over more paper. Converted to grams per square meter, 65 lb cover is about 176 g/m², while 80 lb text is only about 118 g/m². When you compare papers of different grades, always look at the gsm value.</p>
<h3>Which paper stops markers bleeding through?</h3>
<p>No plain office paper fully stops alcohol-based markers. Heavier paper (105–120 g/m²) reduces show-through for fineliners and water-based markers; for alcohol markers, print on one side only.</p>

<h2>Sources and standards</h2>
<ul><li><strong>ISO 216</strong> – A-series paper sizes (A4, A5) and the 1 : √2 aspect ratio.</li>
<li><strong>ISO 536</strong> – determination of grammage (g/m²) for paper and board.</li>
<li><strong>ANSI/ASME Y14.1</strong> – US sheet sizes (size A = 8.5 × 11 in).</li>
<li>Pound-to-gsm conversions are calculated from the basis sizes named above and the definition 1 lb = 453.59 g; manufacturers may round differently.</li></ul>
""",
},
{
"slug": "printable-calendar-2027",
"published": "2026-11-03", "modified": "2026-11-18",
"title": "Printable calendar 2027: week numbers, holidays and layout choices",
"teaser": "What is special about 2027, how ISO week numbers work, US federal holidays and which layout to print.",
"description": "Everything you need for a printed 2027 calendar: ISO 8601 week numbers (week 1 starts January 4), US federal holidays and observed dates, Monday vs Sunday start, and which layout and paper size to choose.",
"body": """
<p>A calendar looks like the simplest printable there is – until you notice that January 1 is in “week 53”, that a holiday moved to a Friday, or that May needs six rows instead of five. This guide collects the facts about 2027 that matter when you print a calendar, and explains the layout choices in our calendar templates so you can pick the right one in a minute.</p>

<h2>2027 at a glance</h2>
<p>2027 is a common year with 365 days. It begins on a Friday and ends on a Friday. The next leap year is 2028, when February has 29 days again. A few consequences for printed calendars:</p>
<ul><li><strong>Week numbers:</strong> under ISO 8601, 2027 has 52 weeks. Week 1 starts on Monday, January 4. Friday, January 1 to Sunday, January 3 still belong to week 53 of 2026.</li>
<li><strong>Six-row months:</strong> with a Monday start, May and August need six rows. With a Sunday start, January, May and October do. Six-row months have shorter day boxes, so they are worth checking before you print.</li>
<li><strong>End of the year:</strong> week 52 of 2027 runs from Monday, December 27, 2027 to Sunday, January 2, 2028. Week 1 of 2028 begins on January 3, 2028.</li></ul>

<h2>How ISO week numbers work</h2>
<p>ISO 8601 is the international standard for writing dates and times. Its week rules are short: weeks start on Monday, and week 1 is the week that contains the first Thursday of the year. An equivalent rule is “the week that contains January 4”. A year therefore has 52 or 53 weeks. It has 53 when it starts on a Thursday, or when it is a leap year that starts on a Wednesday – 2026 is such a year, and the next one after that is 2032.</p>
<p>Week numbers are used in many workplaces, schools and supply chains, especially in Europe, because “delivery in week 14” is shorter than a date range. In the US they are less common, but they are useful for anything planned in weeks: training plans, school terms, sprints or the number of weeks until a due date.</p>
<p>In our <a href="/monthly-calendar.html">monthly calendar</a>, the small gray number at the left of each row is the ISO week. If you start the week on Sunday, each row runs Sunday to Saturday, while ISO weeks run Monday to Sunday; the number shown is the ISO week of the Monday in that row, which covers six of its seven days.</p>

<h2>US federal holidays in 2027</h2>
<p>Our calendars leave holidays blank, because they differ between countries, states and employers. If you are in the US, these are the federal holidays for 2027 to write in. When a holiday falls on a Saturday, federal employees normally observe it on the Friday before; when it falls on a Sunday, on the Monday after. Private employers and schools may handle this differently.</p>
<div class="table-wrap"><table>
<thead><tr><th>Holiday</th><th>Date in 2027</th><th>Observed (federal)</th></tr></thead>
<tbody>
<tr><td>New Year's Day</td><td>Friday, January 1</td><td>January 1</td></tr>
<tr><td>Birthday of Martin Luther King, Jr.</td><td>Monday, January 18</td><td>January 18</td></tr>
<tr><td>Washington's Birthday</td><td>Monday, February 15</td><td>February 15</td></tr>
<tr><td>Memorial Day</td><td>Monday, May 31</td><td>May 31</td></tr>
<tr><td>Juneteenth National Independence Day</td><td>Saturday, June 19</td><td>Friday, June 18</td></tr>
<tr><td>Independence Day</td><td>Sunday, July 4</td><td>Monday, July 5</td></tr>
<tr><td>Labor Day</td><td>Monday, September 6</td><td>September 6</td></tr>
<tr><td>Columbus Day</td><td>Monday, October 11</td><td>October 11</td></tr>
<tr><td>Veterans Day</td><td>Thursday, November 11</td><td>November 11</td></tr>
<tr><td>Thanksgiving Day</td><td>Thursday, November 25</td><td>November 25</td></tr>
<tr><td>Christmas Day</td><td>Saturday, December 25</td><td>Friday, December 24</td></tr>
</tbody></table></div>
<p>One more date belongs on a 2027 calendar: New Year's Day 2028 falls on a Saturday, so its federal observance moves to Friday, December 31, 2027. Other dates people often add are Easter Sunday (March 28, 2027 in Western churches), Mother's Day (May 9) and Father's Day (June 20); these are not federal holidays. Outside the US, use your government's official list of public holidays.</p>

<h2>Which layout should you print?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Layout</th><th>Pages for 2027</th><th>Best for</th><th>Day box size (A4 / Letter)</th></tr></thead>
<tbody>
<tr><td><a href="/yearly-calendar.html">Yearly calendar</a></td><td>1</td><td>Vacations, deadlines, counting weeks</td><td>Numbers only, no writing space</td></tr>
<tr><td><a href="/monthly-calendar.html">Monthly calendar</a>, landscape</td><td>12</td><td>Wall, desk, family appointments</td><td>about 30 × 26 mm / 27 × 27 mm (six-row month)</td></tr>
<tr><td>Monthly calendar, portrait</td><td>12</td><td>Ring binders, clipboards</td><td>about 26 × 35 mm / 26 × 32 mm (six-row month)</td></tr>
<tr><td><a href="/weekly-planner.html">Weekly planner</a></td><td>52–53</td><td>Detailed planning with to-dos</td><td>about 49 × 80 mm (A4 landscape)</td></tr>
</tbody></table></div>
<p>A common combination is one yearly page at the front of a binder, twelve monthly pages behind it, and weekly pages printed only for the current week.</p>

<h2>Monday or Sunday?</h2>
<p>In the US, Canada and Japan, wall calendars traditionally start on Sunday; ISO 8601 and most European calendars start on Monday. Neither is more correct. A practical test: if your weekend plans usually span Saturday and Sunday, a Monday start keeps them together at the end of the row. If your week “begins” at church, with family on Sunday or with Sunday meal prep, a Sunday start may match your routine better. All our calendars offer both.</p>

<h2>Worked example: a 2027 wall calendar in ten minutes</h2>
<ol><li>Open the <a href="/monthly-calendar.html?year=2027&amp;month=all&amp;orient=landscape&amp;weeks=1&amp;notes=1">monthly calendar with these settings</a>: year 2027, <em>All 12 months</em>, landscape, week numbers and the notes column switched on.</li>
<li>Choose the paper size that is in your printer.</li>
<li>Pick Sunday or Monday as the first day, and an accent color you like.</li>
<li>Download the 12-page PDF and print it at 100% (see <a href="/print-at-actual-size.html">printing at actual size</a>).</li>
<li>Go through the holiday table above and write each observed date into its box, plus birthdays, school breaks and paydays.</li>
<li>Print the <a href="/yearly-calendar.html?year=2027">yearly calendar for 2027</a> in the same accent color and use it as the cover page.</li></ol>
<p>The same twelve pages can be made with month and weekday names in ten languages, for example <a href="/monthly-calendar.html?year=2027&amp;month=all&amp;lang=es&amp;ws=mon">Spanish with a Monday start</a> or <a href="/monthly-calendar.html?year=2027&amp;month=all&amp;lang=de&amp;ws=mon">German</a>. The holiday table above covers the United States only.</p>
<p>Punch the sheets for a binder or clip them to a board; with two-sided printing, each month's back stays free for notes.</p>

<h2>FAQ</h2>
<h3>Why does my phone show a different week number?</h3>
<p>Some apps use the US convention, in which week 1 is the week containing January 1 and weeks start on Sunday. ISO weeks start on Monday and week 1 contains January 4, so the two systems can differ by one.</p>
<h3>Does 2027 have a week 53?</h3>
<p>No. 2027 has 52 ISO weeks. The days January 1–3, 2027 belong to week 53 of 2026.</p>
<h3>Can I print a calendar that starts in a month other than January?</h3>
<p>Yes. Print single months one at a time – for example September 2027 to August 2028 for a school year.</p>
<h3>Are holidays printed automatically?</h3>
<p>No, the boxes stay blank so the calendar works in any country. Use the table above or your official national list.</p>

<h2>Sources and standards</h2>
<ul><li><strong>ISO 8601</strong> – date and time representation, including the week-numbering rules (Monday start, week 1 contains January 4).</li>
<li><strong>5 U.S.C. § 6103</strong> – the US federal holidays, and the federal rule for observing holidays that fall on a Saturday or Sunday.</li>
<li><strong>Gregorian calendar</strong> leap-year rule (divisible by 4, except century years not divisible by 400). Easter is calculated with the Gregorian computus used by Western churches.</li>
<li>Dates and week numbers in this guide were calculated with the same date code that draws our calendars.</li></ul>
""",
},
{
"slug": "plan-a-week-on-paper",
"published": "2026-11-03", "modified": "2026-11-18",
"title": "How to plan a week on paper (with the weekly planner)",
"teaser": "A 25-minute weekly review, a capacity check in hours, and a filled example page.",
"description": "A step-by-step routine for planning a week on a printed page: review, fixed appointments, three priorities, a simple hours-based capacity check and a filled example of the weekly planner.",
"body": """
<p>A weekly plan is the sweet spot of paper planning. A day is too short to see trade-offs, a month too long to decide what happens next. On one sheet you can see all seven days, the tasks that need to happen and the space that is actually left. This guide describes a routine that takes about 25 minutes, a simple way to check whether your plan fits, and a filled example of our <a href="/weekly-planner.html">weekly planner</a>.</p>

<h2>Set up the page</h2>
<p>Open the weekly planner and decide three things before you print.</p>
<ul><li><strong>Dated or undated.</strong> Enter the first day of the week and every box gets its weekday and date. The planner starts on whatever day you enter: enter a Monday for a Monday-to-Sunday week, or a Sunday if your week starts on Sunday. Leave the field empty to print undated pages that run Monday to Sunday.</li>
<li><strong>Landscape or portrait.</strong> Landscape gives eight tall boxes in two rows of four and a 60 mm to-do column on the right; on A4 each day box is about 49 × 80 mm with ten writing lines. Portrait arranges the boxes in four rows of two and puts a 42 mm high to-do strip at the bottom, which suits ring binders.</li>
<li><strong>Writing lines.</strong> The lines in the day boxes are 6.5 mm apart. Turn them off if you prefer to draw time blocks or small sketches.</li></ul>
<p>The eighth box is labeled Notes. It is the place for things that belong to the week but not to a day: a phone number, a shopping item, an idea you do not want to lose.</p>

<h2>The 25-minute weekly review</h2>
<p>Do this at the same time every week, for example on Sunday afternoon or Friday after work. The times are guidelines; what matters is the order.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Minutes</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>1. Look back</td><td>5</td><td>Read last week's page. Tick what is done, circle what moves forward, cross out what no longer matters.</td></tr>
<tr><td>2. Fixed appointments</td><td>5</td><td>Copy meetings, classes, school pick-ups and deadlines from your digital calendar or monthly page into the day boxes.</td></tr>
<tr><td>3. Collect tasks</td><td>5</td><td>Write every open task you know of into the to-do column. Do not sort yet.</td></tr>
<tr><td>4. Choose three priorities</td><td>5</td><td>Mark the three tasks that would make the week a success and give each one a day.</td></tr>
<tr><td>5. Capacity check</td><td>5</td><td>Estimate hours and compare with the free time you really have (see below). Move or drop tasks until it fits.</td></tr>
</tbody></table></div>
<p>The look-back step is the one most people skip, and it is the one that keeps the system honest: a task that has moved forward three weeks in a row needs a decision, not another arrow.</p>

<h2>The capacity check in hours</h2>
<p>Paper planners fail quietly when a week holds twice as much as fits. A rough calculation prevents that:</p>
<ol><li>Write down your available working hours for the week, for example 40.</li>
<li>Subtract the hours already taken by fixed appointments.</li>
<li>Subtract a buffer for interruptions, email and small requests. A buffer of 20–30% of the remaining time is a sensible starting point; adjust it after a few weeks based on what really happened.</li>
<li>Add up the estimated hours of your priorities and other planned tasks.</li></ol>
<p>If the tasks need more time than is left, the plan does not fit. Decide now what moves to next week instead of finding out on Thursday evening. The same calculation works for a household week with “free evening hours” instead of working hours.</p>

<h2>Worked example: one filled page</h2>
<p>Here is how a page for the week of Monday, March 15, 2027 (ISO week 11) could look for someone working full-time with two evening commitments. The example is made up to illustrate the method.</p>
<ul><li><strong>Header:</strong> title “Weekly plan”, date range Mar 15 – Mar 21, 2027 printed automatically. <a href="/weekly-planner.html?start=2027-03-15&amp;orient=landscape&amp;todo=1&amp;lines=1&amp;lang=en">Open this exact page</a> and change the date to your own week.</li>
<li><strong>Monday:</strong> 9:00 team meeting (1 h), 14:00 dentist. Priority 1: draft the project report – block 10:30–12:30.</li>
<li><strong>Tuesday:</strong> report, second block 9:00–11:00; 18:30 choir.</li>
<li><strong>Wednesday:</strong> 13:00–15:00 client workshop. Priority 2: prepare workshop slides on Tuesday afternoon (written there as well).</li>
<li><strong>Thursday:</strong> buffer morning, no new tasks. 19:00 parents' evening.</li>
<li><strong>Friday:</strong> Priority 3: send the report; 30 minutes to plan next week.</li>
<li><strong>Saturday and Sunday:</strong> shopping, a bike ride, nothing work-related.</li>
<li><strong>To-do column:</strong> eleven smaller tasks such as “renew library card” or “reply to Sam about dates”, each with a check box.</li>
<li><strong>Capacity check in the Notes box:</strong> 40 h available − 9 h of meetings = 31 h; minus a 25% buffer ≈ 23 h; priorities estimated at 12 h, smaller tasks at 8 h – total 20 h, so the plan fits.</li></ul>

<h2>Keeping the page alive during the week</h2>
<ul><li><strong>Morning, two minutes:</strong> read today's box and the to-do column. Choose what happens next.</li>
<li><strong>When something new comes in:</strong> write it in the to-do column, not straight into a day. It gets a day at the next review unless it is urgent.</li>
<li><strong>When a task moves:</strong> draw an arrow and write it into the new day. Moving is fine; moving without deciding is the problem.</li>
<li><strong>Busy days:</strong> add a <a href="/daily-planner.html">daily planner</a> page with an hourly schedule for the days that are fully booked.</li></ul>
<p>If you track routines such as exercise or reading, a monthly <a href="/habit-tracker.html">habit tracker</a> next to the weekly page works better than squeezing them into the day boxes. For the bigger picture, keep a <a href="/monthly-calendar.html">monthly calendar</a> in front of the weekly pages.</p>

<h2>FAQ</h2>
<h3>Should I plan on Sunday or Friday?</h3>
<p>Either works. Friday planning uses the knowledge you have at the end of the work week; Sunday planning feels fresher. Pick one and keep it fixed for a month before you judge.</p>
<h3>What if my week starts on Sunday?</h3>
<p>Enter a Sunday as the start date. The boxes then run Sunday to Saturday with the correct dates.</p>
<h3>How many tasks should go on the to-do list?</h3>
<p>As many as you know of, but only three are priorities. In landscape on A4 the column holds 22 lines, which is a useful natural limit.</p>
<h3>Do I still need a digital calendar?</h3>
<p>For reminders and shared appointments, usually yes: a printed page cannot ring and cannot be shared. A simple split is to keep everything that has a time in the digital calendar and to copy the week's appointments onto the page during the weekly review.</p>

<h2>Sources and standards</h2>
<ul><li><strong>ISO 8601</strong> – week numbering (weeks start on Monday; week 11 of 2027 runs from March 15 to March 21).</li>
<li>Box sizes and line counts are measured from the weekly planner template itself (A4, default settings). The buffer percentage is a planning suggestion, not a research figure.</li></ul>
""",
},
{
"slug": "meal-planning-one-page",
"published": "2026-11-03", "modified": "2026-11-18",
"title": "Meal planning on one page: a 20-minute weekly routine",
"teaser": "Plan seven days of meals and a sorted grocery list on one sheet – with leftover timing that stays food-safe.",
"description": "A practical 20-minute routine for planning a week of meals on one printed page: checking the calendar and fridge, themes, cook once eat twice, a grocery list by category and food-safe leftover timing.",
"body": """
<p>Most meal plans fail for one of two reasons: they are too ambitious, or they live somewhere nobody looks. A single printed page on the fridge solves the second problem. A fixed routine of about twenty minutes solves the first, because it forces you to plan around the week you will really have, not an ideal one. This guide walks through that routine with our <a href="/meal-planner.html">meal planner</a>, shows a filled example and adds the food-safety numbers that matter for leftovers.</p>

<h2>What goes on the page</h2>
<p>The meal planner prints a grid with seven day columns and one row per meal, plus a grocery list. You choose the rows: breakfast, lunch and dinner; all three plus snacks; lunch and dinner; or dinner only. Fewer rows mean taller cells. On A4 landscape with three meals, each cell is about 27 × 52 mm; with dinner only, a cell is the full height of the grid. The grocery list is split into five groups – produce, protein, dairy, pantry and other – and sits in a column on the right in landscape or as a strip along the bottom in portrait.</p>
<p>If you enter a start date, the day headings show the dates. Enter a date that falls on the first day of your week (a Monday if the week starts on Monday, a Sunday if it starts on Sunday), so the weekday names and dates line up.</p>

<h2>The 20-minute routine</h2>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Minutes</th><th>Result on the page</th></tr></thead>
<tbody>
<tr><td>1. Check the calendar</td><td>3</td><td>Busy evenings marked “quick” or “leftovers”</td></tr>
<tr><td>2. Check fridge, freezer and pantry</td><td>4</td><td>Ingredients that need using up placed in the first two days</td></tr>
<tr><td>3. Fill the dinner row</td><td>5</td><td>Seven dinners, including one or two planned leftovers</td></tr>
<tr><td>4. Fill breakfasts and lunches</td><td>3</td><td>Repeating simple options; lunches from dinner leftovers</td></tr>
<tr><td>5. Write the grocery list</td><td>5</td><td>Everything missing, written straight into the five groups</td></tr>
</tbody></table></div>
<p>Do the routine at the same time each week, ideally the day before your main shopping trip, so the list goes straight into your bag. Start with dinners because they need the most cooking and drive most of the shopping. Breakfasts and lunches are often the same few options on repeat, and that is fine – variety is not the goal of the plan, fewer decisions are.</p>

<h2>Three techniques that make the plan realistic</h2>
<ul><li><strong>Theme nights:</strong> give some days a fixed theme such as pasta, soup, a vegetarian dish or “clean out the fridge”. Choosing a recipe inside a theme takes seconds.</li>
<li><strong>Cook once, eat twice:</strong> double one or two dinners and write the second portion into a later lunch or dinner cell. Mark it with an arrow so everyone knows it is already covered.</li>
<li><strong>A quick meal for the hardest day:</strong> one evening in most weeks is crowded by sports, overtime or appointments. Plan something that takes under 15 minutes or comes from the freezer, instead of pretending you will cook from scratch.</li></ul>

<h2>Leftovers: the food-safety numbers</h2>
<p>Planned leftovers only help if they are eaten in time. The US Department of Agriculture's Food Safety and Inspection Service advises keeping the refrigerator at 40 °F (4 °C) or below, getting cooked food into the fridge within two hours, and eating refrigerated leftovers within three to four days – or freezing them. For the plan this means:</p>
<ul><li>A dinner cooked on Sunday can be planned for Monday, Tuesday or Wednesday – not for Friday.</li>
<li>If a second portion would land later than that, write “freeze” next to it and move it to next week's plan.</li>
<li>Label containers with the cooking date; the planner's date headings make it easy to copy.</li></ul>

<h2>Worked example: a week for a household of three</h2>
<p>This is an illustrative plan for two adults and a child, week starting Monday, with football practice on Tuesday and Thursday evenings. It uses the “breakfast, lunch, dinner” rows. <a href="/meal-planner.html?meals=bld&amp;ws=mon&amp;grocery=1&amp;orient=landscape">Open the empty page for this plan</a> (three meal rows, Monday start, grocery list, landscape).</p>
<ul><li><strong>Monday:</strong> dinner – vegetable lasagna, double batch. The spinach and zucchini from last week are used up here.</li>
<li><strong>Tuesday (practice):</strong> dinner – lasagna leftovers, 10 minutes to reheat. Lunch – bean salad.</li>
<li><strong>Wednesday:</strong> soup night – lentil soup with bread; extra portion written into Thursday's lunch cell.</li>
<li><strong>Thursday (practice):</strong> dinner – quesadillas, 15 minutes.</li>
<li><strong>Friday:</strong> pasta night with tomato sauce; the remaining sauce is frozen.</li>
<li><strong>Saturday:</strong> “clean out the fridge” – omelets with whatever vegetables are left.</li>
<li><strong>Sunday:</strong> roast chicken with potatoes; the leftover chicken goes into Monday's lunch wraps.</li>
<li><strong>Breakfasts:</strong> oatmeal on weekdays, pancakes on Saturday.</li></ul>
<p>The grocery list for this plan, sorted into the printed groups, might read: <em>Produce</em> – onions, carrots, tomatoes, lettuce, potatoes, apples; <em>Protein</em> – whole chicken, eggs, lentils, canned beans; <em>Dairy</em> – mozzarella, milk, yogurt, cheddar; <em>Pantry</em> – lasagna sheets, pasta, oats, tortillas, flour; <em>Other</em> – foil, dish soap. Writing the list by group means one walk through the store instead of three.</p>

<h2>Keeping it going</h2>
<ul><li>Keep old plans in a folder. After a month you have a personal list of meals that worked, and planning gets faster every week.</li>
<li>If you also track spending, the grocery total fits the groceries line in the <a href="/budget-planner.html">budget planner</a>.</li>
<li>For a fixed weekly shopping list that rarely changes, the <a href="/checklist.html">checklist maker</a> can print it pre-filled.</li>
<li>Plan meals as part of your <a href="/plan-a-week-on-paper.html">weekly review</a>, so busy days are visible when you choose the quick meals.</li></ul>

<h2>FAQ</h2>
<h3>Should I plan all three meals?</h3>
<p>Only if you need to. Many households plan dinners only and keep breakfast and lunch on a short rotation; the “dinner only” option gives you large cells for recipe notes.</p>
<h3>What if plans change mid-week?</h3>
<p>Swap two days with an arrow. The groceries are already in the house, so the order matters less than the list.</p>
<h3>How long can I keep cooked food in the fridge?</h3>
<p>The USDA guidance is three to four days at 40 °F (4 °C) or below. Freeze anything you will not eat in that window.</p>

<h2>Sources and standards</h2>
<ul><li><strong>USDA Food Safety and Inspection Service</strong> – consumer guidance on leftovers and refrigerator temperatures (40 °F / 4 °C, two-hour rule, three to four days).</li>
<li><strong>ISO 8601</strong> – the date format YYYY-MM-DD, handy for labeling containers without US/European ambiguity.</li>
<li>Cell sizes are measured from the meal planner template (A4 landscape). Meals in the example are illustrations, not nutrition advice.</li></ul>
""",
},
{
"slug": "bullet-journal-starter",
"published": "2026-10-29", "modified": "2026-11-18",
"title": "Bullet journal for beginners: a starter kit you can print",
"teaser": "Rapid logging, the core collections and a first month set up step by step.",
"description": "A beginner-friendly introduction to bullet journaling: rapid logging symbols, index, future log, monthly and daily log, migration, a first month set up page by page, and printed pages vs a notebook.",
"body": """
<p>Bullet journaling is a paper planning method developed by designer Ryder Carroll and described in his book <em>The Bullet Journal Method</em> (2018). It needs no artistic skill and no special notebook: short notes, a handful of symbols and a few pages that you set up yourself. This guide explains the core ideas, sets up a first month page by page, and shows where printed pages are a good alternative to a bound notebook.</p>

<h2>Rapid logging: short entries with symbols</h2>
<p>Instead of full sentences you write short entries, each starting with a symbol that says what kind of entry it is. The symbol changes as the entry's status changes, so a glance at the page shows what is still open.</p>
<div class="table-wrap"><table>
<thead><tr><th>Symbol</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>•</td><td>Task, still open</td><td>• Book car service</td></tr>
<tr><td>×</td><td>Task done</td><td>× Pay electricity bill</td></tr>
<tr><td>&gt;</td><td>Task migrated (moved to a later page)</td><td>&gt; Sort tax papers</td></tr>
<tr><td>&lt;</td><td>Task scheduled into the future log</td><td>&lt; Renew passport (June)</td></tr>
<tr><td>○</td><td>Event</td><td>○ Anna's birthday</td></tr>
<tr><td>–</td><td>Note</td><td>– Plumber recommends new valve</td></tr>
</tbody></table></div>
<p>Many people add a few signifiers in front of the symbol, such as an asterisk for priority. Start with the six symbols above and add your own only when you miss something.</p>

<h2>The core collections</h2>
<p>A “collection” is any page or group of pages with one topic. The method starts with four of them:</p>
<ol><li><strong>Index</strong> – the first two pages. Number every page as you go and note topics with page numbers, for example “March 2027: 9–12”.</li>
<li><strong>Future log</strong> – events and tasks for the coming months. A printed <a href="/yearly-calendar.html">yearly calendar</a> makes a quick overview page next to it.</li>
<li><strong>Monthly log</strong> – a list of the month's dates on the left page, tasks for the month on the right. A printed <a href="/monthly-calendar.html">monthly calendar</a> is a handy alternative if you prefer a grid.</li>
<li><strong>Daily log</strong> – rapid logging, day by day, written as the day happens.</li></ol>
<p>Many users add a weekly log between monthly and daily pages. It is not part of the original core, but it is one of the most popular additions; our <a href="/weekly-planner.html">weekly planner</a> prints one ready-made.</p>

<h2>Migration: the monthly clean-up</h2>
<p>At the end of each month – and, if you like, at the end of each week – you look through open tasks. Each one gets one of three decisions: do it now, move it to the new monthly log (mark it with &gt;) or schedule it into the future log (mark it with &lt;). If a task is not worth rewriting, cross it out – it probably was not worth doing. This deliberate rewriting is what keeps the journal from turning into an endless list. Plan about 15 minutes for it; with 20 or more open tasks it is a sign that the monthly list was too ambitious, and the next one should be shorter.</p>

<h2>Worked example: setting up January 2027</h2>
<p>Here is a complete setup for a new journal on 5 mm dot grid, page by page. It takes about 30 minutes. For loose pages, <a href="/dot-grid.html?paper=a5&amp;gap=5&amp;size=m">open the A5 dot grid used in this example</a> (5 mm, medium dots).</p>
<ul><li><strong>Pages 1–2: Index.</strong> Write “Index” at the top of both pages and leave them empty for now.</li>
<li><strong>Pages 3–4: Future log.</strong> Divide each page into three boxes – six months across two pages. On an A5 dot grid page (27 × 38 dots in our generator) each box is about 12 dots high. Enter known dates such as birthdays and trips.</li>
<li><strong>Page 5: Monthly log, calendar side.</strong> Write the numbers 1–31 down the left edge, one per row of dots, with the weekday initial next to each. January 1, 2027 is a Friday.</li>
<li><strong>Page 6: Monthly log, task side.</strong> List what should happen in January: “• Book dentist”, “• Plan spring trip”.</li>
<li><strong>Page 7: Habit collection.</strong> A small grid with 31 columns and three or four rows, or a printed <a href="/habit-tracker.html?year=2027&amp;month=0">habit tracker for January 2027</a> glued or clipped in.</li>
<li><strong>Page 8 onward: Daily log.</strong> Write today's date as a heading and start logging.</li>
<li><strong>Back to the index:</strong> add “Future log 3–4”, “January 2027 5–8”.</li></ul>
<p>On January 31, migrate open tasks to a new February monthly log and add “February 2027” to the index.</p>

<h2>Printed pages or a bound notebook?</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Bound dotted notebook</th><th>Printed pages in a ring binder</th></tr></thead>
<tbody>
<tr><td>Rearranging pages</td><td>Not possible</td><td>Any time</td></tr>
<tr><td>Fixing a spread you dislike</td><td>Cover it or live with it</td><td>Print the page again</td></tr>
<tr><td>Ready-made layouts</td><td>Drawn by hand</td><td>Calendars, trackers and lists printed in seconds</td></tr>
<tr><td>Portability</td><td>Slim and robust</td><td>Bulkier, rings can catch</td></tr>
<tr><td>Paper quality</td><td>Often 80–120 g/m², varies by brand</td><td>Whatever you load; 90–120 g/m² works well</td></tr>
</tbody></table></div>
<p>A good middle path: print <a href="/dot-grid.html">5 mm dot grid</a> for the pages you design yourself and the ready-made templates for calendars and trackers, then keep them together in an A5 binder. A5 is exactly half of A4, so you can also fold A4 sheets.</p>

<h2>Keep it simple</h2>
<p>Social media shows elaborate spreads with lettering and illustrations. They are a hobby of their own, not a requirement. The method works with plain handwriting, a ruler and a pen that does not bleed through. Spend the time on planning unless decorating is what you enjoy.</p>

<h2>FAQ</h2>
<h3>Do I need dot grid paper?</h3>
<p>No, any paper works. Dot grid is popular because the dots help with boxes and columns without getting in the way of handwriting.</p>
<h3>What if I miss a few days?</h3>
<p>Nothing breaks. Write today's date and continue; the index and monthly log keep everything findable.</p>
<h3>How is a bullet journal different from a planner?</h3>
<p>A planner comes with fixed pages for every day and week, whether you need them or not. A bullet journal grows page by page: a busy day can take two pages, a quiet week a few lines, and new collections appear only when you need them.</p>
<h3>Which pen should I use?</h3>
<p>Any pen that does not bleed through your paper. Test it on the back page first; gel pens and fineliners usually work on 90 g/m² and heavier, while alcohol markers bleed through almost any office paper.</p>
<h3>Should every month look the same?</h3>
<p>Ideally yes for the first few months. Repeating a simple setup makes it fast, and you will learn which parts you actually use.</p>

<h2>Sources and standards</h2>
<ul><li>Ryder Carroll, <em>The Bullet Journal Method</em> (2018) – origin of rapid logging, the core collections and migration.</li>
<li><strong>ISO 216</strong> – A5 (148 × 210 mm) is half of A4.</li>
<li>Dot counts are measured from our dot grid template with default margins.</li></ul>
<p class="small muted">Bullet Journal® is a registered trademark of Ryder Carroll. Printable Joy Lab is not affiliated with the official Bullet Journal method.</p>
""",
},
]
