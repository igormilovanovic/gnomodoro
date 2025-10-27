"""Unit tests for settings module"""

import unittest
import tempfile
import shutil
from pathlib import Path
from gnomodoro.logic.settings import Settings


class TestSettings(unittest.TestCase):
    """Test cases for Settings class"""

    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.test_config_dir = Path(self.test_dir) / ".config" / "gnomodoro"
        
        # Monkey patch the config_dir for testing
        self.original_home = Path.home
        Path.home = lambda: Path(self.test_dir)
        
        self.settings = Settings()

    def tearDown(self):
        """Clean up test fixtures"""
        # Restore original Path.home
        Path.home = self.original_home
        
        # Remove temporary directory
        shutil.rmtree(self.test_dir)

    def test_default_settings(self):
        """Test default settings values"""
        self.assertEqual(self.settings.get("work_duration"), 25)
        self.assertEqual(self.settings.get("short_break_duration"), 5)
        self.assertEqual(self.settings.get("long_break_duration"), 15)
        self.assertEqual(self.settings.get("pomodoros_until_long_break"), 4)
        self.assertEqual(self.settings.get("notifications_enabled"), True)

    def test_get_setting(self):
        """Test getting a setting value"""
        value = self.settings.get("work_duration")
        self.assertEqual(value, 25)

    def test_get_setting_with_default(self):
        """Test getting a non-existent setting with default value"""
        value = self.settings.get("non_existent", "default_value")
        self.assertEqual(value, "default_value")

    def test_set_setting(self):
        """Test setting a value"""
        self.settings.set("work_duration", 30)
        self.assertEqual(self.settings.get("work_duration"), 30)

    def test_save_and_load(self):
        """Test saving and loading settings"""
        self.settings.set("work_duration", 30)
        self.settings.set("short_break_duration", 10)
        
        # Create a new settings instance (should load saved settings)
        new_settings = Settings()
        self.assertEqual(new_settings.get("work_duration"), 30)
        self.assertEqual(new_settings.get("short_break_duration"), 10)

    def test_reset_settings(self):
        """Test resetting settings to defaults"""
        self.settings.set("work_duration", 30)
        self.settings.reset()
        self.assertEqual(self.settings.get("work_duration"), 25)


if __name__ == "__main__":
    unittest.main()
