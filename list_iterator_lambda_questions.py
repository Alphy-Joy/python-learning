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
    filter(lambda x:x[1] >= 400 ,enumerate(statuses)) # here x = (1, 404) - a tuple,x[0] = 1,2,3,4,5 and x[1] = 404,500,403 etc for each iteration
    )
print(invalid)
print('\n----------------------------------------------\n')

# 3. Normalize Usernames

# Given a list of usernames with whitespace,
# 👉 Strip spaces and convert to lowercase using an iterator.
usernames = [' User1 ','USER2 ','user']
valid_username = list(map(lambda x : x.lower().strip(),usernames))
print(valid_username)
print('\n----------------------------------------------\n')

# 4. Email Validation Report

# You have emails and validation flags.
# 👉 Return only invalid emails with their positions.
emails = ['alphy@gmail.com','test.com','localhost']
flags = ['valid','invalid','invalid']
invalid_emails = list(filter(lambda x:x[1][1] == 'invalid', enumerate(zip(emails,flags))))
print(invalid_emails)
print('\n----------------------------------------------\n')
# 5. Sales vs Target Comparison

# Given two lists: actual_sales and targets,
# 👉 Find positions where sales < target.
actual_sales = [555,101,300,610]
target = [400,110,350,280]
sales_diff =list(filter(lambda x:x[1][0]<x[1][1],enumerate(zip(actual_sales,target)))) #x[0] → index , x[1][0] → actual sales , x[1][1] → target
# zip(actual_sales, target)
# # → (555,400), (101,110), (300,350), (610,280)
# enumerate(zip(...))
# # → (0,(555,400)), (1,(101,110)), ...
print(sales_diff)
print('\n----------------------------------------------\n')

# 6. Dataset Column Quality Check

# Given a list of column values,
# 👉 Identify missing values (None, '', False) with index.
columns = ['name','dob',None,'phone','',False]
# missing_value = list(filter(lambda x:x[1] is None or x[1]==''or x[1] is False,enumerate(columns)))
missing_value = list(
    filter(lambda x: not x[1], enumerate(columns))
)
print(missing_value)
print('\n----------------------------------------------\n')

# 7. Detect Out-of-Range Sensor Values
# Given sensor readings,
# 👉 Flag readings not between 10 and 100.
readings = [23,45,8,78,2]
invalid_readings = list(filter(lambda x:not (10 <= x <= 100),readings))
print(invalid_readings)
print('\n----------------------------------------------\n')


# 8. Time-Series Drop Detection

# Given daily revenue values,
# 👉 Identify days where revenue dropped compared to previous day.
revenue = [1200, 1250, 1180, 1180, 1300, 1270]

drops = list(
    filter(
        lambda x: x[1][1] < x[1][0],
        enumerate(zip(revenue, revenue[1:]), start=1)
    )
)
print(drops)
print('\n----------------------------------------------\n')


# 9. Standardize Country Codes

# Convert country codes to uppercase and remove invalid ones.
codes = ['in','c123','ca','usa','uk']
cleaned_code = list(filter(lambda x: x.isalpha() and len(x) == 2, map(lambda x : x.upper(),codes)))
print(cleaned_code)
print('\n----------------------------------------------\n')

# 10. Log Severity Filter

# From a list of logs,
# 👉 Extract (index, log) where log is 'ERROR' or 'CRITICAL'.
logs = ['WARNING','OK','ERROR','TEST','CRITICAL']
filtered_logs = list(filter(lambda x : x[1] in ('ERROR', 'CRITICAL'), enumerate(logs)))
print(filtered_logs)
print('\n----------------------------------------------\n')

# 11. Deduplicate Cleaned Names

# Trim and lowercase names, then deduplicate using iterators.
usernames = [' Alphy ','JOY ','user','JOY ']
valid_username = list(map(lambda x : x.lower().strip(),usernames))
seen =[]
for name in valid_username:
    if name in seen:
        print(f"Duplicate found - {name}")
    else:
        seen.append(name)
print(seen)
print('\n----------------------------------------------\n')

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