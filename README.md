# Si_placements_Assignment

This repository contains a Django-based web application designed to scrape job and internship listings from Internshala. Users can specify a job description, location, and experience level to find relevant opportunities. The scraped data is then processed, cleaned, and saved into a JSON file.

## Features

*   **Web-Based Search:** Provides a simple web interface to input search criteria for jobs.
*   **Targeted Scraping:** Scrapes job listings from [Internshala](https://internshala.com/) based on job description, location, and experience level (fresher or experienced).
*   **Data Normalization:** Cleans and formats scraped data—such as title, company, salary, and experience—for consistency.
*   **JSON Output:** Saves the structured job data to an `outputs/json.json` file for easy access and further use.

## Technology Stack

*   **Backend:** Python, Django
*   **Web Scraping:** Beautiful Soup 4, Requests
*   **Frontend:** HTML

## Project Structure

```
.
├── jobscraper/
│   ├── manage.py             # Django's command-line utility
│   ├── core/                 # Django app for core functionality (views, urls)
│   ├── jobscraper/           # Main project configuration (settings.py)
│   ├── outputs/
│   │   └── json.json         # Output file for scraped job data
│   ├── scraper/
│   │   └── internshala_scraper.py # The web scraping logic
│   ├── templates/
│   │   └── search.html       # The HTML template for the search form
│   └── utils/
│       └── formatter.py      # Helper functions for data cleaning
└── README.md
```

## Setup and Usage

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/zaidsaiyed1/si_placements.git
```

### 2. Install Dependencies

This project requires Python 3. Make sure you have it installed. Then, run virtual enviroment:

 **Windows (CMD)**
```cmd
env\Scripts\activate 
```

**MACOS (Terminal)**
```macOS / iOS (Terminal)
source env/bin/activate 
```

### 3. Run the Development Server

Once the virtuak enviroment started, then start the Django development server:

 **Windows (CMD)**
```bash
cd si_placements/jobscraper
python manage.py runserver 
```

**MACOS (Terminal)**
```bash
python3 manage.py runserver 
```

### 4. Use the Application

1.  Open your web browser and navigate to `http://127.0.0.1:8000/`.
2.  You will see a search form with three fields:
    *   **Job Description:** (e.g., "python developer", "data analyst")
    *   **Location:** (e.g., "mumbai", "remote")
    *   **Experience Level:** (e.g., "fresher", "1-3 years")
3.  Fill in the fields and click the **Search** button.
4.  The application will scrape Internshala for relevant job listings. After the search is complete, you will be redirected back to the search page.
5.  The scraped job data will be saved in the `jobscraper/outputs/json.json` file. Each new search appends its results to this file.

##  Sample Input & Output

**Input**
<img width="1914" height="983" alt="image" src="https://github.com/user-attachments/assets/ce3ed105-0246-4b8d-a4d2-1c87c9e0a656" />

**Output (Output will display in json.json file)**

<img width="345" height="425" alt="image" src="https://github.com/user-attachments/assets/4c605b7d-787e-4207-97f5-bf54891708a3" />

<img width="1907" height="873" alt="image" src="https://github.com/user-attachments/assets/c1e1f30f-d462-4389-aebd-cdb05e6d903b" />


## Challenges Faced
Handling dynamic HTML content from job portals

JSON formatting and maintaining consistent structure

Parsing complex and nested data using class-based selectors

Managing missing or dynamically loaded fields (location, experience, salary)
