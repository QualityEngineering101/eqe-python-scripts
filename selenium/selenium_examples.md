### Selenium Examples

Automation scripts that create Selenium webdrivers, navigate to websites, finds or interacts with elements on the page.`QEWebDriverHelper.py` is a lightweight utility that standardizes browser setup for Selenium tests. It supports launching Chrome, Edge, and Firefox with simplified configuration for URL, browser type, and mode (headed/headless).

<span style="color:red"><strong>Note:</strong> This will only work sometimes since Amazon doesn't allow repeated automation scripts to run against their site. This script does implement a helper to show how that might work. However, this script is going to be rewritten to get change how it works and "come with" its own web server so we can hard code some functional website pages</span>

  `**Dependencies**: Python>=3.9, selenium=4.29.0, webdriver-manager=4.0.2
  `
  
  **Features**

* [QEWebDriverHelper.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/EQEUtils/QEWebDriverHelper.py) - automatic detection of installed browsers, manages WebDriver binaries, supports headed and headless execution modes, error handling and logging capabilities, cross-browser testing
* [browser_tester.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/selenium/src/browser_tester.py) - a demonstration script that leverages QEWebDriverHelper to launch broswers (Chrome, Edge, Firefox), interact with one set of code to test across browsers and publish test results, demonstrates interacting with different types of web elements

## How to Clone and Run `selenium`

These steps assume you're using Python 3.12+ and have `pip` available.

---

### 1. Clone the Repository

```bash
git clone https://github.com/QualityEngineering101/eqe-python-scripts.git
cd eqe-python-scripts/selenium
```

---

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # Linux/macOS
venv\Scripts\activate          # Windows
```

---

### 📥 3. Install Dependencies

```bash
pip install -r ../selenium_requirements.txt
```

---

### ▶️ 4. Run the Project

```bash
python src/browser_tester.py
```

This script will:

* Launch Chrome, Edge, and Firefox in headed mode
* Open <https://www.amazon.com> in each browser
* Pause briefly (5 seconds) to allow visual confirmation
* Automatically close the browsers

**Tip**: If any browser fails to launch, ensure it is installed and compatible with `webdriver-manager`.

---

### 📈 5. View the Results

Review the opened browser windows during execution. No logs or reports are generated—this is a visual demo.
