"""Templates: metadata and the guide text shown under each generator."""

CATS = [("paper", "Paper"), ("calendars", "Calendars"), ("planners", "Planners"), ("trackers", "Trackers & lists")]

TOOLS = [
# ------------------------------------------------------------------ PAPER
{
"slug": "lined-paper", "cat": "paper", "name": "Lined paper", "accent": "ink",
"teaser": "Wide, college or narrow ruled – with margin and header line.",
"title": "Printable Lined Paper – Wide, College & Narrow Ruled (Free PDF)",
"description": "Make free printable lined paper in A4, US Letter or A5: wide, college or narrow ruled, custom spacing, margin line and header. Instant vector PDF.",
"lead": "Choose the ruling, paper size and line colour, then download a crisp vector PDF or print straight away.",
"guide": """
<h2>Which ruling should you pick?</h2>
<p>Lined paper is described by the distance between its lines. The three standard rulings come from US school paper, but they are used everywhere:</p>
<ul><li><strong>Wide ruled</strong> – 11/32 inch (8.7 mm). Generous space for larger handwriting, younger writers and anyone who finds tight lines tiring.</li>
<li><strong>College ruled</strong> – 9/32 inch (7.1 mm). The most common choice for notes, letters and journals. It fits more text without feeling cramped.</li>
<li><strong>Narrow ruled</strong> – 1/4 inch (6.35 mm). Popular with people who write small or want to squeeze a lot onto one page.</li></ul>
<p>Need something else? Pick <em>Custom</em> and enter any spacing between 3 and 20 mm. Many European school exercise books use around 8–9 mm, while 6 mm suits compact note-taking.</p>
<h2>Margin line and header</h2>
<p>The red margin line gives you a column for dates, question numbers or notes in the margin – it is the classic look of exercise paper. The optional header adds a <em>Name</em> and <em>Date</em> line at the top, which is handy for worksheets, exam practice and letters.</p>
<h2>Light lines write better</h2>
<p>Very dark lines compete with your handwriting. For everyday writing, the light grey setting is usually the most pleasant; choose <em>Blue</em> for the familiar notebook look or <em>Medium</em> if your printer prints faintly. When you scan or photocopy your notes later, light lines also disappear more cleanly.</p>
<h2>Printing tips</h2>
<p>Select the same paper size here as in your printer, and set scaling to <strong>100 % / Actual size</strong> rather than “Fit to page”. That keeps the spacing exactly as chosen. Our PDFs are vector files, so lines stay razor-sharp on any printer and at any zoom level.</p>
<p>Printing double-sided for a notebook? Print odd pages first, flip the stack and print again – or just use the same page on both sides, since lined paper has no front or back.</p>
""",
"faq": [("Is college ruled the same as 7 mm lines?", "Almost: college ruling is 9/32 inch, which is 7.14 mm. For most purposes the difference to 7 mm is invisible."),
        ("Can I use the paper commercially?", "You may print and use the pages for yourself, your family, your classroom or your own business. Please do not resell the files or offer them for download elsewhere.")],
},
{
"slug": "graph-paper", "cat": "paper", "name": "Graph paper", "accent": "teal",
"teaser": "Metric or imperial grids, with bold lines every few squares.",
"title": "Printable Graph Paper – 5 mm, 1 cm, 1/4 Inch Grid (Free PDF)",
"description": "Create free printable graph paper: 4 mm, 5 mm, 1 cm, 1/4 or 1/5 inch grids with optional bold lines, in A4, Letter or A5. Download as vector PDF.",
"lead": "Square grid paper for maths, sketching, floor plans and pixel art – in metric or imperial sizes.",
"guide": """
<h2>Metric or imperial?</h2>
<p>Graph paper (also called grid or squared paper) comes in two families. <strong>Metric</strong> grids of 5 mm or 1 cm are standard in most of Europe and in science. <strong>Imperial</strong> grids divide each inch into 4 or 5 squares – “4 squares per inch” (1/4 inch) is the classic US quad-ruled paper used in schools and engineering notebooks.</p>
<h2>Bold lines make counting easy</h2>
<p>A bold line every 5 or 10 squares turns the grid into a ruler. With 5 mm squares and bold lines every 2, each bold square is exactly one centimetre; with bold lines every 10, each bold square is 5 cm – handy for scale drawings. For quad-ruled imperial paper, bold lines every 4 squares mark whole inches.</p>
<h2>What graph paper is good for</h2>
<ul><li><strong>Maths and statistics:</strong> plotting functions, drawing bar charts, keeping columns of numbers aligned.</li>
<li><strong>Floor plans and garden layouts:</strong> let one square stand for 10 cm or 1 foot and you can sketch rooms to scale.</li>
<li><strong>Knitting, cross-stitch and pixel art:</strong> each square is one stitch or pixel.</li>
<li><strong>Handwriting practice:</strong> squares help keep letters evenly sized, which is why many schools use squared exercise books.</li></ul>
<h2>Scale drawings in three steps</h2>
<ol><li>Measure the longest side of the room or object.</li>
<li>Divide the number of squares that fit across the page by that length – this gives you squares per metre (or foot).</li>
<li>Round down to a convenient scale, such as 1 square = 25 cm, and write it in a corner of the page.</li></ol>
<p>Always print at 100 % scale. If the printer shrinks the page to fit its margins, a “5 mm” grid becomes 4.8 mm and your scale drawing will be slightly off.</p>
""",
"faq": [("How many squares fit on an A4 page?", "With a 5 mm grid and our 12 mm margins, the page holds 37 squares across and 53 down in portrait orientation."),
        ("What is engineering paper?", "Engineering paper is usually a light green 1/5 inch grid printed on the back so it shows through faintly. Choose the 1/5 inch grid and the light line colour for a similar look.")],
},
{
"slug": "dot-grid", "cat": "paper", "name": "Dot grid paper", "accent": "plum",
"teaser": "The bullet journal favourite – 5 mm dots and more.",
"title": "Printable Dot Grid Paper – 5 mm Bullet Journal Dots (Free PDF)",
"description": "Free printable dot grid paper for bullet journals, sketching and lettering: 4 mm, 5 mm, 1/4 inch, 7 mm or 1 cm spacing, fine to bold dots, A4/Letter/A5 PDF.",
"lead": "Structure without clutter: dots guide your lines, layouts and lettering, then step back so your writing stands out.",
"guide": """
<h2>Why dot grid?</h2>
<p>Dot grid paper sits between lined and blank. The dots give you a grid for straight lines, boxes and tables, but they are quiet enough that drawings and handwriting stay in the foreground. That flexibility made dot grid the standard paper for bullet journaling.</p>
<h2>Choosing the spacing</h2>
<ul><li><strong>5 mm</strong> is the bullet journal standard used by most dotted notebooks. Two dots are roughly one line of handwriting.</li>
<li><strong>4 mm</strong> suits small handwriting and dense layouts like habit grids.</li>
<li><strong>7 mm or 1 cm</strong> works well for lettering practice, children and large headings.</li>
<li><strong>1/4 inch</strong> matches US dotted notebooks and planner inserts.</li></ul>
<h2>Fine, medium or bold dots?</h2>
<p>If your printer prints lightly or you plan to photocopy the pages, choose medium or bold dots so they don't vanish. For fountain pens and watercolour lettering, fine dots in a light colour are almost invisible once the page is filled.</p>
<h2>Bullet journal layouts to try</h2>
<ul><li><strong>Future log:</strong> divide a page into six boxes for the next six months.</li>
<li><strong>Weekly spread:</strong> seven boxes of equal height plus a to-do column.</li>
<li><strong>Tracker grid:</strong> one dot per day across, one row per habit.</li>
<li><strong>Collections:</strong> books to read, gift ideas, packing lists.</li></ul>
<p>Prefer ready-made pages? Our <a href="/weekly-planner.html">weekly planner</a> and <a href="/habit-tracker.html">habit tracker</a> generate those layouts for you – and they can be printed on the same paper size.</p>
<h2>Making a dotted notebook</h2>
<p>Print a stack of pages, fold A4 sheets in half for an A5 booklet, or punch them for a ring binder. Thick 100–120 g/m² paper reduces ghosting when you use markers.</p>
""",
"faq": [("What size dots do bullet journals use?", "Most dotted notebooks use a 5 mm grid. That is our default setting."),
        ("Will the dots show when I scan my notes?", "Light, fine dots usually disappear or turn very faint in scans – one reason dot grid is popular for notes you want to digitise.")],
},
{
"slug": "isometric-paper", "cat": "paper", "name": "Isometric paper", "accent": "olive",
"teaser": "Triangle grid for 3D sketches, game maps and design.",
"title": "Printable Isometric Graph Paper – Lines or Dots (Free PDF)",
"description": "Free printable isometric paper with 60° triangle grid or isometric dots for 3D drawings, game maps, architecture and design. A4, Letter, A5 vector PDF.",
"lead": "A grid of 60° lines that makes three-dimensional sketches easy – for design, architecture, maths and tabletop games.",
"guide": """
<h2>What is isometric paper?</h2>
<p>Isometric paper is covered in equilateral triangles. Three sets of lines run vertically and at 30° to either side of horizontal. Because all three axes are drawn at the same scale, cubes and boxes look three-dimensional without any vanishing points – perfect for quick technical sketches.</p>
<h2>How to draw a cube</h2>
<ol><li>Pick a point where lines meet. Draw a vertical edge along a vertical line.</li>
<li>From the top and bottom of that edge, follow the two diagonal lines – one to the left, one to the right – for the same number of triangles.</li>
<li>Close the shape with vertical edges and copy the top diagonals to finish the lid.</li></ol>
<p>Every edge follows the grid, so the proportions are always right. Bigger shapes are just stacks of cubes.</p>
<h2>Who uses it?</h2>
<ul><li><strong>Designers and architects</strong> for product sketches and room layouts.</li>
<li><strong>Game designers</strong> for isometric maps and pixel art.</li>
<li><strong>Teachers</strong> for volume, nets and spatial reasoning tasks.</li>
<li><strong>Makers</strong> planning woodwork or 3D prints.</li></ul>
<h2>Lines or dots?</h2>
<p>Full lines are easiest for beginners. The dot version shows only the points where lines would cross: your drawings look cleaner and the grid disappears into the background – a good choice for finished illustrations.</p>
<h2>Choosing the triangle size</h2>
<p>5 mm triangles give lots of detail for small objects. 7 mm or 1 cm triangles are easier to see and suit classroom use or large maps. Print at 100 % scale so the angles stay exact.</p>
""",
"faq": [("Is isometric the same as perspective drawing?", "No. In perspective drawing, parallel lines meet in a vanishing point. In isometric drawing they stay parallel, so measurements along each axis remain to scale."),
        ("Can I use the grid for hex maps?", "Yes – groups of six triangles form hexagons, so isometric paper works for simple hex maps too.")],
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
<p>In the US, Canada and Japan, calendars traditionally start the week on <strong>Sunday</strong>. In most of Europe and under the international standard ISO 8601, the week starts on <strong>Monday</strong>. Choose whichever matches the way you plan – weekends then sit together at the end of each row.</p>
<h2>Week numbers explained</h2>
<p>Week numbers follow ISO 8601: week 1 is the week that contains the first Thursday of the year. That is why the first days of January sometimes belong to week 52 or 53 of the previous year. Week numbers are widely used in business, logistics and schools, so they are a handy addition to work calendars.</p>
<h2>Twelve months in one file</h2>
<p>Select <em>All 12 months</em> to create a complete year as a 12-page PDF – ready for a ring binder, a clipboard on the fridge or a wall calendar. Print it double-sided and every month will have a blank back for notes.</p>
<h2>Ideas for using a monthly calendar</h2>
<ul><li><strong>Family planner:</strong> give each person a colour for appointments, sports and school events.</li>
<li><strong>Content or project calendar:</strong> plan posts, deadlines and launches at a glance.</li>
<li><strong>Bill calendar:</strong> mark due dates for rent, subscriptions and insurance.</li>
<li><strong>Meal theme calendar:</strong> pasta Tuesday, soup Friday – fewer daily decisions.</li></ul>
<h2>Landscape or portrait?</h2>
<p>Landscape gives wider day boxes and a notes column on the right – best for desks and walls. Portrait fits binders and planners and moves the notes area below the grid.</p>
<p>Need the whole year on one page? Use the <a href="/yearly-calendar.html">yearly calendar</a>.</p>
""",
"faq": [("Does the calendar include holidays?", "No – holidays differ between countries and regions, so the day boxes are left free for you to fill in."),
        ("Which years can I create?", "Any year from 1900 to 2100. All dates are calculated with the Gregorian calendar.")],
},
{
"slug": "yearly-calendar", "cat": "calendars", "name": "Yearly calendar", "accent": "sand",
"teaser": "All twelve months on one page – year at a glance.",
"title": "Printable Yearly Calendar 2027 – Year at a Glance on One Page",
"description": "Free printable year-at-a-glance calendar for 2027 or any year: all 12 months on one page, Monday or Sunday start, weekends shaded. A4, Letter or A5 PDF.",
"lead": "The whole year on a single sheet – perfect for planning holidays, deadlines and long-term goals.",
"guide": """
<h2>Why a year-at-a-glance page?</h2>
<p>Monthly and weekly planners are great for the details, but they hide the big picture. A one-page yearly calendar shows how long until a deadline, which weeks are already busy and where a holiday would fit best. Pin it next to your desk or put it at the front of your planner.</p>
<h2>Ways to use it</h2>
<ul><li><strong>Holiday planning:</strong> mark school breaks and public holidays, then look for long weekends.</li>
<li><strong>Goal tracking:</strong> colour in each day you exercise, practise or write – the year fills up as a visible streak.</li>
<li><strong>Year in pixels:</strong> give each day a colour for your mood or energy and see patterns over months.</li>
<li><strong>Countdowns:</strong> highlight a wedding, move or exam date and cross off the days.</li></ul>
<h2>Portrait or landscape?</h2>
<p>Portrait arranges the months in four rows of three, which suits binders and planners. Landscape uses three rows of four and leaves larger numbers – better for walls and noticeboards.</p>
<h2>Leap years</h2>
<p>February gets its 29th day automatically in leap years. A year is a leap year when it is divisible by 4 – except for years divisible by 100, unless they are also divisible by 400. So 2028 is a leap year, while 2100 is not.</p>
<p>For day-by-day planning, create a matching <a href="/monthly-calendar.html">monthly calendar</a> in the same accent colour.</p>
""",
"faq": [("Can I print a calendar for a past year?", "Yes – enter any year between 1900 and 2100, for example to document a past year in a scrapbook."),
        ("Are weekends highlighted?", "Weekend dates appear in your accent colour and can be shaded; switch the shading off in the settings if you prefer a cleaner look.")],
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
<p>Enter a start date and every box is labelled with the weekday and date – handy if you print week by week. Leave the date empty to get an undated planner that you can print in bulk and use whenever you need it, without wasting pages on weeks you skip.</p>
<h2>A simple weekly planning routine</h2>
<ol><li><strong>Look back (5 minutes):</strong> what got done last week, what moves forward?</li>
<li><strong>Fixed appointments first:</strong> enter meetings, classes and family commitments.</li>
<li><strong>Pick three priorities:</strong> the tasks that would make the week a success. Put them on the to-do list.</li>
<li><strong>Give each priority a day:</strong> a task with a slot gets done far more often than a task on an open list.</li>
<li><strong>Leave buffer:</strong> keep some space free on each day for the unexpected.</li></ol>
<h2>Landscape or portrait?</h2>
<p>In landscape, the days sit in two rows of four boxes with a tall to-do column on the right – the classic desk planner. Portrait stacks the days in four rows and moves the to-do list to the bottom, which fits ring binders and clipboards.</p>
<h2>Weekends included</h2>
<p>Saturday and Sunday get their own boxes, lightly tinted so the work week stands out. The eighth box is for notes – shopping, ideas, phone numbers or a quote for the week.</p>
<h2>Combine with other pages</h2>
<p>Many people use a <a href="/monthly-calendar.html">monthly calendar</a> for the overview, this weekly page for planning and a <a href="/daily-planner.html">daily planner</a> for busy days. All three share the same accent colours, so your printed set looks consistent.</p>
""",
"faq": [("Can I print several weeks at once?", "Print the undated version as many times as you like, or create dated pages week by week by changing the start date."),
        ("Does the planner work in A5 binders?", "Yes – choose A5 or Half Letter. Portrait orientation usually works best for small binders.")],
},
{
"slug": "daily-planner", "cat": "planners", "name": "Daily planner", "accent": "tomato",
"teaser": "Hour-by-hour schedule, top 3 priorities, to-dos and notes.",
"title": "Printable Daily Planner – Hourly Schedule & To-Do List (Free PDF)",
"description": "Free printable daily planner with hourly or half-hourly schedule, top 3 priorities, to-do list, notes, gratitude and water tracker. A4, Letter, A5 PDF.",
"lead": "Time-block your day: an hourly schedule on the left, priorities, to-dos and notes on the right.",
"guide": """
<h2>Time blocking in a nutshell</h2>
<p>A to-do list tells you <em>what</em> to do; a schedule tells you <em>when</em>. Time blocking combines both: you give your most important tasks a slot in the day, just like a meeting. It protects focused work and makes it obvious when a day is already full.</p>
<h2>How to fill in the page</h2>
<ol><li><strong>Top 3 priorities:</strong> write down the three things that matter most today. If you only do these, the day was a success.</li>
<li><strong>Schedule:</strong> block time for appointments first, then for your priorities. Choose half-hour slots for busy days.</li>
<li><strong>To do:</strong> collect the smaller tasks – emails, calls, errands – and batch them into one or two blocks.</li>
<li><strong>Notes:</strong> capture ideas and loose ends so they do not distract you.</li>
<li><strong>Evening:</strong> tick off what is done and note one thing you are grateful for.</li></ol>
<h2>Adjust the schedule to your day</h2>
<p>Early riser? Start the schedule at 5:00. Night owl? Run it until midnight. The planner divides the available space evenly, so a shorter day gets more room per hour.</p>
<h2>The small extras</h2>
<p>The water tracker has eight glasses to tick off – a simple visual nudge, not a medical recommendation. The gratitude box takes a minute at the end of the day; many people find it a pleasant way to close the page. Switch both off if you need more space for notes.</p>
<h2>Dated or undated</h2>
<p>Enter a date to print a page for a specific day – for example an important event or a travel day. Leave it empty to print a stack of undated pages for everyday use.</p>
""",
"faq": [("Can I make the schedule start earlier?", "Yes – choose any start hour from 4:00 and any end hour up to 24:00."),
        ("Is there a version without the water tracker?", "Untick “Water tracker” and “Gratitude & reflection” and the notes area grows automatically.")],
},
# ------------------------------------------------------------------ TRACKERS & LISTS
{
"slug": "habit-tracker", "cat": "trackers", "name": "Habit tracker", "accent": "olive",
"teaser": "Your habits, every day of the month – tick and keep the streak.",
"title": "Printable Habit Tracker – Monthly, Customisable (Free PDF)",
"description": "Free printable monthly habit tracker: type your own habits, choose month and year, download one month or a whole year as PDF. A4, Letter, A5.",
"lead": "Type your habits, pick the month and fill in a circle every day you keep your promise to yourself.",
"guide": """
<h2>Why tracking works</h2>
<p>A habit tracker makes progress visible. Every filled circle is a small reward, and an unbroken row – a streak – becomes something you do not want to break. The act of ticking also forces a daily moment of reflection: did I do it today?</p>
<h2>How long does a habit take?</h2>
<p>The popular “21 days” rule is a myth. In a well-known study by Phillippa Lally and colleagues at University College London (published 2010), participants needed a median of 66 days before a new behaviour felt automatic – with a wide range from 18 to 254 days. Missing a single day did not significantly harm the process. So track for at least two or three months, and do not give up after a slip.</p>
<h2>Tips for a tracker that sticks</h2>
<ul><li><strong>Start small:</strong> three to five habits are plenty. Too many rows turn the tracker into a guilt list.</li>
<li><strong>Make habits concrete:</strong> “Read 20 pages” works better than “Read more”.</li>
<li><strong>Keep the tracker visible:</strong> on the fridge, next to your toothbrush or inside your planner.</li>
<li><strong>Never miss twice:</strong> one missed day is normal; two in a row is the start of a new pattern.</li>
<li><strong>Review monthly:</strong> use the “Done” column to count your days and decide what to keep, change or drop.</li></ul>
<h2>Whole year in one file</h2>
<p>Choose <em>All 12 months</em> to get a 12-page PDF with your habits already filled in. The extra empty rows leave room to add a habit mid-month.</p>
<p>Want a bigger picture? Colour one day per square on a <a href="/yearly-calendar.html">yearly calendar</a> to see your whole year of streaks.</p>
""",
"faq": [("How many habits can I track?", "Up to 15 named habits plus up to 10 empty rows – but most people do best with three to seven."),
        ("Can I track habits weekly instead of daily?", "Use the checklist template with numbered lines for weekly goals, or mark only certain days on the monthly tracker.")],
},
{
"slug": "checklist", "cat": "trackers", "name": "Checklist & to-do list", "accent": "ink",
"teaser": "Squares, circles or numbers – pre-fill items if you like.",
"title": "Printable Checklist & To-Do List Maker – Free PDF",
"description": "Make a free printable checklist or to-do list: your title, 5–60 lines, one or two columns, square or round boxes or numbers, optional pre-filled items. PDF.",
"lead": "From packing lists to project steps: give your list a title, choose the layout and pre-fill items if you want.",
"guide": """
<h2>A checklist for every occasion</h2>
<p>Checklists are one of the simplest tools for getting things done reliably. Pilots and surgeons use them to avoid forgetting critical steps – at home they save you from leaving the charger behind or missing an item on the moving-day list.</p>
<h2>Ideas</h2>
<ul><li><strong>Packing list</strong> for holidays, hospital bags or camping trips.</li>
<li><strong>Moving checklist</strong>: utilities, address changes, keys.</li>
<li><strong>Cleaning schedule</strong> with weekly and monthly tasks.</li>
<li><strong>Project steps</strong> for renovations, events or product launches.</li>
<li><strong>Reading or watch list</strong>, gift ideas and wish lists.</li></ul>
<h2>Pre-filled or blank?</h2>
<p>Type items into the box (one per line) and they are printed on the lines – ideal for lists you reuse, like a weekly shopping list or a packing list. Leave it empty for a blank to-do list you fill in by hand.</p>
<h2>Squares, circles or numbers?</h2>
<p>Squares are the classic tick box. Circles look softer and are popular in bullet journals. Numbered lines work best for ranked lists and step-by-step instructions. The optional priority column adds three dots per line – fill in one, two or three to mark importance.</p>
<h2>Make a better to-do list</h2>
<ol><li>Write tasks as actions: “Call the plumber”, not “Plumber”.</li>
<li>Split big tasks into steps that take less than an hour.</li>
<li>Mark the three most important items and do them first.</li>
<li>Move unfinished items to tomorrow's list deliberately – or delete them.</li></ol>
""",
"faq": [("How many items fit on one page?", "Up to 60 lines in two columns. With fewer lines, the spacing grows so the page still looks balanced."),
        ("Can I save my pre-filled list?", "Your last settings are remembered in this browser. You can also copy a share link that contains your list.")],
},
{
"slug": "meal-planner", "cat": "planners", "name": "Meal planner", "accent": "olive",
"teaser": "Weekly meals plus a grocery list sorted by aisle.",
"title": "Printable Weekly Meal Planner with Grocery List (Free PDF)",
"description": "Free printable weekly meal planner with breakfast, lunch, dinner and snacks plus a grocery list by category. Dated or undated, A4/Letter PDF.",
"lead": "Plan the week's meals in one grid and write the shopping list right next to it – sorted by category so you shop faster.",
"guide": """
<h2>Why plan meals?</h2>
<p>Deciding what to eat every evening takes surprising energy. Planning the week in one go means one shopping trip, less food thrown away and fewer last-minute takeaways. It also makes it easier to use up leftovers on purpose.</p>
<h2>A 20-minute planning routine</h2>
<ol><li><strong>Check the calendar:</strong> busy evenings get quick meals or leftovers.</li>
<li><strong>Look in the fridge:</strong> plan the first meals around what needs using up.</li>
<li><strong>Pick themes:</strong> for example pasta, soup, a vegetarian dish and a “fridge clean-out” night.</li>
<li><strong>Cook once, eat twice:</strong> double a recipe and plan the second portion for lunch.</li>
<li><strong>Write the grocery list</strong> straight from the plan, sorted by category.</li></ol>
<h2>Grocery list by category</h2>
<p>The list is divided into produce, protein, dairy, pantry and other – roughly the way most supermarkets are laid out. Writing items in the right section saves walking back and forth in the store.</p>
<h2>Choose your meals</h2>
<p>Select breakfast, lunch and dinner, add a row for snacks, or plan only lunch and dinner – or only dinner if that is the meal you need help with. The rows resize automatically so every cell has room to write.</p>
<h2>Stick it on the fridge</h2>
<p>A printed plan on the fridge answers the daily “What's for dinner?” question for the whole household. Landscape format works best there; portrait suits planners and binders.</p>
""",
"faq": [("Can I start the week on Sunday?", "Yes – switch “Week starts on” to Sunday. Enter a start date to have the dates printed above each day."),
        ("Is there a version without the grocery list?", "Untick “Grocery list” and the meal grid uses the full page.")],
},
{
"slug": "budget-planner", "cat": "trackers", "name": "Budget planner", "accent": "sand",
"teaser": "Planned vs actual for income and every expense category.",
"title": "Printable Monthly Budget Planner – Planned vs Actual (Free PDF)",
"description": "Free printable monthly budget planner: income and your own expense categories with planned, actual and difference columns, summary boxes and notes. PDF.",
"lead": "Write down what you plan to spend, track what you actually spent and see the difference at a glance – with your own categories.",
"guide": """
<h2>How the budget page works</h2>
<p>Each row has three columns: <strong>Planned</strong> (what you expect or allow), <strong>Actual</strong> (what really happened) and <strong>Difference</strong>. At the end of the month, the differences show where your money went differently than planned – the starting point for next month's budget.</p>
<h2>Setting up your categories</h2>
<p>Edit the category list to match your life. Start with fixed costs such as rent, utilities, insurance and subscriptions; then add variable spending such as groceries, transport, eating out and shopping. Include savings as a category of its own – paying yourself first is easier when it is a line on the page.</p>
<h2>A popular rule of thumb: 50/30/20</h2>
<p>One widely used guideline splits take-home pay into about 50 % for needs (housing, food, bills), 30 % for wants and 20 % for savings and paying off debt. It is a starting point, not a rule – in expensive cities housing alone can take half of the income. The point is to choose your split consciously.</p>
<h2>Tips for sticking with it</h2>
<ul><li><strong>Track weekly:</strong> ten minutes every Sunday with your bank app is easier than reconstructing a whole month.</li>
<li><strong>Round up:</strong> exact cents are not important; trends are.</li>
<li><strong>Plan irregular costs:</strong> divide annual bills such as insurance or gifts by twelve and budget that amount every month.</li>
<li><strong>Review, don't judge:</strong> an overspent category is information for next month, not a failure.</li></ul>
<p class="small muted">The planner is an organising tool and not financial advice.</p>
""",
"faq": [("Can I use a different currency?", "Choose $, €, £ or no symbol. The summary boxes show the symbol; amounts in the table are written by hand."),
        ("Can I print a whole year?", "Choose “All 12 months” for a 12-page budget binder with your categories on every page.")],
},
]

BY = {t["slug"]: t for t in TOOLS}
