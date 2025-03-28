# Backend
This is the backend for the Keylogger Detector, responsible for scanning processes, detecting potential keyloggers, and returning the results to the frontend.

# Features
* Detects keyloggers using keyboard hooks and active window monitoring
* Uses Windows API to analyze running processes
* Provides structured results for the frontend to display
* Implements a safe-list to reduce false positives

# Dependencies Used
psutil - Process monitoring

pywin32 - Windows API access

