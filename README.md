# Gnomodoro

A Pomodoro timer application for the Gnome desktop environment.

## Features

- Customizable work and break intervals
- Desktop notifications for timer events
- Seamless Gnome desktop integration
- Simple and intuitive user interface
- Pause and reset timer functionality

## Requirements

- Linux with Gnome desktop environment
- Python 3.8 or higher
- GTK+ 3.0 or higher
- PyGObject

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/igormilovanovic/gnomodoro.git
cd gnomodoro

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m gnomodoro
```

## Usage

Launch the application and use the controls to:
- Start/pause the Pomodoro timer
- Reset the timer
- Configure work and break durations in settings

## Development

### Project Structure

```
gnomodoro/
├── src/gnomodoro/    # Main application package
│   ├── ui/           # GTK+ user interface components
│   └── core/         # Timer logic and core functionality
├── assets/           # Icons, images, and other resources
├── tests/            # Unit tests
└── docs/             # Documentation
```

### Running Tests

```bash
python -m pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

Igor Milovanovic
