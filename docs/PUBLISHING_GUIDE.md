# Publishing Guide

This guide provides detailed instructions for maintainers on publishing Gnomodoro to various distribution channels.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Publishing to PyPI](#publishing-to-pypi)
3. [Publishing to Flathub](#publishing-to-flathub)
4. [Creating GitHub Releases](#creating-github-releases)
5. [Version Management](#version-management)
6. [Post-Release Tasks](#post-release-tasks)

---

## Prerequisites

### Required Accounts
- **PyPI Account**: Register at [pypi.org](https://pypi.org/account/register/)
- **TestPyPI Account**: Register at [test.pypi.org](https://test.pypi.org/account/register/) (for testing)
- **Flathub**: GitHub account with access to Flathub organization
- **GitHub**: Repository maintainer access

### Required Tools
```bash
# Install build and publishing tools
pip install --upgrade build twine

# Install Flatpak build tools
sudo apt install flatpak flatpak-builder  # Ubuntu/Debian
# or
sudo dnf install flatpak flatpak-builder  # Fedora
# or
sudo pacman -S flatpak flatpak-builder    # Arch
```

### API Tokens

#### PyPI Token
1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Scroll to "API tokens" section
3. Click "Add API token"
4. Name: `gnomodoro-upload`
5. Scope: "Entire account" or "Project: gnomodoro"
6. Save the token securely (you'll only see it once)

#### GitHub Token
1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Generate new token (classic)
3. Scopes: `repo`, `workflow`
4. Save the token securely

---

## Publishing to PyPI

### Step 1: Prepare the Release

1. **Update Version in setup.py**
   ```python
   setup(
       name="gnomodoro",
       version="1.1.0",  # Update this
       # ...
   )
   ```

2. **Update CHANGELOG.md**
   - Move unreleased changes to new version section
   - Add release date
   - Update comparison links

3. **Commit version changes**
   ```bash
   git add setup.py CHANGELOG.md
   git commit -m "Bump version to v1.1.0"
   git push
   ```

4. **Create and push tag**
   ```bash
   git tag -a v1.1.0 -m "Release version 1.1.0"
   git push origin v1.1.0
   ```

### Step 2: Build Distribution Packages

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build source distribution and wheel
python3 -m build

# Verify the build
ls -lh dist/
```

You should see:
- `gnomodoro-1.1.0.tar.gz` (source distribution)
- `gnomodoro-1.1.0-py3-none-any.whl` (wheel distribution)

### Step 3: Test on TestPyPI (Optional but Recommended)

```bash
# Upload to TestPyPI
python3 -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --no-deps gnomodoro
```

### Step 4: Upload to PyPI

```bash
# Upload to PyPI
python3 -m twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your PyPI API token (including the `pypi-` prefix)

### Step 5: Verify the Release

1. Visit [https://pypi.org/project/gnomodoro/](https://pypi.org/project/gnomodoro/)
2. Verify version number, description, and metadata
3. Test installation:
   ```bash
   pipx install gnomodoro
   gnomodoro --version
   ```

### Troubleshooting PyPI Upload

**Issue**: "File already exists"
- You cannot re-upload the same version. Increment the version and rebuild.

**Issue**: "Invalid distribution"
- Check your `setup.py` for syntax errors
- Ensure all required files are included in `MANIFEST.in`

**Issue**: "Authentication failed"
- Verify your API token is correct
- Ensure username is `__token__` (with double underscores)

---

## Publishing to Flathub

### Initial Flathub Submission

1. **Request a new repository**
   - Each application gets its own repository in the Flathub organization
   - Repository name will be: `flathub/com.github.igormilovanovic.gnomodoro`
   - Follow the [Flathub app submission guide](https://github.com/flathub/flathub/wiki/App-Submission)

2. **Prepare your application repository**
   - Clone the newly created repository
   ```bash
   git clone https://github.com/flathub/com.github.igormilovanovic.gnomodoro.git
   cd com.github.igormilovanovic.gnomodoro
   ```
   - Add your manifest and metadata files

3. **Prepare Flatpak manifest**
   
   Create these files in the repository:
   
   File: `com.github.igormilovanovic.gnomodoro.yml`
   ```yaml
   app-id: com.github.igormilovanovic.gnomodoro
   runtime: org.gnome.Platform
   # Use the latest stable GNOME runtime version. At the time of publication, '45' was current.
   # Before publishing, check https://flathub.org/docs/for-app-authors.html for the latest stable version.
   runtime-version: '45'
   sdk: org.gnome.Sdk
   command: gnomodoro
   
   finish-args:
     - --share=ipc
     - --socket=fallback-x11
     - --socket=wayland
     - --device=dri
     - --talk-name=org.freedesktop.Notifications
   
   modules:
     - name: gnomodoro
       buildsystem: simple
       build-commands:
         - pip3 install --no-index --find-links="file://${PWD}" --prefix=${FLATPAK_DEST} .
       sources:
         - type: archive
           url: https://files.pythonhosted.org/packages/.../gnomodoro-1.1.0.tar.gz
           sha256: <CHECKSUM>
   ```

4. **Generate SHA256 checksum**
   ```bash
   wget https://files.pythonhosted.org/packages/.../gnomodoro-1.1.0.tar.gz
   sha256sum gnomodoro-1.1.0.tar.gz
   ```

5. **Test build locally**
   ```bash
   flatpak-builder --user --install --force-clean build-dir \
     com.github.igormilovanovic.gnomodoro.yml
   
   # Test the application
   flatpak run com.github.igormilovanovic.gnomodoro
   ```

6. **Submit to Flathub**
   - Commit your manifest files to the repository
   ```bash
   git add .
   git commit -m "Initial submission of Gnomodoro"
   git push origin main
   ```
   - Create a pull request to the `flathub/flathub` repository's app-submissions branch
   - Fill out the submission template
   - Wait for review and approval by Flathub maintainers

### Updating Existing Flathub Package

1. **Update manifest with new version**
   ```yaml
   sources:
     - type: archive
       url: https://files.pythonhosted.org/packages/.../gnomodoro-1.2.0.tar.gz
       sha256: <NEW_CHECKSUM>
   ```

2. **Test the update**
   ```bash
   flatpak-builder --user --install --force-clean build-dir \
     com.github.igormilovanovic.gnomodoro.yml
   ```

3. **Commit and push**
   ```bash
   git add com.github.igormilovanovic.gnomodoro.yml
   git commit -m "Update to version 1.2.0"
   git push origin main
   ```

4. **Flathub will automatically build and publish** (after review)

### Flatpak Metadata Files

Ensure these files are up to date:

**Desktop Entry**: `com.github.igormilovanovic.gnomodoro.desktop`
```desktop
[Desktop Entry]
Name=Gnomodoro
Comment=Pomodoro timer for GNOME
Exec=gnomodoro
Icon=com.github.igormilovanovic.gnomodoro
Terminal=false
Type=Application
Categories=Utility;GTK;GNOME;
Keywords=pomodoro;timer;productivity;
```

**AppStream Metadata**: `com.github.igormilovanovic.gnomodoro.metainfo.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
  <id>com.github.igormilovanovic.gnomodoro</id>
  <name>Gnomodoro</name>
  <summary>Pomodoro timer for GNOME</summary>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>MIT</project_license>
  <description>
    <p>
      Gnomodoro is a simple and elegant Pomodoro timer application for the GNOME desktop.
    </p>
  </description>
  <launchable type="desktop-id">com.github.igormilovanovic.gnomodoro.desktop</launchable>
  <url type="homepage">https://github.com/igormilovanovic/gnomodoro</url>
  <url type="bugtracker">https://github.com/igormilovanovic/gnomodoro/issues</url>
  <releases>
    <release version="1.1.0" date="2025-01-15"/>
  </releases>
</component>
```

---

## Creating GitHub Releases

### Step 1: Prepare Release Notes

Use the template from `RELEASE_ANNOUNCEMENT.md`:

```markdown
# Gnomodoro v1.1.0

Brief introduction about this release.

## ✨ Highlights
- Feature 1
- Feature 2

## 📋 What's Changed
[See changelog]

## 📦 Installation
[Installation instructions]
```

### Step 2: Create Release on GitHub

1. Go to [Releases page](https://github.com/igormilovanovic/gnomodoro/releases)
2. Click "Draft a new release"
3. Select tag: `v1.1.0`
4. Release title: `Gnomodoro v1.1.0 - [Short Description]`
5. Paste prepared release notes
6. Add release assets (if any):
   - Source archives are auto-generated
   - Optional: Add pre-built packages
7. Check "Set as the latest release"
8. Click "Publish release"

### Step 3: Verify Release

- Check release appears on main page
- Verify download links work
- Confirm release notes are formatted correctly

---

## Version Management

### Semantic Versioning Rules

- **Major (X.0.0)**: Breaking changes
  - API changes
  - Removed features
  - Major refactoring
  
- **Minor (X.Y.0)**: New features
  - New functionality
  - Enhancements
  - Backward compatible changes
  
- **Patch (X.Y.Z)**: Bug fixes
  - Bug fixes
  - Security patches
  - Minor improvements

### Version Update Checklist

Before releasing a new version:

- [ ] All tests pass
- [ ] Code is linted and formatted
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated
- [ ] Version in setup.py is updated
- [ ] Git tag is created
- [ ] Build artifacts are tested

---

## Post-Release Tasks

### 1. Verify Installation Methods

Test that users can install from all channels:

```bash
# PyPI
pipx install gnomodoro
gnomodoro --version

# Flatpak (once published)
flatpak install flathub com.github.igormilovanovic.gnomodoro
flatpak run com.github.igormilovanovic.gnomodoro
```

### 2. Update Project Links

- [ ] Update README badges (if version badges exist)
- [ ] Update documentation with new version
- [ ] Update any external references

### 3. Announce Release

Use templates from `RELEASE_ANNOUNCEMENT.md`:

- [ ] Post on GitHub Discussions (if enabled)
- [ ] Share on social media (Twitter, Mastodon)
- [ ] Post to Reddit (r/linux, r/gnome, r/productivity)
- [ ] Update project website (if applicable)
- [ ] Send email to mailing list (if applicable)

### 4. Monitor Feedback

- [ ] Watch GitHub Issues for bug reports
- [ ] Monitor social media for feedback
- [ ] Check PyPI download statistics
- [ ] Review Flathub metrics

### 5. Plan Next Release

- [ ] Create milestone for next version
- [ ] Review feature requests
- [ ] Prioritize bug fixes
- [ ] Update CHANGELOG.md with "Unreleased" section

---

## Automated Release Workflows

The project now includes automated GitHub Actions workflows for releases:

### Available Workflows

1. **publish-python.yml** - Automatically builds and publishes to PyPI, creates GitHub releases
   - Triggers on tag push (e.g., `v1.0.0`, `v1.2.3`)
   - Builds source distribution and wheel
   - Uploads to PyPI using `PYPI_API_TOKEN` secret
   - Creates GitHub Release with artifacts
   - Extracts release notes from CHANGELOG.md

2. **flatpak-build.yml** - Builds Flatpak bundles for distribution
   - Triggers on tag push or manual dispatch
   - Builds Flatpak bundle
   - Uploads as artifact to GitHub
   - Attaches to GitHub Release when triggered by tag

### Setup Instructions

See [.github/RELEASE_WORKFLOW_SETUP.md](../.github/RELEASE_WORKFLOW_SETUP.md) for detailed setup instructions including:
- How to generate and configure PyPI API tokens
- How to trigger automated releases
- Troubleshooting common issues
- Testing workflows before production use

### Using Automated Releases

Once configured, releases are simple:

```bash
# 1. Update version in setup.py and CHANGELOG.md
# 2. Commit changes
git add setup.py CHANGELOG.md
git commit -m "Bump version to v1.1.0"
git push origin main

# 3. Create and push tag
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin v1.1.0

# 4. Workflows automatically:
#    - Build distributions
#    - Publish to PyPI
#    - Create GitHub Release
#    - Build Flatpak bundle
```

For release notes templates and best practices, see [.github/RELEASE_NOTES_TEMPLATE.md](../.github/RELEASE_NOTES_TEMPLATE.md).

### Manual Release (Alternative)

You can still release manually if preferred. Follow the steps in the sections above for PyPI and GitHub releases.

---

## Support and Resources

### Documentation
- [Python Packaging Guide](https://packaging.python.org/)
- [Flatpak Documentation](https://docs.flatpak.org/)
- [Flathub Submission Guidelines](https://github.com/flathub/flathub/wiki/App-Submission)
- [Semantic Versioning](https://semver.org/)

### Getting Help
- Open an issue on GitHub for technical questions
- Join GNOME community channels for Flatpak support
- Consult PyPI support for publishing issues

---

## Quick Reference

### One-Command Release to PyPI
```bash
# After version bump and tag creation
rm -rf dist/ && python3 -m build && python3 -m twine upload dist/*
```

### One-Command Flatpak Build
```bash
flatpak-builder --user --install --force-clean build-dir \
  com.github.igormilovanovic.gnomodoro.yml && \
  flatpak run com.github.igormilovanovic.gnomodoro
```

### Version Bump Commands
```bash
# Example: 1.0.0 -> 1.1.0
# 1. Update setup.py version
sed -i 's/version=".*"/version="1.1.0"/' setup.py
# 2. Commit and tag
git add setup.py CHANGELOG.md
git commit -m "Bump version to v1.1.0"
git tag -a v1.1.0 -m "Release version 1.1.0"
git push && git push --tags
```

---

**Last Updated**: January 2025
