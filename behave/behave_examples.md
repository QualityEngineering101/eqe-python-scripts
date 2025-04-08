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