import tkinter as tk
from tkinter import ttk, messagebox
from keylogger_detector import detect_keyloggers  # Import backend function

# GUI Setup
root = tk.Tk()
root.title("Keylogger Detector")
root.geometry("600x450")
root.configure(bg="#121212")

# Title Label
title_label = tk.Label(root, text="🛡️ Keylogger Detector", font=("Arial", 18, "bold"), fg="lime", bg="#121212")
title_label.pack(pady=10)

# Text Area for Displaying Results
text_area = tk.Text(root, height=14, width=70, bg="#1e1e1e", fg="white", font=("Arial", 10))
text_area.pack(pady=10)

# Custom Tags for Styling
text_area.tag_config("warning", foreground="red", font=("Arial", 10, "bold"))
text_area.tag_config("safe", foreground="lime", font=("Arial", 10, "bold"))

# Status Image
status_label = tk.Label(root, text="", bg="#121212", font=("Arial", 12))
status_label.pack(pady=5)

# Function to Scan for Keyloggers
def run_detection():
    text_area.delete("1.0", tk.END)  # Clear previous results
    text_area.insert(tk.END, "🔍 Scanning for keyloggers...\n")

    result = detect_keyloggers()

    if result["status"] == "danger":
        text_area.insert(tk.END, "\n⚠️ Possible Keyloggers Detected:\n", "warning")
        for pid, name in result["suspected"]:
            text_area.insert(tk.END, f"  - PID: {pid}, Process: {name}\n", "warning")
        status_label.config(text="⚠️ Suspicious activity detected!", fg="red")
        messagebox.showwarning("Keylogger Alert", "Suspicious activity detected!")
    else:
        text_area.insert(tk.END, "\n✅ No keyloggers found. Your system is safe!\n", "safe")
        status_label.config(text="✅ No threats detected!", fg="lime")

# Scan Button
scan_button = ttk.Button(root, text="🔍 Scan Now", command=run_detection)
scan_button.pack(pady=10)

# Run the GUI
root.mainloop()
