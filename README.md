<div align="center">
<video src="https://github.com/user-attachments/assets/925ca379-74ab-4d81-b72f-dcd6949e754f" controls width="100%" 
  style="max-width: 750px; border-radius: 6px;"></video>
 <p><strong>Project Demonstration video</strong></p></div>

# Simple Python Log Analyzer

An automated, lightweight Python script designed to parse system authorization logs (`auth.log`) to identify and count failed login attempts. This tool helps security analysts automate log reviews and spot potential brute-force activities.

## Features
- **Efficient File Handling:** Reads files line-by-line using `with open()` to maintain low memory usage on large log datasets.
- **Real-Time Alerting:** Prints a terminal warning immediately whenever a failed login string is identified.
- **Log Summarization:** Outputs a clear numerical summary tracking the total count of security anomalies.

## How It Works
The script searches text streams for a specific security string modifier (`"FAILED"`). When located, it increments a local variable counter and extracts the problematic entry to the console.

### Sample Terminal Output
```text
Starting Log Analysis for Security Anomaly Detection...
--------------------------------------------------
[ALERT] Security Incident Identified: 2   2026-05-29 08:02:15 WARN  root   FAILED  Failed login attempt        203.0.113.5
[ALERT] Security Incident Identified: 4   2026-05-29 08:04:10 WARN  admin  FAILED  Failed login attempt        198.51.100.42
[ALERT] Security Incident Identified: 5   2026-05-29 08:05:01 WARN  root   FAILED  Failed login attempt        203.0.113.5
--------------------------------------------------
Total Failed Login Attempts Blocked: 3
--------------------------------------------------
```

##  Requirements
- Python 3.x
