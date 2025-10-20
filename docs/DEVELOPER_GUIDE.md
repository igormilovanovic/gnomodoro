# Gnomodoro Developer Guide

## Architecture Overview

Gnomodoro follows a modular architecture with clear separation of concerns:

```
gnomodoro/
├── logic/      # Business logic layer
├── ui/         # User interface layer  
├── utils/      # Utility modules
└── app.py      # Application entry point
```

## Core Components

### Timer Logic (`logic/timer.py`)

The `PomodoroTimer` class implements the core timer functionality:

- **State Management**: Tracks timer state (IDLE, RUNNING, PAUSED, COMPLETED)
- **Timer Types**: Manages different timer types (WORK, SHORT_BREAK, LONG_BREAK)
- **Callbacks**: Provides hooks for tick, completion, and state change events
- **Customization**: Allows configuration of durations and behavior

Key methods:
- `start()`: Start/resume the timer
- `pause()`: Pause the timer
- `reset()`: Reset to initial state
- `tick()`: Decrease time by one second

### Settings Management (`logic/settings.py`)

The `Settings` class handles configuration persistence:

- Stores settings in JSON format
- Provides get/set interface for settings
- Auto-saves on changes
- Supports defaults for missing values

Settings location: `~/.config/gnomodoro/settings.json`

### Statistics Tracking (`logic/statistics.py`)

The `Statistics` class manages productivity data:

- Uses SQLite for data persistence
- Tracks completed pomodoros with timestamps
- Manages tasks (add, complete, delete)
- Provides aggregated statistics (daily, weekly)

Database location: `~/.local/share/gnomodoro/statistics.db`

### Notifications (`utils/notifications.py`)

The `NotificationManager` class handles desktop notifications:

- Uses libnotify for GNOME integration
- Supports different urgency levels
- Can be enabled/disabled

### User Interface (`ui/`)

#### Main Window (`ui/main_window.py`)

The main application window built with GTK+:

- Timer display with large, readable font
- Control buttons (Start, Pause, Reset)
- Quick access to settings, tasks, and statistics
- Real-time updates via GLib timeout

#### Settings Dialog (`ui/settings_dialog.py`)

Configuration interface:

- Spin buttons for duration settings
- Checkboxes for behavior options
- Theme selector
- Validates and saves settings

#### Tasks Dialog (`ui/tasks_dialog.py`)

Task management interface:

- Add new tasks
- Mark tasks as complete
- Delete tasks
- Real-time list updates

#### Statistics Dialog (`ui/statistics_dialog.py`)

Statistics visualization:

- Today's summary
- Weekly history
- Formatted time displays

## Data Flow

1. **User Action** → UI Component
2. **UI Component** → Business Logic (Timer, Settings, Statistics)
3. **Business Logic** → Callback/Event
4. **Callback** → UI Update or Notification

Example: Starting a timer
```python
User clicks "Start"
→ MainWindow.on_start_clicked()
→ PomodoroTimer.start()
→ GLib.timeout_add_seconds() starts ticking
→ PomodoroTimer.tick() every second
→ MainWindow._update_timer_display() updates UI
```

## GTK+ Integration

### GLib Main Loop

The application uses GLib's main loop for:
- Timer updates (`GLib.timeout_add_seconds`)
- Event handling
- UI updates

### Signal Handling

GTK widgets use signals for events:
```python
button.connect("clicked", self.on_button_clicked)
```

### Threading Considerations

All UI updates must happen on the main thread. The timer uses GLib timeouts rather than separate threads to ensure thread safety.

## Adding New Features

### Adding a New Setting

1. Add default value in `Settings.DEFAULT_SETTINGS`
2. Add UI control in `SettingsDialog`
3. Save/load in `_save_settings()` method
4. Use setting in relevant component

Example:
```python
# In settings.py
DEFAULT_SETTINGS = {
    ...
    "new_setting": default_value,
}

# In settings_dialog.py
self.new_setting_widget = Gtk.Widget()
# ... configure widget ...

# In _save_settings()
self.settings.set("new_setting", self.new_setting_widget.get_value())
```

### Adding a New Timer Type

1. Add enum value to `TimerType` in `timer.py`
2. Update `_get_duration_for_current_type()`
3. Update completion logic in `_complete_current_timer()`
4. Add UI label in `MainWindow._update_type_label()`

### Adding a Statistics View

1. Add database query in `Statistics` class
2. Create UI in `StatisticsDialog`
3. Format and display data

## Testing

### Unit Tests

Tests are located in the `tests/` directory:

- `test_timer.py`: Tests timer logic
- `test_settings.py`: Tests settings management

Run tests:
```bash
python3 -m unittest discover tests
```

### Manual Testing

Test checklist:
- [ ] Timer counts down correctly
- [ ] Pause/resume works
- [ ] Reset works at any state
- [ ] Notifications appear
- [ ] Settings persist
- [ ] Statistics record correctly
- [ ] Tasks can be added/completed/deleted
- [ ] Theme changes apply

## Debugging

### Logging

Add debug prints during development:
```python
print(f"Timer state: {self.timer.state}")
print(f"Remaining time: {self.timer.remaining_time}")
```

### GTK Inspector

Enable GTK Inspector for UI debugging:
```bash
GTK_DEBUG=interactive python3 gnomodoro.py
```

### Database Inspection

Inspect the SQLite database:
```bash
sqlite3 ~/.local/share/gnomodoro/statistics.db
.tables
SELECT * FROM pomodoros;
```

## Building and Packaging

### Flatpak

Build the Flatpak:
```bash
flatpak-builder build-dir com.github.igormilovanovic.gnomodoro.yml
```

Install locally:
```bash
flatpak-builder --user --install --force-clean build-dir \
    com.github.igormilovanovic.gnomodoro.yml
```

### Desktop Entry

The `.desktop` file enables:
- Application menu entry
- Icon display
- Proper categorization

### AppStream Metadata

The `.metainfo.xml` file provides:
- App description
- Screenshots
- Release information
- For software centers

## Code Style

Follow PEP 8 with these specifics:

- **Line length**: 100 characters max
- **Imports**: Group by standard library, third-party, local
- **Docstrings**: Use for all public classes and methods
- **Type hints**: Use for function signatures
- **Naming**:
  - Classes: `PascalCase`
  - Functions/methods: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`
  - Private: `_leading_underscore`

## Dependencies

### Required

- Python 3.8+
- PyGObject (GTK+ 3.0 bindings)
- GTK+ 3.0
- GLib
- Libnotify

### Optional

- pytest (for testing)
- sphinx (for documentation)

## Performance Considerations

- Timer uses 1-second intervals (not sub-second precision)
- Statistics queries are lightweight (indexed by date)
- UI updates are minimal (only when needed)
- No background threads (uses GLib timeouts)

## Security Considerations

- All data stored locally
- No network access required
- Settings/database files use standard permissions
- No sensitive data collected

## Future Improvements

Potential areas for enhancement:

1. **Sound notifications**: Add audio alerts
2. **System tray**: Minimize to tray
3. **Keyboard shortcuts**: Global hotkeys
4. **Data export**: Export statistics to CSV
5. **Multiple profiles**: Different timer presets
6. **Integration**: Calendar/task manager integration

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines.

## Resources

- [GTK Documentation](https://docs.gtk.org/)
- [PyGObject Documentation](https://pygobject.readthedocs.io/)
- [GNOME HIG](https://developer.gnome.org/hig/)
- [Flatpak Documentation](https://docs.flatpak.org/)
