import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configure logging
logging.basicConfig(filename='scrape_errors.log', level=logging.ERROR, format='%(asctime)s %(message)s')

# Read the existing eBay listings CSV file
try:
    df = pd.read_csv('./updated_listings_with_images.csv')
except FileNotFoundError:
    print("CSV file not found.")
    exit(1)

# Function to scrape product description from eBay with retries and delays
def scrape_description(item_number):
    url = f"https://www.ebay.com/itm/{item_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    retries = 3
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=20)  # Increased timeout duration
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Update the parsing logic to match the current eBay page structure
                description = soup.find('div', {'id': 'viTabs_0_is'})
                if description:
                    return description.get_text(strip=True)
                else:
                    logging.error(f"Description not found for {url}")
            else:
                logging.error(f"Failed to retrieve {url}, status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Error retrieving {url}: {e}")
        
        # Wait before retrying
        time.sleep(2 ** i)
    
    return "Description not found"

# Function to apply scraping with multithreading
def scrape_descriptions_multithreaded(item_numbers):
    descriptions = {}
    with ThreadPoolExecutor(max_workers=20) as executor:  # Increased number of threads
        future_to_item = {executor.submit(scrape_description, item): item for item in item_numbers}
        for future in tqdm(as_completed(future_to_item), total=len(item_numbers), desc="Scraping product descriptions"):
            item = future_to_item[future]
            try:
                descriptions[item] = future.result()
            except Exception as e:
                logging.error(f"Error processing item {item}: {e}")
                descriptions[item] = "Description not found"
    return descriptions

# Get the item numbers
item_numbers = df['Item number'].tolist()

# Scrape descriptions using multithreading
descriptions = scrape_descriptions_multithreaded(item_numbers)

# Add the descriptions to the DataFrame
df['Product Description'] = df['Item number'].map(descriptions)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_listings_with_descriptions.csv', index=False)

print("Product descriptions have been added and saved to 'updated_listings_with_descriptions.csv'")