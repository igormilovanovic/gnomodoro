# Development Guide

## Getting Started

### Prerequisites

- Python 3.8 or higher
- GTK+ 3.0 or higher
- PyGObject
- Git

### Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/igormilovanovic/gnomodoro.git
cd gnomodoro
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e ".[dev]"  # Install in development mode with dev dependencies
```

## Project Structure

```
gnomodoro/
├── src/gnomodoro/           # Main application package
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Application entry point
│   ├── ui/                  # User interface components
│   │   ├── __init__.py
│   │   └── main_window.py   # Main application window
│   └── core/                # Core logic
│       └── __init__.py
├── assets/                  # Resources (icons, images)
├── tests/                   # Unit tests
│   ├── __init__.py
│   └── test_basic.py
├── docs/                    # Documentation
│   └── DEVELOPMENT.md       # This file
├── pyproject.toml           # Project configuration
├── requirements.txt         # Dependencies
├── README.md                # Project README
└── LICENSE                  # MIT License
```

## Running the Application

From the project root directory:

```bash
python -m gnomodoro
```

Or if installed:

```bash
gnomodoro
```

## Running Tests

```bash
pytest tests/
```

With coverage:

```bash
pytest --cov=gnomodoro tests/
```

## Code Style

We use:
- **black** for code formatting
- **flake8** for linting
- **mypy** for type checking

Format code:
```bash
black src/ tests/
```

Check code style:
```bash
flake8 src/ tests/
```

Type check:
```bash
mypy src/
```

## Development Workflow

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes
3. Run tests and checks
4. Commit your changes
5. Push and create a pull request

## Architecture

### UI Layer (`src/gnomodoro/ui/`)
- GTK+ based user interface
- Main window and dialogs
- Event handlers

### Core Layer (`src/gnomodoro/core/`)
- Timer logic
- Business logic
- Data models

## Milestone Roadmap

- [x] **Milestone 1**: Project Setup
- [ ] **Milestone 2**: Implement the Timer
- [ ] **Milestone 3**: Gnome Integration
- [ ] **Milestone 4**: User Interface
- [ ] **Milestone 5**: Optional Features
- [ ] **Milestone 6**: Testing and Documentation
- [ ] **Milestone 7**: Packaging and Deployment

## Contributing

See the main README.md for contribution guidelines.
