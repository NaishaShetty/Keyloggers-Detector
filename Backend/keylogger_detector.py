import psutil
import win32api
import win32process
import win32gui

# Function to get running processes
def get_process_info():
    process_list = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_list.append((process.info['pid'], process.info['name']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return process_list

# Function to check for keyboard hooks (keyloggers)
def check_keyboard_hooks():
    suspected_processes = []
    trusted_processes = ["explorer.exe", "chrome.exe", "notepad.exe", "cmd.exe", "python.exe", "taskmgr.exe"]

    for pid, name in get_process_info():
        if name.lower() in trusted_processes:
            continue  # Ignore trusted processes

        try:
            h_process = win32api.OpenProcess(win32process.PROCESS_QUERY_INFORMATION, False, pid)
            modules = win32process.EnumProcessModules(h_process)
            for module in modules:
                module_name = win32process.GetModuleFileNameEx(h_process, module)
                if "keyboard" in module_name.lower() or "hook" in module_name.lower():
                    suspected_processes.append((pid, name))
        except Exception:
            continue

    return suspected_processes

# Function to check active window monitoring
def check_active_window_logging():
    suspected = []
    safe_processes = ["notepad.exe", "chrome.exe", "explorer.exe", "python.exe"]

    for pid, name in get_process_info():
        if name.lower() in safe_processes:
            continue  # Ignore safe apps

        try:
            window = win32gui.GetForegroundWindow()
            _, process_id = win32process.GetWindowThreadProcessId(window)

            if pid == process_id:
                suspected.append((pid, name))
        except Exception:
            continue

    return suspected

# Function to detect keyloggers and return results
def detect_keyloggers():
    keyloggers = check_keyboard_hooks()
    window_loggers = check_active_window_logging()

    results = {
        "status": "safe",
        "suspected": []
    }

    if keyloggers or window_loggers:
        results["status"] = "danger"
        results["suspected"] = keyloggers + window_loggers

    return results
