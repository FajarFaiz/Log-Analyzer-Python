# File: log_analyzer.py
log_file_path = "auth.log"
failed_attempts = 0

print("Starting Log Analysis for Security Anomaly Detection...")
print("-" * 50)

with open(log_file_path, "r") as file:
    for line in file:
        # look for lines containing the "failed" status signature
        if "FAILED"in line:
         failed_attempts += 1
         print(f"[ALERT] Security Incident Identified: {line.strip()}")
print("-" * 50)
print(f"Total Failed Login Attempts Blocked: {failed_attempts}")
print("-" * 50)
