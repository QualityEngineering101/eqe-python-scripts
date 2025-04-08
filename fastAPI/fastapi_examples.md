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