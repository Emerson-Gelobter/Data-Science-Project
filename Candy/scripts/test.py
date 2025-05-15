import sqlite3
import pandas as pd

# Connect to your SQLite DB
conn = sqlite3.connect("data/candy.db")

# Load first 5 rows from 'sales' table
df = pd.read_sql_query("SELECT * FROM sales LIMIT 5", conn)

# Print nicely
print(df)

conn.close()