# eBay Scraper

This project is designed to scrape eBay listings and extract relevant information, including image URLs, to facilitate importing these listings to other platforms, starting with Amazon.

## Features

- Scrapes eBay listings to extract item details and image URLs.
- Saves the extracted data to a CSV file.
- Extracts item numbers from the CSV file and saves them to a `.txt` file for easy import to other platforms.

## Requirements

- Python 3.x
- pandas
- requests
- beautifulsoup4
- tqdm
- selenium

## Setup

1. **Install Dependencies**:  
   Make sure you have the required libraries installed:

   ```sh
   pip install pandas requests beautifulsoup4 tqdm selenium
   ```

2. **Download WebDriver**:  
   Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and ensure it's in your system's PATH. Update the path in the script accordingly:
   ```python
   service = Service('/path/to/chromedriver') # Update with the path to your ChromeDriver
   ```

## Usage

### Scraping eBay Listings

1. **Run the Scraper**:  
   Execute the `main.py` script to scrape eBay listings and save the data to a CSV file:

   ```sh
   python main.py
   ```

2. **Check the Output CSV**:  
   Open the `updated_listings.csv` file to see the image URLs added to the new column `image_url`.

### Extracting Item Numbers

1. **Run the Extractor**:  
   Execute the `convert.py` script to extract item numbers from the updated CSV file and save them to a `.txt` file:

   ```sh
   python convert.py
   ```

2. **Check the Output .txt File**:  
   Open the `item_numbers.txt` file to see the list of item numbers.

## CSV File Format

The CSV file should have the following columns (at a minimum):

- **Item number**: The unique identifier for each eBay listing.

## Purpose

This project was created to help import eBay listings to other platforms, starting with Amazon. By extracting item numbers and image URLs, the data can be easily formatted and uploaded to other e-commerce platforms. Hopefully. This is probably way easier with an eBay API key, but I made this while waiting for one lol (takes about a day I think).

## Contributing

Feel free to submit issues or pull requests if you have any improvements or suggestions.

## License

This project is licensed under the MIT License.
