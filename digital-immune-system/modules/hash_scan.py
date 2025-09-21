import hashlib
from pathlib import Path
from modules import logger

def sha256_of_file(path):
    """Compute SHA256 hash of a file safely, with debug info."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            chunk_count = 0
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                h.update(chunk)
                chunk_count += 1
                if chunk_count % 1000 == 0:
                    msg = f"[DEBUG] Scanned {chunk_count*8192} bytes..."
                    logger.log(msg)
        return h.hexdigest()
    except PermissionError:
        msg = f"[!] Permission denied: {path}"
        logger.log(msg)
        return None
    except FileNotFoundError:
        msg = f"[!] File not found: {path}"
        logger.log(msg)
        return None
    except Exception as e:
        msg = f"[!] Error reading file {path}: {e}"
        logger.log(msg)
        return None

def run(file_path):
    """Run hash scan and log results in timestamped scan file."""
    path = Path(file_path)
    if not path.exists():
        msg = f"[!] File not found: {file_path}"
        logger.log(msg)
        logger.log_scan_result(path.name, msg)
        return

    msg = f"[DEBUG] Starting hash scan for: {file_path}"
    logger.log(msg)
    logger.log_scan_result(path.name, msg)

    hash_value = sha256_of_file(path)
    if hash_value:
        msg = f"[+] SHA256 hash: {hash_value}"
    else:
        msg = "[!] Hash could not be computed."

    logger.log(msg)
    logger.log_scan_result(path.name, msg)
