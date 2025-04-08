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

  `**Dependencies**: Python>=3.9, selenium=4.29.0, webdriver-manager=4.0.2
  `
  
  **Features**:

* [QEWebDriverHelper.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/EQEUtils/QEWebDriverHelper.py) - automatic detection of installed browsers, manages WebDriver binaries, supports headed and headless execution modes, error handling and logging capabilities, cross-browser testing
* [browser_tester.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/browser_tester.py) - a demonstration script that leverages QEWebDriverHelper to launch broswers (Chrome, Edge, Firefox), interact with one set of code to test across browsers and publish test results, demonstrates interacting with different types of web elements

  **How to clone and run**
  
  [Coming Soon!]

### Behave Examples

BDD implementation highlighting use of .feature file, step implementations, and environments.py

  `**Dependencies**: Behave=1.2.6, assertpy=1.1, selenium=4.29.0, webdriver-manager=4.0.2, urllib3=2.3.0, allure-behave=2.13.5
  `

   **Features**:

* [home_page_vsitor_experience.feature](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/home_page_visitor_experience.feature) - contains a (near) complete set of test scenarios for a given application feature written in plain text, focuses on what the application should do from a business perspective, removes all technical details
* [home_page_visitor_experience.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/steps/home_page_visitor_experience.py) - Translates business needs documented in the .feature file to actual automation steps, demonstrates use of asserts to report on failures, represents different XPATH methods (including executing javascript) to interact with the application, and utilizes WebDriverWait conditions to wait for web elements to be present or have visibility
* [bdd_test_runner.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/bdd_test_runner.py) - a simply python script that enables the passing of arguments to specify the mode to run in and uses subprocess and generator statements to execute the tests across multiple browsers
* [environment.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/environment.py) - enables setup and team down functions required across all tests, features, scenarios, and/or steps.
* [Optional] Allure Reports uses capture of test results in JSON files as input to a suite of HTML reports that are presented in webpage form as a working website.

  **How to clone and run**
  
  [Coming Soon!]

### BDD Step Auto Generation

Script that parses `.feature` files and auto-generates matching `*_steps.py` implementations for each scenario and step. Currently set up to work with a `features/login.feature` file and produce `features/steps/login_steps.py`.

  `**Dependencies** Python>=3.9
  `

  **Features**

* [stepgen.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/bdd-step-autogen/stepgen.py) - Scans feature files for BDD steps (Given/When/Then), generates structured and commented Python step definitions in the appropriate `steps/` directory, skips duplicates, and supports incremental regeneration.

  **How to clone and run**

  [Coming Soon!]

### Sqlite3 Examples

Demonstrates creating and archiving a database, creating table, loading data, and then performing full compare validations across databases and tables

  `**Dependencies**: selenium=4.29.0
  `
  
  **Features**:

* [get_orangehrm_su_data.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/get_orangehrm_su_data.py) - a script that logs into a demo website, navigates pages using menu/menu items, extracts user data from objects, and packages that data into a structure that can be used by other python scripts
* [database_utils.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/database_utils.py) - a collection of database utilities that creates sqlite3 databases, archives databases, loads data from a list passed to it, and then performs multiple validations like row counts and complete database table validation. Can be used for implementing baseline compares (run yesterday, run today, compare the results). Database code is decopled from application logic so that we maximize reusability.
* [extract_and_compare.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/sqlite3/extract_and_compare.py) - a test runner that executes the full compliment of steps from invoking the browser, to nagivating to the application, getting the data, archiving the database, creating and loading data into the database and performing all of the compares.

  **How to clone and run**
  
  [Coming Soon!]

### FastAPI - API Development, Automated Testing, and CI/CD/CT Pipeline Automation (with GitHub and Docker)

#### API Development

Implements modern Python-based APIs using [FastAPI](https://fastapi.tiangolo.com/), [Pydantic](https://docs.pydantic.dev/), and [SQLAlchemy](https://www.sqlalchemy.org/). This solution enables API creation, data validation, and database interaction with clean separation of concerns.

  `**Dependencies**: fastapi=0.115.1, pydantic=2.10.6, sqlalchemy=2.0.39
  `

**Key files:**
* `main.py` – Initializes the FastAPI app and includes route definitions
* `schemas.py`, `app_models.py` – Defines Pydantic models for validation and SQLAlchemy models for persistence
* `app_db.py`, `db_init.py` – Manages database sessions and initialization logic
* `crud.py` – Centralizes DB operations in a reusable data access layer
* `seed_db.py` – Provides database seed logic for test/demo data
* `routes/` – Contains all route files, grouped by domain:
  * `product_routes.py`
  * `test_plan_routes.py`
  * `test_suite_routes.py`

---

#### Automated Testing

Comprehensive test suite built with `pytest`, organized into layered test files for validating business logic and API contract behavior. Tests are built to run both locally and inside a containerized CI pipeline.

  `**Dependencies**: pytest=8.3.4, fastapi=0.115.1
  `

**Key files:**
* `tests/conftest.py` – Provides shared test fixtures
* `tests/test_100_products.py` – Product API tests
* `tests/test_200_test_plans.py` – Test Plan API tests
* `tests/test_300_test_suites.py` – Test Suite API tests
* `tests/test_400_association_plans_suites.py` – Association logic tests
* `tests/old_test_TestProducts.py` – Deprecated or experimental test stub

---

#### DevOps or CI/CD/CT Automation

Includes multiple GitHub Actions workflows that handle test execution, containerization, and deployment to GCP VMs in test and production environments. SSH-based deploys are used for VM orchestration with post-deployment validation.

  `**Dependencies**: docker, pytest=8.3.4, GitHub Actions runners (ubuntu-latest)
  `

**Key files:**
* `Dockerfile` – Containerizes the FastAPI app for local use, testing, or deployment

**GitHub Workflows:**
* `.github/workflows/dev-check-in-tests.yml`  
  ➤ Runs pytest suite for any branch matching `fastAPI*` on push/PR  
* `.github/workflows/build-and-deploy-test.yml`  
  ➤ Builds, tests, and deploys to the **Test environment** when `fastAPI` is pushed  
* `.github/workflows/build-and-deploy-prod.yml`  
  ➤ Builds, tests, and deploys to the **Production environment** on `main` branch push  
* `.github/workflows/deploy.yml`  
  ➤ Runs after successful test completion (from "API Tests" workflow); builds Docker image, runs tests inside container, pushes to Docker Hub, and deploys to GCP  
* `.github/workflows/test-connectivity-test.yml` & `prod-connectivity-test.yml`  
  ➤ Manually triggered SSH connectivity checks for **Test** and **Production** VMs, ensuring GitHub Actions can connect before full deployment flows
  
  [Coming Soon!]
