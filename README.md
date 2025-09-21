Digital Immune System 🛡️

Description:
The Digital Immune System (DIS) is a cross-platform security prototype designed to scan files, APKs, and URLs for malicious or suspicious content. It computes SHA256 hashes, analyzes APK permissions, detects phishing URLs, and manages quarantined files. The system is modular, lightweight, and works on Windows, Linux, and Android (Termux).

Features
Feature	Status
File hash scanning	✅ Implemented
APK permission analysis	✅ Implemented
URL phishing detection	✅ Implemented
Folder auto-watcher	⏳ In Progress
Quarantine & restore management	✅ Implemented
Supported Platforms (Tested)

Windows ✅

Linux ✅

Android/Termux ✅

Installation
Step 1: Clone the repository
git clone https://github.com/cyboy18/digital-immune-system.git
cd digital-immune-system

Step 2: Setup Python environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Step 3: Install dependencies
pip install -r requirements.txt

Usage
File Hash Scan
python disimmune.py scan-hash <file_path>

APK Permission Scan
python disimmune.py scan-apk <apk_path>

URL Phishing Check
python disimmune.py check-url <url>

Folder Watcher
python disimmune.py watch <folder_path> --interval 5

Quarantine Management
python disimmune.py quarantine-list
python disimmune.py quarantine-restore <filename> --restore-dir <path>

Logging & Results

All scans are logged with timestamps.

Individual scan results are saved in DigitalImmuneLogs/Scanned_Results with filenames like:

Wireshark_exe_21-09-2025_214500.txt


This allows easy review and auditing of past scans.

Contribution

We welcome contributions!

Find a bug? Open an Issue.

Have a new idea? Submit a Pull Request.

Disclaimer

The developer is not responsible for misuse. Use this tool only for educational purposes or authorized security testing. By using this code, you agree to all terms of responsible use and local laws.

Donate ❤️

If this project helps you, consider supporting development.
Any contribution is appreciated to improve and maintain the project.
