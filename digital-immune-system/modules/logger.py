import os
from datetime import datetime
from pathlib import Path
import platform

def get_log_file(filename="digital_immune_log.txt"):
    """Return cross-platform main log file path."""
    try:
        system = platform.system()
        if system == "Windows":
            folder = Path.home() / "Documents" / "DigitalImmuneLogs"
        else:
            folder = Path.home() / "DigitalImmuneLogs"
        folder.mkdir(parents=True, exist_ok=True)
        return folder / filename
    except Exception:
        return Path(filename)

def get_scan_results_folder():
    """
    Returns folder path for individual scan results:
    DigitalImmuneLogs/Scanned_Results
    """
    base = get_log_file().parent
    folder = base / "Scanned_Results"
    folder.mkdir(parents=True, exist_ok=True)
    return folder

def log(message, log_file=None):
    """Print to console and append to main log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    try:
        log_path = Path(log_file) if log_file else get_log_file()
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception as e:
        print(f"[!] Could not write to log file: {e}")

def log_scan_result(scan_name, message):
    """
    Append a message to a scan-specific file inside Scanned_Results folder.
    - scan_name: file name or URL (invalid chars replaced)
    - Adds timestamp to filename in DD-MM-YYYY_HHMMSS format
    """
    folder = get_scan_results_folder()
    # Sanitize filename
    safe_name = "".join([c if c.isalnum() or c in "_-." else "_" for c in scan_name])
    # Timestamp in DD-MM-YYYY_HHMMSS format
    timestamp_str = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    path = folder / f"{safe_name}_{timestamp_str}.txt"
    
    # Add timestamp to each log entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception as e:
        print(f"[!] Could not write scan result to file: {e}")
