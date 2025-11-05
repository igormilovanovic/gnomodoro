# Release Workflow Setup Guide

This guide explains how to configure the automated release workflows for Gnomodoro.

## Overview

The project includes two automated workflows:

1. **publish-python.yml** - Builds and publishes to PyPI, creates GitHub releases
2. **flatpak-build.yml** - Builds Flatpak bundles for distribution

## Prerequisites

### For PyPI Publishing

You need a PyPI account and API token:

1. Create an account at [pypi.org](https://pypi.org/account/register/)
2. (Optional) Test on [test.pypi.org](https://test.pypi.org/) first

### For GitHub Releases

GitHub automatically provides a `GITHUB_TOKEN` with necessary permissions. No setup required.

## Configuration Steps

### Step 1: Generate PyPI API Token

1. Log in to your PyPI account
2. Navigate to Account Settings: https://pypi.org/manage/account/
3. Scroll to the "API tokens" section
4. Click "Add API token"
5. Configure the token:
   - **Token name**: `gnomodoro-github-actions` (or your preferred name)
   - **Scope**: Select "Project: gnomodoro" (recommended) or "Entire account"
   - Click "Add token"
6. **IMPORTANT**: Copy the token immediately - you'll only see it once!
   - The token starts with `pypi-` and looks like: `pypi-AgEIcHlwaS5vcmc...`

### Step 2: Add Secret to GitHub Repository

1. Go to your GitHub repository: https://github.com/igormilovanovic/gnomodoro
2. Click **Settings** (repository settings, not your account)
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Configure the secret:
   - **Name**: `PYPI_API_TOKEN` (must match exactly)
   - **Secret**: Paste your PyPI API token
   - Click "Add secret"

### Step 3: Verify Setup

The secret should now appear in the list (the value will be hidden).

## How to Trigger a Release

### Automated Release Process

When you push a version tag, the workflows automatically:

1. Build Python distributions (sdist and wheel)
2. Upload to PyPI
3. Create a GitHub Release with artifacts
4. Build and attach Flatpak bundle

### Creating a Release

1. **Update version in setup.py**:
   ```python
   setup(
       name="gnomodoro",
       version="1.1.0",  # Update this
       # ...
   )
   ```

2. **Update CHANGELOG.md**:
   - Add your release notes under a new `## [1.1.0]` section
   - The workflow will extract these notes for the GitHub release

3. **Commit and push changes**:
   ```bash
   git add setup.py CHANGELOG.md
   git commit -m "Bump version to v1.1.0"
   git push origin main
   ```

4. **Create and push a tag**:
   ```bash
   git tag -a v1.1.0 -m "Release version 1.1.0"
   git push origin v1.1.0
   ```

5. **Monitor the workflow**:
   - Go to the "Actions" tab in your repository
   - Watch the "Publish Python Package" workflow run
   - Check for any errors

### Tag Format

Tags must follow the format: `v*.*.*` (e.g., `v1.0.0`, `v1.2.3`, `v2.0.0-beta`)

The workflow triggers on any tag starting with `v` followed by version numbers.

## Workflow Details

### publish-python.yml

**Triggers**: Push of tags matching `v*.*.*`

**Steps**:
1. Checks out the code
2. Sets up Python environment
3. Installs build tools (build, twine)
4. Builds source distribution and wheel
5. Validates distributions with twine
6. Uploads to PyPI using `PYPI_API_TOKEN`
7. Extracts release notes from CHANGELOG.md
8. Creates GitHub Release with artifacts

**Artifacts**:
- `gnomodoro-{version}.tar.gz` (source distribution)
- `gnomodoro-{version}-py3-none-any.whl` (wheel)

### flatpak-build.yml

**Triggers**: 
- Push of tags matching `v*.*.*`
- Manual trigger via workflow_dispatch

**Steps**:
1. Builds Flatpak bundle using the manifest
2. Uploads bundle as GitHub artifact
3. Attaches bundle to GitHub Release (if triggered by tag)

**Artifacts**:
- `gnomodoro.flatpak` (Flatpak bundle)

## Testing Before Release

### Test PyPI (Recommended)

Before your first production release, test with TestPyPI:

1. Create a TestPyPI account: https://test.pypi.org/
2. Generate a TestPyPI API token
3. Temporarily modify the workflow to use TestPyPI:
   ```yaml
   - name: Publish to TestPyPI
     env:
       TWINE_USERNAME: __token__
       TWINE_PASSWORD: ${{ secrets.TEST_PYPI_API_TOKEN }}
     run: twine upload --repository testpypi dist/*
   ```
4. Create a test tag (e.g., `v0.1.0-test`)
5. Verify the package appears on TestPyPI
6. Test installation: `pip install --index-url https://test.pypi.org/simple/ gnomodoro`

### Local Testing

Before pushing tags, test the build locally:

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build distributions
python -m pip install --upgrade build twine
python -m build

# Check distributions
twine check dist/*

# Test installation locally
pip install dist/gnomodoro-*.whl
```

## Troubleshooting

### "403 Forbidden" Error on PyPI Upload

**Cause**: Invalid or missing API token, or insufficient permissions

**Solutions**:
1. Verify the secret name is exactly `PYPI_API_TOKEN`
2. Ensure the token hasn't expired
3. Check the token has the correct scope (project or account)
4. Regenerate the token if necessary

### "File already exists" Error

**Cause**: Attempting to upload the same version twice

**Solution**: 
- PyPI doesn't allow re-uploading the same version
- Increment the version number in setup.py
- Delete the old tag and create a new one with the new version

### Workflow Doesn't Trigger

**Possible causes**:
1. Tag doesn't match the pattern `v*.*.*`
2. Workflow file has syntax errors
3. GitHub Actions are disabled for the repository

**Solutions**:
1. Verify tag format: `git tag -l`
2. Check workflow syntax: https://www.yamllint.com/
3. Enable Actions: Settings → Actions → General → Allow all actions

### Build Fails

**Common issues**:
1. **Missing dependencies**: Ensure `build` and `twine` are installed in the workflow
2. **setup.py errors**: Test `python -m build` locally first
3. **Network timeouts**: GitHub Actions may have temporary network issues; re-run the workflow

### Release Not Created

**Check**:
1. Workflow has `contents: write` permission (already configured)
2. `GITHUB_TOKEN` is available (automatically provided)
3. Review workflow logs in the Actions tab

## Flatpak Submission to Flathub

After successful Flatpak builds, you can submit to Flathub:

1. **Fork the Flathub repository**: https://github.com/flathub/flathub
2. **Create application repository**:
   - Flathub will create `flathub/com.github.igormilovanovic.gnomodoro`
3. **Copy manifest and metadata**:
   - `com.github.igormilovanovic.gnomodoro.yml`
   - `com.github.igormilovanovic.gnomodoro.desktop`
   - `com.github.igormilovanovic.gnomodoro.metainfo.xml`
4. **Submit pull request** following Flathub guidelines
5. **Wait for review** by Flathub maintainers

See the [Flathub submission guide](https://github.com/flathub/flathub/wiki/App-Submission) for details.

## Maintenance

### Updating Python Version

If you need to change the Python version used in workflows:

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'  # Change as needed
```

### Updating Flatpak Runtime

If updating the GNOME runtime version:

1. Update `runtime-version` in `com.github.igormilovanovic.gnomodoro.yml`
2. Update the container image in `.github/workflows/flatpak-build.yml`:
   ```yaml
   container:
     image: bilelmoussaoui/flatpak-github-actions:gnome-46  # Update version
   ```

## Security Notes

- **Never commit API tokens** to the repository
- Store all secrets in GitHub repository secrets
- Regularly rotate API tokens
- Use project-scoped tokens when possible (not account-wide)
- Review workflow permissions periodically

## Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Documentation](https://pypi.org/help/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Flatpak Documentation](https://docs.flatpak.org/)
- [Flathub Submission Guidelines](https://github.com/flathub/flathub/wiki)

## Getting Help

If you encounter issues:

1. Check workflow logs in the Actions tab
2. Review this guide and troubleshooting section
3. Search existing GitHub issues
4. Open a new issue with:
   - Workflow run link
   - Error messages
   - Steps to reproduce

---

**Last Updated**: November 2025
