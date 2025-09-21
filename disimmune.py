#!/usr/bin/env python3
"""
Digital Immune System (Full Prototype Skeleton with Logging)
"""

import argparse
from modules import hash_scan, apk_scan, url_check, watcher, quarantine

# Global output file
OUTPUT_FILE = "scan_results.txt"

def log_print(msg):
    """Print to console and append to output file."""
    print(msg)
    try:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception as e:
        print(f"[!] Could not write to {OUTPUT_FILE}: {e}")

def main():
    parser = argparse.ArgumentParser(
        prog="disimmune",
        description="Digital Immune System Prototype with Quarantine and Logging"
    )
    sub = parser.add_subparsers(dest="cmd")

    # --- File hash scan ---
    a = sub.add_parser("scan-hash", help="Compute SHA256 hash of a file")
    a.add_argument("file", help="File path to scan")
    a.add_argument("--quarantine", action="store_true", help="Move file to quarantine after scan")

    # --- APK permission scan ---
    b = sub.add_parser("scan-apk", help="Scan APK file permissions")
    b.add_argument("apk", help="APK file path")

    # --- URL phishing check ---
    c = sub.add_parser("check-url", help="Check URL for phishing heuristics")
    c.add_argument("url", help="URL to check")

    # --- Folder watcher ---
    d = sub.add_parser("watch", help="Watch a folder and auto-scan new files")
    d.add_argument("folder", help="Folder path")
    d.add_argument("--interval", type=int, default=5, help="Polling interval in seconds")

    # --- Quarantine management ---
    q_list = sub.add_parser("quarantine-list", help="List quarantined files")
    q_restore = sub.add_parser("quarantine-restore", help="Restore a quarantined file")
    q_restore.add_argument("filename", help="Name of the quarantined file")
    q_restore.add_argument("--restore-dir", default=".", help="Directory to restore the file to")

    args = parser.parse_args()

    if args.cmd == "scan-hash":
        hash_scan.run(args.file)  # logger handles scan result file
        if args.quarantine:
            quarantine.move_to_quarantine(args.file)

    elif args.cmd == "scan-apk":
        apk_scan.run(args.apk)

    elif args.cmd == "check-url":
        url_check.run(args.url)

    elif args.cmd == "watch":
        watcher.run(args.folder, args.interval)

    elif args.cmd == "quarantine-list":
        quarantine.list_quarantine()

    elif args.cmd == "quarantine-restore":
        quarantine.restore_file(args.filename, args.restore_dir)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
