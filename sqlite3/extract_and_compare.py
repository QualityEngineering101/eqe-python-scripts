from sqlite3 import OperationalError
import database_utils
import get_orangehrm_su_data

ARCHIVE_PATH = "./archives/orangehrm"
DB_PATH = "./data/orangehrm_data.db"
TABLE_NAME = "orangehrm_users"

conn = None

try:
    get_orangehrm_su_data.login()
    get_orangehrm_su_data.navigate_to_users()
    user_data = get_orangehrm_su_data.extract_table_data()

    # Ensure we have data so we can create the table in the database
    # It doesn't make sense to move forward if we don't have data
    if user_data:
        column_names = list(user_data[0].keys())
    else:
        raise ValueError("Error: No data extracted, cannot create table.")

    # Archive the previous run's database to a new archive (baseline)
    baseline_db = database_utils.archive_db(DB_PATH)

    if database_utils.create_db(DB_PATH, TABLE_NAME, column_names):
        print("New database created.")
    else:
        raise OperationalError("New database was not created so terminating.")

    if database_utils.load_table_data(DB_PATH, TABLE_NAME, user_data):
        print("Data from site was loaded into new database.")
    else:
        raise OperationalError(
            "Website data was not loaded into the table so terminating."
        )

    # Uncomment for debugging purposes
    # database_utils.select_table_data(DB_PATH, TABLE_NAME)
    # database_utils.select_table_data(baseline_db, TABLE_NAME)

    # Compare database row counts in the baseline db and new db
    if database_utils.compare_row_count_to_baseline(baseline_db, DB_PATH, TABLE_NAME):
        print("Baseline DB Row Count equals New DB Row Count.")
    else:
        print("Error:Baseline DB Row Count does not equal New DB Row Count.")

    # Identify any mismatches in the baseline db and new db
    key_column = "Username"
    mismatched_rows = database_utils.identify_mismatched_rows(
        baseline_db, DB_PATH, TABLE_NAME, key_column
    )
    if mismatched_rows:
        print("Error: Mismatches found between the baseline db and new db")
        for mismatch in mismatched_rows:
            print(mismatch)
    else:
        print("No mismatches found. Tables are identical.")
except Exception as e:
    print(f"Exception: {e}")
finally:
    if conn:
        conn.close()
