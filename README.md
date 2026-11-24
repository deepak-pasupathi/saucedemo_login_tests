## Saucedemo Login Tests

Small test automation project using Python, Playwright and Pytest.

## Tests
- Valid login
- Wrong password
- Locked-out user

## Concepts used
Page Object Model, Pytest fixtures (`page`), screenshot on failure.

## Setup
python3 -m venv venv
source venv/bin/activate
pip install pytest-playwright
playwright install

## Run
pytest -v
pytest --headed --slowmo 700