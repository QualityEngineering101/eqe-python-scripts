# EQE-PYTHON-SCRIPTS
## Project Details
This project provides examples of using python with existing packages to accelerate learning or implementation of automation scripts by quality engineers, automation engineers, or quality assurance analysts. 

### Sub Directories
* [selenium](https://github.com/QualityEngineering101/eqe-python-scripts/tree/main/selenium) - scripts created using selenium
* [behave](https://github.com/QualityEngineering101/eqe-python-scripts/tree/main/behave) - scripts created using the behave package (BDD) with selenium
* [sqlite3](https://github.com/QualityEngineering101/eqe-python-scripts/tree/main/sqlite3) - scripts created using the sqlite3 db package with selenium
* (coming soon) playwright - scripts created using playwright

## Feature List
### Selenium Examples
Automation scripts that create Selenium webdrivers, navigate to websites, finds or interacts with elements on the page.

  `**Dependencies**: Python>=3.9, selenium=4.29.0, webdriver-manager=4.0.2`
  
  **Features**:
  - [QEWebDriverHelper.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/EQEUtils/QEWebDriverHelper.py)
  - [browser_tester.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/browser_tester.py)

### Behave Examples 
BDD implementation highlighting use of .feature file, step implementations, and environments.py

  `**Dependencies**: Behave=1.2.6, assertpy=1.1, selenium=4.29.0, webdriver-manager=4.0.2, urllib3=2.3.0, allure-behave=2.13.5`
   
   **Features**:
  - [home_page_vsitor_experience.feature](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/home_page_visitor_experience.feature)
  - [home_page_visitor_experience.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/steps/home_page_visitor_experience.py)
  - [bdd_test_runner.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/bdd_test_runner.py)
  - [environment.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/environment.py)
  - Optionally: Allure Reports ...

### Sqlite3 Examples
Demonstrates creating and archiving a database, creating table, loading data, and then performing full compare validations across databases and tables

  `**Dependencies**: selenium=4.29.0`
  
  **Features**: 
  - [get_orangehrm_su_data.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/get_orangehrm_su_data.py)
  - [database_utils.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/database_utils.py)
  - [extract_and_compare.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/extract_and_compare.py)

