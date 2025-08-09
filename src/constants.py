# Main constants
ssr = True
host = "0.0.0.0"  # Used if ssr (Server Side Rendering) is False
port = "8000"  # Used if ssr (Server Side Rendering) is False

me = {
    "name": "Liam Borer Seabloom",
    "email": "lborerseabloom26@cornellcollege.edu",
    "location": "Iowa, United States",
    "school": "Cornell College",
    "short_bio" : "Senior Data Science and Finace major at Cornell College, passionate about using data to solve real world problems.",
    "bio": ["I’m a Data Science and Finance major at Cornell College (Class of 2026), with a minor in Computer Science and a passion for using data to drive positive change in communities. My academic work and professional experiences have focused on data cleaning, analysis, and visualization through a variety of projects and team enviroments.",
        "I’ve worked as a Data Analytics Consultant at the University of Minnesota, supporting a global network of scientists by modeling and cleaning complex datasets in R and SQL. The projects I have worked on have ranged from building an interactive Shiny app to calculate solar panel runoff, to developing predictive models for national analytics competitions, to analyzing socioeconomic and demographic disparities in housing access for nonprofit organizations.",
        "Technically, I’m skilled in R (tidyverse, statistical modeling, machine learning, Shiny), Python (pandas, Matplotlib, APIs), SQL, and Excel. I enjoy working with large, complex datasets of all kinds. Beyond my technical skills, I’m committed to diversity, inclusion, and leadership, shaped by hundreds of hours of volunteer work, mentorship, and team-based projects in diverse environments",
        "No matter what I am working on my goal has always been the same: to turn data into actionable insights that make a real difference in the world.",
    ],
}

# Metadata
main_metadata = {
    "locale": "US",
    "author": "Liam Borer Seabloom",
    "title": "Personal Website",
    "desc": "Personal website to catalog my relevant work experience.",
    "image": "/static/assets/avatar.jpg",
    "favicon": "/static/assets/avatar.jpg",
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