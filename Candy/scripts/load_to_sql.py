import pandas as pd
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "candy.db")
CLEAN_DIR = os.path.join(BASE_DIR, "data", "cleaned_data")

conn = sqlite3.connect(DB_PATH)

tables = {
    "sales": "candy_sales.csv",
    "products": "candy_products.csv",
    "factories": "candy_factories.csv",
    "targets": "candy_targets.csv",
    "zips": "uszips.csv"
}

for table_name, filename in tables.items():
    path = os.path.join(CLEAN_DIR, filename)
    print(f"Loading {filename} into table '{table_name}'")
    df = pd.read_csv(path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)

conn.close()
print(f"✅ All tables loaded into: {DB_PATH}")
