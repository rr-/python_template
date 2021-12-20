template_project
================

This is a template that I use for a typical vanilla Python project. Includes:

- MIT license
- CLI endpoint template
- pre-commit configuration
    - black
    - isort
    - pylint
    - mypy
- Poetry template
- type hints stubs (PEP-561)
- GitHub actions template

To use it:
- copy the directory tree
- replace every `template_project` occurrence with a name of your project
- replace every `Author Name` occurrence with your name
- go through every field in `pyproject.toml`

## Installation

```
pip install --user template_project
```

## Contributing

```sh
# Clone the repository:
git clone https://github.com/rr-/template_project.git
cd template_project

# Install to a local venv:
poetry install

# Install pre-commit hooks:
poetry run pre-commit install

# Enter the venv:
poetry shell
```

This project uses [poetry](https://python-poetry.org/) for packaging,
install instructions at [poetry#installation](https://python-poetry.org/docs/#installation)
