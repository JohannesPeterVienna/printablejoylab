"""Templates: metadata and the guide text shown under each generator."""

CATS = [("paper", "Paper"), ("calendars", "Calendars"), ("planners", "Planners"), ("trackers", "Trackers & lists")]

TOOLS = [
# ------------------------------------------------------------------ PAPER
{
"slug": "lined-paper", "cat": "paper", "name": "Lined paper", "accent": "ink",
"teaser": "Wide, college or narrow ruled – with margin and header line.",
"title": "Printable Lined Paper – Wide, College & Narrow Ruled (Free PDF)",
"description": "Make free printable lined paper in A4, US Letter or A5: wide, college or narrow ruled, custom spacing, margin line and header. Instant vector PDF.",
"lead": "Choose the ruling, paper size and line color, then download a crisp vector PDF or print straight away.",
"guide": """
<h2>Which ruling should you pick?</h2>
<p>Lined paper is described by the distance between its lines. The three standard rulings come from US school paper, but they are used everywhere:</p>
<ul><li><strong>Wide ruled</strong> – 11/32 inch (8.7 mm). Generous space for larger handwriting, younger writers and anyone who finds tight lines tiring.</li>
<li><strong>College ruled</strong> – 9/32 inch (7.1 mm). The most common choice for notes, letters and journals. It fits more text without feeling cramped.</li>
<li><strong>Narrow ruled</strong> – 1/4 inch (6.35 mm). Popular with people who write small or want to squeeze a lot onto one page.</li></ul>
<p>Need something else? Pick <em>Custom</em> and enter any spacing between 3 and 20 mm in half-millimeter steps. Many European exercise books use around 8–9 mm, while 6 mm suits compact note-taking. On a portrait A4 sheet with the header switched on, college ruling gives 35 writing lines; on US Letter it gives 33.</p>
<h2>How to set up the page</h2>
<ol><li><strong>Paper size and orientation:</strong> choose the sheet that is in your printer. Portrait is normal for writing; landscape is useful for wide tables of words, such as vocabulary lists in two languages.</li>
<li><strong>Ruling:</strong> pick wide, college, narrow or a custom value.</li>
<li><strong>Margin line:</strong> the pale red vertical line sits 32 mm from the left edge on A4 and Letter (22 mm on A5 and Half Letter). It leaves a column for dates, question numbers or keywords.</li>
<li><strong>Header:</strong> adds a short <em>Name</em> and <em>Date</em> line at the top – useful for worksheets, exam practice and letters, unnecessary for a private journal.</li>
<li><strong>Line color:</strong> light gray, medium, dark, blue or your accent color.</li></ol>
<h2>A filled example: lecture notes</h2>
<p>A student prints ten college-ruled A4 pages with margin and header. In the header go the course name and the date written as 2027-02-08, so the pages sort correctly later. During the lecture the main lines hold the notes in short sentences; the margin column is reserved for keywords such as “definition”, “exam!” or a question mark next to anything unclear. After class, the student writes a two-line summary on the last lines of the page. When revising, reading only the margin column and the summaries gives a quick overview of the whole lecture.</p>
<h2>Light lines write better</h2>
<p>Very dark lines compete with your handwriting. The light gray setting is the most pleasant for everyday writing; <em>Blue</em> gives the familiar notebook look, and <em>Medium</em> helps if your printer prints faintly. Light lines also fade more cleanly when you scan or photocopy finished notes.</p>
<h2>Spacing and handwriting size</h2>
<p>A useful rule of thumb: the body of your lowercase letters – the x-height, the height of an “a” or “n” – should fill a little less than half the gap between two lines. The rest is room for ascenders (b, d, h) and descenders (g, p, y) without touching the neighboring lines. That puts an x-height of about 2.5 mm on narrow ruling, about 3 mm on college ruling and 3.5 mm or more on wide ruling. If your loops keep hitting the line below, switch to the next wider ruling instead of trying to write smaller.</p>
<h2>How many lines you get on other sizes</h2>
<div class="table-wrap"><table><thead><tr><th>Page (header on)</th><th>Wide</th><th>College</th><th>Narrow</th></tr></thead><tbody>
<tr><td>A5 portrait</td><td>20</td><td>24</td><td>27</td></tr>
<tr><td>Half Letter portrait</td><td>20</td><td>25</td><td>28</td></tr>
<tr><td>A4 landscape</td><td>–</td><td>23</td><td>–</td></tr>
<tr><td>US Letter landscape</td><td>–</td><td>24</td><td>–</td></tr></tbody></table></div>
<p>Switching the header off usually adds one more line. Landscape trades lines for length: each line is about 297 mm long on A4, which suits two-column word lists but is tiring for continuous writing.</p>
<h2>Paper and printer settings</h2>
<ul><li><strong>Pick the paper by the pen:</strong> pencil and ballpoint are happy on everyday 75–80 g/m² copy paper. Gel pens and fountain pens show through less on heavier, smoother paper.</li>
<li><strong>Use normal quality, not draft:</strong> draft and toner-saving modes thin out light lines, and the light gray setting can break up into dots. If that happens, print at normal quality or choose <em>Medium</em>.</li>
<li><strong>Grayscale is fine:</strong> lines printed in grayscale look almost the same; only the blue and accent colors turn gray, and the red margin line becomes a pale gray line.</li>
<li><strong>Punching holes:</strong> a standard two-hole punch (ISO 838) places 6 mm holes with their centers 12 mm from the edge, so the holes end about 15 mm in – well clear of the margin line at 32 mm.</li>
<li><strong>Double-sided:</strong> for portrait pages choose “flip on long edge” so the back is the right way up when you turn the sheet like a book page.</li></ul>
<h2>Printing tips</h2>
<p>The lines run all the way across the sheet; your printer simply leaves its own unprintable border white, so nothing important is lost. Keep the print scale at 100% so the spacing stays exactly as chosen – our <a href="/print-at-actual-size.html">guide to printing at actual size</a> shows where that setting hides. Lined paper has no front or back, so for a notebook you can print the same page on both sides of each sheet. For fountain pens, 90–100 g/m² paper reduces show-through; see <a href="/choose-the-right-paper.html">which paper for which job</a> for weights in pounds and gsm.</p>
""",
"faq": [("Is college ruled the same as 7 mm lines?", "Almost: college ruling is 9/32 inch, which is 7.14 mm. For most purposes the difference to 7 mm is invisible."),
        ("How do I make handwriting practice sheets?", "Choose wide ruling or a custom spacing of 10–12 mm, switch the header on for the child's name, and use the medium line color so the lines stay visible."),
        ("Why does the margin line go from top to bottom?", "It marks a full-height column, as in classic exercise paper. If you do not need it, untick “Red margin line” and the lines run uninterrupted."),
        ("Can I use the paper commercially?", "You may print and use the pages for yourself, your family, your classroom or your own business. Please do not resell the files or offer them for download elsewhere."),
        ("Why do my printed lines look broken or dotted?", "Light gray is printed as a fine pattern of tiny dots on most printers, and draft or toner-saving modes thin it further. Print at normal quality, or choose the Medium line color for a solid-looking line."),
        ("Can I make Cornell-style notes with this paper?", "Yes, with one pencil line. The classic Cornell layout has a cue column about 2.5 inches (63 mm) wide on the left and a summary area of about 2 inches (50 mm) at the bottom. Our margin line sits at 32 mm, so draw the cue line by hand at 63 mm, or simply use the narrower margin column for keywords."),
        ("Will the pages mix with store-bought college-ruled paper?", "The spacing is the same 9/32 inch, so the lines match. The position of the first line and the margin can differ slightly between brands, so pages side by side in a binder may not line up exactly.")],
},
{
"slug": "graph-paper", "cat": "paper", "name": "Graph paper", "accent": "teal",
"teaser": "Metric or imperial grids, with bold lines every few squares.",
"title": "Printable Graph Paper – 5 mm, 1 cm, 1/4 Inch Grid (Free PDF)",
"description": "Create free printable graph paper: 4 mm, 5 mm, 1 cm, 1/4 or 1/5 inch grids with optional bold lines, in A4, Letter or A5. Download as vector PDF.",
"lead": "Square grid paper for math, sketching, floor plans and pixel art – in metric or imperial sizes.",
"guide": """
<h2>Metric or imperial?</h2>
<p>Graph paper (also called grid or squared paper) comes in two families. <strong>Metric</strong> grids of 4 mm, 5 mm or 1 cm are standard in most of Europe and in the sciences. <strong>Imperial</strong> grids divide each inch into 4 or 5 squares: 1/4 inch (6.35 mm) is the classic US quad-ruled paper used in schools, and 1/5 inch (5.08 mm) is common on engineering pads. Choose <em>Custom</em> for anything from 2 to 25 mm. The grid is centered on the page, so the white border is the same on both sides. With 5 mm squares, a portrait A4 page holds 37 × 53 squares and a US Letter page 38 × 50.</p>
<h2>Bold lines make counting easy</h2>
<p>A heavier line every few squares turns the grid into a ruler. With 5 mm squares and bold lines every 2, each bold square is exactly 1 cm; with bold lines every 10, each bold square is 5 cm. On a 1/4 inch grid, bold lines every 4 squares mark whole inches. Choose <em>No bold lines</em> for pixel art or stitch charts, where every square counts the same, or bold lines every 10 for charts where you count stitches in tens.</p>
<h2>How to use it for a scale drawing</h2>
<ol><li>Measure the longest side of the room, garden bed or object.</li>
<li>Count how many squares fit along the matching side of the page (landscape usually gives more).</li>
<li>Choose a round scale that fits, such as 1 square = 10 cm or 1 square = 6 inches, and write it in a corner.</li>
<li>Draw outer walls first, then doors and windows, then furniture or plants.</li></ol>
<h2>A filled example: a raised garden bed</h2>
<p>A gardener plans a 1.2 m × 2.4 m bed on 5 mm graph paper in landscape, with bold lines every 10 squares. At 1 square = 5 cm, the bed is 24 × 48 squares – it fits with room for notes. Each bold square now covers 50 × 50 cm. Tomatoes go along the back in four 50 cm sections, lettuce and radishes in a strip of 6 squares at the front, and a path of 2 squares is marked between them. The planting dates are written beside each section, and the page goes into a plastic sleeve in the shed.</p>
<h2>More uses</h2>
<ul><li><strong>Math and statistics:</strong> plotting functions, bar charts and aligned columns of numbers.</li>
<li><strong>Knitting, cross-stitch and pixel art:</strong> one square per stitch or pixel; a light line color keeps the chart readable after you fill it in.</li>
<li><strong>Handwriting:</strong> a 1 cm grid helps children keep letters the same size.</li></ul>
<h2>How many squares fit on other sizes</h2>
<div class="table-wrap"><table><thead><tr><th>Grid</th><th>A4 landscape</th><th>Letter landscape</th><th>A5 portrait</th><th>Half Letter portrait</th></tr></thead><tbody>
<tr><td>4 mm</td><td>68 × 45</td><td>63 × 46</td><td>32 × 46</td><td>30 × 48</td></tr>
<tr><td>5 mm</td><td>54 × 36</td><td>51 × 37</td><td>26 × 37</td><td>24 × 38</td></tr>
<tr><td>1/5 inch</td><td>53 × 35</td><td>50 × 36</td><td>25 × 36</td><td>23 × 37</td></tr>
<tr><td>1/4 inch</td><td>42 × 28</td><td>40 × 29</td><td>20 × 29</td><td>19 × 30</td></tr>
<tr><td>1 cm</td><td>27 × 18</td><td>25 × 18</td><td>13 × 18</td><td>12 × 19</td></tr></tbody></table></div>
<p>The first number is the count across, the second down. The bold lines differ from the fine ones by weight, not color: fine lines are 0.16 mm wide, bold lines 0.42 mm, both in the line color you choose. That is why the bold grid stays clear in grayscale prints and on photocopies.</p>
<h2>A filled example: a cross-stitch chart</h2>
<p>A stitcher wants a motif of 60 × 40 stitches. On the 4 mm grid in A4 landscape (68 × 45 squares) it fits with a few squares to spare, and bold lines every 10 squares make counting in tens easy. Each filled square is one cross. Stitched on 14-count Aida, which has 14 stitches per inch, the finished motif measures 60 ÷ 14 ≈ 4.3 in by 40 ÷ 14 ≈ 2.9 in – about 10.9 × 7.3 cm. On 18-count fabric the same chart comes out smaller, about 8.5 × 5.6 cm, so the fabric count decides the final size, not the chart.</p>
<h2>Paper choices for grid work</h2>
<ul><li><strong>Pencil and eraser:</strong> 90–100 g/m² paper survives repeated erasing better than thin copy paper.</li>
<li><strong>Coloring squares:</strong> for pixel art with markers, 120 g/m² keeps the colors from bleeding into the next sheet.</li>
<li><strong>A grid underlay:</strong> print a 5 mm or 1 cm grid with the dark line color and lay it under a sheet of plain paper. On a window or light pad the lines show through and keep handwriting or a sketch straight, while the final sheet stays blank.</li></ul>
<h2>Printing tips</h2>
<p>Scale matters more for graph paper than for any other template: if the printer shrinks the page to fit its margins, a 5 mm grid becomes about 4.8 mm and scale drawings drift. Print at 100% and check ten squares with a ruler. For engineering-style sheets, pick the light line color; for photocopying, medium or dark.</p>
""",
"faq": [("How many squares fit on an A4 page?", "With a 5 mm grid and our 12 mm margins, the page holds 37 squares across and 53 down in portrait orientation."),
        ("What is engineering paper?", "Engineering paper is usually a light green 1/5 inch grid printed on the back so it shows through faintly. Choose the 1/5 inch grid and the light line color for a similar look."),
        ("Which grid is best for algebra and geometry homework?", "A 5 mm or 1/4 inch grid. It is fine enough to fit a whole graph on half a page and large enough to write numbers inside the squares."),
        ("Can I get a grid with an exact number of squares?", "Choose a custom grid size in half-millimeter steps. The preview redraws instantly, so you can count the squares along an edge before you print."),
        ("Why are the bold lines the same color as the fine lines?", "They are drawn thicker instead – 0.42 mm against 0.16 mm. A difference in weight survives grayscale printing and photocopying, whereas two shades of a light color often merge."),
        ("How do I make a grid I can put under plain paper?", "Choose a 5 mm or 1 cm grid, the dark line color and bold lines every 5 or 10 squares, then print. Place the sheet under the page you write on; with a light behind it, the grid shows through."),
        ("Which grid matches my cross-stitch fabric?", "Any grid works for the chart, because one square is one stitch. The fabric count sets the finished size: divide the number of stitches by the count to get inches.")],
},
{
"slug": "dot-grid", "cat": "paper", "name": "Dot grid paper", "accent": "plum",
"teaser": "The bullet journal favorite – 5 mm dots and more.",
"title": "Printable Dot Grid Paper – 5 mm Bullet Journal Dots (Free PDF)",
"description": "Free printable dot grid paper for bullet journals, sketching and lettering: 4 mm, 5 mm, 1/4 inch, 7 mm or 1 cm spacing, fine to bold dots, A4/Letter/A5 PDF.",
"lead": "Structure without clutter: dots guide your lines, layouts and lettering, then step back so your writing stands out.",
"guide": """
<h2>Why dot grid?</h2>
<p>Dot grid paper sits between lined and blank. The dots give you a grid for straight lines, boxes and tables, but they are quiet enough that drawings and handwriting stay in the foreground. That flexibility made dot grid the standard paper for bullet journaling, and it is just as useful for meeting notes with small diagrams, lettering practice and quick wireframes. With 5 mm spacing, a portrait A4 page holds 38 × 54 dots, a US Letter page 39 × 51 and an A5 page 27 × 38.</p>
<h2>Choosing the spacing and dot size</h2>
<ul><li><strong>5 mm</strong> is the spacing most dotted notebooks use. One row of handwriting usually takes the height of one dot gap, larger letters two.</li>
<li><strong>4 mm</strong> suits small handwriting and dense layouts such as a 31-day tracker grid.</li>
<li><strong>7 mm or 1 cm</strong> works well for lettering practice, children and big headings.</li>
<li><strong>1/4 inch</strong> matches US dotted notebooks and planner inserts.</li></ul>
<p>Not sure? Print one page each of 4 mm and 5 mm and write a paragraph on both; the one where your handwriting looks natural is your spacing.</p>
<p>The dots come in three sizes: fine (about 0.36 mm across), medium (0.52 mm) and bold (0.72 mm). Fine dots almost vanish under ink; bold dots survive faint printers and photocopies. Medium gray is the default color because it stays visible without dominating.</p>
<h2>How to lay out a page in three minutes</h2>
<ol><li>Count dots instead of measuring: decide that a heading takes two rows and a box border sits one dot inside the edge.</li>
<li>Draw only the outer lines with a ruler; the dots line up everything inside them.</li>
<li>Leave one empty dot row between sections. It reads as clear spacing without wasting space.</li></ol>
<h2>A filled example: a monthly overview spread</h2>
<p>On an A5 page with 5 mm dots, the month name goes in the top two rows. Below it, 31 rows on the left list the dates with weekday initials; that uses 31 of the 38 rows and leaves room for a short note at the bottom. On the right half of the page, a box 12 dots wide holds the month's tasks, and a smaller box below it collects birthdays. Each column of the date list is three dots wide: one for the date, one for a symbol, one for space before the text.</p>
<h2>Bullet journal layouts to try</h2>
<ul><li><strong>Future log:</strong> six boxes for the next six months, three per page.</li>
<li><strong>Weekly spread:</strong> seven boxes of equal height plus a to-do column.</li>
<li><strong>Tracker grid:</strong> one dot per day across, one row per habit.</li>
<li><strong>Collections:</strong> books to read, gift ideas, packing lists.</li></ul>
<p>Prefer ready-made pages? The <a href="/weekly-planner.html">weekly planner</a> and <a href="/habit-tracker.html">habit tracker</a> generate those layouts for you, and the <a href="/bullet-journal-starter.html">bullet journal starter kit</a> explains the method.</p>
<h2>Dot counts for every spacing</h2>
<div class="table-wrap"><table><thead><tr><th>Spacing</th><th>A4</th><th>US Letter</th><th>A5</th><th>Half Letter</th></tr></thead><tbody>
<tr><td>4 mm</td><td>47 × 68</td><td>48 × 63</td><td>33 × 47</td><td>31 × 49</td></tr>
<tr><td>1/4 inch</td><td>30 × 43</td><td>31 × 40</td><td>21 × 30</td><td>20 × 31</td></tr>
<tr><td>7 mm</td><td>27 × 39</td><td>28 × 36</td><td>19 × 27</td><td>18 × 28</td></tr>
<tr><td>1 cm</td><td>19 × 27</td><td>20 × 26</td><td>14 × 19</td><td>13 × 20</td></tr></tbody></table></div>
<p>All counts are for portrait pages, dots across × dots down; on Half Letter, 5 mm spacing gives 25 × 39. Because the grid is centered, there is always the same white border left and right.</p>
<h2>Hand lettering on dots</h2>
<p>Dots make consistent letter heights easy. On a 5 mm grid, a simple lettering layout uses two dot gaps (10 mm) for the x-height and one more gap above and below for ascenders and descenders, so one line of lettering takes four gaps. Mark the baseline with a light pencil stroke from dot to dot, keep the slant constant by aiming at a dot two rows up and one column across, and leave one empty gap between lines of text.</p>
<h2>Paper, markers and ghosting</h2>
<p>Two different things happen with markers. <strong>Ghosting</strong> is a shadow of the ink visible from the back; <strong>bleed-through</strong> means the ink actually soaks through the paper. Heavier, more opaque paper of 120 g/m² or more reduces both, and a spare sheet behind the page catches the rest. Test markers on a printed scrap first: some alcohol-based markers can smear inkjet ink, while laser toner is generally unaffected. In draft or toner-saving mode, fine dots may drop out completely, so print dot grid at normal quality.</p>
<h2>Printing tips</h2>
<p>To make an A5 booklet, print A5 pages directly, or print A4 pages and cut them in half. Heavier 100–120 g/m² paper reduces ghosting with markers. Keep the scale at 100% so the 5 mm dots really are 5 mm apart – otherwise pages printed on different days will not line up in a binder.</p>
""",
"faq": [("What size dots do bullet journals use?", "Most dotted notebooks use a 5 mm grid. That is our default setting."),
        ("Will the dots show when I scan my notes?", "Light, fine dots usually disappear or turn very faint in scans – one reason dot grid is popular for notes you want to digitize."),
        ("Which dot size works with watercolor or brush pens?", "Fine dots in the light color. They are easy to see while you plan the layout and almost invisible once the page is painted or lettered."),
        ("Can I print dots on both sides?", "Yes. The grid is centered on the page, so on most printers the dots on the front and back line up closely."),
        ("What is the difference between ghosting and bleed-through?", "Ghosting is when you can see the writing from the back of the sheet; bleed-through is when the ink passes through and marks the next page. Thicker, more opaque paper helps with both."),
        ("Why do some dots disappear when I print?", "Fine dots are only about 0.36 mm across. Draft and toner-saving modes, or a nearly empty cartridge, can skip them. Use normal print quality or the medium dot size."),
        ("Can I use the 1/4 inch spacing for US planner inserts?", "Yes. 1/4 inch matches many US dotted notebooks and inserts; on Half Letter it gives 20 × 31 dots.")],
},
{
"slug": "isometric-paper", "cat": "paper", "name": "Isometric paper", "accent": "olive",
"teaser": "Triangle grid for 3D sketches, game maps and design.",
"title": "Printable Isometric Graph Paper – Lines or Dots (Free PDF)",
"description": "Free printable isometric paper with 60° triangle grid or isometric dots for 3D drawings, game maps, architecture and design. A4, Letter, A5 vector PDF.",
"lead": "A grid of 60° lines that makes three-dimensional sketches easy – for design, architecture, math and tabletop games.",
"guide": """
<h2>What is isometric paper?</h2>
<p>Isometric paper is covered in equilateral triangles. In the line version, three sets of lines run vertically and at 30° to either side of horizontal. Because all three axes are drawn at the same scale, cubes and boxes look three-dimensional without vanishing points, and every edge can be measured by counting triangles. The triangle size you choose is the length of one side: a 5 mm triangle is about 4.33 mm high, a 1 cm triangle about 8.66 mm.</p>
<h2>How to draw a cube</h2>
<ol><li>Pick a point where lines meet. Draw a vertical edge along a vertical line, for example three triangles long.</li>
<li>From the top and bottom of that edge, follow the two diagonal lines – one to the left, one to the right – for the same number of triangles.</li>
<li>Close the sides with two more vertical edges and copy the top diagonals to finish the lid.</li></ol>
<p>Every edge follows the grid, so the proportions are always right. Larger shapes are stacks of cubes: draw the overall block first, then cut away the parts you do not need. Shade the three visible faces in three tones – light on top, medium on one side, dark on the other – and the object immediately looks solid.</p>
<h2>A filled example: planning a bookshelf</h2>
<p>A maker plans a shelf 90 cm wide, 30 cm deep and 200 cm tall on 5 mm isometric paper. At 1 triangle side = 10 cm, the shelf is 9 triangles along one diagonal axis, 3 along the other and 20 up the vertical lines. The outer box is drawn first, then four shelves at 40 cm intervals, each 4 triangles above the last, with the real measurements written next to them. Hidden edges are dashed. The finished sketch shows at a glance whether the depth looks right before any wood is cut.</p>
<h2>Who uses it?</h2>
<ul><li><strong>Designers and architects</strong> for product sketches and room layouts.</li>
<li><strong>Game designers and tabletop players</strong> for isometric maps, dungeons and pixel-art style scenes.</li>
<li><strong>Teachers</strong> for volume, nets of solids and spatial reasoning tasks.</li>
<li><strong>Makers</strong> planning woodwork, 3D prints or LEGO builds.</li></ul>
<h2>Lines or dots?</h2>
<p>Full lines are easiest for beginners. The dot version shows only the points where lines would cross: drawings look cleaner and the grid disappears into the background, which suits finished illustrations. In the dot version the rows run horizontally, offset by half a triangle, so turn the sheet a quarter turn if you want vertical edges to follow a column of dots.</p>
<h2>How the grid is measured</h2>
<p>On the line version, the vertical lines are spaced at the height of one triangle, not its side: with 5 mm triangles they sit about 4.33 mm apart, with 1 cm triangles about 8.66 mm. Along any of the three line directions, however, the crossings are exactly one triangle side apart. So you measure an edge by counting steps along the line it follows. A portrait page holds 44 vertical lines on A4 and 45 on US Letter with 5 mm triangles; with 1 cm triangles it is 23 on both.</p>
<h2>Three views and one isometric drawing</h2>
<p>Technical drawing classes often pair isometric paper with ordinary graph paper. The front, top and side views of an object go on graph paper, one square per unit; the isometric view goes on this sheet, one triangle side per unit. Building the isometric view from the three flat views is a classic spatial-reasoning exercise: every corner in the flat views becomes a crossing point on the triangle grid. Using the same unit on both sheets lets you check each edge by counting.</p>
<h2>Isometric games and pixel art</h2>
<p>Many video games described as “isometric” actually use a 2:1 pixel slope – two pixels across for one up, an angle of about 26.6° – because it gives clean pixel steps. Our grid is true isometric, with lines at 30°. For true isometric sketches, maps and board-game tiles it is exactly right; for planning 2:1 pixel art, use <a href="/graph-paper.html">graph paper</a> and step two squares across for every square up.</p>
<h2>Paper for shading and tracing</h2>
<p>For shading the three faces of an object with colored pencils, a smooth 100–120 g/m² paper takes several layers without pilling. The dot version uses dots of about 0.56 mm, larger than the fine dots of our dot grid, so they stay visible after shading. If you use the sheet as a drawing underlay on a light pad, print the lines in the dark color.</p>
<h2>Choosing the triangle size and printing</h2>
<p>4–5 mm triangles give lots of detail for small objects; 7 mm or 1 cm triangles are easier to see and suit classroom use, children and large maps. Print at 100% so the 60° angles and the scale stay exact – a page shrunk to fit a different paper size distorts nothing visibly but makes measured drawings slightly off. A light line color keeps your pencil lines readable; use medium if you plan to photocopy the sheet.</p>
""",
"faq": [("Is isometric the same as perspective drawing?", "No. In perspective drawing, parallel lines meet in a vanishing point. In isometric drawing they stay parallel, so measurements along each axis remain to scale."),
        ("Can I use the grid for hex maps?", "Yes – groups of six triangles form hexagons, so isometric paper works for simple hex maps too."),
        ("Which triangle size should children use?", "1 cm triangles. They are large enough to count easily and to color in, and simple cube buildings stay clearly readable."),
        ("Why do circles look like ovals on isometric drawings?", "A circle on the face of a cube is seen at an angle, so in isometric view it becomes an ellipse. Sketch it inside a rhombus of grid lines and round the corners."),
        ("How do I measure a slanted edge?", "Count the triangle sides along the line the edge follows. With a 5 mm grid, an edge of six steps along a 30° line is 30 mm in the drawing, just like six steps up a vertical line."),
        ("Is this the same grid video games use?", "Not quite. Many games use a 2:1 pixel slope of about 26.6°. This paper is true isometric with 30° lines, which is what technical drawing and most board-game maps use."),
        ("Why are the vertical lines closer together than the triangle size?", "Their spacing is the triangle height, which is the side × √3 ÷ 2 – about 4.33 mm for a 5 mm triangle. Measurements along the lines still use the full triangle side.")],
},
# ------------------------------------------------------------------ CALENDARS
{
"slug": "monthly-calendar", "cat": "calendars", "name": "Monthly calendar", "accent": "tomato",
"teaser": "Any month, any year – or all twelve in one PDF.",
"title": "Printable Monthly Calendar 2027 – Any Month, Monday or Sunday Start",
"description": "Make a free printable monthly calendar for any month and year, starting Monday or Sunday, with week numbers and notes. Download one month or all 12 as PDF.",
"lead": "A clean month grid with room to write. Pick the year and month – or all twelve months – and start the week on Monday or Sunday.",
"guide": """
<h2>A calendar that fits your week</h2>
<p>In the US, Canada and Japan, calendars traditionally start the week on <strong>Sunday</strong>. In most of Europe and under the international standard ISO 8601, the week starts on <strong>Monday</strong>. Choose whichever matches the way you plan: with a Monday start, Saturday and Sunday sit together at the end of each row; with a Sunday start, the weekend frames the week. Weekend boxes are lightly shaded and their dates appear in your accent color, so they stand out in either layout. Any year from 1900 to 2100 works, calculated with the Gregorian calendar.</p>
<h2>Week numbers explained</h2>
<p>The small gray numbers at the left edge are ISO 8601 week numbers: weeks start on Monday, and week 1 is the week that contains the first Thursday of the year. That is why the first days of January sometimes belong to week 52 or 53 of the previous year – January 1–3, 2027, for example, are still in week 53 of 2026. With a Sunday start, the number shown belongs to the Monday in that row. Our <a href="/printable-calendar-2027.html">2027 calendar guide</a> lists the week dates and the US federal holidays for the year.</p>
<h2>How to make your calendar</h2>
<ol><li>Enter the year and choose a single month or <em>All 12 months</em> for a 12-page PDF.</li>
<li>Pick Monday or Sunday as the first day of the week.</li>
<li>Choose the paper size and orientation. Landscape adds a 52 mm notes column on the right; portrait places a notes area below the grid.</li>
<li>Switch week numbers and notes on or off, pick an accent color and a title style.</li></ol>
<p>Months that span six rows – May 2027 in both layouts, for instance – get slightly shorter boxes. On A4 landscape a six-row month still gives day boxes of about 30 × 26 mm, enough for two or three short entries.</p>
<h2>A filled example: a family calendar for one month</h2>
<p>A family prints September in landscape and gives each person a pen color: blue for one parent's work trips, green for the other's late shifts, orange for the children's school and sports dates. Paydays are marked with a small “$”, the trash pickup with a dot in the corner of each Tuesday box. The notes column collects things that belong to the month but not to a day: the school supply list, the new soccer schedule, a reminder to book flu shots. The page hangs on the fridge, and whoever adds an appointment writes it straight into the box.</p>
<h2>More ideas</h2>
<ul><li><strong>Content or project calendar:</strong> plan posts, deadlines and launches with one color per channel or project.</li>
<li><strong>Bill calendar:</strong> mark due dates for rent, subscriptions and insurance and tick them off when paid.</li>
<li><strong>Training plan:</strong> write the planned distance in each box and the actual one next to it.</li></ul>
<h2>How big are the day boxes?</h2>
<p>A month needs four, five or six rows, depending on the weekday it starts on, its length and your week start. February 2027 is a rare four-row month with a Monday start: February 1 is a Monday and the month has exactly 28 days. With a Sunday start it needs five rows. The table shows the day box size in millimeters (width × height) with week numbers and notes switched on.</p>
<div class="table-wrap"><table><thead><tr><th>Page</th><th>4 rows</th><th>5 rows</th><th>6 rows</th></tr></thead><tbody>
<tr><td>A4 landscape</td><td>29.9 × 38.5</td><td>29.9 × 30.8</td><td>29.9 × 25.7</td></tr>
<tr><td>US Letter landscape</td><td>27.3 × 40.0</td><td>27.3 × 32.0</td><td>27.3 × 26.7</td></tr>
<tr><td>A4 portrait</td><td>25.6 × 52.8</td><td>25.6 × 42.2</td><td>25.6 × 35.2</td></tr>
<tr><td>US Letter portrait</td><td>26.4 × 48.3</td><td>26.4 × 38.7</td><td>26.4 × 32.2</td></tr>
<tr><td>A5 landscape</td><td>18.3 × 24.5</td><td>18.3 × 19.6</td><td>18.3 × 16.3</td></tr></tbody></table></div>
<p>As a rule, one handwritten entry needs about 6–7 mm of height, so a 26 mm box holds three short lines and a 16 mm box on A5 one or two. If you write a lot into single days, portrait gives the tallest boxes; landscape gives the widest ones and the separate notes column.</p>
<h2>Printing in black and white</h2>
<p>The weekday bar is filled with your accent color and carries white lettering. In grayscale, light accents such as sand turn into a pale gray, and the white weekday names lose contrast. For black-and-white printers, choose the ink or mono accent; tomato, teal and plum also stay readable. Weekend boxes are tinted with a very light warm gray that usually survives grayscale printing as a faint shade.</p>
<h2>More practical setups</h2>
<ul><li><strong>Chore rotation:</strong> write one person's initials in the corner of each box, so the rota is visible to everyone.</li>
<li><strong>Reusable month:</strong> slip a printed month into a sheet protector and write with a wet-erase marker; dry-erase markers smudge more easily when you touch the page.</li>
<li><strong>Shift schedule:</strong> one letter per shift type – E, L, N – in the box, and a legend in the notes column.</li></ul>
<h2>Printing tips</h2>
<p>For a wall calendar, print all twelve months double-sided so each month has a blank back, or single-sided on 120 g/m² paper so ink does not show through. Use the paper size that is in your tray – an A4 calendar printed on US Letter loses its bottom row unless the printer shrinks it. Need the whole year on one sheet? Use the <a href="/yearly-calendar.html">yearly calendar</a>.</p>
""",
"faq": [("Does the calendar include holidays?", "No – holidays differ between countries and regions, so the day boxes are left free for you to fill in. US federal holidays for 2027 are listed in our 2027 calendar guide."),
        ("Which years can I create?", "Any year from 1900 to 2100. All dates are calculated with the Gregorian calendar."),
        ("Can I print a school year from August to July?", "Yes. Create the months one by one, changing the year when you reach January, and print them in order."),
        ("Why does my calendar show week 53?", "Some years have 53 ISO weeks. 2026 is one of them, so its last week continues into the first days of January 2027."),
        ("Why does February 2027 have only four rows?", "February 1, 2027 is a Monday and the month has 28 days, so with a Monday start it fills exactly four weeks. With a Sunday start, February 1 is the second column and the month spills into a fifth row."),
        ("Which accent color is best for a black-and-white printer?", "Ink or mono. The weekday bar is filled with the accent color behind white text, and dark accents keep that text readable when printed in grayscale."),
        ("How much can I write in a day box?", "On A4 or US Letter, two or three short entries in most months. Six-row months have the smallest boxes; if a month is busy, print it in portrait for taller boxes.")],
},
{
"slug": "yearly-calendar", "cat": "calendars", "name": "Yearly calendar", "accent": "sand",
"teaser": "All twelve months on one page – year at a glance.",
"title": "Printable Yearly Calendar 2027 – Year at a Glance on One Page",
"description": "Free printable year-at-a-glance calendar for 2027 or any year: all 12 months on one page, Monday or Sunday start, weekends shaded. A4, Letter or A5 PDF.",
"lead": "The whole year on a single sheet – perfect for planning vacations, deadlines and long-term goals.",
"guide": """
<h2>Why a year-at-a-glance page?</h2>
<p>Monthly and weekly planners are great for the details, but they hide the big picture. A one-page yearly calendar shows how many weeks are left until a deadline, which months are already crowded and where a vacation would fit best. It is also the quickest way to count: the number of school days in a term, the Fridays until a move, the weeks between two appointments. Pin it next to your desk or put it at the front of a binder. From October on, the generator suggests the coming year, so you can plan ahead.</p>
<h2>How to set it up</h2>
<ol><li>Enter the year. Any year from 1900 to 2100 works.</li>
<li>Choose Monday or Sunday as the first day of each week row.</li>
<li>Pick portrait or landscape. Portrait arranges the months in four rows of three, which suits binders; landscape uses three rows of four and fits a wall or noticeboard.</li>
<li>Keep weekend shading on to see weekends as stripes through the year, or switch it off for a cleaner look and more room for colored markings.</li>
<li>Choose an accent color for month names and weekend dates.</li></ol>
<h2>A filled example: planning vacation days</h2>
<p>Someone with 15 vacation days for 2027 prints the year in landscape. First, the public holidays from the employer's list are circled – in the US, our <a href="/printable-calendar-2027.html">2027 calendar guide</a> shows that Independence Day is observed on Monday, July 5, and Christmas on Friday, December 24. Next to those, bridge days become obvious: taking Tuesday to Friday of the same week as Monday, July 5 turns four vacation days into a nine-day break. The remaining days are shaded in two other blocks, and a running total is written in the corner: 4 + 5 + 6 = 15. The page stays at the front of the planner all year.</p>
<h2>Other ways to use it</h2>
<ul><li><strong>Year in pixels:</strong> give each day a color for mood, energy or sleep and look for patterns across months.</li>
<li><strong>Streak calendar:</strong> fill in each day you exercised, practiced an instrument or wrote – the year fills up visibly.</li>
<li><strong>Countdowns:</strong> highlight a wedding, exam or moving date and cross off the days.</li>
<li><strong>Shared custody or shift schedule:</strong> two colors show at a glance who is where.</li>
<li><strong>School year:</strong> shade term dates and breaks, then count the teaching weeks left before each exam.</li></ul>
<h2>Leap years</h2>
<p>February gets its 29th day automatically in leap years. A year is a leap year when it is divisible by 4, except for years divisible by 100 unless they are also divisible by 400. So 2027 has 365 days, 2028 is a leap year, and 2100 is not. If you print a calendar for 2028, February 29 falls on a Tuesday.</p>
<h2>How small are the days?</h2>
<p>Twelve months on one sheet leave little room per day. The generator sets the day numbers at up to 8 pt and shrinks them when the cells get smaller. The table shows the size of one day cell:</p>
<div class="table-wrap"><table><thead><tr><th>Page</th><th>Day cell</th><th>Day numbers</th></tr></thead><tbody>
<tr><td>A4 portrait / landscape</td><td>8.3 × 7.8 mm / 9.1 × 6.5 mm</td><td>8 pt</td></tr>
<tr><td>US Letter portrait / landscape</td><td>8.6 × 7.1 mm / 8.5 × 6.8 mm</td><td>8 pt</td></tr>
<tr><td>A5 portrait / landscape</td><td>5.6 × 4.4 mm / 6.2 × 3.4 mm</td><td>7.1 pt / 5.4 pt</td></tr>
<tr><td>Half Letter portrait / landscape</td><td>5.2 × 4.7 mm / 6.4 × 2.9 mm</td><td>7.5 pt / 4.7 pt</td></tr></tbody></table></div>
<p>On A5 and Half Letter, portrait is clearly the better choice: in landscape the numbers drop below 6 pt, which many people find hard to read. On A4 and Letter, a cell of about 7–8 mm takes a colored dot, a short stroke of a highlighter or a small round sticker of about 6 mm.</p>
<h2>Making a large wall planner</h2>
<p>Because the PDF is a vector file, it can be enlarged without blurring. A copy shop can print an A4 page on A3 at 141%, or a US Letter page on Tabloid (11 × 17 in) at about 129%; everything grows in proportion, and A3 cells become about 12 × 11 mm in portrait. Ask for the PDF to be printed at that exact scale rather than “fit to page”, so the margins stay even. On a home printer, the same result needs a poster or tiling option, which glues four sheets together – fiddly, but it works.</p>
<h2>Paper and pens</h2>
<p>Highlighters can smear fresh inkjet prints, so let the page dry for a few minutes or test on a corner first. For a planner you mark with dots and stickers all year, 160–200 g/m² card stock stays flat on a wall and survives repeated sticker removal. Fine-liners of 0.3 mm or less fit a short note into a cell; for anything longer, write the details on a <a href="/monthly-calendar.html">monthly calendar</a> and only a dot on the year page.</p>
<h2>Printing tips</h2>
<p>Day numbers on a one-page year are small, so this is the page where a sharp printer setting pays off: print at 100% rather than letting the printer shrink the page, and use the dark-gray default text. For a wall version, 120–176 g/m² paper keeps the sheet flat. For day-by-day planning, create a matching <a href="/monthly-calendar.html">monthly calendar</a> in the same accent color.</p>
""",
"faq": [("Can I print a calendar for a past year?", "Yes – enter any year between 1900 and 2100, for example to document a past year in a scrapbook."),
        ("Are weekends highlighted?", "Weekend dates appear in your accent color and can be shaded; switch the shading off in the settings if you prefer a cleaner look."),
        ("Does the yearly calendar show week numbers?", "No, there is no room for them on one page. Use the monthly calendar if you need ISO week numbers."),
        ("Is there space to write on it?", "Only small marks and colors fit into the day cells. For appointments with text, combine it with monthly or weekly pages."),
        ("How do I print it as a large wall planner?", "Print the PDF on A3 (from A4) at 141% or on Tabloid (from US Letter) at about 129%, at a copy shop or on a large-format printer. The vector PDF stays sharp at any size."),
        ("Which paper size is still easy to read?", "A4 and US Letter in either orientation, with 8 pt day numbers. On A5 and Half Letter, choose portrait; landscape makes the numbers very small."),
        ("Does the yearly calendar show holidays?", "No. Mark them yourself with a colored dot; the US federal holidays for 2027 are listed in our 2027 calendar guide.")],
},
# ------------------------------------------------------------------ PLANNERS
{
"slug": "weekly-planner", "cat": "planners", "name": "Weekly planner", "accent": "teal",
"teaser": "Seven days, notes and a to-do column – dated or undated.",
"title": "Printable Weekly Planner – Dated or Undated, Free PDF",
"description": "Create a free printable weekly planner: dated or undated, landscape or portrait, with to-do list, notes and writing lines. A4, Letter or A5 PDF.",
"lead": "Plan your week on one page: a box for every day, space for notes and a to-do list that keeps your priorities in view.",
"guide": """
<h2>Dated or undated?</h2>
<p>Enter a start date and every box is labeled with the weekday and date, and the header shows the date range – handy if you print week by week. The planner begins with whatever day you enter: choose a Monday for a Monday-to-Sunday week, or a Sunday if your week starts on Sunday. Leave the date empty to get an undated page running Monday to Sunday that you can print in bulk and use whenever you need it, without wasting pages on weeks you skip. The title at the top is yours to change, for example to “Week 11” or “Project launch”.</p>
<h2>What is on the page</h2>
<ul><li><strong>Seven day boxes and a Notes box:</strong> in landscape they sit in two rows of four, on A4 about 49 × 80 mm each with ten writing lines. In portrait they form four rows of two.</li>
<li><strong>To do this week:</strong> a 60 mm column with 22 check boxes in A4 landscape, or a strip along the bottom in portrait.</li>
<li><strong>Weekend tint:</strong> Saturday and Sunday are lightly shaded so the work week stands out.</li>
<li><strong>Writing lines:</strong> 6.5 mm apart; switch them off to draw time blocks or sketches.</li>
<li><strong>Title and accent color:</strong> the title replaces “Weekly plan”, and the accent color is used for the header line and day labels.</li></ul>
<h2>How to plan the week</h2>
<ol><li><strong>Look back (5 minutes):</strong> what got done last week, what moves forward?</li>
<li><strong>Fixed appointments first:</strong> meetings, classes and family commitments go into the day boxes.</li>
<li><strong>Collect tasks</strong> in the to-do column.</li>
<li><strong>Pick three priorities</strong> and give each a day – a task with a slot gets done far more often than a task on an open list.</li>
<li><strong>Leave buffer</strong> on every day for the unexpected.</li></ol>
<p>Our step-by-step guide <a href="/plan-a-week-on-paper.html">how to plan a week on paper</a> adds a simple capacity check in hours and a fully filled example.</p>
<h2>A filled example: a student's exam week</h2>
<p>A student prints a dated page for an exam week. Exams go into the day boxes first, in red: statistics on Tuesday at 9:00, history on Thursday at 13:00. Revision blocks follow, written as times with the topic (“Mon 14–17: statistics, chapters 4–6”). The to-do column holds the small things – return library books, print the formula sheet, book a bike repair – each with a check box. The Notes box holds room numbers and the professor's office hours. On Friday evening, every finished revision block is ticked, and two topics that did not get enough time go straight onto next week's page. Saturday is deliberately left almost empty: one line says “rest, groceries”.</p>
<h2>How much room each day gets</h2>
<div class="table-wrap"><table><thead><tr><th>Page</th><th>Day box (with to-do)</th><th>Writing lines</th><th>To-do lines</th></tr></thead><tbody>
<tr><td>US Letter landscape</td><td>44.6 × 82.5 mm</td><td>11</td><td>23</td></tr>
<tr><td>US Letter portrait</td><td>94.0 × 43.6 mm</td><td>5</td><td>4 long lines</td></tr>
<tr><td>A5 landscape</td><td>28.8 × 51.5 mm</td><td>6</td><td>14</td></tr>
<tr><td>Half Letter landscape</td><td>30.2 × 47.3 mm</td><td>5</td><td>13</td></tr>
<tr><td>A5 portrait</td><td>63.0 × 27.8 mm</td><td>2</td><td>4 long lines</td></tr></tbody></table></div>
<p>Without the to-do column, landscape boxes get wider (60.8 mm on US Letter) and portrait boxes taller, with up to seven lines. On A5 portrait, the to-do strip leaves only two lines per day, so either switch the to-do list off there or use landscape.</p>
<p>The writing lines inside the day boxes are 6.5 mm apart – slightly tighter than college ruling (about 7.1 mm) and a little wider than narrow ruling (6.35 mm). Most people can write one line of normal handwriting per line; if you write large, switch the lines off and use the box freely.</p>
<h2>More ways to use the page</h2>
<ul><li><strong>Hours log:</strong> freelancers write the hours per client in each day box and the weekly total into Notes, which makes invoicing quick at the end of the month.</li>
<li><strong>Lesson plan:</strong> teachers use one box per school day with the periods as lines; the eighth box holds materials to prepare.</li>
<li><strong>Shared household week:</strong> one page on the fridge, one color per person, and the to-do column for chores anyone can take.</li></ul>
<h2>Paper for a planner you write in daily</h2>
<p>Weekly pages are written, crossed out and carried around for seven days. 90–100 g/m² paper keeps gel pens from showing through and stands up to a ring binder better than thin copy paper. If you print double-sided in portrait, choose “flip on long edge” so the back page is the right way up.</p>
<h2>Printing tips</h2>
<p>Landscape fills a clipboard or desk best and gives each day the most writing lines; portrait fits ring binders, especially in A5 or Half Letter. Print several undated pages at once and keep them with your <a href="/monthly-calendar.html">monthly calendar</a>; add a <a href="/daily-planner.html">daily planner</a> for the busiest days. All three share the same accent colors, so a printed set looks consistent.</p>
""",
"faq": [("Can I print several weeks at once?", "Print the undated version as many times as you like, or create dated pages week by week by changing the start date."),
        ("Does the planner work in A5 binders?", "Yes – choose A5 or Half Letter. Portrait orientation usually works best for small binders."),
        ("Can the week start on Sunday?", "Yes. Enter a Sunday as the start date and the boxes run Sunday to Saturday with the correct dates. Undated pages start on Monday."),
        ("Can I remove the to-do list?", "Untick “To-do column” and the day boxes use the full width or height of the page."),
        ("What is the eighth box for?", "It is labeled Notes and holds everything that belongs to the week but not to a day: phone numbers, a shopping item, ideas or a quote for the week."),
        ("How many lines are in each day box?", "On A4 landscape ten, on US Letter landscape eleven, and fewer on small or portrait pages – see the table above. The lines are 6.5 mm apart."),
        ("Which setting gives the most writing room per day?", "US Letter or A4 in landscape with the to-do column switched off: each day box is then about 61–65 mm wide and 80 mm tall.")],
},
{
"slug": "daily-planner", "cat": "planners", "name": "Daily planner", "accent": "tomato",
"teaser": "Hour-by-hour schedule, top 3 priorities, to-dos and notes.",
"title": "Printable Daily Planner – Hourly Schedule & To-Do List (Free PDF)",
"description": "Free printable daily planner with hourly or half-hourly schedule, top 3 priorities, to-do list, notes, gratitude and water tracker. A4, Letter, A5 PDF.",
"lead": "Time-block your day: an hourly schedule on the left, priorities, to-dos and notes on the right.",
"guide": """
<h2>Time blocking in a nutshell</h2>
<p>A to-do list tells you <em>what</em> to do; a schedule tells you <em>when</em>. Time blocking combines both: you give your most important tasks a slot in the day, just like a meeting. It protects focused work, and it makes it obvious when a day is already full – if the schedule has no gap left, a new task has to replace something rather than squeeze in. This page puts the schedule on the left and everything else on the right, so you see both at once.</p>
<h2>What is on the page</h2>
<ul><li><strong>Schedule:</strong> one line per hour, or per half hour with dashed lines in between. On A4 with the default 6:00 to 21:00, each hour gets about 15 mm.</li>
<li><strong>Top 3 priorities:</strong> three numbered lines for the tasks that make the day a success.</li>
<li><strong>To do:</strong> a list with check boxes – 11 on A4 – for small tasks.</li>
<li><strong>Notes, “Grateful for” and a water tracker</strong> with eight glasses; both extras can be switched off.</li></ul>
<h2>How to fill in the page</h2>
<ol><li><strong>Write the three priorities first.</strong> If you only do these, the day was a success.</li>
<li><strong>Block appointments</strong> in the schedule, then give each priority its own block, ideally at the time of day when you concentrate best.</li>
<li><strong>Batch small tasks:</strong> collect emails, calls and errands in the to-do list and give them one or two blocks.</li>
<li><strong>Capture loose ends</strong> in Notes so they do not distract you.</li>
<li><strong>In the evening,</strong> tick what is done and move the rest deliberately to tomorrow.</li></ol>
<h2>A filled example: a working day with a deadline</h2>
<p>The page is dated for a Wednesday with a report due. Priorities: 1. finish the report draft, 2. send it to the team, 3. book the venue for next month. The schedule shows a 9:00 stand-up (30 minutes), the draft blocked from 9:30 to 12:00, lunch, a client call at 14:00, and “email + calls” from 15:00 to 15:45 for the to-do items. At 16:00 the report is sent, at 16:15 the venue is booked. The notes box holds a phone number from the call; the gratitude box says “quiet morning to write”.</p>
<h2>Adjust the schedule to your day</h2>
<p>Early riser? Start the schedule as early as 4:00. Night owl? Run it until midnight. The planner divides the available height evenly, so a shorter day gets more room per hour: 8:00 to 18:00 on A4 gives about 22 mm per hour, enough for two lines of text in each slot. Half-hour slots suit days full of short appointments, such as a clinic shift or a day of back-to-back calls.</p>
<h2>Space per hour on every paper size</h2>
<div class="table-wrap"><table><thead><tr><th>Page</th><th>6:00–21:00</th><th>8:00–18:00</th><th>To-do lines</th></tr></thead><tbody>
<tr><td>A4</td><td>15.2 mm</td><td>22.1 mm</td><td>11</td></tr>
<tr><td>US Letter</td><td>14.1 mm</td><td>20.5 mm</td><td>10</td></tr>
<tr><td>A5</td><td>10.1 mm</td><td>14.7 mm</td><td>7</td></tr>
<tr><td>Half Letter</td><td>10.5 mm</td><td>15.3 mm</td><td>7</td></tr></tbody></table></div>
<p>With half-hour slots, each half hour gets half of that – about 7.8 mm on A4 for 6:00 to 21:00, enough for one short line. Full hours are marked by a solid line with the time; half hours by a thinner dashed line, so the hours stay easy to find in a busy schedule. A handwritten line needs roughly 6–7 mm, so on A5 and Half Letter shorten the schedule to the hours you really use if you want two lines per hour.</p>
<h2>Schedules that do not fit the default</h2>
<p>The schedule can start at any full hour from 4:00 to 16:00 and end at any full hour from 13:00 to 24:00. A night shift that runs past midnight therefore does not fit in one block. Two practical options: plan the evening part on today's page and the early hours on tomorrow's, or choose a schedule from 13:00 to 24:00 and write the hours after midnight into the notes area.</p>
<h2>Paper and pens</h2>
<p>A daily page is used intensively for one day and then usually filed or thrown away, so everyday 80 g/m² paper is enough for most people. If you color your time blocks with highlighters, test the highlighter on a printed page first – some smear fresh inkjet ink – and let the print dry for a minute. Erasable gel pens work well for schedules that change during the day.</p>
<h2>Printing tips</h2>
<p>The page is always portrait. A5 or Half Letter turns it into a pocket-sized day card, though the hours get tighter, so shorten the schedule to the hours you really need. Print a small stack of undated pages for normal days and a dated one for special days such as a move, a trip or an exam. Plan the week first with the <a href="/weekly-planner.html">weekly planner</a>, then use this page only on days that need hour-by-hour detail.</p>
""",
"faq": [("Can I make the schedule start earlier?", "Yes – choose any start hour from 4:00 and any end hour up to 24:00."),
        ("Is there a version without the water tracker?", "Untick “Water tracker” and “Gratitude & reflection” and the notes area grows automatically."),
        ("Should I fill in every hour?", "No. Block appointments and priorities, and leave the rest open. A schedule packed from start to finish usually breaks by lunchtime."),
        ("Does the water tracker set a target?", "It has eight glasses to tick as a simple visual reminder. It is not a medical recommendation; how much you need depends on you."),
        ("Can I plan a night shift that crosses midnight?", "Not in one schedule block: it ends at 24:00 at the latest. Use two pages, or a 13:00–24:00 schedule plus the notes area for the hours after midnight."),
        ("Why are some lines in the schedule dashed?", "With half-hour slots switched on, the half hours are thinner dashed lines and the full hours solid lines with the time, so you can find the hours at a glance."),
        ("How many to-do lines are there?", "Eleven on A4, ten on US Letter and seven on A5 or Half Letter, each with a check box.")],
},
# ------------------------------------------------------------------ TRACKERS & LISTS
{
"slug": "habit-tracker", "cat": "trackers", "name": "Habit tracker", "accent": "olive",
"teaser": "Your habits, every day of the month – tick and keep the streak.",
"title": "Printable Habit Tracker – Monthly, Customizable (Free PDF)",
"description": "Free printable monthly habit tracker: type your own habits, choose month and year, download one month or a whole year as PDF. A4, Letter, A5.",
"lead": "Type your habits, pick the month and fill in a circle every day you keep your promise to yourself.",
"guide": """
<h2>Why tracking works</h2>
<p>A habit tracker makes progress visible. Every filled circle is a small reward, and an unbroken row – a streak – becomes something you do not want to break. Ticking also forces a short daily check: did I do it today? On paper that check happens where you can see it, on the fridge or in your planner, instead of behind an app icon. This template prints your own habit names down the left side, one circle for every day of the month, the weekday initial above each date, and a “Done” box at the end of every row for the monthly count.</p>
<h2>How to set it up</h2>
<ol><li>Type your habits into the box, one per line – up to 15. Names longer than about 32 characters are shortened, so keep them crisp.</li>
<li>Add a few empty rows (up to 10) for habits you may start mid-month. The page holds 24 rows at most.</li>
<li>Choose the month, or <em>All 12 months</em> to get a 12-page PDF with your habits printed on every page.</li>
<li>Pick the paper size, landscape or portrait, an accent color and the title style.</li></ol>
<p>Landscape gives the 28–31 day columns more width and is the better choice for most people; portrait suits a narrow spot on a door or a binder.</p>
<h2>Write habits you can tick</h2>
<p>A row only works if the answer each evening is a clear yes or no. “Read more” never gets a tick; “Read 10 pages” does. Add the trigger in brackets if it helps – “Stretch (after coffee)”. Our article <a href="/habit-tracker-ideas.html">habit tracker ideas that actually stick</a> has a table of vague goals rewritten as trackable rows, and explains why research does not support the popular “21 days” rule: in the best-known study, forming a habit took a median of 66 days.</p>
<h2>A filled example: January with five habits</h2>
<p>A tracker for January 2027 lists: Read 10 pages, Walk 20 minutes, Phone in kitchen by 10 pm, Spanish lesson, Floss – plus three empty rows. Each evening the owner fills in the circles while setting the alarm. By the end of the month, the “Read” row has 25 filled circles out of 31, “Walk” has 17, and the gaps in the walking row cluster on Saturdays and Sundays. The “Done” boxes get the numbers, and a note at the bottom of the page records the decision for February: arrange the weekend walks with a friend, keep the rest.</p>
<h2>Tips for a tracker that sticks</h2>
<ul><li><strong>Start small:</strong> three to five habits are plenty. Too many rows turn the tracker into a guilt list.</li>
<li><strong>Tick at a fixed time:</strong> filling in a week from memory makes the page unreliable.</li>
<li><strong>Never miss twice:</strong> one missed day is normal; two in a row is the start of a new pattern.</li>
<li><strong>Review monthly:</strong> use the “Done” column to decide what to keep, change or drop.</li></ul>
<h2>Row height and circle size</h2>
<p>Each habit row is up to 10 mm tall; with many rows the generator shrinks them so that everything fits on one page. The circles scale with the space for each day:</p>
<div class="table-wrap"><table><thead><tr><th>Page (31-day month)</th><th>Circle diameter</th><th>Row height with 24 rows</th></tr></thead><tbody>
<tr><td>A4 landscape</td><td>about 3.9 mm</td><td>6.4 mm</td></tr>
<tr><td>US Letter landscape</td><td>about 3.5 mm</td><td>6.6 mm</td></tr>
<tr><td>A4 portrait</td><td>about 2.3 mm</td><td>10 mm</td></tr>
<tr><td>A5 or Half Letter landscape</td><td>about 2.4 mm</td><td>3.7–4.0 mm</td></tr></tbody></table></div>
<p>Shorter months get slightly larger circles; February on A4 landscape has circles of about 4.3 mm. The numbers explain the advice to use landscape: in portrait the circles are barely larger than a pen tip. On A5 and Half Letter, keep the list to about ten rows, so the rows stay tall enough to read the habit names.</p>
<h2>Ways to fill the circles</h2>
<ul><li><strong>Full or half:</strong> fill the circle when you did the habit completely and only half of it for a reduced version – ten minutes of reading instead of thirty still counts as showing up.</li>
<li><strong>Dot for a planned rest day:</strong> a small dot in the middle marks a day you deliberately skipped, so the gap does not look like a failure when you review the month.</li>
<li><strong>Two colors:</strong> one color for weekdays and another for weekends makes patterns easier to see.</li></ul>
<h2>Other uses for the grid</h2>
<p>The layout is simply names down the side and one circle per day, so it works for more than personal habits. As a <strong>chore chart</strong>, each row is one child and one chore, such as “Mia – set the table”. In a <strong>classroom</strong>, each row is a student and a circle is filled when the reading log comes back. For <strong>plant care</strong>, each row is a plant and a filled circle means watered. The “Done” box then gives the monthly count for each row.</p>
<h2>Paper and printing</h2>
<p>A tracker hangs in one place for a whole month and gets touched every day. 120 g/m² paper stays flat on a fridge or door and does not crease when you pin it up. The circles are outlined in a light gray, so they print clearly in grayscale and on any home printer.</p>
<h2>Printing tips</h2>
<p>Print the whole year in one go and keep the sheets in a folder next to the current page, so a new month is always ready. The circles are drawn in a light gray outline, so any pen color shows; a highlighter fills them quickly. For a yearly view, color one habit day by day on a <a href="/yearly-calendar.html">yearly calendar</a>.</p>
""",
"faq": [("How many habits can I track?", "Up to 15 named habits plus empty rows, 24 rows at most – but most people do best with three to seven."),
        ("Can I track habits weekly instead of daily?", "Use the checklist template with numbered lines for weekly goals, or mark only certain days on the monthly tracker."),
        ("Why does the tracker show weekday letters?", "They help you spot patterns, such as habits that are always missed on weekends or on one particular weekday."),
        ("Can I track numbers, like hours of sleep?", "Yes – write the number inside the circle instead of filling it in. Keep such rows to one or two, as they take longer to fill in."),
        ("How big are the circles?", "About 3.9 mm on A4 landscape and 3.5 mm on US Letter landscape in a 31-day month. In portrait they shrink to about 2.3 mm, which is why landscape is the better choice for most people."),
        ("Can I use it as a chore chart for several children?", "Yes. Type one line per child and chore, such as “Ben – feed the cat”. Each row gets its own circles and its own “Done” count for the month."),
        ("Does the tracker follow a Monday or Sunday week?", "Neither: the columns are simply the days of the month from 1 to 28–31. The weekday letter above each date shows where the weekends fall.")],
},
{
"slug": "checklist", "cat": "trackers", "name": "Checklist & to-do list", "accent": "ink",
"teaser": "Squares, circles or numbers – pre-fill items if you like.",
"title": "Printable Checklist & To-Do List Maker – Free PDF",
"description": "Make a free printable checklist or to-do list: your title, 5–60 lines, one or two columns, square or round boxes or numbers, optional pre-filled items. PDF.",
"lead": "From packing lists to project steps: give your list a title, choose the layout and pre-fill items if you want.",
"guide": """
<h2>A checklist for every occasion</h2>
<p>Checklists are one of the simplest tools for doing things reliably. Aviation and hospitals use them so that routine steps are not skipped under pressure; at home they stop you from leaving the charger behind or forgetting to cancel the newspaper before a move. The value of a printed list is that it is complete before you start and visible while you work – you do not need to remember what is next, only to tick what is done. This generator makes one page with your title, 5 to 60 lines in one or two columns, and an optional priority mark on every line.</p>
<h2>How to build your list</h2>
<ol><li>Give it a title, such as “Camping trip” or “Move – week before”.</li>
<li>Choose the number of lines. Fewer lines get more space: 25 lines on A4 are about 10 mm apart; 60 lines in two columns about 8 mm.</li>
<li>Pick square boxes, round boxes or numbers.</li>
<li>Optionally type items into the box, one per line, and they are printed on the lines – up to about 60 characters each.</li>
<li>Tick “Priority column” to add three small dots at the end of each line; fill one, two or three to rank items.</li></ol>
<h2>Squares, circles or numbers?</h2>
<p>Squares are the classic tick box and the easiest to see from a distance. Circles look softer and match bullet-journal pages. Numbered lines suit step-by-step instructions and ranked lists, where the order matters – a recipe, a setup procedure or your top ten books of the year.</p>
<h2>A filled example: a packing list you reuse</h2>
<p>A family types its standard packing list once: passports, chargers, medication, toothbrushes, swimwear, rain jackets, snacks for the car, and so on – 34 items. With two columns and 40 lines, the page has six empty lines at the end for trip-specific items. Before each trip they print a fresh copy, add “ski gloves” or “beach tent” by hand, and tick items as they go into the bags. Because the settings are remembered in the browser (or saved as a share link), next year's list is ready in seconds.</p>
<h2>More ideas</h2>
<ul><li><strong>Moving checklist:</strong> utilities, address changes, keys, meter readings.</li>
<li><strong>Cleaning routine:</strong> a numbered list of weekly tasks in the order you do them.</li>
<li><strong>Shopping list:</strong> pre-fill the items you buy every week; the meal planner has a category list for the rest.</li>
<li><strong>Project steps:</strong> renovations, events or launches, one action per line.</li></ul>
<h2>Write better list items</h2>
<p>Start each item with a verb – “Call the plumber”, not “Plumber”. Split anything that takes more than an hour into steps. Keep a single list per purpose instead of one endless list, and print a fresh one when more than half is ticked.</p>
<h2>Line spacing on each paper size</h2>
<div class="table-wrap"><table><thead><tr><th>Page</th><th>25 lines, one column</th><th>60 lines, two columns</th><th>Column width (two columns)</th></tr></thead><tbody>
<tr><td>A4</td><td>9.8 mm</td><td>8.2 mm</td><td>89 mm</td></tr>
<tr><td>US Letter</td><td>9.1 mm</td><td>7.6 mm</td><td>92 mm</td></tr>
<tr><td>A5</td><td>6.6 mm</td><td>5.5 mm</td><td>61 mm</td></tr>
<tr><td>Half Letter</td><td>6.8 mm</td><td>5.7 mm</td><td>57 mm</td></tr></tbody></table></div>
<p>The spacing never exceeds 10 mm, so short lists do not stretch over the whole page. On A5 and Half Letter, 25 or more lines end up between 5.5 and 7 mm apart – fine for a shopping list, tight for longer items. For pre-filled items in two columns, keep each item to roughly 50 characters on A4 or Letter and about 30 on A5; longer items run into the next column.</p>
<h2>Read-do or do-confirm?</h2>
<p>Checklists used in aviation and surgery come in two types, a distinction popularized by the surgeon Atul Gawande in <em>The Checklist Manifesto</em>. A <strong>read-do</strong> list is followed step by step as you work, like a recipe or a setup procedure – the numbered style fits it best. A <strong>do-confirm</strong> list is checked after you have done the work from memory, like a packing list you run through before leaving the house – square boxes fit it best. Gawande recommends keeping each checklist short, at about five to nine items per pause point, and concentrating on the steps that are most often missed rather than listing everything.</p>
<h2>Paper for lists that get handled</h2>
<p>A list that lives in a bag or on a clipboard needs more than copy paper: 120 g/m² or more does not wrinkle as quickly. For a reusable list in a sheet protector, print on 160–200 g/m² card stock so it stays stiff, and tick the boxes with a wet-erase marker. A list printed in grayscale loses nothing, because the boxes and lines are gray anyway.</p>
<h2>Printing tips</h2>
<p>The page is always portrait. For lists you laminate and reuse with a dry-erase marker, choose large spacing and bold square boxes, and print on heavier paper before laminating. A5 and Half Letter make handy pocket lists for shopping. For a weekly to-do list tied to dates, use the <a href="/weekly-planner.html">weekly planner</a>; for daily routines tracked over a month, the <a href="/habit-tracker.html">habit tracker</a>.</p>
""",
"faq": [("How many items fit on one page?", "Up to 60 lines in two columns. With fewer lines, the spacing grows so the page still looks balanced."),
        ("Can I save my pre-filled list?", "Your last settings are remembered in this browser. You can also copy a share link that contains your list."),
        ("Can I print a list with two columns of different topics?", "Choose two columns and pre-fill the items in order: the first half of your lines fills the left column, the rest the right column. Leave empty lines to separate topics."),
        ("Can I make a numbered list without check boxes?", "Yes. Choose “Numbered” as the checkbox style and every line gets a number instead of a box."),
        ("Do long pre-filled items fit in two columns?", "Roughly 50 characters fit in a column on A4 or US Letter and about 30 on A5. Longer items run into the next column, so shorten them or use one column."),
        ("Which checkbox style should I use for step-by-step instructions?", "Numbered. When the order matters – a recipe, a setup, a closing routine – numbers make it easy to see where you stopped.")],
},
{
"slug": "meal-planner", "cat": "planners", "name": "Meal planner", "accent": "olive",
"teaser": "Weekly meals plus a grocery list sorted by aisle.",
"title": "Printable Weekly Meal Planner with Grocery List (Free PDF)",
"description": "Free printable weekly meal planner with breakfast, lunch, dinner and snacks plus a grocery list by category. Dated or undated, A4/Letter PDF.",
"lead": "Plan the week's meals in one grid and write the shopping list right next to it – sorted by category so you shop faster.",
"guide": """
<h2>Why plan meals?</h2>
<p>Deciding what to eat every evening takes surprising energy, and the decision usually comes when everyone is already hungry. Planning the week in one go means one main shopping trip, less food thrown away and fewer last-minute takeaways. It also lets you use leftovers on purpose instead of rediscovering them at the back of the fridge. This template puts the whole week on a single sheet: a grid with seven day columns and one row per meal, and a grocery list sorted into five groups right next to it.</p>
<h2>How to set it up</h2>
<ol><li>Choose the meals: breakfast, lunch and dinner; all three plus snacks; lunch and dinner; or dinner only. Fewer rows give taller cells – on A4 landscape, three meals give cells of about 27 × 52 mm.</li>
<li>Choose Monday or Sunday as the first day.</li>
<li>Optionally enter a start date. Pick a date that falls on your first day of the week, so names and dates line up.</li>
<li>Keep the grocery list on, or switch it off to give the meal grid the whole page – useful if you shop online and keep the list in an app.</li>
<li>Landscape puts the list in a column on the right; portrait moves it to a strip along the bottom.</li></ol>
<h2>A quick weekly routine</h2>
<p>Look at the calendar first and mark the busy evenings for quick meals or leftovers. Then check the fridge and plan the first days around what needs using up. Fill the dinner row, then breakfasts and lunches, and finally write everything you are missing into the grocery list. Our guide <a href="/meal-planning-one-page.html">meal planning on one page</a> breaks this into a timed 20-minute routine and includes the USDA guidance that cooked leftovers should be eaten within three to four days.</p>
<h2>A filled example: dinners only</h2>
<p>A couple who both work late plans dinners only, so each cell is tall enough for a recipe name and a page number. Monday: chili, double batch. Tuesday: chili with rice – arrow from Monday. Wednesday: stir-fry with the vegetables bought on Saturday. Thursday: “quick” – pasta with pesto. Friday: pizza night, homemade dough started Thursday. Saturday: eat out. Sunday: roast vegetables and fish. The grocery list reads: <em>Produce</em> peppers, onions, broccoli, carrots, basil; <em>Protein</em> ground beef, kidney beans, salmon; <em>Dairy</em> mozzarella, parmesan; <em>Pantry</em> rice, pasta, flour, canned tomatoes, yeast; <em>Other</em> baking paper.</p>
<h2>Grocery list by category</h2>
<p>The five groups – produce, protein, dairy, pantry and other – follow roughly the way many supermarkets are laid out. Writing each item into its group as you plan saves walking back and forth in the store, and an empty group tells you at a glance that you have, for example, planned no vegetables yet. If you shop at two stores, mark the items for the second store with a small letter in front.</p>
<h2>Cell sizes for each layout</h2>
<div class="table-wrap"><table><thead><tr><th>Page (landscape, with grocery list)</th><th>3 meals</th><th>4 meals</th><th>2 meals</th><th>Dinner only</th></tr></thead><tbody>
<tr><td>US Letter</td><td>24.3 × 54.0 mm</td><td>24.3 × 40.5 mm</td><td>24.3 × 81.0 mm</td><td>24.3 × 161.9 mm</td></tr>
<tr><td>A5</td><td>15.3 × 33.3 mm</td><td>15.3 × 25.0 mm</td><td>15.3 × 50.0 mm</td><td>15.3 × 100 mm</td></tr></tbody></table></div>
<p>Without the grocery list, the day columns get wider: 33.9 mm on US Letter, 36.4 mm on A4 and 24.9 mm on A5. A column of 15 mm on A5 holds only a word or two per line, so on small paper either switch the list off or plan dinners only.</p>
<p>The grocery list itself has room for 20 items on A4 landscape (four per group), 25 on US Letter landscape (five per group) and 30 in portrait, where the five groups sit side by side along the bottom of the page. On A5 landscape there are only two lines per group – enough for a top-up shop, not for the big weekly one.</p>
<h2>A four-week rotation</h2>
<p>Many households eat a limited set of dinners anyway. Fill in four meal plans once, number them 1 to 4 in the title – “Meal plan 1”, “Meal plan 2” – and print them again whenever the cycle comes round. After a month, cross out the meals nobody liked and replace them. Because the grocery list is on the same page, each rotation week comes with its shopping list already written.</p>
<h2>Paper and printing</h2>
<p>A meal plan on the fridge gets splashed and touched for a week; 100–120 g/m² paper holds up better under a magnet than thin copy paper. To reuse a basic plan, put it in a sheet protector and write the changing parts with a wet-erase marker. In grayscale the colored day headers turn gray with white lettering, so choose a dark accent such as ink or mono if you print in black and white.</p>
<h2>Printing tips</h2>
<p>A printed plan on the fridge answers the daily “What's for dinner?” question for the whole household; landscape works best there. Portrait suits binders, where you can keep past weeks as a library of meals that worked. If you track food spending, carry the receipt total over to the groceries line of the <a href="/budget-planner.html">budget planner</a>.</p>
""",
"faq": [("Can I start the week on Sunday?", "Yes – switch “Week starts on” to Sunday. Enter a start date to have the dates printed above each day."),
        ("Is there a version without the grocery list?", "Untick “Grocery list” and the meal grid uses the full page."),
        ("Can I plan two weeks on one page?", "Not on one page, but you can print two copies and enter the start dates of consecutive weeks."),
        ("Where do recipes go?", "Write the recipe name and where to find it – a cookbook page or a website name – in the cell. Dinner-only plans leave the most room."),
        ("How many grocery items fit on the list?", "Twenty on A4 landscape, 25 on US Letter landscape, 30 in portrait and ten on A5 or Half Letter landscape, spread across the five groups."),
        ("Which layout works for an A5 planner?", "Dinner only, or switch the grocery list off. With three meals and the list, each day column on A5 is only about 15 mm wide."),
        ("Can I reuse the same plan every month?", "Yes. Fill in up to four plans with titles like “Meal plan 1”, keep them as a rotation and print them again when the cycle comes round.")],
},
{
"slug": "budget-planner", "cat": "trackers", "name": "Budget planner", "accent": "sand",
"teaser": "Planned vs actual for income and every expense category.",
"title": "Printable Monthly Budget Planner – Planned vs Actual (Free PDF)",
"description": "Free printable monthly budget planner: income and your own expense categories with planned, actual and difference columns, summary boxes and notes. PDF.",
"lead": "Write down what you plan to spend, track what you actually spent and see the difference at a glance – with your own categories.",
"guide": """
<h2>How the budget page works</h2>
<p>Each row has three columns: <strong>Planned</strong> (what you expect or allow), <strong>Actual</strong> (what really happened) and <strong>Difference</strong>. At the end of the month, the differences show where your money went differently than planned – the starting point for next month's budget. Above the tables, four summary boxes hold the month's totals: Income, Expenses, Saved and Left over. The income table has rows for salary, side income, other income and a total; the expense table lists your own categories, followed by a total line and a box for notes and goals.</p>
<h2>How to set it up</h2>
<ol><li>Choose the month, or <em>All 12 months</em> for a 12-page budget binder with your categories on every page.</li>
<li>Pick the currency symbol for the summary boxes: $, €, £ or none.</li>
<li>Edit the expense categories, one per line – up to 18. The default list starts with rent or mortgage, utilities and groceries and ends with savings and other.</li>
<li>Change the title if you like, for example to a household name.</li></ol>
<p>With 13 categories on A4, each expense row is about 10 mm high; with 18 it shrinks to about 8 mm, still enough for handwritten amounts.</p>
<h2>Setting up your categories</h2>
<p>Start with fixed costs – rent, utilities, insurance, phone, subscriptions – and then variable spending such as groceries, transport, eating out and shopping. Keep savings as a category of its own, so paying yourself first is a visible line. Irregular costs like car repairs or gifts are easier when you divide the yearly amount by twelve and plan that amount every month.</p>
<h2>A filled example: one month</h2>
<p>A household plans $4,200 of income and fills in: rent $1,450 planned and actual; groceries $600 planned, $655 actual (difference −$55); eating out $150 planned, $90 actual (+$60); transport $220 planned, $240 actual (−$20); savings $500 planned and actual. At the end of the month the Expenses box reads $3,980 against $4,000 planned, and Left over shows $220. The note under “Notes &amp; goals” says: “Groceries over twice in a row – raise to $640, lower eating out to $110.” The example is made up to show the method; your categories and numbers will be different.</p>
<h2>A popular rule of thumb: 50/30/20</h2>
<p>One widely used guideline splits take-home pay into about 50% for needs, 30% for wants and 20% for savings and paying off debt. It is a starting point, not a rule: in expensive cities housing alone can take half of the income. The point is to choose your split consciously and write it into the Planned column.</p>
<h2>Tips for sticking with it</h2>
<ul><li><strong>Update weekly:</strong> ten minutes with your bank statement on a fixed day is easier than reconstructing a whole month.</li>
<li><strong>Round to whole amounts:</strong> trends matter more than cents.</li>
<li><strong>Review, don't judge:</strong> an overspent category is information for next month.</li></ul>
<h2>How many categories fit?</h2>
<div class="table-wrap"><table><thead><tr><th>Page</th><th>8 categories</th><th>13 categories</th><th>18 categories</th></tr></thead><tbody>
<tr><td>A4</td><td>16.4 mm</td><td>10.6 mm</td><td>7.8 mm</td></tr>
<tr><td>US Letter</td><td>14.5 mm</td><td>9.3 mm</td><td>6.9 mm</td></tr>
<tr><td>A5</td><td>7.4 mm</td><td>4.8 mm</td><td>3.5 mm</td></tr>
<tr><td>Half Letter</td><td>8.1 mm</td><td>5.2 mm</td><td>3.8 mm</td></tr></tbody></table></div>
<p>The values are the height of one expense row. Handwritten amounts need about 6 mm, so on A5 and Half Letter keep the list to about eight categories – group small ones, for example “Phone, internet & subscriptions”. On A4 and US Letter the full 18 categories still work.</p>
<h2>Which way round is the difference?</h2>
<p>The page leaves the sign to you, so decide once and write it into the notes. A common convention is <strong>planned minus actual</strong> for expenses, so a positive difference means you stayed under budget – as in the example above, where groceries came out at −$55. For income it is the other way round, <strong>actual minus planned</strong>, so a positive number is again good news. With that rule every plus is a reason to smile and every minus a line to look at.</p>
<h2>Zero-based planning and irregular income</h2>
<p>In <strong>zero-based budgeting</strong>, you fill the Planned column until planned expenses, including savings, equal your planned income – every dollar gets a job before the month starts. If your income varies, plan with the income of a lean month and treat anything above it as extra: write it into “Other” in the income table and decide in the notes where it goes, for instance into savings or a fund for irregular bills.</p>
<h2>Paper and pens</h2>
<p>Write the Planned column in pencil if you expect to adjust it mid-month, and the Actual column in pen. Everyday 80 g/m² paper is enough for a page you update weekly; a year of pages fits in a slim binder behind a <a href="/yearly-calendar.html">yearly calendar</a> on which you mark paydays and due dates.</p>
<h2>Printing tips</h2>
<p>The page is always portrait and works on A4, US Letter, A5 or Half Letter; the larger sizes leave more room for amounts. Print a year at once and file each month behind the last, so you can compare the same category across months.</p>
<p class="small muted">The planner is an organizing tool and not financial advice.</p>
""",
"faq": [("Can I use a different currency?", "Choose $, €, £ or no symbol. The summary boxes show the symbol; amounts in the table are written by hand."),
        ("Can I print a whole year?", "Choose “All 12 months” for a 12-page budget binder with your categories on every page."),
        ("Can I rename the income rows?", "The income rows are fixed (salary, side income, other, total), but you can cross one out and write your own label; the expense categories are fully editable."),
        ("What goes into “Saved” and “Left over”?", "Saved is what you moved to savings this month (it also appears as a category). Left over is total income minus total expenses, savings included – money still available or carried into next month."),
        ("How many categories fit on A5?", "About eight, if you want rows tall enough for handwritten amounts. With 13 categories, A5 rows shrink to about 5 mm."),
        ("Should the difference be positive or negative?", "That is up to you. A common rule is planned minus actual for expenses and actual minus planned for income, so a positive difference is always the good direction.")],
},
]

BY = {t["slug"]: t for t in TOOLS}
