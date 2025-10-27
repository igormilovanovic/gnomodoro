"""Settings dialog"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SettingsDialog(Gtk.Dialog):
    """Settings configuration dialog"""

    def __init__(self, parent, settings, timer):
        """Initialize settings dialog"""
        super().__init__(title="Settings", parent=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        
        self.settings = settings
        self.timer = timer
        
        self.set_default_size(400, 400)
        self.set_border_width(10)
        
        box = self.get_content_area()
        
        # Timer durations section
        durations_frame = Gtk.Frame(label="Timer Durations (minutes)")
        durations_frame.set_margin_bottom(10)
        box.pack_start(durations_frame, False, False, 0)
        
        durations_grid = Gtk.Grid()
        durations_grid.set_border_width(10)
        durations_grid.set_row_spacing(10)
        durations_grid.set_column_spacing(10)
        durations_frame.add(durations_grid)
        
        # Work duration
        work_label = Gtk.Label(label="Work Duration:")
        work_label.set_halign(Gtk.Align.START)
        durations_grid.attach(work_label, 0, 0, 1, 1)
        
        self.work_spin = Gtk.SpinButton()
        self.work_spin.set_range(1, 120)
        self.work_spin.set_increments(1, 5)
        self.work_spin.set_value(self.settings.get("work_duration", 25))
        durations_grid.attach(self.work_spin, 1, 0, 1, 1)
        
        # Short break duration
        short_break_label = Gtk.Label(label="Short Break Duration:")
        short_break_label.set_halign(Gtk.Align.START)
        durations_grid.attach(short_break_label, 0, 1, 1, 1)
        
        self.short_break_spin = Gtk.SpinButton()
        self.short_break_spin.set_range(1, 60)
        self.short_break_spin.set_increments(1, 5)
        self.short_break_spin.set_value(self.settings.get("short_break_duration", 5))
        durations_grid.attach(self.short_break_spin, 1, 1, 1, 1)
        
        # Long break duration
        long_break_label = Gtk.Label(label="Long Break Duration:")
        long_break_label.set_halign(Gtk.Align.START)
        durations_grid.attach(long_break_label, 0, 2, 1, 1)
        
        self.long_break_spin = Gtk.SpinButton()
        self.long_break_spin.set_range(1, 120)
        self.long_break_spin.set_increments(1, 5)
        self.long_break_spin.set_value(self.settings.get("long_break_duration", 15))
        durations_grid.attach(self.long_break_spin, 1, 2, 1, 1)
        
        # Pomodoros until long break
        long_break_count_label = Gtk.Label(label="Pomodoros Until Long Break:")
        long_break_count_label.set_halign(Gtk.Align.START)
        durations_grid.attach(long_break_count_label, 0, 3, 1, 1)
        
        self.long_break_count_spin = Gtk.SpinButton()
        self.long_break_count_spin.set_range(1, 10)
        self.long_break_count_spin.set_increments(1, 1)
        self.long_break_count_spin.set_value(self.settings.get("pomodoros_until_long_break", 4))
        durations_grid.attach(self.long_break_count_spin, 1, 3, 1, 1)
        
        # Behavior section
        behavior_frame = Gtk.Frame(label="Behavior")
        behavior_frame.set_margin_bottom(10)
        box.pack_start(behavior_frame, False, False, 0)
        
        behavior_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        behavior_box.set_border_width(10)
        behavior_frame.add(behavior_box)
        
        self.auto_start_breaks_check = Gtk.CheckButton(label="Auto-start breaks")
        self.auto_start_breaks_check.set_active(self.settings.get("auto_start_breaks", False))
        behavior_box.pack_start(self.auto_start_breaks_check, False, False, 0)
        
        self.auto_start_work_check = Gtk.CheckButton(label="Auto-start work sessions")
        self.auto_start_work_check.set_active(self.settings.get("auto_start_work", False))
        behavior_box.pack_start(self.auto_start_work_check, False, False, 0)
        
        self.notifications_check = Gtk.CheckButton(label="Enable notifications")
        self.notifications_check.set_active(self.settings.get("notifications_enabled", True))
        behavior_box.pack_start(self.notifications_check, False, False, 0)
        
        # Theme section
        theme_frame = Gtk.Frame(label="Appearance")
        box.pack_start(theme_frame, False, False, 0)
        
        theme_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        theme_box.set_border_width(10)
        theme_frame.add(theme_box)
        
        theme_label = Gtk.Label(label="Theme:")
        theme_label.set_halign(Gtk.Align.START)
        theme_box.pack_start(theme_label, False, False, 0)
        
        self.theme_combo = Gtk.ComboBoxText()
        self.theme_combo.append("system", "System Default")
        self.theme_combo.append("light", "Light")
        self.theme_combo.append("dark", "Dark")
        self.theme_combo.set_active_id(self.settings.get("theme", "system"))
        theme_box.pack_start(self.theme_combo, False, False, 0)
        
        self.show_all()
        
        response = self.run()
        if response == Gtk.ResponseType.OK:
            self._save_settings()

    def _save_settings(self):
        """Save settings"""
        # Save timer durations
        work_duration = int(self.work_spin.get_value())
        short_break_duration = int(self.short_break_spin.get_value())
        long_break_duration = int(self.long_break_spin.get_value())
        long_break_count = int(self.long_break_count_spin.get_value())
        
        self.settings.set("work_duration", work_duration)
        self.settings.set("short_break_duration", short_break_duration)
        self.settings.set("long_break_duration", long_break_duration)
        self.settings.set("pomodoros_until_long_break", long_break_count)
        
        # Update timer
        self.timer.set_work_duration(work_duration)
        self.timer.set_short_break_duration(short_break_duration)
        self.timer.set_long_break_duration(long_break_duration)
        self.timer.pomodoros_until_long_break = long_break_count
        
        # Save behavior settings
        self.settings.set("auto_start_breaks", self.auto_start_breaks_check.get_active())
        self.settings.set("auto_start_work", self.auto_start_work_check.get_active())
        self.settings.set("notifications_enabled", self.notifications_check.get_active())
        
        # Save theme
        theme = self.theme_combo.get_active_id()
        self.settings.set("theme", theme)
        
        # Apply theme
        settings = Gtk.Settings.get_default()
        if theme == "dark":
            settings.set_property("gtk-application-prefer-dark-theme", True)
        elif theme == "light":
            settings.set_property("gtk-application-prefer-dark-theme", False)
