### BDD Step Auto Generation

Script that parses `.feature` files and auto-generates matching `*_steps.py` implementations for each scenario and step. Currently set up to work with a `features/login.feature` file and produce `features/steps/login_steps.py`.

  `**Dependencies** Python>=3.9
  `

  **Features**

* [stepgen.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/bdd-step-autogen/stepgen.py) - Scans feature files for BDD steps (Given/When/Then), generates structured and commented Python step definitions in the appropriate `steps/` directory, skips duplicates, and supports incremental regeneration.

  **How to clone and run**

 These steps assume you're using Python 3.12+ and have `pip` available.

---

### 🌀 1. Clone the Repository

```bash
git clone https://github.com/QualityEngineering101/eqe-python-scripts.git
cd eqe-python-scripts/bdd-step-autogen
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
pip install -r ../bdd-step-autogen_requirements.txt
```

---

### ▶️ 4. Run the Project

```bash
# Run the generator script
```

```bash
python stepgen.py
```

---

### 📈 5. View the Results

If successful, you should see:

* a login_steps.py file created in the features/steps directory. This is the auto-generated step file.
* the script should have opened a browser and ran the tests automatically:
  1 feature passed, 0 failed, 0 skipped
  1 scenario passed, 0 failed, 0 skipped
  8 steps passed, 0 failed, 0 skipped, 0 undefined
