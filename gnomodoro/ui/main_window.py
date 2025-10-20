"""Main application window"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk

from ..logic.timer import PomodoroTimer, TimerState, TimerType
from ..logic.settings import Settings
from ..logic.statistics import Statistics
from ..utils.notifications import NotificationManager


class MainWindow(Gtk.ApplicationWindow):
    """Main application window for Gnomodoro"""

    def __init__(self, application):
        """Initialize the main window"""
        super().__init__(application=application, title="Gnomodoro")
        
        self.set_default_size(400, 300)
        self.set_border_width(20)
        
        # Initialize components
        self.settings = Settings()
        self.statistics = Statistics()
        self.notification_manager = NotificationManager()
        
        # Initialize timer
        self.timer = PomodoroTimer(
            work_duration=self.settings.get("work_duration", 25),
            short_break_duration=self.settings.get("short_break_duration", 5),
            long_break_duration=self.settings.get("long_break_duration", 15),
            pomodoros_until_long_break=self.settings.get("pomodoros_until_long_break", 4),
        )
        
        # Set timer callbacks
        self.timer.set_on_tick_callback(self.on_timer_tick)
        self.timer.set_on_complete_callback(self.on_timer_complete)
        self.timer.set_on_state_change_callback(self.on_timer_state_change)
        
        # GLib timeout for timer updates
        self.timeout_id = None
        
        # Build UI
        self._build_ui()
        
        # Apply theme
        self._apply_theme()

    def _build_ui(self):
        """Build the user interface"""
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add(main_box)
        
        # Timer type label
        self.type_label = Gtk.Label()
        self.type_label.set_markup("<span font_size='14000'>Work Session</span>")
        main_box.pack_start(self.type_label, False, False, 0)
        
        # Timer display
        self.timer_label = Gtk.Label()
        self.timer_label.set_markup("<span font_size='48000' weight='bold'>25:00</span>")
        main_box.pack_start(self.timer_label, True, True, 0)
        
        # Control buttons
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        button_box.set_halign(Gtk.Align.CENTER)
        main_box.pack_start(button_box, False, False, 0)
        
        self.start_button = Gtk.Button(label="Start")
        self.start_button.connect("clicked", self.on_start_clicked)
        self.start_button.set_size_request(100, 40)
        button_box.pack_start(self.start_button, False, False, 0)
        
        self.pause_button = Gtk.Button(label="Pause")
        self.pause_button.connect("clicked", self.on_pause_clicked)
        self.pause_button.set_size_request(100, 40)
        self.pause_button.set_sensitive(False)
        button_box.pack_start(self.pause_button, False, False, 0)
        
        self.reset_button = Gtk.Button(label="Reset")
        self.reset_button.connect("clicked", self.on_reset_clicked)
        self.reset_button.set_size_request(100, 40)
        button_box.pack_start(self.reset_button, False, False, 0)
        
        # Statistics info
        self.stats_label = Gtk.Label()
        self.stats_label.set_markup("<span font_size='10000'>Today: 0 pomodoros</span>")
        main_box.pack_start(self.stats_label, False, False, 0)
        
        # Menu button
        menu_button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        menu_button_box.set_halign(Gtk.Align.END)
        main_box.pack_start(menu_button_box, False, False, 0)
        
        settings_button = Gtk.Button(label="Settings")
        settings_button.connect("clicked", self.on_settings_clicked)
        menu_button_box.pack_start(settings_button, False, False, 0)
        
        tasks_button = Gtk.Button(label="Tasks")
        tasks_button.connect("clicked", self.on_tasks_clicked)
        menu_button_box.pack_start(tasks_button, False, False, 0)
        
        stats_button = Gtk.Button(label="Statistics")
        stats_button.connect("clicked", self.on_statistics_clicked)
        menu_button_box.pack_start(stats_button, False, False, 0)
        
        self._update_statistics_display()

    def _apply_theme(self):
        """Apply theme based on settings"""
        theme_preference = self.settings.get("theme", "system")
        settings = Gtk.Settings.get_default()
        
        if theme_preference == "dark":
            settings.set_property("gtk-application-prefer-dark-theme", True)
        elif theme_preference == "light":
            settings.set_property("gtk-application-prefer-dark-theme", False)
        # "system" uses default

    def on_start_clicked(self, button):
        """Handle start button click"""
        self.timer.start()
        self.start_button.set_sensitive(False)
        self.pause_button.set_sensitive(True)
        self.pause_button.set_label("Pause")
        
        # Start GLib timeout
        if self.timeout_id is None:
            self.timeout_id = GLib.timeout_add_seconds(1, self.update_timer)

    def on_pause_clicked(self, button):
        """Handle pause/resume button click"""
        if self.timer.state == TimerState.RUNNING:
            self.timer.pause()
            self.pause_button.set_label("Resume")
        elif self.timer.state == TimerState.PAUSED:
            self.timer.resume()
            self.pause_button.set_label("Pause")

    def on_reset_clicked(self, button):
        """Handle reset button click"""
        self.timer.reset()
        self.start_button.set_sensitive(True)
        self.pause_button.set_sensitive(False)
        self.pause_button.set_label("Pause")
        
        # Stop GLib timeout
        if self.timeout_id is not None:
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
        
        self._update_timer_display()
        self._update_type_label()

    def on_settings_clicked(self, button):
        """Show settings dialog"""
        from .settings_dialog import SettingsDialog
        dialog = SettingsDialog(self, self.settings, self.timer)
        dialog.run()
        dialog.destroy()
        self._update_timer_display()
        self._update_type_label()

    def on_tasks_clicked(self, button):
        """Show tasks dialog"""
        from .tasks_dialog import TasksDialog
        dialog = TasksDialog(self, self.statistics)
        dialog.run()
        dialog.destroy()

    def on_statistics_clicked(self, button):
        """Show statistics dialog"""
        from .statistics_dialog import StatisticsDialog
        dialog = StatisticsDialog(self, self.statistics)
        dialog.run()
        dialog.destroy()

    def update_timer(self):
        """Update timer (called by GLib timeout)"""
        if not self.timer.tick():
            # Timer completed
            return False
        
        self._update_timer_display()
        return True

    def on_timer_tick(self, remaining_time):
        """Callback for timer tick"""
        pass  # Display update handled by update_timer

    def on_timer_complete(self, next_timer_type):
        """Callback for timer completion"""
        # Stop the GLib timeout
        if self.timeout_id is not None:
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
        
        # Record completed pomodoro
        if self.timer.timer_type in [TimerType.SHORT_BREAK, TimerType.LONG_BREAK]:
            # Previous timer was work
            work_duration = self.settings.get("work_duration", 25)
            self.statistics.add_completed_pomodoro(work_duration * 60)
            self._update_statistics_display()
        
        # Send notification
        if next_timer_type == TimerType.WORK:
            self.notification_manager.send_notification(
                "Break Complete!",
                "Time to get back to work!",
                urgency="normal"
            )
            self.type_label.set_markup("<span font_size='14000'>Work Session</span>")
        elif next_timer_type == TimerType.SHORT_BREAK:
            self.notification_manager.send_notification(
                "Work Complete!",
                "Time for a short break!",
                urgency="normal"
            )
            self.type_label.set_markup("<span font_size='14000'>Short Break</span>")
        else:
            self.notification_manager.send_notification(
                "Work Complete!",
                "Time for a long break!",
                urgency="normal"
            )
            self.type_label.set_markup("<span font_size='14000'>Long Break</span>")
        
        self._update_timer_display()
        
        # Reset buttons
        self.start_button.set_sensitive(True)
        self.pause_button.set_sensitive(False)
        self.pause_button.set_label("Pause")
        
        # Auto-start next timer if enabled
        auto_start_breaks = self.settings.get("auto_start_breaks", False)
        auto_start_work = self.settings.get("auto_start_work", False)
        
        if (next_timer_type == TimerType.WORK and auto_start_work) or \
           (next_timer_type in [TimerType.SHORT_BREAK, TimerType.LONG_BREAK] and auto_start_breaks):
            self.on_start_clicked(None)

    def on_timer_state_change(self, state):
        """Callback for timer state change"""
        pass

    def _update_timer_display(self):
        """Update the timer display"""
        time_str = self.timer.get_remaining_time_formatted()
        self.timer_label.set_markup(f"<span font_size='48000' weight='bold'>{time_str}</span>")

    def _update_type_label(self):
        """Update the timer type label"""
        if self.timer.timer_type == TimerType.WORK:
            self.type_label.set_markup("<span font_size='14000'>Work Session</span>")
        elif self.timer.timer_type == TimerType.SHORT_BREAK:
            self.type_label.set_markup("<span font_size='14000'>Short Break</span>")
        else:
            self.type_label.set_markup("<span font_size='14000'>Long Break</span>")

    def _update_statistics_display(self):
        """Update the statistics display"""
        stats = self.statistics.get_today_stats()
        count = stats["count"]
        self.stats_label.set_markup(f"<span font_size='10000'>Today: {count} pomodoros</span>")

    def cleanup(self):
        """Clean up resources"""
        if self.timeout_id is not None:
            GLib.source_remove(self.timeout_id)
        self.notification_manager.cleanup()
