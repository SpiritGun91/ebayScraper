import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service('/usr/bin/chromedriver')  # Update with the path to your ChromeDriver

# Read the CSV file
try:
    df = pd.read_csv('./eBay-all-active-listings-report-2024-10-08-11187678997.csv')
except FileNotFoundError:
    print("CSV file not found.")
    exit(1)

# Function to scrape all image URLs from eBay using Selenium
def scrape_image_urls(item_number):
    url = f"https://www.ebay.com/itm/{item_number}"
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    
    try:
        # Wait for the images to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src]'))
        )
        
        # Find all image elements with a 'src' attribute
        image_elements = driver.find_elements(By.CSS_SELECTOR, 'img[src]')
        image_urls = [img.get_attribute('src') for img in image_elements]
        
        # Only return unique URLs and avoid duplicate thumbnails, if necessary
        unique_image_urls = list(set(image_urls))
        print(f"Found {len(unique_image_urls)} image URLs for item number {item_number}")
        
        # Return all URLs as a comma-separated string
        return ','.join(unique_image_urls)
    
    except Exception as e:
        print(f"Failed to find images for item number {item_number}: {e}")
        return ''
    
    finally:
        driver.quit()

# Add a new column for image URLs with progress bar
tqdm.pandas(desc="Scraping eBay listings")
df['image_urls'] = df['Item number'].progress_apply(scrape_image_urls)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_listings_with_images.csv', index=False)

print("Updated CSV file has been saved as 'updated_listings_with_images.csv'")
