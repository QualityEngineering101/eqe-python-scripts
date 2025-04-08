### BDD Step Auto Generation

Script that parses `.feature` files and auto-generates matching `*_steps.py` implementations for each scenario and step. Currently set up to work with a `features/login.feature` file and produce `features/steps/login_steps.py`.

  `**Dependencies** Python>=3.9
  `

  **Features**

* [stepgen.py](https://github.com/QualityEngineering101/eqe-python-scripts/blob/main/bdd-step-autogen/stepgen.py) - Scans feature files for BDD steps (Given/When/Then), generates structured and commented Python step definitions in the appropriate `steps/` directory, skips duplicates, and supports incremental regeneration.

  **How to clone and run**

  [Coming Soon!]