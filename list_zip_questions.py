# Actual vs Expected Validation
# Compare expected sales vs actual sales and stop processing when a mismatch is found.

actual_sales = [1111,455,567,911]
excepted_sales = [1111,455,561,911]

for actual,expected in zip(actual_sales,excepted_sales):
    if actual != expected:
        print(f'Mismatch found. Expected {expected} - Actual {actual}')
        break
print('\n----------------------------------------------\n')

# Email + Status Pairing
# You have two lists: emails and validation statuses.
# 👉 Print only the invalid emails.
emails = ['alphy@gmail.com','help@dfdf','localhost']
statuses = ['valid','invalid','invalid']
for email,status in zip(emails,statuses):
    if status == 'invalid':
        print(f'❌Invalid email - {email}')

print('\n----------------------------------------------\n')

# Column Name & Data Type Validation
# Zip column names with inferred data types and flag mismatches against expected schema.
columns = ['id', 'name', 'salary']
types = ['int', 'str', 'str']
expected = ['int', 'str', 'float']

for col, actual, exp in zip(columns, types, expected):
    if actual != exp:
        print(f"❌Data type mismatch in column {col}")
print('\n----------------------------------------------\n')

# Multi-Source Data Merge
# Combine product IDs and prices from two separate systems and generate unified records.

product_ids = [101, 102, 103]
prices = [50, 75, 100]

records = list(zip(product_ids, prices))
print(records)
print('\n----------------------------------------------\n')

# Time-Series Comparison
# Compare revenue across two months (list of days) and detect where values differ.
jan_rev = [100,200,300,400]
feb_rev = [100,200,301,400]
for day,(jan,feb) in enumerate(zip(jan_rev,feb_rev),start=1):
    if jan != feb:
        print(f"Mismatch day is {day}")