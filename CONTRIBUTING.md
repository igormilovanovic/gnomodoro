# Contributing to Gnomodoro

Thank you for your interest in contributing to Gnomodoro! This document provides guidelines for contributing to the project.

## Code of Conduct

Be respectful and considerate of others. We aim to create a welcoming environment for all contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, GTK version)

### Suggesting Features

Feature suggestions are welcome! Please open an issue with:
- A clear description of the feature
- The problem it solves
- Possible implementation approach

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Write or update tests as needed
5. Ensure all tests pass
6. Update documentation if necessary
7. Submit a pull request

#### Pull Request Guidelines

- Keep changes focused and atomic
- Write clear commit messages
- Follow the existing code style
- Add tests for new functionality
- Update documentation for user-facing changes
- Ensure all tests pass before submitting

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/gnomodoro.git
cd gnomodoro
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run the application:
```bash
python3 gnomodoro.py
```

4. Run tests:
```bash
python3 -m unittest discover tests
```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions small and focused
- Add comments for complex logic

## Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR
- Aim for good test coverage
- Test on multiple Python versions if possible

## Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions and classes
- Update inline comments as needed
- Keep documentation clear and concise

## Git Workflow

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Add feature: description"
```

3. Push to your fork:
```bash
git push origin feature/your-feature-name
```

4. Open a pull request on GitHub

## Commit Messages

Write clear, descriptive commit messages:
- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Add detailed description if needed
- Reference issues when applicable

Example:
```
Add task priority feature

- Add priority field to task model
- Update UI to display priorities
- Add tests for priority functionality

Fixes #123
```

## Questions?

If you have questions, feel free to:
- Open an issue on GitHub
- Ask in your pull request
- Contact the maintainers

## License

By contributing to Gnomodoro, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing!
