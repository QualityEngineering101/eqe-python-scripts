import os
import sqlite3
import shutil
import stat
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any


class DatabaseError(Exception):
    pass


class FileSystemError(Exception):
    pass


def archive_db(db_path: str) -> Path:
    # Create backup from previous run (if exists)
    db_path = Path(db_path)
    archive_dir = db_path.parent

    try:
        archive_dir.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        raise FileSystemError(
            f"Permission denied: Cannot create directory '{archive_dir}'."
        )
    except Exception as e:
        raise FileSystemError(f"Failed to create directory '{archive_dir}': {e}") from e

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = archive_dir / f"{db_path.stem}_{timestamp}.db"

    counter = 1
    while archive_path.exists():
        archive_path = archive_dir / f"{db_path.stem}_{timestamp}_{counter}.db"
        counter += 1

    try:
        if db_path.exists():
            if not os.access(db_path, os.W_OK):
                print(
                    f"Warning: File '{db_path}' is read-only. Attempting to change permissions."
                )
                os.chmod(db_path, stat.S_IWRITE)
            shutil.move(db_path, archive_path)
            print(f"Database successfully archived at: {archive_path}")
            return archive_path
        else:
            raise FileSystemError(
                f"Database file '{db_path}' does not exist, so it cannot be archived."
            )
    except PermissionError:
        raise FileSystemError(
            f"Database file '{db_path}' does not exist, so it cannot be archived."
        )
    except FileNotFoundError:
        raise FileSystemError(f"File not found: '{db_path}' no longer exists.")
    except Exception as e:
        raise FileSystemError(
            f"Failed to archive db '{db_path}' to '{archive_path}'"
        ) from e


def create_db(db_path: str, table_name: str, column_names: List[str]) -> bool:
    # Create Db based on database column names passed as argument
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create table
        create_table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}"({", ".join([f'"{col}" TEXT' for col in column_names])})'
        cursor.execute(create_table_query)
        conn.commit()
        cursor = conn.cursor()
        # Remove the comments below to debug
        # cursor.execute("PRAGMA table_info(orangehrm_users);")
        # print("Actual DB Columns After Table Creation:", cursor.fetchall())
        return True
    except sqlite3.Error as e:
        if conn:
            conn.close()
        raise RuntimeError(f"Database creation failed for '{db_path}': {e}")


def load_table_data(db_path: str, table_name: str, data: List[Dict[str, Any]]) -> bool:
    if not data:
        raise ValueError("No data provided for insertion.")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Extract column names from the first column of the dictionary
        columns = list(data[0].keys())
        placeholders = ", ".join(["?" for _ in columns])
        query = (
            f'INSERT INTO "{table_name}" ({", ".join(columns)}) VALUES ({placeholders})'
        )
        # Get the data from the data passed into the arg
        values = [tuple(row[col] for col in columns) for row in data]

        print(f"Generated Query: {query}")
        print(f"Values: {values}")

        cursor.executemany(query, values)
        conn.commit()
        return True

    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to insert data into '{table_name}': {e}") from e


def select_table_data(db_path: str, table_name: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT * FROM '{table_name}'"
    cursor.execute(query)
    data = cursor.fetchall()
    for _ in data:
        print(_)


def compare_row_count_to_baseline(
    baseline_db: str, new_db: str, table_name: str
) -> bool:
    """Compares row counts between two databases and returns True if they match, otherwise False"""

    def get_table_row_count(conn: sqlite3.Connection, table_name: str) -> int:
        """Returns the total number of rows in a table."""
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        return cursor.fetchone()[0]

    # Open connections to both datbases
    conn_baseline = sqlite3.connect(baseline_db)
    conn_new = sqlite3.connect(new_db)

    try:
        count_baseline = get_table_row_count(conn_baseline, table_name)
        count_new = get_table_row_count(conn_new, table_name)

        print(f"Baseline DB Table Row Count: {count_baseline}")
        print(f"New DB Table Row Count: {count_new}")

        return count_baseline == count_new  # If they equal return True, else False

    except sqlite3.Error as e:
        print(f"Error comparing row counts: {e}")
        return False
    finally:
        conn_baseline.close()
        conn_new.close()


def identify_mismatched_rows(
    baseline_db: str, new_db: str, table_name: str, key_column: str
):
    """Identifies rows in the baseline_db that do not match the new_db.

    Returns:
        List of dictionaries with mismatch details.

    """
    conn_baseline = sqlite3.connect(baseline_db)
    conn_new = sqlite3.connect(new_db)

    cursor_baseline = conn_baseline.cursor()
    cursor_new = conn_new.cursor()

    mismatches = []

    try:
        # Get all data from both tables
        cursor_baseline.execute(f"SELECT * FROM {table_name}")
        data_baseline = {row[0]: row[1:] for row in cursor_baseline.fetchall()}

        cursor_new.execute(f"SELECT * FROM {table_name}")
        data_new = {row[0]: row[1:] for row in cursor_new.fetchall()}

        baseline_keys = set(data_baseline.keys())
        new_keys = set(data_new.keys())

        # Identify missing rows
        missing_in_new = baseline_keys - new_keys
        missing_in_baseline = new_keys - baseline_keys

        for key in missing_in_new:
            mismatches.append(
                {
                    "Database": "New DB",
                    "Issue": "Missing Row",
                    "Row ID": key,
                    "Data": data_baseline[key],
                }
            )

        for key in missing_in_baseline:
            mismatches.append(
                {
                    "Database": "Baseline DB",
                    "Issue": "Missing Row",
                    "Row ID": key,
                    "Data": data_new[key],
                }
            )

        # Identify mismatch raw data
        for key in baseline_keys & new_keys:
            if data_baseline[key] != data_new[key]:
                mismatches.append(
                    {
                        "Database": "Both",
                        "Issue": "Data Mismatches",
                        "Row ID": key,
                        "Baseline Data": data_baseline[key],
                        "New Data": data_new[key],
                    }
                )
    except sqlite3.Error as e:
        print(f"Error comparing database tables: {e}")
    finally:
        conn_baseline.close()
        conn_new.close()

    return mismatches
