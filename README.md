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


