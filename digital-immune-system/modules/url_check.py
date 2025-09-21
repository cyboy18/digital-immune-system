import re
from modules import logger

def heuristic(url: str):
    findings = []
    if not url.lower().startswith("https://"):
        findings.append("Not HTTPS")
    if len(url) > 120:
        findings.append("Very long URL")
    if re.search(r"(login|verify|account|update|secure)", url, re.I):
        findings.append("Suspicious keyword")
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        findings.append("IP address in URL")
    if "xn--" in url:
        findings.append("Punycode domain")
    return findings

def run(url):
    """Run URL phishing check and log results in timestamped scan file."""
    # Log start of URL scan
    msg = f"[DEBUG] Starting URL check for: {url}"
    logger.log(msg)
    logger.log_scan_result(url, msg)

    # Run heuristics
    issues = heuristic(url)

    if issues:
        msg = "[!] Potential phishing indicators detected:"
        logger.log(msg)
        logger.log_scan_result(url, msg)
        for i in issues:
            issue_msg = f"    - {i}"
            logger.log(issue_msg)
            logger.log_scan_result(url, issue_msg)
    else:
        msg = "[+] URL looks clean (no obvious signs)"
        logger.log(msg)
        logger.log_scan_result(url, msg)
