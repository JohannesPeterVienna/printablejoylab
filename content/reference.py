"""Paper size reference page and the two interactive checks (print scale calculator, ruler check).

The forms are plain HTML; assets/sizes.js fills in the results. All figures quoted in the text come from
content/sizes.py (checked at build time), never typed by hand.
"""
from html import escape
from content.sizes import GROUPS, rows, check

ACCESSED = "18 November 2026"
A4, LETTER, A5 = "iso_a4_210x297mm", "na_letter_8.5x11in", "iso_a5_148x210mm"

MEASURE = """<div class="calc" data-measure>
<form onsubmit="return false" aria-label="Ruler check">
<label class="f" for="m-across"><span>Square measured across (mm)</span><input id="m-across" name="across" type="text" inputmode="decimal" autocomplete="off" maxlength="8" placeholder="100"></label>
<label class="f" for="m-down"><span>Square measured down (mm)</span><input id="m-down" name="down" type="text" inputmode="decimal" autocomplete="off" maxlength="8" placeholder="100"></label>
</form>
<p class="chips"><span>Examples:</span> <button type="button" data-example="100,100">100 × 100</button> <button type="button" data-example="94,94">94 × 94</button> <button type="button" data-example="97.3,97.3">97.3 × 97.3</button> <button type="button" data-example="96,96">96 × 96</button></p>
<div class="calc-out" data-out aria-live="polite"><p class="muted">Enter both measurements in millimeters. The result is calculated in your browser.</p></div>
<p class="calc-actions"><button class="linkbtn" type="button" data-copy>Copy result</button> <button class="linkbtn" type="button" data-share>Copy link to this result</button></p>
</div>"""

CALC = f"""<div class="calc" data-scalecalc>
<form onsubmit="return false" aria-label="Print scale calculator">
<label class="f" for="c-doc"><span>Page size of the PDF</span><select id="c-doc" name="doc" data-def="{A4}"></select></label>
<label class="f" for="c-sheet"><span>Paper in the printer</span><select id="c-sheet" name="sheet" data-def="{LETTER}"></select></label>
<label class="f" for="c-mode"><span>Print setting</span><select id="c-mode" name="mode"><option value="fit">Fit / Fit to page / Fit to printable area</option><option value="shrink">Shrink oversized pages only</option><option value="actual">100% / Actual size</option><option value="custom">Custom percentage</option></select></label>
<label class="f" for="c-percent" data-percent hidden><span>Custom scale (%)</span><input id="c-percent" name="percent" type="number" inputmode="decimal" min="10" max="400" step="1" value="100"></label>
<label class="f" for="c-border"><span>Printer's blank border on each side (mm)</span><input id="c-border" name="border" type="number" inputmode="decimal" min="0" max="30" step="0.5" value="0"></label>
<label class="f" for="c-feature"><span>A spacing in your PDF to follow (mm)</span><input id="c-feature" name="feature" type="number" inputmode="decimal" min="0.1" max="500" step="0.05" value="5"></label>
</form>
<p class="chips"><span>Examples:</span>
<button type="button" data-example="doc={A4}&amp;sheet={LETTER}&amp;mode=fit&amp;border=0">A4 page on US Letter, Fit</button>
<button type="button" data-example="doc={LETTER}&amp;sheet={A4}&amp;mode=fit&amp;border=0">US Letter page on A4, Fit</button>
<button type="button" data-example="doc={A4}&amp;sheet={A4}&amp;mode=fit&amp;border=4">A4 on A4, fitted inside a 4 mm border</button>
<button type="button" data-example="doc={A4}&amp;sheet={LETTER}&amp;mode=actual&amp;border=0">A4 page on US Letter at 100%</button>
<button type="button" data-example="doc={A5}&amp;sheet={A4}&amp;mode=fit&amp;border=0">A5 page on A4, Fit</button></p>
<div class="calc-result"><div class="calc-out" data-out aria-live="polite"><p class="muted">The calculator needs JavaScript. The table below works without it.</p></div><div class="calc-fig" data-fig aria-hidden="true"></div></div>
<p class="small muted">Drawing: gray = sheet, dashed = area the printer can reach, red = the printed page, all to one scale.</p>
<p class="calc-actions"><button class="linkbtn" type="button" data-copy>Copy result</button> <button class="linkbtn" type="button" data-share>Copy link to this calculation</button></p>
</div>"""


def _table():
    labels = dict(GROUPS)
    trs = []
    for r in rows():
        hay = " ".join([r["label"], labels[r["group"]], r["pwg"], r["mm"], r["inch"], r["pt"], r["css"]]).lower().replace("×", "x")
        make = f'<a href="/graph-paper.html?paper={r["ours"]}">make a page</a>' if r["ours"] else ""
        trs.append(f'<tr data-size="{r["pwg"]}" data-name="{escape(r["label"])}" data-w="{r["wmm"]}" data-h="{r["hmm"]}" data-g="{r["group"]}" data-ours="{r["ours"]}" data-hay="{escape(hay)}">'
                   f'<th scope="row">{escape(r["label"])}</th><td>{r["mm"]}</td><td>{r["inch"]}</td><td>{r["pt"]}</td><td>{r["ratio"]}</td><td>{labels[r["group"]]}</td>'
                   f'<td><code>{r["pwg"]}</code></td><td>{("<code>" + r["css"] + "</code>") if r["css"] else ""}</td><td>{make}</td></tr>')
    opts = "".join(f'<option value="{g}">{escape(l)}</option>' for g, l in GROUPS)
    return f"""<div data-sizetable>
<div class="filter"><label class="f" for="t-search"><span>Search name or number</span><input id="t-search" type="text" data-search maxlength="40" placeholder="e.g. legal, 210, b5" autocomplete="off"></label>
<label class="f" for="t-group"><span>Group</span><select id="t-group" data-group><option value="">All groups</option>{opts}</select></label>
<p class="filter-actions"><button class="linkbtn" type="button" data-clear>Clear filter</button> <button class="linkbtn" type="button" data-csv>Download the rows shown as CSV</button></p></div>
<p class="small muted" data-count aria-live="polite">{len(trs)} sizes</p>
<div class="table-wrap"><table class="sizes"><thead><tr><th>Size</th><th>Millimeters</th><th>Inches</th><th>PDF points</th><th>Sides</th><th>Group</th><th>PWG name</th><th>CSS keyword</th><th>Our generators</th></tr></thead>
<tbody>{"".join(trs)}</tbody></table></div></div>"""


def page():
    """Returns (first part, second part) for page.html – the first ad sits between the two, away from all controls."""
    c = check()
    r = {x["label"]: x for x in rows()}
    ratio = lambda k: f'{r[k]["hmm"] / r[k]["wmm"]:.3f}'
    first = f"""<h2 id="scale">Print scale calculator</h2>
<p>Pick the page size stored in your PDF, the paper that is in the printer and the setting in the print dialog. The calculator shows the scale the page is printed at, what a grid or line spacing turns into, and whether anything is cut off.</p>
{CALC}
<p><strong>How it is calculated.</strong> At 100% the page keeps its size; whatever is wider or taller than the area the printer can reach is lost. With a “Fit” setting the program divides the reachable width by the page width and the reachable height by the page height and uses the smaller of the two numbers as the scale. “Shrink oversized pages” does the same but never goes above 100%. The reachable area is the sheet minus the printer's blank border on each side.</p>
<p><strong>What it assumes.</strong> Page and sheet have the same orientation, the page is centered, and the border is the same on all four sides. Real printers often have a wider border on one side. You can measure yours with the edge rulers on the <a href="/print-test-page.html">print test page</a> and enter the largest value.</p>"""
    table = f"""<h2 id="table">{c["count"]} paper sizes in millimeters, inches and points</h2>
<p>The table lists the sheet sizes of the ISO A, B and C series, the North American office, engineering and architectural sizes, the Japanese JIS B series and the RA and SRA press sheets. Every row carries the standardized media name that printers and print systems use for that size, so you can check each value against the source yourself.</p>
{_table()}
<h2>How to read the columns</h2>
<ul><li><strong>Millimeters and inches.</strong> One of the two is the defining value: the Printer Working Group list gives ISO and Japanese sizes in millimeters and North American sizes in inches. The other column is converted with 1 inch = 25.4 mm, which is exact by definition, and rounded to one decimal (mm) or two decimals (inches).</li>
<li><strong>PDF points.</strong> A PDF describes its page in units of 1/72 inch unless the file says otherwise. A4 is therefore {r["A4"]["pt"]} points and US Letter {r["US Letter"]["pt"]} points – the numbers you meet in PDF tools and print drivers.</li>
<li><strong>Sides.</strong> Long side divided by short side. Two sizes with the same value have the same shape, and one can be scaled onto the other without blank strips.</li>
<li><strong>PWG name.</strong> The self-describing media name from PWG 5101.1. It contains the size itself, for example <code>{r["A4"]["pwg"]}</code>.</li>
<li><strong>CSS keyword.</strong> Ten sizes have a keyword for the CSS <code>size</code> property, as in <code>@page {{ size: A4 }}</code>. All other sizes have to be written as lengths.</li>
<li><strong>Our generators.</strong> The four sizes in which every template on this site can be made. The link opens graph paper in that size.</li></ul>
"""
    second = f"""<h2>What the numbers show</h2>
<p>These statements are recalculated from the table every time the site is built; if one stopped being true, the build would fail.</p>
<ul><li><strong>Halving.</strong> In the A, B, C, JIS B, RA and SRA rows, each size is the next larger one cut in half across its long side, with half millimeters rounded down. A4 (210 × 297) halves to A5 (148 × 210), because 297 ÷ 2 = 148.5.</li>
<li><strong>A0 is one square meter, almost.</strong> 841 × 1189 mm is {c["a0_area"]:.6f} m². B0 is exactly 1000 mm wide.</li>
<li><strong>The shape stays the same.</strong> From A0 to A6 and B0 to B6 the sides stay within {c["ratio_dev"]:.3f} of 1 : 1.414 (the square root of 2). That is why an A4 page reduced to A5 fills the sheet. US sizes do not behave this way: US Letter is 1 : {ratio("US Letter")}, Half Letter 1 : {ratio("Half Letter (Statement)")}, US Legal 1 : {ratio("US Legal")} and Ledger 1 : {ratio("Ledger / Tabloid")}. A Letter page reduced onto Half Letter leaves blank strips; try it in the calculator above.</li>
<li><strong>C sits between A and B.</strong> Every C size is within 1 mm of the geometric mean of the A and B size with the same number, so an unfolded A4 sheet ({r["A4"]["mm"]} mm) fits inside a C4 envelope ({r["C4"]["mm"]} mm).</li>
<li><strong>A4 and US Letter.</strong> US Letter is {r["US Letter"]["wmm"] - r["A4"]["wmm"]:.1f} mm wider and {r["A4"]["hmm"] - r["US Letter"]["hmm"]:.1f} mm shorter than A4. Fitting an A4 page onto Letter therefore gives {r["US Letter"]["hmm"] / r["A4"]["hmm"] * 100:.1f}%, and fitting a Letter page onto A4 gives {r["A4"]["wmm"] / r["US Letter"]["wmm"] * 100:.1f}%.</li></ul>
<h2>Sources</h2>
<ul><li><strong>The Printer Working Group, PWG 5101.1-2023, “PWG Media Standardized Names v2.1 (MSN)”</strong>, Candidate Standard, 15 September 2023: <a href="https://ftp.pwg.org/pub/pwg/candidates/cs-pwgmsn21-20230915-5101.1.pdf" rel="noopener">ftp.pwg.org/pub/pwg/candidates/cs-pwgmsn21-20230915-5101.1.pdf</a>. Source of every size and media name in the table. We read the size tables of the 2013 edition in full and checked each of the {c["count"]} names letter for letter against the text of the 2023 edition. Accessed {ACCESSED}.</li>
<li><strong>W3C, “CSS Paged Media Module Level 3”</strong>, Working Draft, 14 September 2023: <a href="https://www.w3.org/TR/css-page-3/" rel="noopener">w3.org/TR/css-page-3</a>. Source of the ten page-size keywords and of the terms “printable area” and “non-printable area”; it describes the non-printable area as printer dependent. Sections on page size and the page model read in full. Accessed {ACCESSED}.</li>
<li><strong>ISO 32000-1:2008, “Document management – Portable document format – Part 1: PDF 1.7”</strong>, copy published by Adobe: <a href="https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf" rel="noopener">opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf</a>. Source of the unit 1/72 inch (default user space, section 8.3.2.3 and the UserUnit entry of the page object). Those passages read. Accessed {ACCESSED}.</li>
<li><strong>NIST, Office of Weights and Measures, “SI Units – Length”</strong>: <a href="https://www.nist.gov/pml/owm/si-units-length" rel="noopener">nist.gov/pml/owm/si-units-length</a>. Source of 1 inch = 25.4 mm exactly (in force since 1 July 1959). Passage read. Accessed {ACCESSED}.</li></ul>
<p class="small muted">What we did not read: ISO 216 (the standard behind the A and B series) and the ASME drawing-sheet standards are sold by their publishers and were not available to us. The table therefore quotes the Printer Working Group list, which reproduces these sizes, and does not quote the standards themselves. Print scales are arithmetic on the listed sizes; they are not measurements of a printer.</p>"""
    return first + table, second   # the ad follows the column notes, far from the calculator and the table filter
