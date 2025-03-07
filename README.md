# EQE-PYTHON-SCRIPTS
## Project Details
This project provides examples of using python with existing packages to accelerate learning or implementation of automation scripts by quality engineers, automation engineers, or quality assurance analysts. 

### Sub Directories
* selenium - scripts created using selenium
* playwright - scripts created using playwright
* behave - scripts created using the behave package (BDD)

## Feature List
### Selenium
<table valign="top" text-align:left>
  <tr>
    <th>Feature</th>
    <th>Description</th>
    <th>Benefits</th>
    <th>Dependencies (found in requirements.txt)</th>
  </tr>
  <tr>
    <td valign="top" text-align:left;><a href="https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/EQEUtils/QEWebDriverHelper.py">QEWebDriverHelper</a> </td>
    <td valign="top"; text-align:left;>QEWebDriverHelper is a Python-based utility that simplifies browser automation using Selenium WebDriver. It automatically detects installed browsers, manages WebDriver binaries, and supports both headless and headed modes.<br><br> As a helper module, it abstracts the setup of Selenium WebDriver, enabling seamless browser automation by ensuring:<br><br>
    <ul valign="top">
      <li>WebDrivers are always up to date.</li>
      <li>Installed browsers are automatically detected</li>
      <li>Test execution is reliable with configurable options</li>
    </ul></td>
    <td valign="top" text-align:left;>
      <ul valign="top">
        <li>Automated Browser Detection: Dynamically finds installed broswers (Chrome, Edge, Firefox)</li>
        <li>WebDriver Management: Users webdriver-manager to install and manage WebDrivers automatically</li>
        <li>Cross-Browser Testing: Supports Chrome, Edge, and Firefox with a unified API</li>
        <li>Headless Mode Support: Allows tests to run in the background for faster execution. (Also support headed versions)</li>
        <li>Error Handling & Logging: Provides detailed logs for debugging and diagnostics</li>
      </ul>
    </td>
    <td valign="top" text-align:left;>
      <ul>
        <li>Python>=3.9
        <li>selenium=4.29.0</li>
        <li>webdriver-manager=4.0.2</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/browser_tester.py">browser_tester</a></td>
    <td valign="top">A demonstration script that leverages QEWebDriverHelper to: <br><br>
      <ul>
        <li>Launch Chrome, Edge, and Firefox.</li>
        <li>Navigate to a sample login page (OrangeHRM demo site).</li>
        <li>Automate login and verify the dashboard page.</li>
        <li>Print test results based on expected vs. actual outcomes.</li>
      </ul>
    </td>
    <td valign="top">Demonstrates how to import and use QEWebDriverHelper to create three browsers, find and interact with web elements using one set of code, and publish the results.<br><br>
      <uL>
        <li>Demonstrates QEWebDriverHelper in Action: Provides a real-world example of how to use QEWebDriverHelpher.py to showcase cross-browser automation without needing manual setup</li>
        <li>Validates Cross-Browser Compatibility: Runs the same test across Chrome, Edge, and Firefox to detect inconsistencies and helps ensure web applications work consistently across different browsers</li>
        <li>Automates Login and Functional Testing: Logs into the OrangeHRM demo site and verifies successful authentication by simulating user interactions (typing credentials, clicking buttons)</li>
        <li>Supports Headless Execution for Faster Testing: Runs in headless mode, reducing resource consumption and execution time, making it ideal for CI/CD pipelines and automated regression. Also supports "Headed" execution for debugging.</li>
        <li>Provides Clear Pass/Fail Test Results: Compares expected resumes to actual results and prints results in an easy-to-read format enabling quick detection of test failures without requiring manual inspection</li>
        <li>Enhances Dubugging with Logging and Error Handling: Prints browser detection results and execution steps, capturing errors when elements are not found to prevent silent failures </li>
        <li>Saves Time and Reduces Manual Effort: Eliminates the need to write additional or redudant code while configuring multiple browsers. Enables the creation of a single test with consistent test steps across all browsers.</li>
      </uL>
    </td>
    <td valign="top">
      <ul>
        <li>Python>=3.9</li>
        <li>selenium=4.29.0</li>
        <li>webdriver-manager=4.0.2</li>
      </ul>
    </td>
  </tr>
</table>
        
### Behave

<table valign="top" text-align:left>
  <tr>
    <th>Feature</th>
    <th>Description</th>
    <th>Benefits</th>
    <th>Dependencies (found in requirements.txt)</th>
  </tr>
  <tr>
    <td valign="top" text-align:left;><a href="https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/steps/home_page_visitor_experience.feature">Home_page_visitor_experience</a> </td>
    <td valign="top"; text-align:left;>The home_page_visitor_experience feature file is written in Gherkin format and defines the application's behavior from a business perspective, guiding its expected interactions and outcomes:<br><br>
    <ul valign="top">
      <li>Uses plain English-like syntax, making it easy for non-technical stakholders (business analysists, testers, product owners) to understand</li>
      <li>The given-when-then structure ensures clarity in describing test scenarios</li>
      <li>Step definitions (e.g. 'When I enter a username' can be used across multiple feature files, reducing redundant test code</li>
      <li>Focuses on what the application should do (behavior) rather than just implementation details.</li>
      <li>Implements reusable steps to reduce redundancy and complexity of code</li>
    </ul></td>
    <td valign="top" text-align:left;>
      <ul valign="top">
        <li>Demonstrates a (near) complete set of validations for a web UI</li>
        <li>Implements simple page validations, data entry, and web element actions</li>
      </ul>
    </td>
    <td valign="top" text-align:left;>
      <ul>
        <li>Behave=1.2.6</li>
        <li>assertpy=1.1</li>
        <li>allure-behave=2.13.5 (optional reporting)</li>
        <li>selenium=4.29.0</li>
        <li>webdriver-manager=4.0.2</li>
    </td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/steps/home_page_visitor_experience.py">Home_page_visitor_experience.py</a></td>
    <td valign="top">The step implementations associated with Given-When-Then in the Home_page_visitor_experience.feature file. Steps in the feature file marked as 'and' or 'but' take on the decorator associated with its parent.<br><br>
      <ul>
        <li>Decorator tags highlight the feature file action or validation</li>
        <li>Each step has unique naming to help in debugging and to better understand the code</li>
        <li>Uses Assert_that to validate the results of each verification point</li>
        <li>Represents various ways of identifying web elements by XPATH including Axes</li>
        <li>Uses various WebDriverWait conditions to demonstrate how to implement them</li>
      </ul>
    </td>
    <td valign="top"> <br><br>
    </td>
    <td valign="top">
      <ul>
        <li>Behave=1.2.6</li>
        <li>assertpy=1.1</li>
        <li>selenium=4.29.0</li>
        <li>webdriver-manager=4.0.2</li>
        <li>urllib3==2.3.0</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top"><a href="https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/behave/features/environment.py">environment.py</a></td>
    <td valign="top">Enables setup and tear down functions required across all tests, features, scenarios, or steps.</td>
    <td valign="top"> <br><br>
    </td>
    <td valign="top">
      <ul>
        <li>Behave=1.2.6</li>
        <li>assertpy=1.1</li>
        <li>selenium=4.29.0</li>
        <li>webdriver-manager=4.0.2</li>
        <li>urllib3==2.3.0</li>
      </ul>
    </td>
  </tr>      
</table>


