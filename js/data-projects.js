const DATA_PROJECTS = [
  {
    id: "northbridge",
    title: "NorthBridge Health Services",
    subtitle: "SLA and Operational Intelligence Platform for a UK healthcare BPO",
    tools: ["Amazon S3", "Airbyte", "Snowflake", "SQL", "Power BI", "DAX"],
    images: [
      "assets/img/projects/northbridge/dashboard-1.png",
      "assets/img/projects/northbridge/dashboard-2.png",
      "assets/img/projects/northbridge/dashboard-3.png",
      "assets/img/projects/northbridge/dashboard-4.png"
    ],
    problem: "NorthBridge processes 11,000+ healthcare service tickets monthly across four UK hubs. Manual workflows and fragmented data caused average first response times to surge to 38 hours against an 8 hour target, leaving a backlog of 2,800+ tickets and over £214,000 in annual SLA penalty payouts.",
    whatIDid: [
      "Designed a cloud pipeline: raw data loaded to Amazon S3, synced via Airbyte into Snowflake across RAW, CLEAN, and REPORTING layers",
      "Built SLA and escalation-monitoring dashboards with DAX-driven KPIs in Power BI",
      "Modeled workload, capacity, and agent productivity analyses across 114 active agents",
      "Delivered time-series forecasting to flag SLA breach risk before it happens"
    ],
    stats: [
      { value: "80.3%", label: "SLA Compliance" },
      { value: "754", label: "Breached Tickets" },
      { value: "35.2%", label: "Escalation Rate" },
      { value: "75%", label: "Productivity Ratio" }
    ],
    featured: true,
    date: "2026-06"
  },
  {
    id: "greentech",
    title: "GreenTech Manufacturing",
    subtitle: "Production downtime root cause analysis recovering roughly $800K in annual value",
    tools: ["SQL Server", "Power BI", "DAX", "Power Query", "Excel"],
    images: [
      "assets/img/projects/greentech/dashboard-1.png",
      "assets/img/projects/greentech/dashboard-2.png",
      "assets/img/projects/greentech/dashboard-3.png",
      "assets/img/projects/greentech/dashboard-4.png"
    ],
    problem: "GreenTech was losing an estimated $1.5M annually to production downtime, with no visibility into whether operators, scheduling, or equipment reliability were driving the losses. After analyzing 645 production batches over a six month period, 56 percent of batches experienced delays, and operator-related issues accounted for nearly 70 percent of downtime events, the largest controllable factor. Scheduling conflicts occurred on 51 production days, and one production line alone accounted for 191 hours of lost production time.",
    whatIDid: [
      "Cleaned and transformed SQL data across 645 production batches and 885 downtime events",
      "Built a three-page interactive Power BI dashboard with DAX measures and KPI tracking",
      "Ran root cause, trend, and operator level downtime analysis across 13 downtime categories",
      "Reframed findings from individual blame toward process and scheduling improvements, and delivered a 180 day roadmap with six prioritized recommendations"
    ],
    stats: [
      { value: "$800K", label: "Projected Recovery" },
      { value: "56%", label: "Batches Delayed" },
      { value: "70%", label: "Operator-Related Downtime" },
      { value: "191 hrs", label: "Lost, Top Line" }
    ],
    featured: true,
    date: "2026-05"
  },
  {
    id: "hawthornevale",
    title: "Hawthorne and Vale Hotel",
    subtitle: "Hospitality revenue intelligence for a 218 room UK boutique hotel",
    tools: ["Tableau", "Data Modeling", "KPI Design"],
    images: [
      "assets/img/projects/hawthornevale/dashboard-1.png",
      "assets/img/projects/hawthornevale/dashboard-2.png"
    ],
    problem: "At 57 percent occupancy, the hotel was busy but management couldn't answer which segments, channels, or room types actually drove profit, and average daily rate had quietly dropped almost 30 percent.",
    whatIDid: [
      "Modeled £11.48M in revenue across 6,867 stays into reusable calculated KPIs",
      "Built a Tableau executive dashboard covering channel mix, room type, seasonality, and guest behavior",
      "Diagnosed a yield gap: direct and online bookings worth roughly £1,760 each versus roughly £1,500 for OTA channels",
      "Delivered five recommendations, leading with rate discipline and channel rebalancing for fastest payback"
    ],
    stats: [
      { value: "£11.48M", label: "Revenue Analyzed" },
      { value: "6,867", label: "Stays" },
      { value: "4%", label: "Cancellation Rate" }
    ],
    featured: true,
    date: "2026-06"
  },
  {
    id: "streamwave",
    title: "StreamWave Entertainment",
    subtitle: "Viewer engagement and strategic content investment analysis for a streaming platform",
    tools: ["Excel", "Pivot Tables", "PowerPoint"],
    images: [
      "assets/img/projects/streamwave/dashboard-1.png",
      "assets/img/projects/streamwave/dashboard-2.png"
    ],
    problem: "Facing rising content costs and churn, StreamWave needed to know which genres earned their investment and why cancellations were outpacing new subscribers across a base of 999 users.",
    whatIDid: [
      "Analyzed viewing activity across 999 users spanning demographics, genre, and subscription tier",
      "Built an interactive Excel dashboard plus a 10 slide executive presentation",
      "Delivered six recommendations: double down on Drama and Comedy, launch a mid-year retention campaign, and convert Basic tier users"
    ],
    stats: [
      { value: "44%", label: "Views: Drama + Comedy" },
      { value: "2.76x", label: "Churn vs Acquisition" },
      { value: "45%", label: "Still on Basic Tier" }
    ],
    featured: true,
    date: "2026-04"
  },
  {
    id: "capstone-survey",
    title: "Global Developer Trends Analysis",
    subtitle: "NPower Canada capstone: 2024 Stack Overflow Developer Survey",
    tools: ["Python", "Pandas", "NumPy", "SQL", "IBM Cognos"],
    images: ["assets/img/projects/capstone-demographics.png"],
    problem: "Organizations and technology professionals need reliable insight into the tools, languages, and platforms shaping software development, and into where the field is headed next.",
    whatIDid: [
      "Independently ran the full analytics lifecycle: cleaning, EDA, feature engineering, and statistical summaries in Python",
      "Built an interactive IBM Cognos dashboard covering current tech usage, future trends, and demographics",
      "Presented findings in a professional capstone report and presentation"
    ],
    resultsList: [
      "JavaScript ranked as the most used language, PostgreSQL the top database, AWS the leading cloud platform",
      "React and Node.js remained the most widely adopted frameworks",
      "Most respondents were 25 to 34 years old and held a Bachelor's degree or higher"
    ],
    featured: true,
    date: "2026-07"
  },
  {
    id: "sales-dashboard",
    title: "Sales Dashboard Analysis",
    subtitle: "Executive Power BI dashboard for revenue and profit performance",
    tools: ["Power BI", "Power Query"],
    images: ["assets/img/projects/sales-dashboard/dashboard-1.jpg"],
    problem: "Leadership needed a single executive view of revenue, profit, and order volume trends to guide pricing and inventory decisions.",
    whatIDid: [
      "Built an executive Power BI dashboard tracking revenue, profit, quantity sold, and average order value",
      "Modeled monthly revenue trends and revenue by segment for at-a-glance performance review"
    ],
    stats: [
      { value: "$2.30M", label: "Total Revenue" },
      { value: "$286.4K", label: "Total Profit" },
      { value: "37.87K", label: "Units Sold" }
    ],
    featured: false,
    date: "2026-03"
  },
  {
    id: "attrition",
    title: "ALIJAZ Attrition Analytics Dashboard",
    subtitle: "HR analytics exploring workforce attrition and retention",
    tools: ["Excel", "Data Visualization"],
    images: ["assets/img/projects/attrition/dashboard-1.png"],
    problem: "HR leadership needed to understand which departments, age groups, and demographics were driving employee attrition to target retention efforts.",
    whatIDid: [
      "Analyzed attrition across 1,470 employees by department, age group, gender, and marital status",
      "Built an Excel dashboard surfacing attrition rate, promotion status, and satisfaction drivers"
    ],
    stats: [
      { value: "1,470", label: "Total Employees" },
      { value: "237", label: "Total Attrition" }
    ],
    featured: false,
    date: "2026-02"
  },
  {
    id: "jiji-cars",
    title: "JIJI Car Sales Dashboard",
    subtitle: "Used car market analysis across 3,959 listings",
    tools: ["Excel", "Power Query"],
    images: ["assets/img/projects/jiji-cars/dashboard-1.jpg"],
    problem: "Understanding pricing and demand patterns across Nigeria's largest used car marketplace to reveal market preferences and pricing patterns by type and year of make.",
    whatIDid: [
      "Cleaned and analyzed 3,959 used car listings across type, year of make, and condition",
      "Built an interactive dashboard surfacing average price by type, year, and the top five most expensive cars"
    ],
    stats: [
      { value: "3,959", label: "Cars Analyzed" },
      { value: "2013", label: "Top Year" }
    ],
    featured: false,
    date: "2026-02"
  },
  {
    id: "tenant-retention",
    title: "Tenant Retention Strategies Report",
    subtitle: "Property management dashboard on lease renewal and satisfaction",
    tools: ["Power BI", "Excel", "Data Visualization"],
    images: ["assets/img/projects/tenant-retention/dashboard-1.jpg"],
    problem: "Property managers needed visibility into churn risk and satisfaction across property types to improve tenant retention strategy.",
    whatIDid: [
      "Built a multi-page dashboard tracking churn rate, satisfaction score, and occupancy rate by property type",
      "Analyzed lease term frequency and renewed versus expired leases by month"
    ],
    stats: [
      { value: "49%", label: "Churn Rate" },
      { value: "89%", label: "Occupancy Rate" }
    ],
    featured: false,
    date: "2026-01"
  },
  {
    id: "personal-finance",
    title: "Personal Finance Tracker",
    subtitle: "Income, spending, and category breakdown dashboard",
    tools: ["Excel", "Data Visualization"],
    images: ["assets/img/projects/personal-finance/dashboard-1.jpg"],
    problem: "Individuals need a clear view of income versus spending, broken down by category, to make better budgeting decisions.",
    whatIDid: [
      "Designed an Excel dashboard tracking available balance, income, and spending by category",
      "Surfaced top spending categories including housing, groceries, and clothing for faster budget decisions"
    ],
    featured: false,
    date: "2025-12"
  },
  {
    id: "clearx",
    title: "CLEARX Sales Analysis",
    subtitle: "Three year sales analysis driving pricing and inventory decisions",
    tools: ["Excel", "Pivot Tables", "SUMIFS"],
    images: ["assets/img/projects/clearx/dashboard-1.jpg"],
    problem: "Leadership needed a three year view (2021 to 2023) of revenue, units, and profit margin by branch, age group, and location to guide pricing and inventory decisions.",
    whatIDid: [
      "Built pivot table and SUMIFS-driven analysis across branches, gender, and competition level",
      "Surfaced revenue by product category, buying age group, and marketing campaign performance"
    ],
    stats: [
      { value: "32,089,767", label: "Total Revenue" },
      { value: "50,226", label: "Total Units" }
    ],
    featured: false,
    date: "2025-11"
  },
  {
    id: "fmcg",
    title: "Sales and Expiry Monitoring Dashboard",
    subtitle: "FMCG retail inventory optimization ahead of expiration",
    tools: ["Power BI", "DAX"],
    images: ["assets/img/projects/fmcg/dashboard-1.jpg"],
    problem: "Retailers needed to track how much product sells before versus after expiry risk to reduce waste and optimize restocking.",
    whatIDid: [
      "Built a Power BI dashboard tracking total quantity sold and sales distribution before and after expiry risk",
      "Surfaced top selling products by quantity to guide restocking priorities"
    ],
    stats: [
      { value: "865", label: "Total Quantity Sold" },
      { value: "85%", label: "Sold Before Expiry" }
    ],
    featured: false,
    date: "2025-10"
  },
  {
    id: "logistics-sales",
    title: "Logistics Sales Dashboard, Alijaz Analytics",
    subtitle: "US regional sales performance and customer behavior analysis",
    tools: ["Excel", "Power Query"],
    images: [],
    problem: "Leadership needed to understand sales performance across US states to uncover customer behavior and product performance trends.",
    whatIDid: [
      "Cleaned and transformed raw sales data in Excel for accuracy and consistency",
      "Built an interactive dashboard tracking regional and product performance to guide business decisions"
    ],
    featured: false,
    date: "2025-05"
  },
  {
    id: "covid-dashboard",
    title: "COVID-19 Data Analysis Dashboard",
    subtitle: "Exploratory analysis of global COVID-19 case data",
    tools: ["Python", "Pandas"],
    images: [],
    problem: "Understanding how global COVID-19 case trends evolved required cleaning and exploring a large, messy public dataset.",
    whatIDid: [
      "Cleaned and explored global COVID-19 case data using Python and Pandas",
      "Built exploratory visualizations and a dashboard script to track case trends over time"
    ],
    featured: false,
    date: "2025-06"
  }
];
