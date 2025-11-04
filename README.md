# Gnomodoro

A simple and elegant Pomodoro timer application for the GNOME desktop environment.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
[![Test and Lint](https://github.com/igormilovanovic/gnomodoro/actions/workflows/test-lint.yml/badge.svg)](https://github.com/igormilovanovic/gnomodoro/actions/workflows/test-lint.yml)

## Features

- **Pomodoro Timer**: Customizable work and break intervals
- **Desktop Notifications**: Get notified when sessions complete
- **GNOME Integration**: Seamless integration with GNOME desktop
- **Task Management**: Track tasks during Pomodoro sessions
- **Statistics**: View your productivity statistics
- **Themes**: Support for light and dark themes
- **Customizable Settings**: Configure timer durations and behavior

## Screenshots

_(Screenshots will be added here)_

## Installation

### Requirements

- Python 3.8 or higher
- GTK+ 3.0
- PyGObject
- Libnotify

### From Source

#### Quick Installation

1. Clone the repository:
```bash
git clone https://github.com/igormilovanovic/gnomodoro.git
cd gnomodoro
```

2. Run the installation script:
```bash
./install.sh
```

This will:
- Install required system dependencies (on supported distributions)
- Install Python dependencies
- Create a desktop entry for easy launching

3. Run the application:
```bash
python3 gnomodoro.py
```

Or search for "Gnomodoro" in your application menu.

#### Manual Installation

If the automatic installation doesn't work, follow these steps:

1. Install system dependencies:
```bash
# On Ubuntu/Debian
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-notify-0.7

# On Fedora
sudo dnf install python3-gobject gtk3 libnotify

# On Arch Linux
sudo pacman -S python-gobject gtk3 libnotify
```

2. Install Python dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run the application:
```bash
python3 gnomodoro.py
```

#### Uninstallation

To uninstall Gnomodoro:
```bash
./uninstall.sh
```

To also remove your settings and data:
```bash
rm -rf ~/.config/gnomodoro ~/.local/share/gnomodoro
```

### Using Flatpak (Recommended)

_(Coming soon)_

## Usage

### Basic Usage

1. **Start a Pomodoro**: Click the "Start" button to begin a work session
2. **Pause/Resume**: Click "Pause" to pause the timer, or "Resume" to continue
3. **Reset**: Click "Reset" to reset the timer to its initial state

### Settings

Access settings by clicking the "Settings" button:

- **Work Duration**: Length of work sessions (default: 25 minutes)
- **Short Break Duration**: Length of short breaks (default: 5 minutes)
- **Long Break Duration**: Length of long breaks (default: 15 minutes)
- **Pomodoros Until Long Break**: Number of work sessions before a long break (default: 4)
- **Auto-start Options**: Automatically start breaks or work sessions
- **Theme**: Choose between system default, light, or dark theme

### Task Management

Click the "Tasks" button to:
- Add new tasks
- Mark tasks as completed
- Delete tasks

### Statistics

View your productivity statistics by clicking the "Statistics" button:
- Today's completed Pomodoros
- Total time spent
- Weekly statistics

## Configuration

Settings are stored in `~/.config/gnomodoro/settings.json`

Statistics and task data are stored in `~/.local/share/gnomodoro/statistics.db`

## Development

### Running Tests

```bash
python3 -m pytest tests/
```

Or run individual test files:

```bash
python3 -m unittest tests/test_timer.py
python3 -m unittest tests/test_settings.py
```

### Project Structure

```
gnomodoro/
├── gnomodoro/          # Main application package
│   ├── logic/          # Business logic
│   │   ├── timer.py    # Pomodoro timer logic
│   │   ├── settings.py # Settings management
│   │   └── statistics.py # Statistics tracking
│   ├── ui/             # User interface
│   │   ├── main_window.py    # Main window
│   │   ├── settings_dialog.py # Settings dialog
│   │   ├── tasks_dialog.py   # Tasks dialog
│   │   └── statistics_dialog.py # Statistics dialog
│   ├── utils/          # Utility modules
│   │   └── notifications.py # Notification manager
│   └── app.py          # Main application class
├── tests/              # Unit tests
├── docs/               # Documentation
├── assets/             # Icons and resources
└── gnomodoro.py        # Entry point
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the Pomodoro Technique® by Francesco Cirillo
- Built with PyGObject and GTK+
- GNOME desktop integration using Libnotify and D-Bus

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/igormilovanovic/gnomodoro/issues) on GitHub.

## Roadmap

- [ ] Flatpak packaging
- [ ] Snap packaging
- [ ] System tray integration
- [ ] Sound notifications
- [ ] Keyboard shortcuts
- [ ] Session history export
- [ ] Multiple task lists
- [ ] Customizable notification messages

## Authors

- Igor Milovanovic - [GitHub](https://github.com/igormilovanovic)

## The Pomodoro Technique

The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato.
