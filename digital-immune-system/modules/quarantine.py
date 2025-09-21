from pathlib import Path
import shutil
from datetime import datetime
from modules import logger

def get_quarantine_folder():
    """
    Returns the folder path for quarantined files:
    DigitalImmuneLogs/Quarantine
    """
    base = logger.get_log_file().parent
    folder = base / "Quarantine"
    folder.mkdir(parents=True, exist_ok=True)
    return folder

def move_to_quarantine(file_path):
    """Move a suspicious file to quarantine folder with timestamp."""
    path = Path(file_path)
    if not path.exists():
        msg = f"[!] File not found: {file_path}"
        logger.log(msg)
        logger.log_scan_result(path.name, msg)
        return

    timestamp = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    safe_name = "".join([c if c.isalnum() or c in "_-." else "_" for c in path.name])
    quarantine_file = get_quarantine_folder() / f"{safe_name}_{timestamp}{path.suffix}"

    try:
        shutil.move(str(path), quarantine_file)
        msg = f"[+] File moved to quarantine: {quarantine_file}"
        logger.log(msg)
        logger.log_scan_result(path.name, msg)
    except Exception as e:
        msg = f"[!] Could not move file to quarantine: {e}"
        logger.log(msg)
        logger.log_scan_result(path.name, msg)

def list_quarantine():
    """List all files in quarantine folder."""
    folder = get_quarantine_folder()
    files = list(folder.iterdir())
    if files:
        logger.log("[+] Quarantined files:")
        for f in files:
            logger.log(f"    - {f.name}")
    else:
        logger.log("[+] Quarantine is empty.")

def restore_file(filename, restore_dir="."):
    """Restore a file from quarantine back to a directory."""
    folder = get_quarantine_folder()
    file_to_restore = folder / filename
    if not file_to_restore.exists():
        msg = f"[!] File not found in quarantine: {filename}"
        logger.log(msg)
        return

    restore_path = Path(restore_dir) / filename
    try:
        shutil.move(str(file_to_restore), restore_path)
        msg = f"[+] File restored to: {restore_path}"
        logger.log(msg)
    except Exception as e:
        msg = f"[!] Could not restore file: {e}"
        logger.log(msg)
