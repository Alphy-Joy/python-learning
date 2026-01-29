# 1. Invalid Transaction Detection

# You receive a list of transaction amounts.
# 👉 Find index + value of all transactions ≤ 0.

amounts = [121, -45, 250, -12]
invalid = list(
    filter(lambda x: x[1] <= 0, enumerate(amounts))
)
print(invalid)
print('\n----------------------------------------------\n')
# 2. Failed API Calls Log

# Given a list of HTTP status codes,
# 👉 Identify positions where status ≥ 400.
statuses = [200, 404, 500, 201, 403]
invalid = list(
    filter(lambda x:x[1] >= 400 ,enumerate(statuses)) # here x = (1, 404) - a tuple
    )
print(invalid)
# 3. Normalize Usernames

# Given a list of usernames with whitespace,
# 👉 Strip spaces and convert to lowercase using an iterator.

# 4. Email Validation Report

# You have emails and validation flags.
# 👉 Return only invalid emails with their positions.

# 5. Sales vs Target Comparison

# Given two lists: actual_sales and targets,
# 👉 Find positions where sales < target.

# 6. Dataset Column Quality Check

# Given a list of column values,
# 👉 Identify missing values (None, '', False) with index.

# 7. Detect Out-of-Range Sensor Values

# Given sensor readings,
# 👉 Flag readings not between 10 and 100.

# 8. Time-Series Drop Detection

# Given daily revenue values,
# 👉 Identify days where revenue dropped compared to previous day.

# 9. Standardize Country Codes

# Convert country codes to uppercase and remove invalid ones.

# 10. Log Severity Filter

# From a list of logs,
# 👉 Extract (index, log) where log is 'ERROR' or 'CRITICAL'.

# 11. Deduplicate Cleaned Names

# Trim and lowercase names, then deduplicate using iterators.

# 12. Mismatch Detection (Expected vs Actual)

# Given two lists,
# 👉 Find mismatches with their index.

# 13. Mask Sensitive Data

# Given phone numbers,
# 👉 Mask last 4 digits using map + lambda.

# 14. Reverse Audit Trail Validation

# Traverse records in reverse and return first valid record.

# 15. High-Spending Customers

# Given customer spend list,
# 👉 Return indices where spend > average.

# 16. Validate Age Column

# Detect ages not between 0 and 120 with index.

# 17. Clean Boolean Flags

# Convert mixed truthy/falsy values to strict True/False.

# 18. Data Type Classification

# Classify values as "numeric" or "invalid" using map.

# 19. Extract Non-Alphabetic Fields

# From mixed input fields,
# 👉 Keep only alphabetic values with index.

# 20. Streaming Data Threshold Alert

# Process values lazily and stop at first value exceeding threshold.