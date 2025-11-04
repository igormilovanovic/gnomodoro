# CI/CD Documentation

## Overview

This project uses GitHub Actions for continuous integration and continuous deployment. The CI pipeline automatically runs tests and linting checks on every push to the main branch and on all pull requests.

## Workflow Details

### Test and Lint Workflow

**File**: `.github/workflows/test-lint.yml`

This workflow runs on:
- Push to `main` branch
- All pull requests targeting `main` branch

#### Python Version Matrix

The workflow tests the code against multiple Python versions:
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

**Note**: While `setup.py` declares compatibility with Python 3.8+, the CI pipeline focuses on Python 3.9+ as these are the actively maintained and tested versions. Python 3.8 reached end-of-life in October 2024.

#### Jobs

The workflow performs the following steps:

1. **Checkout Code**: Uses `actions/checkout@v4` to clone the repository

2. **Setup Python**: Uses `actions/setup-python@v5` to install the specified Python version with pip caching enabled

3. **Install System Dependencies**: Installs required system libraries for PyGObject and GTK:
   - libgirepository1.0-dev
   - gcc
   - libcairo2-dev
   - pkg-config
   - python3-dev
   - gir1.2-gtk-3.0
   - libgtk-3-dev

4. **Install Python Dependencies**: 
   - Upgrades pip
   - Installs production dependencies from `requirements.txt`
   - Installs development dependencies (flake8, black, isort, pytest)

5. **Lint with flake8**:
   - Critical check: Fails on syntax errors and undefined names
   - Warning check: Reports style issues but doesn't fail the build

6. **Check Code Formatting** (black):
   - Reports formatting issues
   - Doesn't fail the build (`continue-on-error: true`)

7. **Check Import Sorting** (isort):
   - Reports import sorting issues
   - Doesn't fail the build (`continue-on-error: true`)

8. **Run Tests**:
   - Primary: unittest discovery (must pass)
   - Secondary: pytest (informational only)

## Local Development

### Running Tests Locally

```bash
# Using unittest (primary test runner)
python3 -m unittest discover tests -v

# Using pytest (alternative)
pytest tests/ -v
```

### Running Linters Locally

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run flake8
flake8 .

# Check code formatting with black
black --check .

# Check import sorting with isort
isort --check-only .
```

### Formatting Code

```bash
# Auto-format with black
black .

# Auto-sort imports with isort
isort .
```

## Configuration Files

### `.flake8`
Configures flake8 with:
- Max line length: 127 characters
- Complexity limit: 10
- Exclusions for build artifacts and virtual environments

### `pyproject.toml`
Contains configuration for:
- **black**: Line length, target Python versions, exclusions
- **isort**: Profile (black-compatible), line length, exclusions
- **pytest**: Test paths, naming conventions, output options

### `requirements-dev.txt`
Lists development dependencies:
- flake8 >= 7.0.0
- black >= 24.0.0
- isort >= 5.13.0
- pytest >= 8.0.0

## CI Status Badge

The README includes a CI status badge that shows the current state of the test and lint workflow:

[![Test and Lint](https://github.com/igormilovanovic/gnomodoro/actions/workflows/test-lint.yml/badge.svg)](https://github.com/igormilovanovic/gnomodoro/actions/workflows/test-lint.yml)

This badge automatically updates based on the workflow status.

## Best Practices

1. **Always run tests locally** before pushing code
2. **Fix critical flake8 errors** before submitting PRs
3. **Consider fixing formatting issues** flagged by black and isort
4. **Ensure all tests pass** in the CI pipeline
5. **Review CI logs** if the workflow fails

## Troubleshooting

### CI Workflow Fails

1. Check the workflow logs in the Actions tab
2. Identify which step failed (linting or testing)
3. Run the same check locally to reproduce the issue
4. Fix the issue and push again

### System Dependencies Not Found

If you see errors related to GTK or GObject:
- Ensure all system dependencies are listed in the workflow
- Update the workflow file if new system dependencies are needed

### Tests Pass Locally But Fail in CI

- Check Python version differences
- Verify all dependencies are in `requirements.txt`
- Check for environment-specific issues
