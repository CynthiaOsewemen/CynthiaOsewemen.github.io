# -*- coding: utf-8 -*-
import os

SITE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(SITE, "projects")
os.makedirs(OUT_DIR, exist_ok=True)

DATA_PROJECTS = [
    dict(id="northbridge", title="NorthBridge Health Services",
         subtitle="SLA and Operational Intelligence Platform for a UK healthcare BPO",
         tools=["Amazon S3", "Airbyte", "Snowflake", "SQL", "Power BI", "DAX"],
         images=["assets/img/projects/northbridge/dashboard-1.png",
                 "assets/img/projects/northbridge/dashboard-2.png",
                 "assets/img/projects/northbridge/dashboard-3.png",
                 "assets/img/projects/northbridge/dashboard-4.png"],
         problem="NorthBridge processes 11,000+ healthcare service tickets monthly across four UK hubs. Manual workflows and fragmented data caused average first response times to surge to 38 hours against an 8 hour target, leaving a backlog of 2,800+ tickets and over £214,000 in annual SLA penalty payouts.",
         whatIDid=["Designed a cloud pipeline: raw data loaded to Amazon S3, synced via Airbyte into Snowflake across RAW, CLEAN, and REPORTING layers",
                   "Built SLA and escalation-monitoring dashboards with DAX-driven KPIs in Power BI",
                   "Modeled workload, capacity, and agent productivity analyses across 114 active agents",
                   "Delivered time-series forecasting to flag SLA breach risk before it happens"],
         stats=[("80.3%", "SLA Compliance"), ("754", "Breached Tickets"), ("35.2%", "Escalation Rate"), ("75%", "Productivity Ratio")]),
    dict(id="greentech", title="GreenTech Manufacturing",
         subtitle="Production downtime root cause analysis recovering roughly $800K in annual value",
         tools=["SQL Server", "Power BI", "DAX", "Power Query", "Excel"],
         images=["assets/img/projects/greentech/dashboard-1.png",
                 "assets/img/projects/greentech/dashboard-2.png",
                 "assets/img/projects/greentech/dashboard-3.png",
                 "assets/img/projects/greentech/dashboard-4.png"],
         problem="GreenTech was losing an estimated $1.5M annually to production downtime, with no visibility into whether operators, scheduling, or equipment reliability were driving the losses. After analyzing 645 production batches over a six month period, 56 percent of batches experienced delays, and operator-related issues accounted for nearly 70 percent of downtime events, the largest controllable factor. Scheduling conflicts occurred on 51 production days, and one production line alone accounted for 191 hours of lost production time.",
         whatIDid=["Cleaned and transformed SQL data across 645 production batches and 885 downtime events",
                   "Built a three-page interactive Power BI dashboard with DAX measures and KPI tracking",
                   "Ran root cause, trend, and operator level downtime analysis across 13 downtime categories",
                   "Reframed findings from individual blame toward process and scheduling improvements, and delivered a 180 day roadmap with six prioritized recommendations"],
         stats=[("$800K", "Projected Recovery"), ("56%", "Batches Delayed"), ("70%", "Operator-Related Downtime"), ("191 hrs", "Lost, Top Line")]),
    dict(id="hawthornevale", title="Hawthorne and Vale Hotel",
         subtitle="Hospitality revenue intelligence for a 218 room UK boutique hotel",
         tools=["Tableau", "Data Modeling", "KPI Design"],
         images=["assets/img/projects/hawthornevale/dashboard-1.png",
                 "assets/img/projects/hawthornevale/dashboard-2.png"],
         problem="At 57 percent occupancy, the hotel was busy but management couldn't answer which segments, channels, or room types actually drove profit, and average daily rate had quietly dropped almost 30 percent.",
         whatIDid=["Modeled £11.48M in revenue across 6,867 stays into reusable calculated KPIs",
                   "Built a Tableau executive dashboard covering channel mix, room type, seasonality, and guest behavior",
                   "Diagnosed a yield gap: direct and online bookings worth roughly £1,760 each versus roughly £1,500 for OTA channels",
                   "Delivered five recommendations, leading with rate discipline and channel rebalancing for fastest payback"],
         stats=[("£11.48M", "Revenue Analyzed"), ("6,867", "Stays"), ("4%", "Cancellation Rate")]),
    dict(id="streamwave", title="StreamWave Entertainment",
         subtitle="Viewer engagement and strategic content investment analysis for a streaming platform",
         tools=["Excel", "Pivot Tables", "PowerPoint"],
         images=["assets/img/projects/streamwave/dashboard-1.png",
                 "assets/img/projects/streamwave/dashboard-2.png"],
         problem="Facing rising content costs and churn, StreamWave needed to know which genres earned their investment and why cancellations were outpacing new subscribers across a base of 999 users.",
         whatIDid=["Analyzed viewing activity across 999 users spanning demographics, genre, and subscription tier",
                   "Built an interactive Excel dashboard plus a 10 slide executive presentation",
                   "Delivered six recommendations: double down on Drama and Comedy, launch a mid-year retention campaign, and convert Basic tier users"],
         stats=[("44%", "Views: Drama + Comedy"), ("2.76x", "Churn vs Acquisition"), ("45%", "Still on Basic Tier")]),
    dict(id="capstone-survey", title="Global Developer Trends Analysis",
         subtitle="NPower Canada capstone: 2024 Stack Overflow Developer Survey",
         tools=["Python", "Pandas", "NumPy", "SQL", "IBM Cognos"],
         images=["assets/img/projects/capstone-demographics.png"],
         problem="Organizations and technology professionals need reliable insight into the tools, languages, and platforms shaping software development, and into where the field is headed next.",
         whatIDid=["Independently ran the full analytics lifecycle: cleaning, EDA, feature engineering, and statistical summaries in Python",
                   "Built an interactive IBM Cognos dashboard covering current tech usage, future trends, and demographics",
                   "Presented findings in a professional capstone report and presentation"],
         resultsList=["JavaScript ranked as the most used language, PostgreSQL the top database, AWS the leading cloud platform",
                      "React and Node.js remained the most widely adopted frameworks",
                      "Most respondents were 25 to 34 years old and held a Bachelor's degree or higher"]),
    dict(id="sales-dashboard", title="Sales Dashboard Analysis",
         subtitle="Executive Power BI dashboard for revenue, profit, and regional performance",
         tools=["Power BI", "DAX"],
         images=["assets/img/projects/sales-dashboard/dashboard-1.jpg"],
         problem="Leadership needed a clear visual summary of overall business performance in Power BI. Monthly revenue trends revealed a decline in recent months, signaling a need to investigate sales strategies or seasonal factors.",
         whatIDid=["Built an executive dashboard surfacing Total Revenue, Profit, Quantity Sold, and Average Order Value front and center for rapid decision making",
                   "Added dynamic filtering by Region and Category so stakeholders can drill into the insights they need",
                   "Identified the West and East regions as revenue leaders, with the Consumer segment accounting for the largest share of sales",
                   "Found Technology and Office Supplies as the top-performing categories, with product TEC-CO-10004722 alone contributing over $61K in revenue"],
         stats=[("$2.30M", "Total Revenue"), ("$286.4K", "Total Profit"), ("37.87K", "Units Sold"), ("$458.61", "Avg Order Value")]),
    dict(id="attrition", title="ALIJAZ Attrition Analytics Dashboard",
         subtitle="HR analytics exploring workforce attrition and retention",
         tools=["Excel", "Data Visualization"],
         images=["assets/img/projects/attrition/dashboard-1.jpg"],
         problem="HR leadership needed to understand which departments, age groups, and demographics were driving employee attrition to target retention efforts.",
         whatIDid=["Analyzed attrition across 1,470 employees by department, age group, gender, and marital status",
                   "Built an Excel dashboard surfacing attrition rate, promotion status, and satisfaction drivers"],
         stats=[("1,470", "Total Employees"), ("237", "Total Attrition")]),
    dict(id="jiji-cars", title="JIJI Car Sales Dashboard",
         subtitle="Used car market analysis across 3,959 listings",
         tools=["Excel", "Power Query"],
         images=["assets/img/projects/jiji-cars/dashboard-1.jpg"],
         problem="Understanding pricing and demand patterns across Nigeria's largest used car marketplace to reveal market preferences and pricing patterns by type and year of make.",
         whatIDid=["Cleaned and analyzed 3,959 used car listings across type, year of make, and condition",
                   "Built an interactive dashboard surfacing average price by type, year, and the top five most expensive cars"],
         stats=[("3,959", "Cars Analyzed"), ("2013", "Top Year")]),
    dict(id="tenant-retention", title="Tenant Retention Strategies Report",
         subtitle="Property management dashboard on lease renewal and satisfaction",
         tools=["Power BI", "Excel", "Data Visualization"],
         images=["assets/img/projects/tenant-retention/dashboard-1.jpg"],
         problem="Property managers needed visibility into churn risk and satisfaction across property types to improve tenant retention strategy.",
         whatIDid=["Built a multi-page dashboard tracking churn rate, satisfaction score, and occupancy rate by property type",
                   "Analyzed lease term frequency and renewed versus expired leases by month"],
         stats=[("49%", "Churn Rate"), ("89%", "Occupancy Rate")]),
    dict(id="personal-finance", title="Personal Finance Tracker",
         subtitle="Income, spending, and category breakdown dashboard",
         tools=["Excel", "Data Visualization"],
         images=["assets/img/projects/personal-finance/dashboard-1.jpg"],
         problem="Individuals need a clear view of income versus spending, broken down by category, to make better budgeting decisions.",
         whatIDid=["Designed an Excel dashboard tracking available balance, income, and spending by category",
                   "Surfaced top spending categories including housing, groceries, and clothing for faster budget decisions"]),
    dict(id="clearx", title="CLEARX Sales Analysis",
         subtitle="Three year sales analysis driving pricing and inventory decisions",
         tools=["Excel", "Pivot Tables", "SUMIFS"],
         images=["assets/img/projects/clearx/dashboard-1.jpg"],
         problem="Leadership needed a three year view (2021 to 2023) of revenue, units, and profit margin by branch, age group, and location to guide pricing and inventory decisions.",
         whatIDid=["Built pivot table and SUMIFS-driven analysis across branches, gender, and competition level",
                   "Surfaced revenue by product category, buying age group, and marketing campaign performance"],
         stats=[("32,089,767", "Total Revenue"), ("50,226", "Total Units")]),
    dict(id="fmcg", title="Sales and Expiry Monitoring Dashboard",
         subtitle="FMCG retail inventory optimization ahead of expiration",
         tools=["Power BI", "DAX"],
         images=["assets/img/projects/fmcg/dashboard-1.jpg"],
         problem="Retailers needed to track how much product sells before versus after expiry risk to reduce waste and optimize restocking.",
         whatIDid=["Built a Power BI dashboard tracking total quantity sold and sales distribution before and after expiry risk",
                   "Surfaced top selling products by quantity to guide restocking priorities"],
         stats=[("865", "Total Quantity Sold"), ("85%", "Sold Before Expiry")]),
    dict(id="logistics-sales", title="Logistics Sales Dashboard, Alijaz Analytics",
         subtitle="US regional sales performance and customer behavior analysis",
         tools=["Excel", "Power Query"],
         images=["assets/img/projects/logistics-sales/dashboard-1.jpg"],
         problem="Leadership needed to understand sales performance across US states to uncover customer behavior and product performance trends.",
         whatIDid=["Cleaned and transformed raw sales data in Excel for accuracy and consistency",
                   "Built an interactive dashboard tracking order volume, sales trends, top states, and top customers",
                   "Surfaced sub-category performance by sales and profit, and segment mix, to guide regional and product decisions"],
         stats=[("$1.36M", "Total Sales"), ("5,968", "Total Ordered"), ("774", "Total Customers"), ("$164K", "Profit")]),
    dict(id="covid-dashboard", title="Canada COVID-19 Health Data Dashboard",
         subtitle="Interactive Dash application tracking national and regional COVID-19 trends",
         tools=["Python", "Pandas", "Plotly", "Dash"],
         images=["assets/img/projects/covid-dashboard/dashboard-1.jpg"],
         problem="Understanding how COVID-19 outcomes varied across Canadian regions, age groups, and gender required cleaning a large Statistics Canada dataset and making it explorable for non-technical users.",
         whatIDid=["Cleaned and deduplicated a Statistics Canada COVID-19 dataset using Python and Pandas",
                   "Built an interactive Dash web application with a year filter and linked Plotly charts",
                   "Delivered views for reported cases by region, nationwide year-over-year trend, age group, and outcome"]),
]

AUTOMATION_PROJECTS = [
    dict(id="asana-exec-support", title="Executive Support Task Management", tool="Asana",
         description="Task tracking system built to support executive workflows and priorities, covering to-do and completed task stages with clear ownership per task.",
         image="assets/img/projects/automation/asana.jpg"),
    dict(id="monday-hr-workflow", title="HR Workflow Management", tool="Monday.com",
         description="Board structured to manage HR processes from onboarding through offboarding, with statuses, owners, and timelines tracked in one place.",
         image="assets/img/projects/automation/monday-hr.png"),
    dict(id="monday-crm-setup", title="Quick CRM Setup, Sales CRM Automation", tool="Monday.com",
         description="A sales CRM built and automated for fast lead tracking and pipeline visibility, reducing manual follow-up.",
         image="assets/img/projects/automation/monday-crm.png"),
    dict(id="monday-production-status", title="Production Status Board Automation", tool="Monday.com",
         description="Automated board tracking production stages and status updates in real time, cutting manual status check-ins.",
         image="assets/img/projects/automation/monday-production.png"),
    dict(id="monday-excel-import", title="Excel Import and Board Structuring", tool="Monday.com",
         description="Migrated Excel based tracking into a structured, automated project board, improving reporting consistency.",
         image="assets/img/projects/automation/monday-excel.png"),
    dict(id="trello-tech-talks", title="Tech Talks Event Planning", tool="Trello",
         description="End to end event planning board covering catering, keynote speakers, audio/visual setup, team meetings, and follow ups for a technical speaker series.",
         image="assets/img/projects/automation/trello-tech-talks.png"),
    dict(id="trello-bible-stories", title="Creation of Bible Stories Channel", tool="Trello",
         description="Content planning and production workflow for a faith based media channel, tracking team roles, scripting, and social media distribution from research through publishing.",
         image="assets/img/projects/automation/trello-bible-stories.png"),
    dict(id="trello-thesis", title="Thesis Project Workflow Planning", tool="Trello",
         description="Research workflow for an AI thesis project, tracking milestones from the foundational prediction model through WebGL interface development and LLM-based explanation integration.",
         image="assets/img/projects/automation/trello-thesis.png"),
    dict(id="jira-trendzy", title="Trendzy Website Redesign", tool="Jira",
         description="Website redesign project tracked through structured sprints and a backlog of design, content, and mobile functionality issues from discovery to launch.",
         image="assets/img/projects/automation/jira-trendzy.jpg"),
]

NAV_ITEMS = [
    ("../index.html", "Home"),
    ("../about.html", "About"),
    ("../portfolio.html", "Portfolio"),
    ("../financial-advisory.html", "Financial Advisory"),
    ("../books.html", "Books"),
    ("../youtube.html", "YouTube"),
    ("../contact.html", "Contact"),
]

HEADER = """<header class="site-header">
  <div class="nav-wrap">
    <a href="../index.html" class="logo">Cynthia <span>Osewemen</span></a>
    <nav class="main-nav" id="mainNav">
      <ul>
{nav_links}
      </ul>
    </nav>
    <div class="nav-actions">
      <a href="../contact.html" class="btn btn-primary btn-sm">Let's Talk</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""

FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <h5>Cynthia Osewemen</h5>
        <p>Data analyst, financial advisor, author, and content creator based in Calgary, Alberta. Bilingual in English and French.</p>
      </div>
      <div class="footer-col">
        <h5>Professional Links</h5>
        <div class="footer-links">
          <a href="https://www.linkedin.com/in/cynthia-osewemen" target="_blank" rel="noopener">LinkedIn</a>
          <a href="https://github.com/CynthiaOsewemen" target="_blank" rel="noopener">GitHub</a>
          <a href="https://www.youtube.com/@Alijazdiary" target="_blank" rel="noopener">YouTube: Alijaz Diary</a>
          <a href="https://selar.com/m/Cynthia497" target="_blank" rel="noopener">Selar Shop</a>
          <a href="https://www.upwork.com/freelancers/~01b94bdc566c6bc6d1" target="_blank" rel="noopener">Upwork</a>
          <a href="https://www.instagram.com/grow_withcynthia" target="_blank" rel="noopener">GrowWithCynthia on Instagram</a>
          <a href="https://www.facebook.com/Growwithcynthia" target="_blank" rel="noopener">GrowWithCynthia on Facebook</a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Personal Social Media</h5>
        <div class="footer-links">
          <a href="https://www.instagram.com/alijazdiary" target="_blank" rel="noopener">Instagram: alijazdiary</a>
          <a href="https://www.tiktok.com/@alijazdiary" target="_blank" rel="noopener">TikTok: alijazdiary</a>
          <a href="https://www.facebook.com/alijazdiary" target="_blank" rel="noopener">Facebook: alijazdiary</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>Copyright <span id="year"></span> Cynthia Chidinma Osewemen. All rights reserved.</p>
    </div>
  </div>
</footer>

<button class="back-to-top" id="backToTop" aria-label="Back to top">Top</button>

<script src="../js/script.js"></script>
</body>
</html>
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def nav_html(active_href):
    lines = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if label == "Portfolio" else ""
        lines.append(f'        <li><a href="{href}"{cls}>{label}</a></li>')
    return "\n".join(lines)


def page_shell(title, description, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>

{HEADER.format(nav_links=nav_html("portfolio.html"))}
<main>
{body}
</main>

{FOOTER}"""


def gallery_html(images, title):
    if not images:
        return f'<div class="detail-noimg">{esc(title)}</div>'
    cls = "single" if len(images) == 1 else ""
    imgs = "\n".join(
        f'        <img src="../{src}" alt="{esc(title)} screenshot {i+1}" loading="lazy">'
        for i, src in enumerate(images)
    )
    return f'<div class="detail-gallery {cls}">\n{imgs}\n      </div>'


def prev_next(items, idx, base):
    prev_link = ""
    next_link = ""
    if idx > 0:
        p = items[idx - 1]
        prev_link = f'<a href="{p["id"]}.html">Previous: {esc(p["title"])}</a>'
    else:
        prev_link = "<span></span>"
    if idx < len(items) - 1:
        n = items[idx + 1]
        next_link = f'<a href="{n["id"]}.html">Next: {esc(n["title"])}</a>'
    else:
        next_link = "<span></span>"
    return f'<div class="detail-nav">\n        {prev_link}\n        {next_link}\n      </div>'


def build_data_project(p, idx):
    tools_html = "".join(f"<span>{esc(t)}</span>" for t in p["tools"])
    gallery = gallery_html(p.get("images", []), p["title"])

    stats_html = ""
    if p.get("stats"):
        pills = "".join(
            f'<div class="stat-pill"><b>{esc(v)}</b><small>{esc(l)}</small></div>'
            for v, l in p["stats"]
        )
        stats_html = f'<div class="detail-stats">{pills}</div>'

    results_html = ""
    if p.get("resultsList"):
        items = "".join(f"<li>{esc(x)}</li>" for x in p["resultsList"])
        results_html = f"""
      <div class="detail-section">
        <h3>Key Findings</h3>
        <ul>{items}</ul>
      </div>"""

    what_i_did = "".join(f"<li>{esc(x)}</li>" for x in p["whatIDid"])

    nav = prev_next(DATA_PROJECTS, idx, "")

    body = f"""
  <section class="page-header">
    <div class="container">
      <p class="breadcrumb"><a href="../portfolio.html">Portfolio</a> / <span class="detail-category">Data Analytics</span></p>
      <p class="eyebrow">Data Analytics Case Study</p>
      <h1>{esc(p['title'])}</h1>
      <p>{esc(p['subtitle'])}</p>
    </div>
  </section>

  <section>
    <div class="container">
      {gallery}
      <div class="detail-tools">{tools_html}</div>

      <div class="detail-section">
        <h3>Objective</h3>
        <p>{esc(p['problem'])}</p>
      </div>

      <div class="detail-section">
        <h3>What I Did</h3>
        <ul>{what_i_did}</ul>
      </div>
{results_html}
      <div class="detail-section">
        <h3>Achievements</h3>
        {stats_html if stats_html else "<p>Delivered a complete, presentation-ready analysis supporting real business decisions.</p>"}
      </div>

      {nav}
    </div>
  </section>
"""
    return page_shell(
        f"{p['title']}, Cynthia Chidinma Osewemen",
        f"{p['title']}: {p['subtitle']}",
        body,
    )


def build_automation_project(p, idx):
    img = p.get("image")
    gallery = gallery_html([img] if img else [], p["title"])
    nav = prev_next(AUTOMATION_PROJECTS, idx, "")

    body = f"""
  <section class="page-header">
    <div class="container">
      <p class="breadcrumb"><a href="../portfolio.html">Portfolio</a> / <span class="detail-category">Automation and PM</span></p>
      <p class="eyebrow">Automation and PM Project</p>
      <h1>{esc(p['title'])}</h1>
      <p>Built with {esc(p['tool'])} as part of freelance project management and CRM automation work.</p>
    </div>
  </section>

  <section>
    <div class="container">
      {gallery}
      <div class="detail-tools"><span>{esc(p['tool'])}</span></div>

      <div class="detail-section">
        <h3>Objective</h3>
        <p>{esc(p['description'])}</p>
      </div>

      <div class="detail-section">
        <h3>What I Did</h3>
        <ul>
          <li>Designed and structured the {esc(p['tool'])} workspace around the client's real workflow</li>
          <li>Set up statuses, ownership, and automations to reduce manual coordination</li>
          <li>Delivered a board the team could adopt immediately with minimal training</li>
        </ul>
      </div>

      <div class="detail-section">
        <h3>Achievements</h3>
        <p>Reduced manual coordination and gave the team a single source of truth for tracking work, contributing to the broader 25 percent delivery speed and 30 percent efficiency gains achieved across this freelance engagement.</p>
      </div>

      {nav}
    </div>
  </section>
"""
    return page_shell(
        f"{p['title']}, Cynthia Chidinma Osewemen",
        f"{p['title']}: a {p['tool']} automation project by Cynthia Chidinma Osewemen.",
        body,
    )


for i, proj in enumerate(DATA_PROJECTS):
    html = build_data_project(proj, i)
    with open(os.path.join(OUT_DIR, f"{proj['id']}.html"), "w", encoding="utf-8") as f:
        f.write(html)

for i, proj in enumerate(AUTOMATION_PROJECTS):
    html = build_automation_project(proj, i)
    with open(os.path.join(OUT_DIR, f"{proj['id']}.html"), "w", encoding="utf-8") as f:
        f.write(html)

print(f"Generated {len(DATA_PROJECTS) + len(AUTOMATION_PROJECTS)} project pages in {OUT_DIR}")
