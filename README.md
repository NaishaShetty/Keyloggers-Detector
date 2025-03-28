# Keyloggers-Detector
Keylogger Detector is a Python-based tool designed to scan, detect, and alert users about potential keyloggers running on their system. It consists of a backend detection module and a modern frontend GUI for easy interaction.

# Features
* Detects keyloggers using keyboard hooks and active window monitoring
* Modern GUI with real-time scan results
* Color-coded alerts for better visualization
* Safe-list implementation to reduce false positives
* Scalable architecture for future API integration

# Dependencies used
psutil - Process monitoring

pywin32 - Windows API access

tkinter - GUI framework (pre-installed with Python)

# How it works?
1)Scans active processes for suspicious activity.

2)Compares against known keylogger behavior (e.g., keyboard hooks).

3)Displays results in an easy-to-read interface.

4)Alerts users in case of threats.
