# Digital Immune System 🛡️

A cross-platform security prototype designed to scan files, APKs, and URLs for malicious or suspicious content.  
It computes SHA256 hashes, analyzes APK permissions, detects phishing URLs, and manages quarantined files.  
The system is modular, lightweight, and works on **Windows, Linux, and Android (Termux)**.

---

## 📑 Table of Contents
- [Description](#description)
- [Features](#features)
- [Supported Platforms](#supported-platforms)
- [Getting Started](#getting-started)
  - [Dependencies](#dependencies)
  - [Installing](#installing)
  - [Setup Environment](#setup-environment)
  - [Install Dependencies](#install-dependencies)
  - [Executing Program](#executing-program)
- [Logging & Results](#logging--results)
- [Contribution](#contribution)
- [Disclaimer](#disclaimer)
- [Donate ❤️](#donate-️)

---

## Description

The **Digital Immune System (DIS)** helps protect against malware by:  
- Scanning files and APKs for threats  
- Detecting phishing URLs  
- Managing quarantined files securely  

All scans are logged with timestamps for auditing and research.

---

## Features

| Feature                     | Status         |
|------------------------------|----------------|
| File hash scanning           | ✅ Implemented |
| APK permission analysis      | ✅ Implemented |
| URL phishing detection       | ✅ Implemented |
| Folder auto-watcher          | ⏳ In Progress |
| Quarantine & restore system  | ✅ Implemented |

---

## Supported Platforms

- ✅ Windows  
- ✅ Linux  
- ✅ Android (Termux)

---

## Getting Started

### Dependencies

* Python 3.11 or higher  
* Windows 10 / Linux / Android (Termux)  
* Required libraries (see `requirements.txt`)

---

### Installing


### Clone Repository

```bash
git clone https://github.com/cyboy18/digital-immune-system.git

cd digital-immune-system



# Setup Python environment and Create a virtual environment

python -m venv venv

# Activate the environment

# 1. Linux / Mac

source venv/bin/activate

# 2. Windows (PowerShell)

venv\Scripts\activate


# Install dependencies

pip install -r requirements.txt


# Executing Program

# 1. File Hash Scan

python disimmune.py scan-hash <file_path>

# 2. APK Permission Scan

python disimmune.py scan-apk <apk_path>

# 3. URL Phishing Check

python disimmune.py check-url <url>

# 4. Folder Watcher

python disimmune.py watch <folder_path> --interval 5

# 5. Quarantine Management

python disimmune.py quarantine-list
python disimmune.py quarantine-restore <filename> --restore-dir <path>


# Logging & Results



# All scan results are saved in:

DigitalImmuneLogs/Scanned_Results

# Example result filename:

Wireshark_exe_21-09-2025_214500.txt
