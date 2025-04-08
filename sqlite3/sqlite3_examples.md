### Sqlite3 Examples

Demonstrates creating and archiving a database, creating table, loading data, and then performing full compare validations across databases and tables

  `**Dependencies**: selenium=4.29.0
  `
  
  **Features**:

* [get_orangehrm_su_data.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/get_orangehrm_su_data.py) - a script that logs into a demo website, navigates pages using menu/menu items, extracts user data from objects, and packages that data into a structure that can be used by other python scripts
* [database_utils.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/database_utils.py) - a collection of database utilities that creates sqlite3 databases, archives databases, loads data from a list passed to it, and then performs multiple validations like row counts and complete database table validation. Can be used for implementing baseline compares (run yesterday, run today, compare the results). Database code is decopled from application logic so that we maximize reusability.
* [extract_and_compare.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/extract_and_compare.py) - a test runner that executes the full compliment of steps from invoking the browser, to nagivating to the application, getting the data, archiving the database, creating and loading data into the database and performing all of the compares.

## How to Clone and Run `sqlite3`

These steps assume you're using Python 3.12+ and have `pip` available.

---

### 🌀 1. Clone the Repository

```bash
git clone https://github.com/QualityEngineering101/eqe-python-scripts.git
cd eqe-python-scripts/sqlite3
```

---

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # Linux/macOS
venv\Scripts\activate          # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r ../sqlite3_requirements.txt
```

---

### 4. Run the Project

```bash
python extract_and_compare.py
```

---

### 5. View the Results

* Run it the first time and you should get a list of database differences since your baseline would not have yet been established.
* Run it a second time and you should get confirmation that there are no differences as noted in this screenshot:

```text

Data from site was loaded into new database.
Baseline DB Table Row Count: 8
New DB Table Row Count: 8
Baseline DB Row Count equals New DB Row Count.
No mismatches found. Tables are identical.

```
