# Internship Scraper

The Internship Scraper is a Python project that uses the Selenium library to scrape internship information from a website and save it to a CSV file. This project is specifically designed to scrape information from thehub.io website for startups in the robotics industry with a specific range of employees.

## Requirements
- Python 3.x
- Selenium library
- Webdriver Manager
- Only works on TheHub.io 

## Installation
1. Clone the project to your local system.
2. Make sure you have Python 3.x installed on your system.
3. Install the required libraries using the following command: 

        pip install selenium pandas webdriver_manager
4. Open the Internship Scraper project in your preferred Python IDE or text editor.


## Running the Project
1. Open the `internship_scraper.py` file in your Python IDE or text editor.
2. Modify the `link` variable to specify which TheHub.io filters you want. The current link is set to 

        https://thehub.io/startups?industries=robotics&numberOfEmployees=1-10&numberOfEmployees=11-50&countryCodes=DK 
    
3. You can also modify the options for the Firefox browser by uncommenting the `opts.add_argument("--headless")` line to run the browser in headless mode, which means the browser will run in the background without displaying a graphical user interface.
4. Save the changes to the `internship_scraper.py` file.
5. Open a terminal or command prompt and navigate to the directory where the `internship_scraper.py` file is located.
6. Run the project using the following command:
        
        python internship_scraper.py
7. The project will start scraping internship information from the specified website and save it to a CSV file named `data.csv` in the same directory.
8. Once the scraping is completed, the Firefox browser will automatically close, and you will be able to find the scraped data in the `data.csv` file.

Note: Please be respectful of websites' terms of service and privacy policies when scraping data. Make sure to review and comply with any legal requirements or restrictions before using this project for any purpose.
