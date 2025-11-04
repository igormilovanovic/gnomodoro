# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Release process documentation
- CHANGELOG.md to track version changes
- RELEASE_ANNOUNCEMENT.md template for maintainers

## [1.0.0] - 2025-01-XX

### Added
- Core Pomodoro timer functionality with customizable durations
- Desktop notifications using Libnotify for session completions
- Task management system (add, complete, delete tasks)
- Statistics tracking with daily and weekly views
- Settings dialog with comprehensive configuration options
- Theme support (system default, light, dark)
- Auto-start options for breaks and work sessions
- SQLite database for persistent storage of tasks and statistics
- GTK+ 3.0 user interface with GNOME integration
- Unit tests for timer logic and settings management
- User guide and developer guide documentation
- Flatpak manifest for easy distribution
- Desktop entry and AppStream metadata
- Installation and uninstallation scripts
- MIT License

### Technical Details
- Python 3.8+ support
- PyGObject integration
- Follows PEP 8 coding standards
- Modular architecture with separation of concerns

[Unreleased]: https://github.com/igormilovanovic/gnomodoro/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/igormilovanovic/gnomodoro/releases/tag/v1.0.0
