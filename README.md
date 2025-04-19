# Calculator Project

A simple Python calculator project for demonstrating Jenkins CI/CD integration.

## Features

- Add function for adding two numbers
- Comprehensive test suite
- Jenkins pipeline integration with Poetry

## Development Setup

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Run tests:
```bash
poetry run pytest tests/ -v
```

## Jenkins Integration

The project includes a Jenkinsfile that defines the CI/CD pipeline with the following stages:

1. Checkout: Retrieves the latest code
2. Setup Python and Poetry: Installs Poetry and configures the environment
3. Install Dependencies: Installs project dependencies using Poetry
4. Run Tests: Executes the test suite

The pipeline will run automatically on every commit to the repository. 