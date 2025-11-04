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

## Versioning and Releases

Gnomodoro follows [Semantic Versioning](https://semver.org/) (SemVer):

### Version Format: `vX.Y.Z`

- **Major (X)**: Breaking changes that are not backward compatible
- **Minor (Y)**: New features that are backward compatible
- **Patch (Z)**: Bug fixes and minor improvements that are backward compatible

Examples:
- `v1.0.0` - Initial stable release
- `v1.1.0` - New features added (e.g., new theme, export functionality)
- `v1.1.1` - Bug fixes (e.g., notification crash fix)
- `v2.0.0` - Breaking changes (e.g., settings file format change)

### Single Source of Truth

The version number is defined in `setup.py` and should be updated there:

```python
setup(
    name="gnomodoro",
    version="1.0.0",  # Update this for new releases
    # ...
)
```

### Release Process (For Maintainers)

1. **Update Version**
   - Edit `setup.py` and update the version number
   - Follow semantic versioning guidelines

2. **Update CHANGELOG.md**
   - Move items from `[Unreleased]` to new version section
   - Add release date
   - Update version comparison links at bottom

3. **Commit Changes**
   ```bash
   git add setup.py CHANGELOG.md
   git commit -m "Bump version to vX.Y.Z"
   ```

4. **Create Git Tag**
   ```bash
   git tag -a vX.Y.Z -m "Release version X.Y.Z"
   git push origin vX.Y.Z
   ```

5. **Create GitHub Release**
   - Go to GitHub Releases page
   - Click "Draft a new release"
   - Select the tag you just created
   - Use the release announcement template from `RELEASE_ANNOUNCEMENT.md`
   - Attach any release artifacts if applicable

6. **Publish to PyPI** (requires maintainer credentials)
   ```bash
   # Build distribution packages
   python3 -m pip install --upgrade build twine
   python3 -m build
   
   # Upload to PyPI
   python3 -m twine upload dist/*
   ```

7. **Update Flathub** (if applicable)
   - Update Flatpak manifest if needed
   - Submit to Flathub repository
   - Follow Flathub submission guidelines

8. **Announce Release**
   - Post release announcement on GitHub
   - Share on social media (Twitter, Mastodon, Reddit)
   - Update project website/documentation

### Release Cadence

- **Major releases**: When breaking changes are necessary
- **Minor releases**: Every 2-3 months or when significant features are ready
- **Patch releases**: As needed for bug fixes, typically within days/weeks of bug discovery

### Pre-release Versions

For pre-release versions, use these suffixes:
- `vX.Y.Z-alpha.N` - Alpha releases (feature incomplete, unstable)
- `vX.Y.Z-beta.N` - Beta releases (feature complete, testing phase)
- `vX.Y.Z-rc.N` - Release candidates (ready for release, final testing)

Example: `v1.1.0-beta.1`

## Changelog Guidelines

Keep the CHANGELOG.md updated with all notable changes:

### Categories
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

### Format
```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New feature description (#PR_number)

### Fixed
- Bug fix description (#PR_number)
```

Always link to relevant pull requests or issues.

## Questions?

If you have questions, feel free to:
- Open an issue on GitHub
- Ask in your pull request
- Contact the maintainers

## License

By contributing to Gnomodoro, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing!
