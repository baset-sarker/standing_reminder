import tkinter as tk
from tkinter import messagebox
import threading
import time
import subprocess

TIMER_MINUTES = 1
STANDING_MINUTES = 1
timer_started = False
current_mode = "idle"

# add logo on notifications
def show_notification(title, message):
    subprocess.run([
        "notify-send",
        "--icon", "./stand_reminder.png",  # replace with actual path to logo
        title,
        message
    ])

def start_timer():
    global timer_started, current_mode
    if timer_started:
        return

    timer_started = True
    current_mode = "Sitting"
    btn.config(state=tk.DISABLED, text="Timer Running...")
    status_label.config(text=f"Mode: {current_mode}")

    # minimize window
    root.iconify()
    
    # run timer in background thread
    threading.Thread(target=run_timer, daemon=True).start()

def run_timer():
    #time.sleep(TIMER_MINUTES * 60)

    # updated remaining time every minute
    for remaining in range(TIMER_MINUTES, 0, -1):
        root.after(0, lambda r=remaining: status_label.config(text=f"Mode: {current_mode} - {r} min left"))
        print(f"Seating running... {remaining} minutes left")
        time.sleep(60)
    
    # show popup when done
    root.after(0, show_popup)

def run_standing_break():
    global current_mode
    current_mode = "Standing"
    root.after(0, lambda: status_label.config(text=f"Mode: {current_mode}"))
    
    #time.sleep(STANDING_MINUTES * 60)
    for remaining in range(STANDING_MINUTES, 0, -1):
        root.after(0, lambda r=remaining: status_label.config(text=f"Mode: {current_mode} - {r} min left"))
        print(f"Standing break... {remaining} minutes left")
        time.sleep(60)
    
    root.after(0, lambda: messagebox.showinfo("Standing Break Over", f"Your {STANDING_MINUTES} minute standing time is over. You can sit back down."))
    #root.after(0, reset_timer)
    #root.after(0,start_timer) # start next sitting timer again
    root.iconify()
    threading.Thread(target=run_timer, daemon=True).start()

def show_popup():
    global timer_started, current_mode
    root.deiconify()  # restore window
    messagebox.showinfo("Reminder", f"You are sitting for {TIMER_MINUTES} minutes. Please stand.")
    root.iconify()
    threading.Thread(target=run_standing_break, daemon=True).start()

def reset_timer():
    global timer_started, current_mode
    timer_started = False
    current_mode = "Sitting"
    btn.config(state=tk.NORMAL, text=f"Start {TIMER_MINUTES} min Timer")
    status_label.config(text=f"Mode: {current_mode}")

root = tk.Tk()
root.title("Standing Reminder")
root.geometry("250x150")

btn = tk.Button(root, text=f"Start {TIMER_MINUTES} min Timer", command=start_timer)
btn.pack(pady=20)

status_label = tk.Label(root, text=f"Mode: {current_mode}", font=("Arial", 14))
status_label.pack(pady=10)

root.mainloop()