# GitHub Workflows and Configuration

This directory contains GitHub Actions workflows and related documentation for automated releases and CI/CD.

## Workflows

### publish-python.yml
Automated workflow for publishing Python packages to PyPI and creating GitHub releases.

**Triggers**: Push of tags matching `v*.*.*` (e.g., v1.0.0, v1.2.3)

**What it does**:
- Builds Python source distribution and wheel
- Validates the build with twine
- Publishes to PyPI using the `PYPI_API_TOKEN` secret
- Extracts release notes from CHANGELOG.md
- Creates a GitHub Release with artifacts attached

**Setup Required**: You must configure the `PYPI_API_TOKEN` secret in repository settings. See [RELEASE_WORKFLOW_SETUP.md](RELEASE_WORKFLOW_SETUP.md) for details.

### flatpak-build.yml
Automated workflow for building Flatpak bundles.

**Triggers**: 
- Push of tags matching `v*.*.*`
- Manual trigger via workflow_dispatch

**What it does**:
- Builds a Flatpak bundle using the project manifest
- Uploads the bundle as a GitHub Actions artifact
- Attaches the bundle to GitHub Release (when triggered by tag)

**Setup Required**: No secrets needed. The workflow uses the manifest file `com.github.igormilovanovic.gnomodoro.yml` from the repository root.

## Documentation

### RELEASE_WORKFLOW_SETUP.md
Complete guide for maintainers on setting up and using the automated release workflows.

**Contents**:
- Prerequisites and requirements
- Step-by-step setup instructions
- How to configure PyPI API tokens
- How to trigger releases
- Troubleshooting guide
- Testing before production releases

### RELEASE_NOTES_TEMPLATE.md
Template and guidelines for writing release notes.

**Contents**:
- Release notes template structure
- Examples for different types of releases
- Best practices for writing good release notes
- Checklist for creating releases
- Release announcement templates

## Quick Start

### For Maintainers

1. **First-time setup**:
   - Read [RELEASE_WORKFLOW_SETUP.md](RELEASE_WORKFLOW_SETUP.md)
   - Generate a PyPI API token
   - Add it as `PYPI_API_TOKEN` secret in repository settings

2. **Creating a release**:
   ```bash
   # Update version and changelog
   vim setup.py CHANGELOG.md
   git add setup.py CHANGELOG.md
   git commit -m "Bump version to v1.1.0"
   git push
   
   # Create and push tag
   git tag -a v1.1.0 -m "Release version 1.1.0"
   git push origin v1.1.0
   ```

3. **Monitor the release**:
   - Go to the Actions tab
   - Watch the workflows run
   - Verify the package on PyPI
   - Check the GitHub Release was created

### For Contributors

These workflows are triggered automatically by maintainers. Contributors don't need to configure anything.

If you're interested in improving the CI/CD workflows, please:
1. Discuss changes in an issue first
2. Test workflow changes in your fork
3. Submit a pull request with clear documentation

## Testing Workflows

Before using workflows in production:

1. **Test the build locally**:
   ```bash
   python -m build
   twine check dist/*
   ```

2. **Use TestPyPI first**:
   - Temporarily modify the workflow to upload to TestPyPI
   - Create a test tag (e.g., `v0.1.0-test`)
   - Verify everything works before using production PyPI

3. **Review workflow logs**:
   - Always check the Actions tab after pushing a tag
   - Review logs for any warnings or errors
   - Verify all artifacts were created correctly

## Security

- **Never commit secrets**: All tokens and credentials must be stored in GitHub Secrets
- **Use scoped tokens**: PyPI tokens should be project-scoped, not account-wide
- **Review permissions**: Workflows have minimal required permissions
- **Rotate tokens regularly**: Update API tokens periodically

## Troubleshooting

Common issues and solutions:

**Workflow doesn't trigger**:
- Verify tag format matches `v*.*.*`
- Check that GitHub Actions are enabled
- Review workflow YAML syntax

**PyPI upload fails**:
- Verify `PYPI_API_TOKEN` secret is set correctly
- Check that you haven't already published this version
- Ensure the token has correct permissions

**Build fails**:
- Test build locally first: `python -m build`
- Check setup.py for errors
- Review workflow logs for specific error messages

For more help, see [RELEASE_WORKFLOW_SETUP.md](RELEASE_WORKFLOW_SETUP.md) or open an issue.

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Publishing Documentation](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
- [Flatpak Documentation](https://docs.flatpak.org/)

---

**Questions?** Open an issue or refer to the detailed documentation in this directory.
