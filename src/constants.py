# Main constants
ssr = True
host = "0.0.0.0"  # Used if ssr (Server Side Rendering) is False
port = "8000"  # Used if ssr (Server Side Rendering) is False

me = {
    "name": "Liam Borer Seabloom",
    "email": "lborerseabloom26@cornellcollege.edu",
    "location": "Iowa, United States",
    "school": "Cornell College",
    "short_bio" : "Senior Data Science and Finace major at Cornell College, passionate about data analysis and financial markets.",
    "bio": "Example bio: Liam Borer Seabloom is a senior at Cornell College, majoring in Data Science and Finance. He has a keen interest in data analysis and financial markets, and is actively involved in various projects that combine these fields. Liam is known for his analytical skills and his ability to derive insights from complex datasets. In his free time, he enjoys exploring new technologies and staying updated with the latest trends in data science and finance.",
}

# Metadata
main_metadata = {
    "locale": "US",
    "author": "Personal Website",
    "title": "Liam Borer Seabloom",
    "desc": "Personal website to catalog my relevant work experience.",
    "image": "https://media.discordapp.net/attachments/712969229506183198/831109920103465000/img_caching.png",
    "favicon": "https://images-ext-2.discordapp.net/external/5Hi7Y5E0rvFTKpKPeGg6Uc1p1-itFQPf4AwEsjzcUqo/https/i.imgur.com/tGibRPY.png",
}

# Social Metadata
social_metadata = {
    "github": {
        "desc": "Discover my work and projects from my GitHub profile.",
        "url": "https://github.com/lborerseabloom",
    },
    "linkedin": {
        "desc": "Check out my LinkedIn profile to know more about my skills & experiences.",
        "url": "https://www.linkedin.com/in/liamborerseabloom",
    },
}

# Main page - Experiences
experiences = [
    {
        "name": "University of Minnesota",
        "position": "Data Analytics Consultant",
        "link": None,
        "time": "August 2024 > Present",
    },
    {
        "name": "Cornell College - Summer Research Institute",
        "position": "Summer Researcher",
        "link": None,
        "time": "May 2025 > July 2025",
    },
    {
        "name": "University of Minnesota - Soil Science Calculator",
        "position": "Consultant",
        "link": "https://z.umn.edu/pv-smart",
        "time": "May 2024",
    },
    {
        "name": "Social Services Housing Project",
        "position": "Student Consultant",
        "link": None,
        "time": "August 2023 > September 2023",
    },
]

# Main page - Education
education = [
    {
        "name": "Cornell College",
        "description": "Data Science and Finance Major",
        "link": "https://www.cornellcollege.edu/",
        "time": "August 2022 > Present",
    },
]

# Main page - Technologies
technologies = [
    {"name": "R (Advanced): Tidyverse, Quarto, Statistical Modeling, Machine Learning", "color": "blue-400", "size": "full"},
    {"name": "Python (Intermediate): pandas, Matplotlib, Data Automation, Website/App Creation", "color": "blue-700", "size": "full"},
    {"name": "SQL (Intermediate): MySQL, Joins, CTEs", "color": "gray-700", "size": "full"},
    {"name": "Excel (Intermediate): Pivot Tables and Macros", "color": "green-600", "size": "full"},
]

# Projects - projects
projects = [
    {
        "name": "Cornell Summer Research Institute",
        "description": [
            "Built an End-to-End processing 10-k financial reports into CSV for analysis using Large Language Models (LLMs)",
            "Worked in Python with APIs from a financial database (EDGAR), OpenAI, and Gemini",
            "Used Pandas, Matplotlib, and Plotly to analyze and visualize data"
        ],
        "time": "May 2025 > July 2025",
        "link": "https://news.cornellcollege.edu/2025/06/CSRI-2026-ECB-Finance.html",
    },
    {
        "name": "Minne MUDAC Data Analytics Competition",
        "description": [
            "Competed in a national data analytics competition with a team of 4 against 34 other universities",
            "Built a predictive model on child retention in the Big Brothers Big Sisters program acheiving the 3rd best RMSE",
            "Placed 2nd overall; being judged on accuracy, insights, and team collaboration.",
        ],
        "time": "Febuary 2025 > April 2025",
        "link": "https://www.youtube.com/watch?v=7KuJB4193no",
    },
    {
        "name": "Time Series Climate Project",
        "description": [
            "Analyzed and visualized time series data from the National Oceanic and Atmospheric Administration (NOAA) as well as other sources",
            "Created a 'Scrollytelling' web app using R Shiny to present findings",
            "Used ggplot2 for data visualization and Tidyverse for data manipulation",
        ],
        "time": "January 2024",
        "link": "https://stats-tgeorge.github.io/STA364_TSApps/project/student_examples/Liam%20Borer.html",
    },
        {
        "name": "Soil Science Calculator",
        "description": [
            "Translated complex solar panel runoff model from Excel to R",
            "Built a Shiny app in R to eventually be hosted as a U of M website (z.umn.edu/pv-smart)"
        ],
        "time": "May 2024",
        "link": "https://erellima.shinyapps.io/SoilCalc/",
    },
]