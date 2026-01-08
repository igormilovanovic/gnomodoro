# Release Notes Template

Use this template when preparing release notes for the CHANGELOG.md file. The automated workflow will extract these notes and use them for the GitHub Release.

## Template Structure

```markdown
## [VERSION] - YYYY-MM-DD

### Added
- New feature 1
- New feature 2

### Changed
- Improvement 1
- Improvement 2

### Deprecated
- Feature scheduled for removal

### Removed
- Removed feature 1

### Fixed
- Bug fix 1
- Bug fix 2

### Security
- Security update 1
```

## Example Release Notes

### Example 1: Minor Feature Release

```markdown
## [1.1.0] - 2025-01-15

### Added
- Sound notifications when timer completes
- Keyboard shortcuts for start/pause/reset (Ctrl+S, Ctrl+P, Ctrl+R)
- Option to customize notification messages

### Changed
- Improved statistics dialog layout
- Enhanced dark mode theme colors
- Updated dependencies to latest versions

### Fixed
- Timer not pausing correctly when system suspends
- Statistics not updating after completing a session
- Desktop notification icon not showing on Wayland
```

### Example 2: Patch Release

```markdown
## [1.0.1] - 2025-01-10

### Fixed
- Critical bug causing crashes on GNOME 44
- Timer continuing after application close
- Settings not persisting between sessions

### Security
- Updated dependencies to address CVE-2024-XXXX
```

### Example 3: Major Release

```markdown
## [2.0.0] - 2025-03-01

### Added
- Multiple task lists with categorization
- Export session history to CSV
- System tray integration
- Custom themes support
- Cloud sync support (optional)

### Changed
- Redesigned main window with modern GTK4 widgets
- Migrated to GTK4 and libadwaita
- Improved performance and reduced memory usage
- New settings organization

### Deprecated
- GTK3 support (will be removed in v3.0.0)

### Removed
- Legacy database migration tool (use v1.x to migrate first)

### Security
- Implemented encrypted storage for cloud sync credentials
```

## Best Practices

### Writing Good Release Notes

1. **Be specific**: Instead of "Fixed bugs", write "Fixed timer not pausing when system suspends"
2. **Use action verbs**: Added, Fixed, Improved, Updated, Removed
3. **Focus on user impact**: Explain what changed from the user's perspective
4. **Group related changes**: Keep similar items together
5. **Link to issues**: Reference issue numbers when applicable (e.g., "Fixed #123")

### Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **Major (X.0.0)**: Breaking changes, major new features
- **Minor (X.Y.0)**: New features, backward compatible
- **Patch (X.Y.Z)**: Bug fixes, no new features

### Release Note Sections

#### Added
New features and capabilities that users can now use.

**Examples**:
- Added sound notifications
- Added keyboard shortcuts
- Added export to CSV feature

#### Changed
Modifications to existing features or improvements.

**Examples**:
- Improved performance of statistics calculation
- Updated UI layout for better usability
- Changed default timer duration to 25 minutes

#### Deprecated
Features that are still present but will be removed in a future version.

**Examples**:
- Deprecated old configuration format (use new JSON format)
- Deprecated GTK3 support (will be removed in v3.0.0)

#### Removed
Features that have been completely removed.

**Examples**:
- Removed support for Python 3.7
- Removed legacy database format

#### Fixed
Bug fixes and corrections.

**Examples**:
- Fixed crash when opening statistics dialog
- Fixed timer not resetting correctly
- Fixed memory leak in notification system

#### Security
Security-related changes, especially important for users to know about.

**Examples**:
- Fixed CVE-2024-XXXX vulnerability in dependency
- Improved input validation to prevent XSS
- Updated to latest version of PyGObject with security fixes

## Updating CHANGELOG.md

### Step 1: Add Your Release Notes

Edit `CHANGELOG.md` and add your release notes under the `[Unreleased]` section or create a new section:

```markdown
## [Unreleased]

### Added
- Feature in development

## [1.1.0] - 2025-01-15

### Added
- New feature 1
- New feature 2

### Fixed
- Bug fix 1
```

### Step 2: Update Comparison Links

At the bottom of CHANGELOG.md, update the comparison links:

```markdown
[Unreleased]: https://github.com/igormilovanovic/gnomodoro/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/igormilovanovic/gnomodoro/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/igormilovanovic/gnomodoro/releases/tag/v1.0.0
```

### Step 3: Commit Before Tagging

```bash
git add CHANGELOG.md
git commit -m "Update CHANGELOG for v1.1.0"
git push origin main
```

## Release Announcement Template

For social media and announcements, use this expanded template:

```markdown
# 🍅 Gnomodoro v1.1.0 Released!

We're excited to announce the release of Gnomodoro v1.1.0, a simple and elegant Pomodoro timer for GNOME!

## ✨ Highlights

- 🔊 Sound notifications when timer completes
- ⌨️ Keyboard shortcuts for quick control
- 🎨 Customizable notification messages

## 📋 What's New

Full changelog: https://github.com/igormilovanovic/gnomodoro/blob/main/CHANGELOG.md

## 📦 Installation

**PyPI**:
```bash
pipx install gnomodoro
```

**Flatpak**:
```bash
flatpak install flathub com.github.igormilovanovic.gnomodoro
```

## 🔗 Links

- Homepage: https://github.com/igormilovanovic/gnomodoro
- Documentation: https://github.com/igormilovanovic/gnomodoro/tree/main/docs
- Report issues: https://github.com/igormilovanovic/gnomodoro/issues

Thank you to all contributors! 🎉
```

## Checklist for Releases

Before creating a release, ensure:

- [ ] All tests pass
- [ ] Version updated in setup.py
- [ ] CHANGELOG.md updated with release notes
- [ ] Documentation updated (if needed)
- [ ] All changes committed to main branch
- [ ] Tag created with correct format (vX.Y.Z)
- [ ] Release notes prepared for GitHub Release
- [ ] Announcement drafted (optional)

After release:

- [ ] Verify package on PyPI
- [ ] Verify GitHub Release created
- [ ] Test installation from PyPI
- [ ] Announce release (social media, forums, etc.)
- [ ] Update documentation site (if applicable)
- [ ] Start planning next release

## Examples from Other Projects

For inspiration, check release notes from similar projects:

- [Pomodone](https://github.com/rlespinasse/pomodone/releases)
- [Gnome Pomodoro](https://github.com/codito/gnome-pomodoro/releases)
- [Tomighty](https://github.com/tomighty/tomighty/releases)

---

**Remember**: Good release notes help users understand what changed and why they should upgrade!
