"""
Main entry point for the Gnomodoro application.
"""

import sys
from gnomodoro.ui.main_window import GnomodoroApp


def main():
    """Run the Gnomodoro application."""
    app = GnomodoroApp()
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
