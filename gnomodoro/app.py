"""Main application class"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

from .ui.main_window import MainWindow


class GnomodoroApplication(Gtk.Application):
    """Main Gnomodoro Application"""

    def __init__(self):
        """Initialize the application"""
        super().__init__(
            application_id="com.github.igormilovanovic.gnomodoro",
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        self.window = None

    def do_activate(self):
        """Activate the application"""
        if not self.window:
            self.window = MainWindow(self)
        self.window.present()

    def do_shutdown(self):
        """Shutdown the application"""
        if self.window:
            self.window.cleanup()
        Gtk.Application.do_shutdown(self)
