import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Read the CSV file
try:
    df = pd.read_csv('./eBay-all-active-listings-report-2024-10-08-11187678997.csv')
except FileNotFoundError:
    print("CSV file not found.")
    exit(1)

# Function to scrape image URL from eBay
def scrape_image_url(listing_id):
    url = f"https://www.ebay.com/itm/{listing_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed for listing ID {listing_id}: {e}")
        return ''
    
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tag = soup.find('img', {'id': 'icImg'})
    if image_tag:
        image_url = image_tag['src']
        print(f"Found image URL for listing ID {listing_id}: {image_url}")
        return image_url
    print(f"No image found for listing ID {listing_id}")
    return ''

# Add a new column for image URLs with progress bar
tqdm.pandas(desc="Scraping eBay listings")
df['image_url'] = df['Item number'].progress_apply(scrape_image_url)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_listings.csv', index=False)

print("Updated CSV file has been saved as 'updated_listings.csv'")