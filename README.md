cookiecutter-behave
===================

Template for BDD tests using behave

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`

Usage
-----
Generate a new Cookiecutter template layout: `cookiecutter gh:dunossauro/cookiecutter-behave`

License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)

Estructure
-------
```
.
├── behave.ini
├── example
│   ├── data
│   │   └── logging.json
│   ├── features
│   │   ├── environment.py
│   │   ├── feature.feature
│   │   └── steps
│   │       └── steps.py
│   ├── helpers
│   │   └── constants.py
│   └── modules
│       └── mymodule.py
├── __init__.py
├── readme.md
├── pyproject.toml
└── requirements.txt
```
