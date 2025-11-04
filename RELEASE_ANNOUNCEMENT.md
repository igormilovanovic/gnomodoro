# Release Announcement Template

This template provides a structured format for announcing new Gnomodoro releases on GitHub and social media channels.

## GitHub Release Template

### Title Format
```
Gnomodoro v{VERSION} - {SHORT_DESCRIPTION}
```

Examples:
- `Gnomodoro v1.0.0 - Initial Release`
- `Gnomodoro v1.1.0 - Task Management Improvements`
- `Gnomodoro v1.0.1 - Bug Fixes and Performance`

### Release Description Template

```markdown
# Gnomodoro v{VERSION}

{BRIEF_INTRODUCTION - 1-2 sentences about this release}

## ✨ Highlights

{LIST_KEY_FEATURES_OR_CHANGES}
- Feature/change 1
- Feature/change 2
- Feature/change 3

## 📋 What's Changed

### Added
- New feature 1
- New feature 2

### Changed
- Changed behavior 1
- Changed behavior 2

### Fixed
- Bug fix 1
- Bug fix 2

### Deprecated
- Deprecated feature 1 (if applicable)

### Removed
- Removed feature 1 (if applicable)

### Security
- Security improvement 1 (if applicable)

## 📦 Installation

### From PyPI (Recommended)
```bash
pipx install gnomodoro
# or
pip install gnomodoro
```

### From Flathub
```bash
flatpak install flathub com.github.igormilovanovic.gnomodoro
```

### From Source
```bash
git clone https://github.com/igormilovanovic/gnomodoro.git
cd gnomodoro
git checkout v{VERSION}
./install.sh
```

## 🔗 Resources

- **Documentation**: [User Guide](https://github.com/igormilovanovic/gnomodoro/blob/main/docs/USER_GUIDE.md)
- **Changelog**: [CHANGELOG.md](https://github.com/igormilovanovic/gnomodoro/blob/main/CHANGELOG.md)
- **Report Issues**: [GitHub Issues](https://github.com/igormilovanovic/gnomodoro/issues)
- **Contributing**: [CONTRIBUTING.md](https://github.com/igormilovanovic/gnomodoro/blob/main/CONTRIBUTING.md)

## 🙏 Acknowledgments

{THANK_CONTRIBUTORS - if applicable}
Thanks to all contributors who made this release possible:
- @contributor1
- @contributor2

## 📊 Full Changelog

See the [full changelog](https://github.com/igormilovanovic/gnomodoro/compare/v{PREVIOUS_VERSION}...v{VERSION}) for all changes.

---

**Enjoy more productive Pomodoro sessions!** 🍅⏲️
```

## Social Media Announcement Templates

### Twitter/X Template (280 characters)
```
🎉 Gnomodoro v{VERSION} is here! 

{1_SENTENCE_HIGHLIGHT}

⬇️ Install: 
pip install gnomodoro

📖 Release notes: {GITHUB_RELEASE_URL}

#Pomodoro #Productivity #GNOME #OpenSource
```

### Mastodon Template
```
🍅 Gnomodoro v{VERSION} Released! 

{BRIEF_DESCRIPTION - 2-3 sentences}

Key highlights:
✨ {FEATURE_1}
✨ {FEATURE_2}
✨ {FEATURE_3}

Install with pipx or flatpak:
$ pipx install gnomodoro

More info: {GITHUB_RELEASE_URL}

#Gnomodoro #Pomodoro #Productivity #GNOME #OpenSource #Linux
```

### Reddit Post Template (r/linux, r/gnome, r/productivity)

**Title:** `Gnomodoro v{VERSION} - {SHORT_DESCRIPTION}`

**Body:**
```markdown
Hi everyone! I'm excited to announce the release of Gnomodoro v{VERSION}!

## About Gnomodoro

Gnomodoro is a simple and elegant Pomodoro timer application for the GNOME desktop environment, designed to help you stay focused and productive.

## What's New in v{VERSION}

{DETAILED_DESCRIPTION_OF_CHANGES - 3-5 sentences}

### Key Features:
- Feature 1
- Feature 2
- Feature 3

## Installation

**PyPI (pipx recommended):**
```bash
pipx install gnomodoro
```

**Flatpak:**
```bash
flatpak install flathub com.github.igormilovanovic.gnomodoro
```

**From Source:**
```bash
git clone https://github.com/igormilovanovic/gnomodoro.git
cd gnomodoro
./install.sh
```

## Links

- GitHub: https://github.com/igormilovanovic/gnomodoro
- Release Notes: {GITHUB_RELEASE_URL}
- Documentation: {DOCS_URL}

## Feedback Welcome!

I'd love to hear your thoughts and feedback. If you encounter any issues or have feature suggestions, please open an issue on GitHub.

Thank you! 🍅⏲️
```

## Developer/Hacker News Template

**Title:** `Gnomodoro v{VERSION} – Pomodoro Timer for GNOME`

**Body:**
```
Gnomodoro is an open-source Pomodoro timer application for the GNOME desktop environment.

Version {VERSION} includes {KEY_CHANGES}.

Built with Python and GTK+, features include:
- Customizable timer durations
- Task management
- Statistics tracking
- Desktop notifications
- Dark/light theme support

Project: https://github.com/igormilovanovic/gnomodoro
License: MIT
Install: pipx install gnomodoro
```

## Email Newsletter Template (if applicable)

```
Subject: Gnomodoro v{VERSION} Released - {HIGHLIGHT}

Hi Gnomodoro users,

We're excited to announce the release of Gnomodoro v{VERSION}!

[BRIEF_OVERVIEW - 2-3 paragraphs about the release]

## Installation

Update your installation:
$ pipx upgrade gnomodoro

Or install fresh:
$ pipx install gnomodoro

## What's Next

[ROADMAP_PREVIEW if applicable]

## Get Involved

Gnomodoro is open source and we welcome contributions! Check out our contributing guide: {CONTRIBUTING_URL}

Happy focusing!
The Gnomodoro Team
```

---

## Release Checklist for Maintainers

Before announcing a release, ensure:

- [ ] All tests pass
- [ ] CHANGELOG.md is updated with version and date
- [ ] Version number is bumped in setup.py
- [ ] Git tag is created (format: `v{VERSION}`)
- [ ] GitHub Release is created with release notes
- [ ] Package is published to PyPI
- [ ] Flatpak is submitted to Flathub (if updated)
- [ ] Documentation is updated
- [ ] Social media posts are scheduled/published
- [ ] Community channels are notified (Reddit, forums, etc.)

## Tips for Writing Release Announcements

1. **Be Clear and Concise**: Users should quickly understand what's new
2. **Highlight User Benefits**: Focus on how changes improve user experience
3. **Use Emojis Sparingly**: They add visual interest but don't overdo it
4. **Provide Context**: Explain why changes were made if relevant
5. **Include Screenshots**: Visual changes should have screenshots
6. **Thank Contributors**: Acknowledge community contributions
7. **Link to Details**: Always link to full changelog and documentation
8. **Test Installation Commands**: Verify all installation instructions work
9. **Proofread**: Check for typos and formatting issues
10. **Timing**: Announce releases during peak community activity times
