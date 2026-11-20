
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Main window
root = tk.Tk()
root.title("Login Attempt Tracker")
root.geometry("650x650")
root.configure(bg="#EAF2F8")

# Login counters
total_attempts = 0
successful_attempts = 0
failed_attempts = 0

# Heading
heading = tk.Label(
    root,
    text="LOGIN ATTEMPT TRACKER",
    font=("Arial", 22, "bold"),
    bg="#EAF2F8",
    fg="#17365D"
)
heading.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Cybersecurity Monitoring Dashboard",
    font=("Arial", 12),
    bg="#EAF2F8"
)
subtitle.pack(pady=5)

# Dashboard counters
total_label = tk.Label(
    root, text="Total Attempts: 0",
    font=("Arial", 14),
      bg="#EAF2F8"
)
total_label.pack(pady=8)

success_label = tk.Label(
    root, text="Successful Logins: 0",
    font=("Arial", 14),
      bg="#EAF2F8"
)
success_label.pack(pady=8)

failed_label = tk.Label(
    root, text="Failed Logins: 0",
    font=("Arial", 14), 
    bg="#EAF2F8"
)
failed_label.pack(pady=8)

# Activity history
history_label = tk.Label(
    root,
    text="LOGIN ACTIVITY HISTORY",
    font=("Arial", 14, "bold"),
    bg="#EAF2F8"
)
history_label.pack(pady=12)

history_box = tk.Listbox(
    root,
    width=65,
    height=10,
    font=("Arial", 10)
)
history_box.pack(pady=5)

# Update dashboard
def update_dashboard():
    total_label.config(text=f"Total Attempts: {total_attempts}")
    success_label.config(
        text=f"Successful Logins: {successful_attempts}"
    )
    failed_label.config(
        text=f"Failed Logins: {failed_attempts}"
    )

# Successful login
def successful_login():
    global total_attempts, successful_attempts

    total_attempts += 1
    successful_attempts += 1

    time_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    history_box.insert(
        tk.END,
        f"{time_now} - Successful Login"
    )

    update_dashboard()

# Failed login
def failed_login():
    global total_attempts, failed_attempts

    total_attempts += 1
    failed_attempts += 1

    time_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    history_box.insert(
        tk.END,
        f"{time_now} - Failed Login"
    )

    update_dashboard()

    if failed_attempts == 3:
        messagebox.showwarning(
            "Security Alert",
            "Warning! 3 failed login attempts detected!"
        )

    elif failed_attempts > 3:
        messagebox.showwarning(
            "Security Alert",
            "Repeated failed login attempts detected!"
        )

# Clear history
def clear_history():
    if messagebox.askyesno(
        "Confirm",
        "Do you want to clear login history?"
    ):
        history_box.delete(0, tk.END)

# Buttons
success_button = tk.Button(
    root,
    text="Successful Login",
    command=successful_login,
    font=("Arial", 12, "bold"),
    bg="#27AE60",
    fg="white",
    width=22
)
success_button.pack(pady=8)

failed_button = tk.Button(
    root,
    text="Failed Login",
    command=failed_login,
    font=("Arial", 12, "bold"),
    bg="#E74C3C",
    fg="white",
    width=22
)
failed_button.pack(pady=8)

clear_button = tk.Button(
    root,
    text="Clear History",
    command=clear_history,
    font=("Arial", 11),
    bg="#34495E",
    fg="white",
    width=22
)
clear_button.pack(pady=8)

# Footer
footer = tk.Label(
    root,
    text="Login Attempt Tracker | Cybersecurity Project",
    font=("Arial", 9),
    bg="#EAF2F8",
    fg="#555555"
)
footer.pack(pady=12)

root.mainloop()
