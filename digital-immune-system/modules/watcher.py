import time
from pathlib import Path
from modules import hash_scan, apk_scan, logger

def run(folder_path, interval=5):
    """
    Watch a folder and auto-scan new files.
    
    :param folder_path: Path to folder to monitor
    :param interval: Polling interval in seconds
    """
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        msg = f"[!] Folder not found or not a directory: {folder_path}"
        logger.log(msg)
        return

    logger.log(f"[DEBUG] Starting folder watcher on: {folder_path} (interval: {interval}s)")
    
    # Keep track of existing files
    known_files = set(folder.iterdir())

    try:
        while True:
            time.sleep(interval)
            current_files = set(folder.iterdir())
            new_files = current_files - known_files

            for f in new_files:
                if f.is_file():
                    msg = f"[DEBUG] New file detected: {f.name}"
                    logger.log(msg)
                    logger.log_scan_result(f.name, msg)

                    # Auto scan: choose module based on extension
                    if f.suffix.lower() == ".apk":
                        apk_scan.run(f)
                    else:
                        hash_scan.run(f)

            # Update known files
            known_files = current_files

    except KeyboardInterrupt:
        logger.log("[+] Folder watcher stopped by user.")
