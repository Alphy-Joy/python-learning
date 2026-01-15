
# LOG PARSING & MONITORING (16–30)

# 16.	Scan log messages and trigger an alert if "error" appears (case-insensitive).

logs = ['Scanning..','Processing..','error..in copying']
for log in logs:
    if 'error' in log.lower():
        print("Alert!! Error detected")
        break
else:
    print("All logs are valid")

#-------------------------------------------------------------------------------------------------------------

# 17.	Count how many "warning" messages appear in logs.

logs = ['success','warning - process aborted','warning..error detected','warning : correction required','completed']
warning_count = 0
for log in logs:
    if 'warning' in log.lower():
        warning_count += 1
print(f"Total warnings - {warning_count}")

#-------------------------------------------------------------------------------------------------------------

# 18.	Stop processing logs when a "CRITICAL" message appears.

logs = ['Scanning..','Processing..','critical..in copying','warning']
for log in logs:
    print(f"\nScanning log - {log}")
    if 'critical' in log.lower():
        print("❌ Alert!! Critical Error detected")
        break
    else:
        print("✅ passed")
else:
    print("All logs are valid")

#-------------------------------------------------------------------------------------------------------------

# 19.	Skip empty or corrupted log entries and continue processing valid logs.

logs = ['Scanning..','Processing..','corrupted..failed copying','warning','']

corrupted_found = False

for log in logs:
    print(f"\nScanning log - {log}")

    # clean the log entry
    log = log.strip()

    if log == "" or 'corrupted' in log.lower():
        print("❌ Alert!! corrupted or empty log detected")
        corrupted_found = True
        continue

    print("✅ Passed")

if not corrupted_found:
    print("\n✅ All logs are valid")
else:
    print("\n⚠️ Some logs were skipped due to corruption")


#-------------------------------------------------------------------------------------------------------------

# 20.	Extract log level (INFO, ERROR, WARNING) from log strings.

logs = ['INFO : scanning','WARNING : package expired','ERROR : disk full']
log_level = []
for log in logs:
    message = log.split(":")[0].strip()
    log_level.append(message)

print(f"Extracted levels : {log_level}")

#-------------------------------------------------------------------------------------------------------------

# 21.	Detect whether logs are ordered by timestamp using string comparison.

logs = ["2025-01-01", "2025-01-02"]

if logs == sorted(logs):
    print("Logs ordered")

#-------------------------------------------------------------------------------------------------------------

# 22.	Validate that every log entry contains a colon (:).

logs = ['INFO : scanning','WARNING : package expired','ERROR  disk full']
log_level = []
for log in logs:
    print(f"\nScanning log - {log}")
    if not ':' in log:
        print(f"❌ : is missing")
    else:
        print("✅valid")

#-------------------------------------------------------------------------------------------------------------

# 23.	Identify the first failed job in a batch log and stop further checks.

logs = ['Scanning..','Processing..','failed..in copying','warning']
for log in logs:
    print(f"\nScanning log - {log}")
    if 'failed' in log.lower():
        print("❌ Alert!! failed Error detected")
        break
    else:
        print("✅ passed")
else:
    print("All logs are valid")

#-------------------------------------------------------------------------------------------------------------

# 24.	Check whether logs belong only to allowed environments (DEV, QA, PROD).

env = 'dev'
allowed_env = ['dev','prod','qa']
if env in allowed_env:
    print("ENV allowed")
else:
    print("ENV not allowed")

#-------------------------------------------------------------------------------------------------------------

# 25.	Count daily errors from log file names using range().

logs = [
    "app_log_day1_error3.txt",
    "app_log_day2_error0.txt",
    "app_log_day3_error5.txt",
    "app_log_day4_error2.txt"
]
daily_errors = {}

for i in range(len(logs)):
    log = logs[i]

    # Extract day number
    day_part = log.split("_")[2]        # 'day1'
    day = int(day_part.replace("day", ""))

    # Extract error count
    error_part = log.split("_")[3]      # 'error3.txt'
    error_count = int(error_part.replace("error", "").replace(".txt", ""))

    daily_errors[day] = error_count

print(daily_errors)

#-------------------------------------------------------------------------------------------------------------

# 26.	Detect repeated error messages in logs.

messages = ['warning','error','failed','warning','critical','failed','failed','failed','failed']
seen = []
repeated = []
for message in messages:
    if message in seen and message not in repeated:
        repeated.append(message)
        print(f"❌ Repeated values detected for {message}")
    else:
        seen.append(message)
print(f"\nRepeated - {repeated}")

# another version
messages = ['warning','error','failed','warning','critical','failed','failed','failed','failed']

frequency = {}

for message in messages:
    if message in frequency:
        frequency[message] += 1
    else:
        frequency[message] = 1

print("\nMessage counts:", frequency)

#-------------------------------------------------------------------------------------------------------------

# 27.	Verify that all log file names follow the same naming convention.

files = ["log_2025_01.txt","log_2025_02.txt","daily_log_2025_02.txt"]

for file in files:
    print(f"Scanning file names --- {file}")
    if file.startswith("log_") and file.endswith(".txt"):
        print("Valid name")
    else:
        print(f"Invalid log name - {file}")

#-------------------------------------------------------------------------------------------------------------

# 28.	Stop monitoring when a security breach keyword is detected.

logs = ['Scanning..','Processing..','error..in copying','unauthorised access']
for log in logs:
    if 'unauthorised' in log.lower():
        print("\nAlert!! unauthorised access detected")
        break
else:
    print("All logs are valid")

#-------------------------------------------------------------------------------------------------------------

# 29.	Skip informational logs and process only errors and warnings.

logs = ['INFO : scanning','WARNING : package expired','ERROR  disk full']
log_level = []
for log in logs:
    print(f"\nScanning log - {log}")
    if log.startswith('INFO'):
        print('skipped')
        continue       
    else:
        print(f"{log}")

#-------------------------------------------------------------------------------------------------------------

# 30.	Ensure that each log entry starts with a valid timestamp format.

log = "2025-12-22 ERROR"

if log[4] == "-" and log[7] == "-":
    print("Valid timestamp")
