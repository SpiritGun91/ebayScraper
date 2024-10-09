# ebayScraper

## Overview

`ebayScraper` is a Python script designed to scrape image URLs from eBay listings based on a CSV file containing active listing details. The script reads the CSV file, fetches the image URLs for each listing, and updates the CSV file with the fetched image URLs.

## Features

- Reads listing details from a CSV file.
- Scrapes eBay for image URLs based on listing IDs.
- Updates the CSV file with the fetched image URLs.
- Handles network errors gracefully.

## Requirements

- Python 3.x
- `pandas`
- `requests`
- `beautifulsoup4`

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/ebayScraper.git
   cd ebayScraper
   ```

2. Install the required Python libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place your CSV file (e.g., `sample-listings-report.csv`) in the project directory.

2. Run the script:

   ```sh
   python main.py
   ```

3. The script will read the CSV file, scrape the image URLs, and save the updated data to `updated_listings.csv`.

## CSV File Format

The CSV file should have the following columns (at a minimum):

- `Item number`: The unique identifier for each eBay listing.
