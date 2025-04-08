# Behave Examples

BDD implementation highlighting use of .feature file, step implementations, and environments.py


## Dependencies

  ` Python>=3.9, Behave=1.2.6, assertpy=1.1, selenium=4.29.0, webdriver-manager=4.0.2, urllib3=2.3.0, allure-behave=2.13.5
  `
  <br><br>Note:
  Requires [Google Chrome](https://www.google.com/chrome/), [Mozilla Firefox](https://www.mozilla.org/firefox/new/), and [Microsoft Edge](https://www.microsoft.com/edge) to be installed on your machine. WebDrivers are automatically handled by `webdriver-manager`, but the browsers themselves must be installed for the scripts to run correctly.

   **Features**:

* [home_page_visitor_experience.feature](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/home_page_visitor_experience.feature) - contains a (near) complete set of test scenarios for a given application feature written in plain text, focuses on what the application should do from a business perspective, removes all technical details
* [home_page_visitor_experience.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/steps/home_page_visitor_experience.py) - Translates business needs documented in the .feature file to actual automation steps, demonstrates use of asserts to report on failures, represents different XPATH methods (including executing javascript) to interact with the application, and utilizes WebDriverWait conditions to wait for web elements to be present or have visibility
* [bdd_test_runner.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/bdd_test_runner.py) - a simply python script that enables the passing of arguments to specify the mode to run in and uses subprocess and generator statements to execute the tests across multiple browsers
* [environment.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/environment.py) - enables setup and team down functions required across all tests, features, scenarios, and/or steps.
* [Optional] Allure Reports uses capture of test results in JSON files as input to a suite of HTML reports that are presented in webpage form as a working website.

## How to Clone and Run `behave`

These steps assume you're using Python 3.12+ and have `pip` available.

---

### 🌀 1. Clone the Repository

```bash
git clone https://github.com/QualityEngineering101/eqe-python-scripts.git
cd eqe-python-scripts/behave
```

---

### 📦 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # Linux/macOS
venv\Scripts\activate          # Windows
```

---

### 📥 3. Install Dependencies

```bash
pip install -r ../behave_requirements.txt
```

---

### ▶️ 4. Run the Project

```bash
behave
```

---

### 📈 5. View the Results

If successful, you should see:

* the script should have opened a browser and ran the tests automatically
* in addition to the individual steps being shown as being executed, you will see the final results as 
  - 1 feature passed, 0 failed, 0 skipped
  - 9 scenario passed, 0 failed, 0 skipped
  - 43 steps passed, 0 failed, 0 skipped, 0 undefined
