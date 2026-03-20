#!/bin/bash

set -euo pipefail

APP_DIR="$HOME/.local/share/stand_reminder"
DESKTOP_FILE="$HOME/.local/share/applications/stand-reminder.desktop"

echo "Uninstalling Stand Reminder..."

# Remove application directory

if [ -d "$APP_DIR" ]; then
	rm -rf "$APP_DIR"
	echo "Removed application files."
else
	echo "Application files not found (already removed)."
fi

# Remove desktop launcher

if [ -f "$DESKTOP_FILE" ]; then
	rm "$DESKTOP_FILE"
	echo "Removed launcher."
else
	echo "Launcher not found (already removed)."
fi

echo "Stand Reminder has been uninstalled."
