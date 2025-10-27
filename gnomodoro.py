#!/usr/bin/env python3
"""Gnomodoro - A Pomodoro Timer for GNOME Desktop

Entry point for the application.
"""

import sys
from gnomodoro.app import GnomodoroApplication


def main():
    """Main entry point"""
    app = GnomodoroApplication()
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
