import os
import re
import subprocess
from pathlib import Path

FEATURE_FILE = "features/login.feature"
STEPS_FILE = "features/steps/login_steps.py"

# Mapping Gherkin keywords to Behave decorators
step_keywords = {
    "Given": "@given",
    "When": "@when",
    "Then": "@then",
    "And": None  # We'll reuse the previous keyword
}

def sanitize_step_text(text):
    return re.sub(r'[^a-zA-Z0-9_]', '_', text.strip().lower())

def extract_steps_from_feature(file_path):
    steps = []
    current_decorator = None

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if any(line.startswith(k) for k in step_keywords):
                keyword = next(k for k in step_keywords if line.startswith(k))
                step_text = line[len(keyword):].strip()

                if keyword == "And":
                    if current_decorator is None:
                        continue  # Malformed scenario
                else:
                    current_decorator = step_keywords[keyword]

                steps.append((current_decorator, step_text))
    return steps

def generate_step_definitions(steps, output_file):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))

    with open(output_file, "w") as f:
        f.write("from behave import given, when, then\n")
        f.write("from selenium import webdriver\n")
        f.write("from selenium.webdriver.common.by import By\n")
        f.write("from selenium.webdriver.chrome.options import Options\n")
        f.write("import time\n\n")
        f.write("driver = None\n\n")

        for decorator, step_text in steps:
            # Replace <param> with {param}
            decorated_text = re.sub(r"<(.*?)>", r"{\1}", step_text)
            func_name = sanitize_step_text(decorated_text)

            # Extract parameters from the decorated text
            param_names = re.findall(r"{(.*?)}", decorated_text)
            param_args = ", ".join(["context"] + param_names)

            f.write(f"{decorator}('{decorated_text}')\n")
            f.write(f"def step_{func_name}({param_args}):\n")

            # Step-specific logic
            if "the browser is open" in step_text:
                f.write("    global driver\n")
                f.write("    options = Options()\n")
                f.write("    driver = webdriver.Chrome(options=options)\n")
                f.write("    driver.maximize_window()\n")
                f.write("    driver.implicitly_wait(10)\n")
            
            elif "navigates to the {site}" in decorated_text:
                f.write("    driver.get(site)\n")

            elif "username field" in decorated_text:
                f.write("    driver.find_element(By.NAME, \"username\").send_keys(username)\n")

            elif "password field" in decorated_text:
                f.write("    driver.find_element(By.NAME, \"password\").send_keys(password)\n")

            elif "clicks the login button" in step_text:
                f.write("    driver.find_element(By.XPATH, \"//button[@type='submit']\").click()\n")

            elif "should see the Dashboard page" in step_text:
                f.write("    time.sleep(2)\n")
                f.write("    assert \"dashboard\" in driver.current_url.lower()\n")

            elif "logs out" in step_text:
                f.write("    driver.find_element(By.CLASS_NAME, \"oxd-userdropdown-tab\").click()\n")
                f.write("    time.sleep(1)\n")
                f.write("    driver.find_element(By.XPATH, \"//a[text()='Logout']\").click()\n")

            elif "should see the login form" in step_text:
                f.write("    time.sleep(2)\n")
                f.write("    assert driver.find_element(By.NAME, \"username\").is_displayed()\n")
                f.write("    assert driver.find_element(By.NAME, \"password\").is_displayed()\n")

            else:
                f.write("    # TODO: Implement this step\n")
                f.write("    pass\n\n")

    print(f"✅ Step definitions with logic generated in {output_file}")

def run_behave():
    print("\n🚀 Running Behave test suite...\n")
    subprocess.run(["behave","-v"], cwd=Path(__file__).resolve().parent)

if __name__ == "__main__":
    steps = extract_steps_from_feature(FEATURE_FILE)
    generate_step_definitions(steps, STEPS_FILE)
    run_behave()
