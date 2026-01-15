# Date Format Validator (Analytics Use Case) Use case: validating CSV date columns before loading to database.

# Input format must be YYYY-MM-DD
# Length must be exactly 10
# Must contain exactly 2 hyphens
# Year must be 4 characters
# Month and day must be 2 characters
# Must not contain spaces

date = "2025-122-229"
valid = True

year = date[0:4]
month = date[5:7]
day = date[8:10]
print(len(month))
# Length must be exactly 10
if not len(date) == 10:
    print("Length must be exactly 10")
    valid = False
# Must contain exactly 2 hyphens
if not date.count("-") == 2:
    print("Must contain exactly 2 hyphens")
    valid = False
# Must not contain spaces
if ' ' in date:
    print("Must not contain spaces")
    valid = False
# Year must be 4 characters
if not len(year) == 4:
    print("Year must be 4 characters")
    valid = False
# Month and day must be 2 characters
if not (len(month) == 2 and len(day) == 2):
    print("Month and day must be 2 characters")
    valid = False
if valid:
    print("Date format is valid")