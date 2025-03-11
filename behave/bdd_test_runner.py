import subprocess
import argparse

browsers = ["chrome", "edge", "firefox"]
parser = argparse.ArgumentParser(description="Run BDD tests across multiple browsers.")
parser.add_argument(
    "--headless",
    choices=["true", "false"],
    default="false",
    help="Run tests in headless mode (default: false)",
)
args = parser.parse_args()

for browser in browsers:
    print(f"Running tests in {browser.upper()}...(Headless = {args.headless})")
    subprocess.run(
        [
            "behave",
            "--no-capture",
            "--define",
            f"browser={browser}",
            "--define",
            f"headless={args.headless}",
        ]
    )
    print(f"Finished running tests in {browser.upper()}...")
