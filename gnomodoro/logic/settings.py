"""Settings management for Gnomodoro"""

import json
import os
from pathlib import Path
from typing import Any, Dict


class Settings:
    """Manage application settings"""

    DEFAULT_SETTINGS = {
        "work_duration": 25,
        "short_break_duration": 5,
        "long_break_duration": 15,
        "pomodoros_until_long_break": 4,
        "notifications_enabled": True,
        "sound_enabled": True,
        "auto_start_breaks": False,
        "auto_start_work": False,
        "theme": "system",  # system, light, dark
    }

    def __init__(self):
        """Initialize settings"""
        self.config_dir = Path.home() / ".config" / "gnomodoro"
        self.config_file = self.config_dir / "settings.json"
        self.settings = self.DEFAULT_SETTINGS.copy()
        self.load()

    def load(self) -> None:
        """Load settings from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    loaded_settings = json.load(f)
                    self.settings.update(loaded_settings)
            except (json.JSONDecodeError, IOError):
                # If loading fails, use defaults
                pass

    def save(self) -> None:
        """Save settings to file"""
        self.config_dir.mkdir(parents=True, exist_ok=True)
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.settings, f, indent=2)
        except IOError:
            pass

    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value"""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a setting value"""
        self.settings[key] = value
        self.save()

    def reset(self) -> None:
        """Reset settings to defaults"""
        self.settings = self.DEFAULT_SETTINGS.copy()
        self.save()
