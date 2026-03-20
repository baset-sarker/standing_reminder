import tkinter as tk
from tkinter import messagebox
import threading
import time
import argparse

TIMER_MINUTES = 25
STANDING_MINUTES = 5
DEBUG = False
timer_started = False
current_mode = "Not Started"

parser = argparse.ArgumentParser(description="Standing Reminder")
parser.add_argument("--debug", action="store_true", help="Enable debug logs")
args = parser.parse_args()
DEBUG = args.debug

def debug_log(message):
    if DEBUG:
        print(message)

def start_timer():
    global timer_started, current_mode
    if timer_started:
        return

    timer_started = True
    current_mode = "Sitting"
    btn.config(state=tk.DISABLED, text="Timer Running...")
    status_label.config(text=f"Mode: {current_mode}")

    root.iconify()
    threading.Thread(target=run_timer, daemon=True).start()

def run_timer():
    for remaining in range(TIMER_MINUTES, 0, -1):
        root.after(0, lambda r=remaining: status_label.config(text=f"Mode: {current_mode} - {r} min left"))
        debug_log(f"Sitting running... {remaining} minutes left")
        time.sleep(60)

    root.after(0, show_popup)

def run_standing_break():
    global current_mode, timer_started
    current_mode = "Standing"
    root.after(0, lambda: status_label.config(text=f"Mode: {current_mode}"))

    for remaining in range(STANDING_MINUTES, 0, -1):
        root.after(0, lambda r=remaining: status_label.config(text=f"Mode: {current_mode} - {r} min left"))
        debug_log(f"Standing break... {remaining} minutes left")
        time.sleep(60)

    root.after(0, on_standing_break_complete)

def show_popup():
    root.deiconify()
    status_label.config(fg="red")
    root.update_idletasks()
    messagebox.showinfo("Reminder", f"Please stand.")

    root.iconify()
    threading.Thread(target=run_standing_break, daemon=True).start()

def on_standing_break_complete():
    global timer_started
    messagebox.showinfo("Standing Break Over", f"Sit back down.")
    status_label.config(fg="black")
    timer_started = False
    start_timer()

root = tk.Tk()
root.title("Standing Reminder")
root.geometry("250x150")

btn = tk.Button(root, text=f"Start {TIMER_MINUTES} min Timer", command=start_timer)
btn.pack(pady=20)

status_label = tk.Label(root, text=f"Mode: {current_mode}", font=("Arial", 14))
status_label.pack(pady=10)

root.mainloop()