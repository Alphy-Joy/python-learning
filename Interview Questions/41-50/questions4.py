# BOOLEAN LOGIC & CONDITIONS (41–50)
#---------------------------------------------------------------------------------------------------
from datetime import date,datetime
# 41.	Decide whether a user is eligible based on multiple conditions (age, country, status).
age = 20
country = 'IN'
status = 'active'

is_adult = age>=18
is_allowed = country in ['IN','USA']
is_active = status == 'active'

if is_adult and is_allowed and is_active:
    print("✅ User is eligible")
else:
    print("❌ User is not eligible")
#---------------------------------------------------------------------------------------------------

# 42.	Check whether input values are truthy or falsy before processing.
user_input = ""
if user_input:
    print("✅Valid input")
else:
    print("❌Invalid input")
#---------------------------------------------------------------------------------------------------

# 43.	Reject records where both email and phone are missing.
email = ""
phone = ""
if email and phone:
    print("✅Valid")
else:
    print("❌Invalid")
#---------------------------------------------------------------------------------------------------

# 44.	Allow access only if role is "admin" and status is "active".
role = 'admin'
status = 'active'
if role == 'admin' and status == 'active':
    print("✅ Access allowed")
else:
    print("❌ Access denied")
#---------------------------------------------------------------------------------------------------

# 45.	Block access if role is "guest" or account is "suspended".
role = 'admin'
status = 'active'
if role == 'admin' and status == 'active':
    print("✅ Access allowed")
else:
    print("❌ Access denied")

# proffessional way

is_admin = role == 'admin'
is_active = status == 'active'

if is_admin and is_active:
    print(f"✅ Access allowed for {role}")
else:
    print("❌ Access denied")
#---------------------------------------------------------------------------------------------------

# 46.	Detect logically impossible values (negative age, future dates).
age = -12
future_date = '2026-01-14'
future_date = datetime.strptime(future_date, "%Y-%m-%d").date()# Dates must be compared as date objects, not string
today = date.today()

valid = True
if age <0:
    print("❌ invalid age")
    valid = False
if future_date > today: # Dates must be compared as date objects, not string
    print("❌ invalid date")
    valid = False
if valid:
    print("✅ Age and date are valid")

#---------------------------------------------------------------------------------------------------

# 47.	Ensure numeric values fall within a valid range using chained comparisons.
salary = 55000
# if salary >= 30000 and salary <= 200000: # Unprofessional Way
if 30000 <= salary <= 200000:
    print("✅ Salary accepted")
else:
    print("❌ Salary out of range")

#---------------------------------------------------------------------------------------------------

# 48.	Validate whether a string belongs to an approved whitelist.
whitelist = ['approved','pending','warning','failed','completed']
string = 'testing'
if string in whitelist:
    print(f"✅ The string '{string}' is whitelisted")
else:
    print(f"❌ The string {string} is not whitelisted")
#---------------------------------------------------------------------------------------------------

# 49.	Check object identity vs equality when comparing cached values.
x = 100
y = 100

print(x == y)   # True
print(x is y)   # True  ✅ same cached object

x = 1000
y = 1000

print(x == y)   # True
print(x is y)   # False ❌ different objects

expected_count = 10
actual_count = 10

# Value comparison (correct)
if actual_count == expected_count:
    print("✅ Counts match")

# Identity comparison (wrong)
if actual_count is expected_count:
    print("❌ Do NOT use is for numbers")

# == compares values, is compares memory identity. Cached objects can make is misleading.
#---------------------------------------------------------------------------------------------------

# 50.	Decide whether a data pipeline passed or failed using for–else
steps = ['ok','ok','failed','ok']
for step in steps:
    if step == 'failed':
        print("❌ Pipeline failed")
        break
else:
    print("✅ Pipeline executed successfully")