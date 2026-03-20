import tkinter as tk
from tkinter import messagebox
import argparse

# ================= CONFIG =================
TIMER_MINUTES = 25
STANDING_MINUTES = 5

# ================= GLOBAL STATE =================
timer_started = False
current_mode = "Not Started"
remaining_minutes = 0
DEBUG = False

# ================= ARGPARSE =================
parser = argparse.ArgumentParser(description="Standing Reminder")
parser.add_argument("--debug", action="store_true", help="Enable debug logs")
args = parser.parse_args()
DEBUG = args.debug


def debug_log(message):
    if DEBUG:
        print(message)


# ================= TIMER LOGIC =================
def start_timer():
    global timer_started, current_mode, remaining_minutes

    if timer_started:
        return

    timer_started = True
    current_mode = "Sitting"
    remaining_minutes = TIMER_MINUTES

    btn.config(state=tk.DISABLED, text="Timer Running...")
    update_timer()
    root.iconify()


def update_timer():
    global remaining_minutes

    status_label.config(
        text=f"Mode: {current_mode} - {remaining_minutes} min left",
        fg="black"
    )

    debug_log(f"Sitting... {remaining_minutes} min left")

    if remaining_minutes > 0:
        remaining_minutes -= 1
        root.after(60000, update_timer)  # 60 seconds
    else:
        show_popup()


# ================= STANDING BREAK =================
def run_standing_break():
    global current_mode, remaining_minutes

    current_mode = "Standing"
    remaining_minutes = STANDING_MINUTES
    update_standing()


def update_standing():
    global remaining_minutes

    status_label.config(
        text=f"Mode: {current_mode} - {remaining_minutes} min left",
        fg="blue"
    )

    debug_log(f"Standing... {remaining_minutes} min left")

    if remaining_minutes > 0:
        remaining_minutes -= 1
        root.after(60000, update_standing)
    else:
        on_standing_break_complete()


# ================= POPUPS =================
def show_popup():
    root.deiconify()
    status_label.config(fg="red")

    messagebox.showinfo("Reminder", "Please stand.")

    root.iconify()
    run_standing_break()


def on_standing_break_complete():
    global timer_started

    root.deiconify()
    messagebox.showinfo("Standing Break Over", "Sit back down.")

    timer_started = False
    btn.config(state=tk.NORMAL, text=f"Start {TIMER_MINUTES} min Timer")

    start_timer()  # auto-restart


# ================= UI =================
root = tk.Tk()
root.title("Standing Reminder")
root.geometry("250x150")

btn = tk.Button(root, text=f"Start {TIMER_MINUTES} min Timer", command=start_timer)
btn.pack(pady=20)

status_label = tk.Label(root, text=f"Mode: {current_mode}", font=("Arial", 14))
status_label.pack(pady=10)

root.mainloop()