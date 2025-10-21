"""
Main window for the Gnomodoro application.
"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class GnomodoroWindow(Gtk.ApplicationWindow):
    """Main application window."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window properties
        self.set_title("Gnomodoro")
        self.set_default_size(400, 300)
        self.set_border_width(20)

        # Create a vertical box layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Welcome label
        label = Gtk.Label()
        label.set_markup("<big><b>Welcome to Gnomodoro!</b></big>")
        label.set_margin_bottom(20)
        vbox.pack_start(label, False, False, 0)

        # Timer display label (placeholder)
        self.timer_label = Gtk.Label()
        self.timer_label.set_markup("<span font='48'>25:00</span>")
        vbox.pack_start(self.timer_label, True, False, 0)

        # Button box
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_box.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(button_box, False, False, 10)

        # Start button
        start_button = Gtk.Button(label="Start")
        start_button.connect("clicked", self.on_start_clicked)
        button_box.pack_start(start_button, False, False, 0)

        # Pause button
        pause_button = Gtk.Button(label="Pause")
        pause_button.connect("clicked", self.on_pause_clicked)
        button_box.pack_start(pause_button, False, False, 0)

        # Reset button
        reset_button = Gtk.Button(label="Reset")
        reset_button.connect("clicked", self.on_reset_clicked)
        button_box.pack_start(reset_button, False, False, 0)

        # Status label
        self.status_label = Gtk.Label()
        self.status_label.set_text("Ready to start a Pomodoro session")
        self.status_label.set_margin_top(10)
        vbox.pack_start(self.status_label, False, False, 0)

    def on_start_clicked(self, button):
        """Handle start button click."""
        self.status_label.set_text("Timer started (feature coming soon)")
        print("Start button clicked")

    def on_pause_clicked(self, button):
        """Handle pause button click."""
        self.status_label.set_text("Timer paused (feature coming soon)")
        print("Pause button clicked")

    def on_reset_clicked(self, button):
        """Handle reset button click."""
        self.status_label.set_text("Timer reset")
        self.timer_label.set_markup("<span font='48'>25:00</span>")
        print("Reset button clicked")


class GnomodoroApp(Gtk.Application):
    """Main Gnomodoro application."""

    def __init__(self):
        super().__init__(application_id="com.github.igormilovanovic.gnomodoro")
        self.window = None

    def do_activate(self):
        """Activate the application."""
        if not self.window:
            self.window = GnomodoroWindow(application=self)
        self.window.show_all()
        self.window.present()

    def do_startup(self):
        """Initialize the application."""
        Gtk.Application.do_startup(self)
