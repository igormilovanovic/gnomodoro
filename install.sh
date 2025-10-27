#!/bin/bash

# Installation script for Gnomodoro

set -e

echo "Installing Gnomodoro..."

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not found."
    echo "Please install Python 3.8 or higher."
    exit 1
fi

# Check for required system packages
if [ -f /etc/debian_version ]; then
    echo "Detected Debian/Ubuntu system"
    echo "Installing system dependencies..."
    sudo apt-get update
    sudo apt-get install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-notify-0.7
elif [ -f /etc/fedora-release ]; then
    echo "Detected Fedora system"
    echo "Installing system dependencies..."
    sudo dnf install -y python3-gobject gtk3 libnotify
elif [ -f /etc/arch-release ]; then
    echo "Detected Arch Linux system"
    echo "Installing system dependencies..."
    sudo pacman -S --needed python-gobject gtk3 libnotify
else
    echo "Warning: Could not detect your distribution."
    echo "Please install the following packages manually:"
    echo "  - Python 3.8+"
    echo "  - PyGObject (python3-gi)"
    echo "  - GTK+ 3.0"
    echo "  - Libnotify"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install --user -r requirements.txt

# Create desktop entry
echo "Creating desktop entry..."
DESKTOP_DIR="$HOME/.local/share/applications"
mkdir -p "$DESKTOP_DIR"

cat > "$DESKTOP_DIR/com.github.igormilovanovic.gnomodoro.desktop" << EOF
[Desktop Entry]
Name=Gnomodoro
GenericName=Pomodoro Timer
Comment=A simple Pomodoro timer for GNOME
Exec=$(pwd)/gnomodoro.py
Icon=$(pwd)/assets/icons/gnomodoro.svg
Terminal=false
Type=Application
Categories=GTK;GNOME;Utility;Office;
Keywords=pomodoro;timer;productivity;time;management;
StartupNotify=true
EOF

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$DESKTOP_DIR"
fi

echo ""
echo "Installation complete!"
echo ""
echo "You can now run Gnomodoro by:"
echo "  1. Searching for 'Gnomodoro' in your application menu"
echo "  2. Running: ./gnomodoro.py"
echo ""
echo "To uninstall, run: ./uninstall.sh"
