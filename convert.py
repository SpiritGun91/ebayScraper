import pandas as pd

# Read the CSV file
csv_file_path = './updated_listings_with_images.csv'
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print("CSV file not found.")
    exit(1)

# Extract the 'Item number' column
item_numbers = df['Item number']

# Save the item numbers to a .txt file
txt_file_path = './item_numbers.txt'
with open(txt_file_path, 'w') as file:
    for item_number in item_numbers:
        file.write(f"{item_number}\n")

print(f"Item numbers have been saved to '{txt_file_path}'")