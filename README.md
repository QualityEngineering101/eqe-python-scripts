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
  - [QEWebDriverHelper.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/EQEUtils/QEWebDriverHelper.py) - automatic detection of installed browsers, manages WebDriver binaries, supports headed and headless execution modes, error handling and logging capabilities, cross-browser testing
  - [browser_tester.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/browser_tester.py) - a demonstration script that leverages QEWebDriverHelper to launch broswers (Chrome, Edge, Firefox), interact with one set of code to test across browsers and publish test results, demonstrates interacting with different types of web elements

  **How to clone and run**
  
  [Coming Soon!]

### Behave Examples 
BDD implementation highlighting use of .feature file, step implementations, and environments.py

  `**Dependencies**: Behave=1.2.6, assertpy=1.1, selenium=4.29.0, webdriver-manager=4.0.2, urllib3=2.3.0, allure-behave=2.13.5`
   
   **Features**:
  - [home_page_vsitor_experience.feature](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/home_page_visitor_experience.feature) - contains a (near) complete set of test scenarios for a given application feature written in plain text, focuses on what the application should do from a business perspective, removes all technical details
  - [home_page_visitor_experience.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/steps/home_page_visitor_experience.py) - Translates business needs documented in the .feature file to actual automation steps, demonstrates use of asserts to report on failures, represents different XPATH methods (including executing javascript) to interact with the application, and utilizes WebDriverWait conditions to wait for web elements to be present or have visibility
  - [bdd_test_runner.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/bdd_test_runner.py) - a simply python script that enables the passing of arguments to specify the mode to run in and uses subprocess and generator statements to execute the tests across multiple browsers
  - [environment.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/environment.py) - enables setup and team down functions required across all tests, features, scenarios, and/or steps.
  - [Optional] Allure Reports uses capture of test results in JSON files as input to a suite of HTML reports that are presented in webpage form as a working website.

  **How to clone and run**
  
  [Coming Soon!]


### Sqlite3 Examples
Demonstrates creating and archiving a database, creating table, loading data, and then performing full compare validations across databases and tables

  `**Dependencies**: selenium=4.29.0`
  
  **Features**: 
  - [get_orangehrm_su_data.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/get_orangehrm_su_data.py) - a script that logs into a demo website, navigates pages using menu/menu items, extracts user data from objects, and packages that data into a structure that can be used by other python scripts
  - [database_utils.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/database_utils.py) - a collection of database utilities that creates sqlite3 databases, archives databases, loads data from a list passed to it, and then performs multiple validations like row counts and complete database table validation. Can be used for implementing baseline compares (run yesterday, run today, compare the results). Database code is decopled from application logic so that we maximize reusability.
  - [extract_and_compare.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/extract_and_compare.py) - a test runner that executes the full compliment of steps from invoking the browser, to nagivating to the application, getting the data, archiving the database, creating and loading data into the database and performing all of the compares.

  **How to clone and run**
  
  [Coming Soon!]

### fastAPI (with Github Actions enabling CI/CT)
![example workflow](https://github.com/QualityEngineering101/eqe-python-scripts/actions/workflows/WORKFLOW-FILE/badge.svg)
Demonstrates using fastAPI, pydantic, and SQLAlchemy to create APIs, pytest to execute a suite of test cases for those APIs, and GitHub actions to run the tests when code is pushed to GitHub.

  `**Dependencies**: fastapi==0.115.11, httpx==0.28.1, pydantic==2.10.6, pytest==8.3.4, pytest-asyncio==0.25.3, SQLAlchemy==2.0.39, uvicorn==0.34.0`

  **Features**: 
  - [Coming soon!] 
  - [Coming soon!]

    **How to clone and run**
  
  [Coming Soon!]