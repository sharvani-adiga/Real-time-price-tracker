# Real-time-price-tracker
Python-based web scraping and price tracking tool. It periodically scrapes product prices and records price history in a SQLite database.

# PriceTracker

PriceTracker is a Python-based web scraping and price tracking tool that allows you to monitor product prices across various online retailers. Whether you're looking to grab a great deal or keep an eye on price fluctuations, PriceTracker has you covered.

## Components

PriceTracker incorporates the following components and dependencies:

- **Python:** The core programming language used for developing the tool.

- **Schedule Module:** Utilized to automate and schedule the extraction of prices at specified intervals.

- **Web Scraping:** The tool leverages web scraping techniques to extract product prices and other relevant information from online retailer websites.

- **SQLite3 Database:** Price history is stored in an SQLite3 database, allowing users to track price changes over time.


## Getting Started

1. Clone this repository to your local machine.

2. Install the beautifulsoup using `pip`:

3. Configure the URLs of the products you want to track in the `scrape.py` script. 2 products are mentionec but the number of products can be modified as per requirement. The URL of the product must be mentioned as product1='place url for product 1', product2='place url for product 2', and so on. The function extract() must be called for each product by sending the url as the parameter.

4. Run the `scheduler.py` script to start price tracking by running the followind on the terminal:
  python3 scheduler.py

5. PriceTracker will scrape and record prices according to the schedule you set. 

## Configuration

- Adjust the scraping frequency and notifications by modifying the scheduling in `scheduler.py`.

- Customize the URLs of the products you want to track in the `scrape.py` script.
