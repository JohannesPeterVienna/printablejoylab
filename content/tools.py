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
<h2>Printing tips</h2>
<p>The lines run all the way across the sheet; your printer simply leaves its own unprintable border white, so nothing important is lost. Keep the print scale at 100% so the spacing stays exactly as chosen – our <a href="/print-at-actual-size.html">guide to printing at actual size</a> shows where that setting hides. Lined paper has no front or back, so for a notebook you can print the same page on both sides of each sheet. For fountain pens, 90–100 g/m² paper reduces show-through; see <a href="/choose-the-right-paper.html">which paper for which job</a> for weights in pounds and gsm.</p>
""",
"faq": [("Is college ruled the same as 7 mm lines?", "Almost: college ruling is 9/32 inch, which is 7.14 mm. For most purposes the difference to 7 mm is invisible."),
        ("How do I make handwriting practice sheets?", "Choose wide ruling or a custom spacing of 10–12 mm, switch the header on for the child's name, and use the medium line color so the lines stay visible."),
        ("Why does the margin line go from top to bottom?", "It marks a full-height column, as in classic exercise paper. If you do not need it, untick “Red margin line” and the lines run uninterrupted."),
        ("Can I use the paper commercially?", "You may print and use the pages for yourself, your family, your classroom or your own business. Please do not resell the files or offer them for download elsewhere.")],
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
<h2>Printing tips</h2>
<p>Scale matters more for graph paper than for any other template: if the printer shrinks the page to fit its margins, a 5 mm grid becomes about 4.8 mm and scale drawings drift. Print at 100% and check ten squares with a ruler. For engineering-style sheets, pick the light line color; for photocopying, medium or dark.</p>
""",
"faq": [("How many squares fit on an A4 page?", "With a 5 mm grid and our 12 mm margins, the page holds 37 squares across and 53 down in portrait orientation."),
        ("What is engineering paper?", "Engineering paper is usually a light green 1/5 inch grid printed on the back so it shows through faintly. Choose the 1/5 inch grid and the light line color for a similar look."),
        ("Which grid is best for algebra and geometry homework?", "A 5 mm or 1/4 inch grid. It is fine enough to fit a whole graph on half a page and large enough to write numbers inside the squares."),
        ("Can I get a grid with an exact number of squares?", "Choose a custom grid size in half-millimeter steps. The preview redraws instantly, so you can count the squares along an edge before you print.")],
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
<h2>Printing tips</h2>
<p>To make an A5 booklet, print A5 pages directly, or print A4 pages and cut them in half. Heavier 100–120 g/m² paper reduces ghosting with markers. Keep the scale at 100% so the 5 mm dots really are 5 mm apart – otherwise pages printed on different days will not line up in a binder.</p>
""",
"faq": [("What size dots do bullet journals use?", "Most dotted notebooks use a 5 mm grid. That is our default setting."),
        ("Will the dots show when I scan my notes?", "Light, fine dots usually disappear or turn very faint in scans – one reason dot grid is popular for notes you want to digitize."),
        ("Which dot size works with watercolor or brush pens?", "Fine dots in the light color. They are easy to see while you plan the layout and almost invisible once the page is painted or lettered."),
        ("Can I print dots on both sides?", "Yes. The grid is centered on the page, so on most printers the dots on the front and back line up closely.")],
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
<h2>Choosing the triangle size and printing</h2>
<p>4–5 mm triangles give lots of detail for small objects; 7 mm or 1 cm triangles are easier to see and suit classroom use, children and large maps. Print at 100% so the 60° angles and the scale stay exact – a page shrunk to fit a different paper size distorts nothing visibly but makes measured drawings slightly off. A light line color keeps your pencil lines readable; use medium if you plan to photocopy the sheet.</p>
""",
"faq": [("Is isometric the same as perspective drawing?", "No. In perspective drawing, parallel lines meet in a vanishing point. In isometric drawing they stay parallel, so measurements along each axis remain to scale."),
        ("Can I use the grid for hex maps?", "Yes – groups of six triangles form hexagons, so isometric paper works for simple hex maps too."),
        ("Which triangle size should children use?", "1 cm triangles. They are large enough to count easily and to color in, and simple cube buildings stay clearly readable."),
        ("Why do circles look like ovals on isometric drawings?", "A circle on the face of a cube is seen at an angle, so in isometric view it becomes an ellipse. Sketch it inside a rhombus of grid lines and round the corners.")],
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
<h2>Printing tips</h2>
<p>For a wall calendar, print all twelve months double-sided so each month has a blank back, or single-sided on 120 g/m² paper so ink does not show through. Use the paper size that is in your tray – an A4 calendar printed on US Letter loses its bottom row unless the printer shrinks it. Need the whole year on one sheet? Use the <a href="/yearly-calendar.html">yearly calendar</a>.</p>
""",
"faq": [("Does the calendar include holidays?", "No – holidays differ between countries and regions, so the day boxes are left free for you to fill in. US federal holidays for 2027 are listed in our 2027 calendar guide."),
        ("Which years can I create?", "Any year from 1900 to 2100. All dates are calculated with the Gregorian calendar."),
        ("Can I print a school year from August to July?", "Yes. Create the months one by one, changing the year when you reach January, and print them in order."),
        ("Why does my calendar show week 53?", "Some years have 53 ISO weeks. 2026 is one of them, so its last week continues into the first days of January 2027.")],
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
<h2>Printing tips</h2>
<p>Day numbers on a one-page year are small, so this is the page where a sharp printer setting pays off: print at 100% rather than letting the printer shrink the page, and use the dark-gray default text. For a wall version, 120–176 g/m² paper keeps the sheet flat. For day-by-day planning, create a matching <a href="/monthly-calendar.html">monthly calendar</a> in the same accent color.</p>
""",
"faq": [("Can I print a calendar for a past year?", "Yes – enter any year between 1900 and 2100, for example to document a past year in a scrapbook."),
        ("Are weekends highlighted?", "Weekend dates appear in your accent color and can be shaded; switch the shading off in the settings if you prefer a cleaner look."),
        ("Does the yearly calendar show week numbers?", "No, there is no room for them on one page. Use the monthly calendar if you need ISO week numbers."),
        ("Is there space to write on it?", "Only small marks and colors fit into the day cells. For appointments with text, combine it with monthly or weekly pages.")],
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
<h2>Printing tips</h2>
<p>Landscape fills a clipboard or desk best and gives each day the most writing lines; portrait fits ring binders, especially in A5 or Half Letter. Print several undated pages at once and keep them with your <a href="/monthly-calendar.html">monthly calendar</a>; add a <a href="/daily-planner.html">daily planner</a> for the busiest days. All three share the same accent colors, so a printed set looks consistent.</p>
""",
"faq": [("Can I print several weeks at once?", "Print the undated version as many times as you like, or create dated pages week by week by changing the start date."),
        ("Does the planner work in A5 binders?", "Yes – choose A5 or Half Letter. Portrait orientation usually works best for small binders."),
        ("Can the week start on Sunday?", "Yes. Enter a Sunday as the start date and the boxes run Sunday to Saturday with the correct dates. Undated pages start on Monday."),
        ("Can I remove the to-do list?", "Untick “To-do column” and the day boxes use the full width or height of the page."),
        ("What is the eighth box for?", "It is labeled Notes and holds everything that belongs to the week but not to a day: phone numbers, a shopping item, ideas or a quote for the week.")],
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
<h2>Printing tips</h2>
<p>The page is always portrait. A5 or Half Letter turns it into a pocket-sized day card, though the hours get tighter, so shorten the schedule to the hours you really need. Print a small stack of undated pages for normal days and a dated one for special days such as a move, a trip or an exam. Plan the week first with the <a href="/weekly-planner.html">weekly planner</a>, then use this page only on days that need hour-by-hour detail.</p>
""",
"faq": [("Can I make the schedule start earlier?", "Yes – choose any start hour from 4:00 and any end hour up to 24:00."),
        ("Is there a version without the water tracker?", "Untick “Water tracker” and “Gratitude & reflection” and the notes area grows automatically."),
        ("Should I fill in every hour?", "No. Block appointments and priorities, and leave the rest open. A schedule packed from start to finish usually breaks by lunchtime."),
        ("Does the water tracker set a target?", "It has eight glasses to tick as a simple visual reminder. It is not a medical recommendation; how much you need depends on you.")],
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
<h2>Printing tips</h2>
<p>Print the whole year in one go and keep the sheets in a folder next to the current page, so a new month is always ready. The circles are drawn in a light gray outline, so any pen color shows; a highlighter fills them quickly. For a yearly view, color one habit day by day on a <a href="/yearly-calendar.html">yearly calendar</a>.</p>
""",
"faq": [("How many habits can I track?", "Up to 15 named habits plus empty rows, 24 rows at most – but most people do best with three to seven."),
        ("Can I track habits weekly instead of daily?", "Use the checklist template with numbered lines for weekly goals, or mark only certain days on the monthly tracker."),
        ("Why does the tracker show weekday letters?", "They help you spot patterns, such as habits that are always missed on weekends or on one particular weekday."),
        ("Can I track numbers, like hours of sleep?", "Yes – write the number inside the circle instead of filling it in. Keep such rows to one or two, as they take longer to fill in.")],
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
<h2>Printing tips</h2>
<p>The page is always portrait. For lists you laminate and reuse with a dry-erase marker, choose large spacing and bold square boxes, and print on heavier paper before laminating. A5 and Half Letter make handy pocket lists for shopping. For a weekly to-do list tied to dates, use the <a href="/weekly-planner.html">weekly planner</a>; for daily routines tracked over a month, the <a href="/habit-tracker.html">habit tracker</a>.</p>
""",
"faq": [("How many items fit on one page?", "Up to 60 lines in two columns. With fewer lines, the spacing grows so the page still looks balanced."),
        ("Can I save my pre-filled list?", "Your last settings are remembered in this browser. You can also copy a share link that contains your list."),
        ("Can I print a list with two columns of different topics?", "Choose two columns and pre-fill the items in order: the first half of your lines fills the left column, the rest the right column. Leave empty lines to separate topics."),
        ("Can I make a numbered list without check boxes?", "Yes. Choose “Numbered” as the checkbox style and every line gets a number instead of a box.")],
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
<h2>Printing tips</h2>
<p>A printed plan on the fridge answers the daily “What's for dinner?” question for the whole household; landscape works best there. Portrait suits binders, where you can keep past weeks as a library of meals that worked. If you track food spending, carry the receipt total over to the groceries line of the <a href="/budget-planner.html">budget planner</a>.</p>
""",
"faq": [("Can I start the week on Sunday?", "Yes – switch “Week starts on” to Sunday. Enter a start date to have the dates printed above each day."),
        ("Is there a version without the grocery list?", "Untick “Grocery list” and the meal grid uses the full page."),
        ("Can I plan two weeks on one page?", "Not on one page, but you can print two copies and enter the start dates of consecutive weeks."),
        ("Where do recipes go?", "Write the recipe name and where to find it – a cookbook page or a website name – in the cell. Dinner-only plans leave the most room.")],
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
<h2>Printing tips</h2>
<p>The page is always portrait and works on A4, US Letter, A5 or Half Letter; the larger sizes leave more room for amounts. Print a year at once and file each month behind the last, so you can compare the same category across months.</p>
<p class="small muted">The planner is an organizing tool and not financial advice.</p>
""",
"faq": [("Can I use a different currency?", "Choose $, €, £ or no symbol. The summary boxes show the symbol; amounts in the table are written by hand."),
        ("Can I print a whole year?", "Choose “All 12 months” for a 12-page budget binder with your categories on every page."),
        ("Can I rename the income rows?", "The income rows are fixed (salary, side income, other, total), but you can cross one out and write your own label; the expense categories are fully editable."),
        ("What goes into “Saved” and “Left over”?", "Saved is what you moved to savings this month (it also appears as a category). Left over is total income minus total expenses, savings included – money still available or carried into next month.")],
},
]

BY = {t["slug"]: t for t in TOOLS}
