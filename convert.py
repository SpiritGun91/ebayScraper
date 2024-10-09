import pandas as pd
import os

# Read the existing eBay listings CSV file
try:
    df = pd.read_csv('./updated_listings_with_images.csv')
except FileNotFoundError:
    print("CSV file not found.")
    exit(1)

# Create a directory to store the category-specific CSV files
output_dir = './category_csvs'
os.makedirs(output_dir, exist_ok=True)

# Define a function to map eBay data to Amazon format
def map_to_amazon_format(row):
    return {
        'SKU': row['Item number'],
        'Product Name': row['Title'],  # eBay Title → Amazon Product Name
        'Price': row['Current price'],  # eBay Price → Amazon Price
        'Quantity': row['Available quantity'],  # Assuming 'Available quantity' column exists in the eBay CSV
        'Image URL': row['image_urls'],  # eBay Image URLs → Amazon Image URLs
        'Product Category': row['eBay category 1 name'],  # eBay Category → Amazon Product Category
        'Condition Type': row['Condition'],  # eBay Item Condition → Amazon Condition Type
        'Brand': '',  # Placeholder, as eBay CSV does not have this field
        'Bullet Points': '',  # Placeholder, as eBay CSV does not have this field
        'Search Terms': ''  # Placeholder, as eBay CSV does not have this field
    }

# Apply the mapping function to each row in the DataFrame
amazon_data = df.apply(map_to_amazon_format, axis=1)

# Convert the list of dictionaries to a DataFrame
amazon_df = pd.DataFrame(list(amazon_data))

# Group the DataFrame by 'Product Category' and save each group to a separate CSV file
for category, group in amazon_df.groupby('Product Category'):
    # Replace any invalid characters in the category name for file naming
    safe_category_name = "".join([c if c.isalnum() else "_" for c in category])
    output_file = os.path.join(output_dir, f"{safe_category_name}.csv")
    group.to_csv(output_file, index=False)
    print(f"Saved category '{category}' to '{output_file}'")

print("All categories have been saved to separate CSV files.")