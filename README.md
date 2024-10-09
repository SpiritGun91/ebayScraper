# eBay Scraper

This project is designed to scrape eBay listings and extract relevant information, including image URLs and product descriptions, to facilitate importing these listings to other platforms, starting with Amazon.

## Features

- Scrapes eBay listings to extract item details, image URLs, and product descriptions.
- Saves the extracted data to a CSV file.
- Extracts item numbers from the CSV file and saves them to a `.txt` file for easy import to other platforms.
- Converts the table to a format suitable for importing to Amazon.
- Supports multiple eBay categories and filters.
- Handles pagination to scrape multiple pages of listings.
- Provides detailed logging for monitoring the scraping process.
- Includes error handling and retry mechanisms for robust scraping.
- Customizable scraping parameters (e.g., search keywords, price range).
- Supports headless browser mode for faster scraping.

## Requirements

- Python 3.x
- pandas
- requests
- beautifulsoup4
- tqdm
- selenium
- lxml

## Setup

1. **Install Dependencies**:  
   Make sure you have the required libraries installed:

   ```sh
   pip install pandas requests beautifulsoup4 tqdm selenium lxml
   ```

2. **Download WebDriver**:  
   Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and ensure it's in your system's PATH. Update the path in the script accordingly:

   ```python
   service = Service('/path/to/chromedriver') # Update with the path to your ChromeDriver
   ```

## Usage

### Scraping eBay Listings

1. **Run the Scraper**:  
   Ensure you have a CSV file with your eBay listings ready. Execute the `main.py` script to scrape eBay listings and save the data to a new CSV file, including image URLs:

   ```sh
   python main.py
   ```

2. **Check the Output CSV**:  
   Open the `updated_listings.csv` file to see the image URLs added to the new column `image_url`.

### Converting eBay Table to Amazon Table

1. **Prepare the CSV File**:  
   Ensure your `updated_listings.csv` file is formatted correctly with all necessary columns.

2. **Run the Conversion Script**:  
   Execute the `convert.py` script to transform the eBay CSV data into a format suitable for Amazon:

   ```sh
   python convert.py
   ```

3. **Check the Output Amazon CSV**:  
   Open the `amazon_listings.csv` file to verify the data has been converted correctly for Amazon import.

## CSV File Format

The CSV file should have the following columns (at a minimum):

- **Item number**: The unique identifier for each eBay listing.
- **Title**: The title of the eBay listing.
- **Price**: The price of the item.
- **Image URL**: The URL of the item's image.
- **Description**: The description of the item.

## Purpose

This project was created to help import eBay listings to other platforms, starting with Amazon. By extracting item numbers and image URLs, the data can be easily formatted and uploaded to other e-commerce platforms. This process can probably be expedited with an eBay API key, which typically takes about a day to obtain.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or suggestions.

## License

This project is licensed under the MIT License.
