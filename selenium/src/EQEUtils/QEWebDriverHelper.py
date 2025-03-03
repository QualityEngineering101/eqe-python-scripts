import os
import logging
import platform
import shutil
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

class BrowserPathDetector:
    """Detects the installation path of browsers dynamically."""
    BROWSER_PATHS: dict[str,str] = {}
    
    COMMON_BROWSER_PATHS = {
        "Chrome": [
            r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        ],
        "Edge": [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        ], 
        "Firefox": [
            r"C:\Program Files\Mozilla Firefox\firefox.exe",
            r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
        ]
    }
    
    BROWSER_COMMANDS = {
        "Windows": "where",
        "Darwin": "which",
        "Linux": "which"
    }

    @staticmethod
    def get_browser_path(browser: str) -> str:
        """ Attempts to find the browser's installation paths efficiently. """
        if browser in BrowserPathDetector.BROWSER_PATHS:
            return BrowserPathDetector.BROWSER_PATHS[browser]
        
        system = platform.system()
        logging.info(f"Locating {browser} on {system}...")
        print(f"System information: {system}")
        
        if system == "Windows":
            for path in BrowserPathDetector.COMMON_BROWSER_PATHS.get(browser, []):
                if os.path.exists(path):
                    logging.info(f"Found {browser} at {path}")
                    BrowserPathDetector.BROWSER_PATHS[browser] = path
                    return path
                else:
                    logging.warning(f"Not found: {path}")
                    
        # User shutil.which as a faster check (cross-platform)
        path = shutil.which(browser.lower()) or ""
        if not path:
            try:
                command = f"where {browser}" if system == "Windows" else f"which {browser}"
                output = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL).decode().strip()
                path = output.split("\n")[0] if output else ""
            except subprocess.CalledProcessError:
                logging.warning(f"{browser} not found using {command}.")
        
        if path:
            logging.info(f"Found {browser} at {path}")
            BrowserPathDetector.BROWSER_PATHS[browser] = path
        else:
            logging.warning(f"{browser} not installed or not found.")
        
        return path

class QEWebDriverHelper:
    """
    A helper class for automating web browser interactions using Selenium WebDriver.

    This class simplifies the setup of Chrome, Edge, and Firefox browsers by:
    - Automatically detecting installed browsers.
    - Managing WebDriver binaries using `webdriver-manager`.
    - Supporting both headless and headed modes.

    Attributes:
        CHROME (str): Constant for Chrome browser.
        EDGE (str): Constant for Edge browser.
        FIREFOX (str): Constant for Firefox browser.
        SUPPORTED_BROWSERS (set): Set of supported browser names.

    Args:
        browser (str): The browser to use (e.g., "Chrome", "Edge", "Firefox").
        url (str): The URL to navigate to after browser launch.
        mode (str, optional): "headed" for visible UI, "headless" for background execution. Defaults to "headed".

    Raises:
        ValueError: If an unsupported browser is provided.
        RuntimeError: If the browser or WebDriver is missing.

    Methods:
        get_driver() -> WebDriver:
            Returns the active WebDriver instance.

        quit() -> None:
            Closes the WebDriver session.

    Example:
        >>> browser_helper = QEWebDriverHelper(browser="Chrome", url="https://www.google.com", mode="headless")
        >>> driver = browser_helper.get_driver()
        >>> print(driver.title)
        >>> browser_helper.quit()
    """
    CHROME = "Chrome"
    EDGE = "Edge"
    FIREFOX = "Firefox"
    SUPPORTED_BROWSERS = {CHROME, EDGE, FIREFOX}

    def __init__(self, browser: str, url: str, mode: str = "headed"):
        browser = browser.capitalize()
        if browser not in self.SUPPORTED_BROWSERS:
            raise ValueError(f"Unsupported browser: {browser}. Use one of: {self.SUPPORTED_BROWSERS}")
        self.browser = browser
        self.url = url
        self.mode = mode
        self.driver = self._setup_driver()

    def _setup_driver(self):
        if self.browser == self.CHROME:
            return self._setup_chrome()
        elif self.browser == self.EDGE:
            return self._setup_edge()
        elif self.browser == self.FIREFOX:
            return self._setup_firefox()

    def _setup_chrome(self):
        options = webdriver.ChromeOptions()
        browser_path = BrowserPathDetector.get_browser_path("Chrome")
        if not browser_path:
            raise RuntimeError("Chrome is not installed or could not be found.")
        options.binary_location = browser_path
        if self.mode == "headless":
            options.add_argument("--headless=new")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return self._initialize_driver(driver)

    def _setup_edge(self):
        options = webdriver.EdgeOptions()
        browser_path = BrowserPathDetector.get_browser_path("Edge")
        if not browser_path:
            raise RuntimeError("Edge is not installed or could not be found.")
        options.binary_location = browser_path
        if self.mode == "headless":
            options.add_argument("--headless")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        return self._initialize_driver(driver)

    def _setup_firefox(self):
        options = webdriver.FirefoxOptions()
        browser_path = BrowserPathDetector.get_browser_path("Firefox")
        if not browser_path:
            raise RuntimeError("Firefox is not installed or could not be found.")
        options.binary_location = browser_path
        if self.mode == "headless":
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        return self._initialize_driver(driver)

    def _initialize_driver(self, driver):
        logging.info(f"✅ Navigating to {self.url}")
        driver.get(self.url)
        if self.mode == "headed":
            driver.maximize_window()
        driver.implicitly_wait(5)
        return driver

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            logging.info(f"🔄 Closing {self.browser} WebDriver.")
            self.driver.quit()