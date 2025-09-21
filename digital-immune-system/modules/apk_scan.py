from modules import logger

# Try to import Androguard
try:
    from androguard.core.bytecodes.apk import APK
except ImportError:
    APK = None

def run(apk_path):
    """Scan APK permissions and log results to timestamped scan file."""
    if APK is None:
        msg = "[!] Androguard not installed. Install via: pip install androguard"
        logger.log(msg)
        logger.log_scan_result(apk_path, msg)
        return

    try:
        app = APK(apk_path)
        perms = app.get_permissions()

        if perms:
            msg = f"[+] Permissions found in APK: {apk_path}"
            logger.log(msg)
            logger.log_scan_result(apk_path, msg)
            for p in perms:
                perm_msg = f"    - {p}"
                logger.log(perm_msg)
                logger.log_scan_result(apk_path, perm_msg)
        else:
            msg = f"[+] No permissions found in APK: {apk_path}"
            logger.log(msg)
            logger.log_scan_result(apk_path, msg)

    except Exception as e:
        msg = f"[!] Failed to parse APK {apk_path}: {e}"
        logger.log(msg)
        logger.log_scan_result(apk_path, msg)
