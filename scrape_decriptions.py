import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# Read the existing eBay listings CSV file
try:
    df = pd.read_csv('./updated_listings_with_images.csv')
except FileNotFoundError:
    print("CSV file not found.")
    exit(1)

# Function to scrape product description from eBay
def scrape_description(item_number):
    url = f"https://www.ebay.com/itm/{item_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        description = soup.find('div', {'id': 'desc_div'})
        if description:
            return description.get_text(strip=True)
    return "Description not found"

# Add a new column for product descriptions
df['Product Description'] = df['Item number'].apply(scrape_description)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_listings_with_descriptions.csv', index=False)

print("Product descriptions have been added and saved to 'updated_listings_with_descriptions.csv'")