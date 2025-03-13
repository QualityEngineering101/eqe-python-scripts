from database_utils import check_table_structure
import sqlite3

DB_PATH = "./data/orangehrm_data.db"
TABLE_NAME = "orangehrm_users"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create query
check_table_query = f'PRAGMA table_info("{TABLE_NAME}")'
cursor.execute(check_table_query)
columns_info = cursor.fetchall()
for _ in columns_info:
    print(_)
