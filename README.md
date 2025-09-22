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

### Installation

After installing both applications above, open `Termux` and follow the steps below -

- Update termux packages and install `git`
```
pkg upgrade && pkg install git
```
- Clone this and enter the repository
```
git clone https://github.com/cyboy18/digital-immune-system.git
cd digital-immune-system
```
- Setup Python environment
```
python -m venv venv
```
