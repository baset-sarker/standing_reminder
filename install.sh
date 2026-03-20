#!/bin/bash

set -euo pipefail

APP_NAME="Stand Reminder"
APP_DIR="$HOME/.local/share/stand_reminder"
DESKTOP_FILE="$HOME/.local/share/applications/stand-reminder.desktop"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_SCRIPT="$SCRIPT_DIR/stand_reminder.py"
SOURCE_ICON="$SCRIPT_DIR/stand_reminder.png"
PYTHON_BIN="$(command -v python3 || true)"

if [ -z "$PYTHON_BIN" ]; then
	echo "Error: python3 not found in PATH."
	exit 1
fi

echo "Installing Stand Reminder..."

# Create application directory

mkdir -p "$APP_DIR"
mkdir -p "$(dirname "$DESKTOP_FILE")"

# Copy files

if [ ! -f "$SOURCE_SCRIPT" ]; then
	echo "Error: $SOURCE_SCRIPT not found."
	exit 1
fi

cp "$SOURCE_SCRIPT" "$APP_DIR/"

if [ -f "$SOURCE_ICON" ]; then
	cp "$SOURCE_ICON" "$APP_DIR/"
fi

# Make python script executable

chmod +x "$APP_DIR/stand_reminder.py"

# Create desktop launcher

cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Version=1.0
Name=Stand Reminder
Comment=20 minute sitting reminder
Exec=$PYTHON_BIN $APP_DIR/stand_reminder.py
Path=$APP_DIR
Terminal=false
Type=Application
Categories=Utility;
EOL

if [ -f "$APP_DIR/stand_reminder.png" ]; then
	printf 'Icon=%s\n' "$APP_DIR/stand_reminder.png" >> "$DESKTOP_FILE"
fi

# Make launcher executable

chmod +x "$DESKTOP_FILE"

echo "Installation complete."
echo "You can now find 'Stand Reminder' in your Applications menu."
echo "Open it once and right-click → Pin to Dock if you want."
