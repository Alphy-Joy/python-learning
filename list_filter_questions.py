# Remove Corrupted Records
# Filter out rows where mandatory fields are empty or None.

records = ['data', None, '', 'valid']
clean = list(filter(None, records))
print(clean)
print('\n----------------------------------------------\n')

# Valid Email Extraction
# Keep only records containing valid email addresses.

emails = ['a@gmail.com', 'b.com']
valid = list(filter(lambda e: '@' in e, emails))
print(valid)
print('\n----------------------------------------------\n')

# Threshold-Based Filtering
# Retain only transactions above a minimum value.
values = [233,678,768,989]
print(list(filter(lambda v : v>500,values)))
print('\n----------------------------------------------\n')

# Anomaly Detection
# Filter out negative or unrealistic measurements.
measurements = [10, -5, 30]
valid = list(filter(lambda x: x >= 0, measurements))
print(valid)
print('\n----------------------------------------------\n')
# Log Severity Filtering
# Extract only ERROR or CRITICAL logs from a large log stream.
logs = ['INFO', 'ERROR', 'WARN', 'ERROR']
errors = list(filter(lambda x: x == 'ERROR', logs))
print(errors)