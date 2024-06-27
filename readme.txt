
CarWale Car URL Scraper
Overview
This project provides a script to scrape URLs of cars from CarWale, a popular automotive website. It utilizes web scraping techniques to extract specific information about cars listed on the site.

Features
Scraping Car URLs: Extracts URLs of cars listed on CarWale.
Customizable: Easily adaptable script for different scraping needs.
CSV Output: Saves the scraped URLs in a CSV format for easy analysis and integration.
Installation
Clone the repository:
https://github.com/viveksoftdev/carwale_scraped.git

Install the required dependencies:
pip install -r requirements.txt

Run the script:
python app.py

Example Output
After running the script, the URLs of cars scraped from CarWale will be saved in the specified CSV file (carwale_url.csv by default)

Dependencies
aiohttp: For making HTTP requests.
beautifulsoup4: For parsing HTML and extracting data.
pandas : For creating the dataframe and writing data to csv.
