#!/bin/bash

# Uninstall script for Gnomodoro

echo "Uninstalling Gnomodoro..."

# Remove desktop entry
DESKTOP_FILE="$HOME/.local/share/applications/com.github.igormilovanovic.gnomodoro.desktop"
if [ -f "$DESKTOP_FILE" ]; then
    echo "Removing desktop entry..."
    rm "$DESKTOP_FILE"
fi

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$HOME/.local/share/applications"
fi

echo ""
echo "Gnomodoro has been uninstalled."
echo ""
echo "Note: Your settings and data are still in:"
echo "  - Settings: ~/.config/gnomodoro/"
echo "  - Data: ~/.local/share/gnomodoro/"
echo ""
echo "To remove these as well, run:"
echo "  rm -rf ~/.config/gnomodoro ~/.local/share/gnomodoro"
