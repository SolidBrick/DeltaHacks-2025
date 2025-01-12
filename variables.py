from cohere import ClassifyExample

CLIMATE_EXAMPLES = [
    ClassifyExample(text="Mapped: How climate change affects extreme weather around the world", label="neutral"),
    ClassifyExample(text="GOAL OF THE MONTH – Goal 7: Affordable and Clean Energy", label="neutral"),
    ClassifyExample(text="Global Greenhouse Gas Overview | US EPA", label="neutral"),
    ClassifyExample(text="What Are the Solutions to Climate Change?", label="neutral"),
    ClassifyExample(text="80 percent of people globally want stronger climate action by governments according to UN Development Programme survey", label="good"),
    ClassifyExample(text="Letter to G20 Leaders Urges Financial Support to World Bank Fund to Achieve Global Sustainable Development", label="good"),
    ClassifyExample(text="In Response to Climate Change, Citizens in Advanced Economies Are Willing To Alter How They Live and Work", label="good"),
    ClassifyExample(text="The role of satellite remote sensing in mitigating and adapting to global climate change", label="good"),
    ClassifyExample(text="Climate change indicators reached record levels in 2023: WMO", label="bad"),
    ClassifyExample(text="Climate change threatens progress across sustainable development, warns new UN report", label="bad"),
    ClassifyExample(text="Climate Change Is Speeding Toward Catastrophe. The Next Decade Is Crucial, U.N. Panel Says. (Published 2023)", label="bad"),
    ClassifyExample(text="Global Climate Change Impact on Crops Expected Within 10 Years, NASA Study Finds", label="bad")
]

CLIMATE_LINKS = ["https://e360.yale.edu/feed.xml", "https://feeds.feedburner.com/ConservationInternationalBlog/ClimateChange", "https://grist.org/feed/"]

POVERTY_EXAMPLES = [
    ClassifyExample(text="September 2024 global poverty update from the World Bank: revised estimates up to 2024", label="neutral"),
    ClassifyExample(text="warning signs: poverty in canada", label="bad"),
    ClassifyExample(text="finance and treasury board", label="neutral"),
    ClassifyExample(text="a guide to statistics", label="neutral"),
    ClassifyExample(text="despite progress on poverty, mexico's first female president inherits shaky economy", label="bad"),
    ClassifyExample(text="floods and patterns of poverty in poverty in brazil", label="neutral"),
    ClassifyExample(text="the growing poverty crisis in iran: a consequence of mismanagement and economic missteps", label="bad"),
    ClassifyExample(text="why poor american kids are so likely to become poor adults", label="neutral"),
    ClassifyExample(text="a year into javier milei's presidencey, argentinas poverty hits a new high", label="bad"),
    ClassifyExample(text="graduate-student stipends in canada below the poverty line", label="bad"),
    ClassifyExample(text="plumbing povery: more people living without running water in US cities since global financial crisis", label="bad"),
    ClassifyExample(text="COMMENTARY: Children in P.E.I. exptected to experience poverty for many years. It does not have to be this way", label="bad"),
    ClassifyExample(text="Poverty Overview: Development news, research, data", label="neutral"),
    ClassifyExample(text="Reconciling the Official Poverty Measure and CBO’s Distributional Analysis of Household Income", label="neutral"),
    ClassifyExample(text="Poverty Reduction Strategy", label="good"),
    ClassifyExample(text="GNWT annouces 2024 Anti-Poverty Fund recipients", label="neutral"),
    ClassifyExample(text="opportunities for All: Tackling Poverty Together", label="neutral"),
    ClassifyExample(text="Reducing inequality and poverty in Portugal", label="good"),
    ClassifyExample(text="Brock community unites against poverty - The Brock News", label="good"),
    ClassifyExample(text="After years of decline, child poverty in Canada is rising swiftly: report", label="bad")
]

POVERTY_LINKS = ["https://politicsofpoverty.oxfamamerica.org/feed/", "https://www.care.org/feed/", "https://borgenproject.org/blog/feed/"]

ENERGY_EXAMPLES = [
    ClassifyExample(text="GOAL OF THE MONTH – Goal 7: Affordable and Clean Energy", label="neutral"),
    ClassifyExample(text="Sustainable energy is possible. Here are 6 ways to make it happen", label="neutral"),
    ClassifyExample(text="Renewable energy – powering a safer future", label="neutral"),
    ClassifyExample(text="New commitments at UN energy summit a major stride towards affordable and clean energy, but much work ahead to halve energy access gap by 2025", label="neutral"),
    ClassifyExample(text="Finance commitments under Energy Compacts reach $1.4 trillion towards achieving global goals on clean energy", label="good"),
    ClassifyExample(text="New how-to guide speeds global race for renewable energy", label="good"),
    ClassifyExample(text="Finance commitments under Energy Compacts reach $1.4 trillion towards achieving global goals on clean energy", label="good"),
    ClassifyExample(text="Foundations announce $1 billion fund for renewables in emerging economies", label="good"),
    ClassifyExample(text="Global progress on affordable and clean energy must be accelerated in order to close energy gap, new report says", label="bad"),
    ClassifyExample(text="Basic energy access lags amid renewable opportunities, new report shows", label="bad"),
    ClassifyExample(text="Analysis: Global CO2 emissions will reach new high in 2024 despite slower growth", label="bad"),
    ClassifyExample(text="Hydropower: How droughts are affecting the world's biggest renewable energy source", label="bad")
]

ENERGY_LINKS = ["https://www.altenergymag.com/rss/news", "https://www.irena.org/iapi/rssfeed/Publications", "https://feeds.feedburner.com/RenewableEnergyNewsRssFeed"]