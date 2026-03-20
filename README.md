# Stand Reminder

A small desktop app that reminds you to alternate between sitting and standing.

Built with Python + Tkinter.

## What It Does

- Starts a sitting timer (default: 25 minutes)
- Shows a popup: "Please stand."
- Runs a standing timer (default: 5 minutes)
- Shows a popup: "Sit back down."
- Automatically restarts the cycle
- Minimizes itself while timers are running

## Requirements

- Linux desktop environment (for app launcher integration)
- Python 3
- Tkinter (usually provided by your OS package `python3-tk`)

## Run Directly

From this folder:

```bash
python3 stand_reminder.py
```

Run with debug logs:

```bash
python3 stand_reminder.py --debug
```

## Install (Application Launcher)

The install script:

- Copies the app to `~/.local/share/stand_reminder`
- Creates a launcher at `~/.local/share/applications/stand-reminder.desktop`
- Uses your current `python3` in `PATH`

Install:

```bash
chmod +x install.sh
./install.sh
```

After installing, open your Applications menu and launch **Stand Reminder**.

## Uninstall

```bash
chmod +x uninstall.sh
./uninstall.sh
```

This removes:

- `~/.local/share/stand_reminder`
- `~/.local/share/applications/stand-reminder.desktop`

## Customize Timer Lengths

Edit constants in `stand_reminder.py`:

- `TIMER_MINUTES = 25`
- `STANDING_MINUTES = 5`

Then re-run or reinstall if you use the launcher copy.

## Notes

- Current `.desktop` comment says "20 minute sitting reminder", but the app default is 25 minutes.
- Backup script versions are kept in `bkp/`.
