# Script to clean and merge raw datasets
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw_data")
CLEAN_DIR = os.path.join(BASE_DIR, "data", "cleaned_data")
os.makedirs(CLEAN_DIR, exist_ok=True)

print("Looking for file at:", os.path.join(RAW_DIR, "Candy_Sales.csv"))
sales = pd.read_csv(os.path.join(RAW_DIR, "Candy_Sales.csv"))
products = pd.read_csv(os.path.join(RAW_DIR, "Candy_Products.csv"))
factories = pd.read_csv(os.path.join(RAW_DIR, "Candy_Factories.csv"))
targets = pd.read_csv(os.path.join(RAW_DIR, "Candy_Targets.csv"))
zips = pd.read_csv(os.path.join(RAW_DIR, "uszips.csv"))

# Clean and save each raw file
def clean_and_save(df, name):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(os.path.join(CLEAN_DIR, f"{name}.csv"), index=False)

# Clean and store all
clean_and_save(sales, "candy_sales")
clean_and_save(products, "candy_products")
clean_and_save(factories, "candy_factories")
clean_and_save(targets, "candy_targets")
clean_and_save(zips, "uszips")

# Merge sales + products
merged = sales.merge(products, on="product_id", how="left")

# Calculate revenue and profit
merged["revenue"] = merged["units"] * merged["unit_price"]
merged["cost"] = merged["units"] * merged["unit_cost"]
merged["profit"] = merged["revenue"] - merged["cost"]
merged["margin"] = merged["profit"] / merged["revenue"]

# Save to cleaned_data
merged.to_csv(os.path.join(CLEAN_DIR, "merged_sales.csv"), index=False)