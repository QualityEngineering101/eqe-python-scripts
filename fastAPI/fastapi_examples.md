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

---

#### DevOps or CI/CD/CT Automation

Includes multiple GitHub Actions workflows that handle test execution, containerization, and deployment to GCP VMs in test and production environments. SSH-based deploys are used for VM orchestration with post-deployment validation.

  `**Dependencies**: docker, pytest=8.3.4, GitHub Actions runners (ubuntu-latest)
  `

**Key files:**

* `Dockerfile` – Containerizes the FastAPI app for local use, testing, or deployment

**GitHub Workflows:**

* `.github/workflows/dev-check-in-tests.yml` - Runs pytest suite for any branch matching `fastAPI*` on push/PR  
* `.github/workflows/build-and-deploy-test.yml` - Builds, tests, and deploys to the **Test environment** when `fastAPI` is pushed  
* `.github/workflows/build-and-deploy-prod.yml` - Builds, tests, and deploys to the **Production environment** on `main` branch push  
* `.github/workflows/deploy.yml` - Runs after successful test completion (from "API Tests" workflow); builds Docker image, runs tests inside container, pushes to Docker Hub, and deploys to GCP  
* `.github/workflows/test-connectivity-test.yml` & `prod-connectivity-test.yml` - Manually triggered SSH connectivity checks for **Test** and **Production** VMs, ensuring GitHub Actions can connect before full deployment flows

## How to Clone and Run `fastAPI`

These steps assume you're using Python 3.12+ and have `pip` available.

---

### 1. Clone the Repository

```bash
git clone https://github.com/QualityEngineering101/eqe-python-scripts.git
cd eqe-python-scripts/fastAPI
```

---

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # Linux/macOS
venv\Scripts\activate          # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r ../fastAPI_requirements.txt
```

---

### 4a. Run the Project (Locally)

**Run locally using uvicorn**

The first step is to run uvicorn that will accept and respond to API requests:

* open a git bash terminal window
* make sure you're in the project directory

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

* You should see something like

```text

INFO:     Will watch for changes in these directories: [..\\fastAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [30092] using StatReload
INFO:     Started server process [19872]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

**Run Pytest to execute tests**

The next step is to run your Pytest tests in a separate terminal

* open a git bash terminal window
* make sure you're in the project directory

```bash
pytest tests/

```

---

### 5. View the Results

You should see the following output when run successfully:

```
========================================= test session starts ==========================================
platform win32 -- Python 3.13.2, pytest-8.3.4, pluggy-1.5.0
rootdir: ...\fastAPI
configfile: pytest.ini
plugins: allure-pytest-2.13.5, anyio-4.9.0, asyncio-0.25.3
asyncio: mode=Mode.AUTO, asyncio_default_fixture_loop_scope=module
collected 36 items

tests\test_100_products ................         [ 44%]
tests\test_200_test_plans ..............         [ 83%]
tests\test_300_test_suites ....                  [ 94%]
tests\test_400_association_plans_suites ..       [100%]

========================================= 36 passed in 0.59s ============================================ 

````

## 4b. CI/CD/CT Automation – How to Trigger and Verify Pipelines

This FastAPI project uses GitHub Actions for continuous integration, testing, and deployment (CI/CD/CT). Below are instructions for triggering and monitoring each stage of the pipeline.

Note: you can execute step 4a without step 4b but to get the full CI-CD-CT experience using GitHub, you need to also run step 4b.

---

### Preconditions

This project requires access to GCP VMs configured as **Test** and **Production** environments.

You have two options:

* Provision your own VMs (ensure SSH access, Python is installed, Docker is installed, and port 8000 is open)

* Or, [open an issue](https://github.com/QualityEngineering101/eqe-python-scripts/issues/new) to request access to the shared FastAPI Test/Prod environments (subject to availability)

---

### 1. Dev Check-in Tests

These tests run automatically for branches that start with `fastAPI`.

**Triggering:**

* Push to a branch like `fastAPI-feature-xyz`
* Create a pull request targeting any `fastAPI*` branch

**Runs:** `.github/workflows/dev-check-in-tests.yml`

**What it does:**

* Checks out the `fastAPI` folder

* Sets up Python 3.11 and a virtual environment
* Installs dependencies
* Runs the full `pytest` suite inside `fastAPI/tests`

**Verify:**  
Go to GitHub → Actions → "Dev Check-in Tests (API)"  
Or check your PR status for pass/fail badge.

---

### 2. Build and Deploy to Test Environment

**Triggering:**  

* Push to the `fastAPI` branch

**Runs:** `.github/workflows/build-and-deploy-test.yml`

**What it does:**

* Builds Docker image for the FastAPI app
* Runs tests inside the container
* Deploys to a remote GCP Test VM via SSH
* Re-runs tests inside the deployed container to confirm health

**Verify:**

* GitHub Actions → "Build and Deploy to Test Env (API)"
* Look for deployment steps: Docker build, SSH connection, post-deploy test logs

---

### 3. Build and Deploy to Prod Environment

**Triggering:**  

* Push to the `main` branch

**Runs:** `.github/workflows/build-and-deploy-prod.yml`

**What it does:**

* Same steps as the Test environment deploy
* Targets the **Production VM** (using separate secrets)

**Verify:**

* GitHub Actions → "Build and Deploy to Prod Env (API)"
* Check for image tagging, SSH steps, and container health validation

---

### 4. Triggered Pipeline: CI/CD FastAPI Deployment

**Runs on:** Completion of another workflow (e.g., "API Tests")

**Runs:** `.github/workflows/deploy.yml`

**What it does:**

* Listens for successful runs of other workflows (like `dev-check-in-tests`)
* If triggered, it:
  * Builds Docker image
  * Runs tests
  * Pushes image to Docker Hub
  * Deploys it to GCP
  * Validates deployment via container-based `pytest`

**Verify:**

* GitHub Actions → "CI/CD Pipeline - FastAPI Deployment to Google Cloud"

---

### 5. Connectivity Checks (Manual)

**Trigger manually** from GitHub → Actions → `prod-connectivity-test.yml` or `test-connectivity-test.yml`

**What it does:**

* Uses SSH to connect to GCP VM
* Confirms that GitHub Actions can reach your deployment targets

---

### Tips

* Make sure required GitHub secrets are set:
  * `SERVER_HOST`, `SERVER_USER`, `SERVER_SSH_KEY` (for test)
  * `*_PROD` variants for production
* All Docker images are tagged and pushed using the `DOCKER_USERNAME` secret
* Ports used: `8000` for the FastAPI app
