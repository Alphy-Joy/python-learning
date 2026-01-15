# DATA CLEANING & VALIDATION (1–15)
#-------------------------------------------------------------------------------------------------------------

# 1.    Validate a list of emails and stop processing as soon as an invalid email is found.

emails = ['alphy@gmail.com','info-yahoo.com','help@hotmail+org','report@gmail.com']
#emails = ['alphy@gmail.com','report@gmail.com'] # contains only valid emails
for email in emails:
    if not '@' in email or not '.' in email:
        print(f"invalid email found - {email}")
        break
else:
    print("All emails are valid")

# Print only invalid emails and store them in a list
invalid_emails = []
count = 0
emails = ['alphy@gmail.com','info-yahoo.com','help@hotmail+org','report@gmail.com','test@gmailcom']
for email in emails:
    if not '@' in email or not '.' in email:
        invalid_emails.append(email)
        count +=1
print(f"{count} invalid emails are {invalid_emails}")

#-------------------------------------------------------------------------------------------------------------  

# 2.	Scan customer names and stop the pipeline if any None value is detected.

names = ['alphy','daisy','joy',None,'maria']
for name in names:
    if name is None:
        print("None value detected")
        break

# the index (position) of the None value.
names = ['alphy','daisy','joy',None,'maria']
for index,name in enumerate(names): # enumerate() gives index + value together
    if name is None:
        print(f"None value detected at position {index}")
        break

#-------------------------------------------------------------------------------------------------------------  

# 3.	Skip empty phone numbers but continue loading valid ones.

numbers = ['12345','45645645','','567657']
for number in numbers:
    if number == "":
        continue
    print(f"valid phone numbers are {number}")

# the index (position) of the None value.
empty_positions = []
valid_numbers = []
numbers = ['','12345','45645645','','567657','']
for index,number in enumerate(numbers):
    if number == "":
        empty_positions.append(index)
        continue
    valid_numbers.append(number)
print(f"valid phone numbers are {valid_numbers}")
print(f"empty positions are {empty_positions}")

#-------------------------------------------------------------------------------------------------------------

# 4.	Detect whether a column contains only numeric strings before converting to numbers.

numbers = ['1','2a','3d','5']
#numbers = ['1','2']
for number in numbers:
    if  not number.isdigit():
        print("Contains numeric string")
        break
else:
    print("Numbers are valid")

#-------------------------------------------------------------------------------------------------------------

# 5.	Validate passwords against multiple rules and report all failures, not just the first.
passwords = ['Al12345#', 'Test@1234', '21324', 'sddada', 'dgdf34534', 'sd324@']

for password in passwords:
    print(f"\nChecking password: {password}")
    valid = True

    # Minimum length
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long")
        valid = False

    # Must contain at least one uppercase letter
    if password == password.lower():
        print("❌ Password must contain at least one uppercase letter")
        valid = False

    # Must contain at least one lowercase letter
    if password == password.upper():
        print("❌ Password must contain at least one lowercase letter")
        valid = False

    # Must contain at least one special character (@ or #)
    if not ('@' in password or '#' in password):
        print("❌ Password must contain @ or #")
        valid = False

    # Final result
    if valid:
        print("✅ Password is valid")
# Why use a valid flag?
# To evaluate all rules and give complete feedback instead of stopping early.

#-------------------------------------------------------------------------------------------------------------

# 6.	Check whether all file names in a batch end with .csv; stop on first failure.

files = ['report.csv','file.pdf','draft.doc','data.csv']
for file in files:
    print(f"\nchecking file - {file}")
    valid = True
    if not file.endswith(".csv"):
        print(f"❌ The file is not csv")
        valid = False
    if valid:
        print("✅ The file is csv")
#-------------------------------------------------------------------------------------------------------------

# 7.	Remove leading/trailing spaces from input data and check if anything becomes empty.

data = [' dfs ','dart ','dadad']
cleaned_data = []
for item in data:
    print(f"\nChecking input data {item}")
    cleaned_item = item.strip()
    if cleaned_item == "":
        print(f"❌ Value became empty after cleaning")
    else:
        cleaned_data.append(cleaned_item)
        print(f"✅ Cleaned value added: {cleaned_item}")
print("\nFinal cleaned data:", cleaned_data)

#-------------------------------------------------------------------------------------------------------------

# 8.	Detect duplicate transaction IDs using loops and count().
ids = ['123','34','567','34','12','123']
duplicate_id = []
for id in ids:
    print(f"\nChecking ID - {id}")
    if ids.count(id) > 1 :
        duplicate_id.append(id)
        print(f"❌ Duplicate detected for {id}")
print(f"\nDuplicates - {duplicate_id}")    

# correct version 
ids = ['123','34','567','34','12','123']

duplicate_ids = []
seen = []

for value in ids:
    print(f"\nChecking ID - {value}")

    if value in seen and value not in duplicate_ids:
        duplicate_ids.append(value)
        print(f"❌ Duplicate detected for {value}")
    else:
        seen.append(value)

print(f"\nDuplicates - {duplicate_ids}")

#-------------------------------------------------------------------------------------------------------------

# 9.	Ensure that all country codes are exactly 2 characters long.

codes = ["US", "IND", "CA", "DAA"]

invalid_codes = []

for code in codes:
    if len(code) != 2:
        invalid_codes.append(code)
        print(f"\n❌ Invalid code: {code} (length = {len(code)})")

print(f"\nInvalid codes list: {invalid_codes}")

#-------------------------------------------------------------------------------------------------------------

# 10.	Stop data ingestion if any string exceeds the maximum allowed length.

texts = ['a','abc','efgh']
allowed_len = 12
for text in texts:
    text = text*5
    if len(text) > 12:
        print(f"\nlength of {text} is {len(text)}. exceeded the limit")

# corrected version

texts = ['a', 'abc', 'efgh']
allowed_len = 12

for text in texts:
    expanded_text = text * 5  # do not overwrite original
    if len(expanded_text) > allowed_len:
        print(
            f"❌ Ingestion stopped. "
            f"Value '{expanded_text}' length = {len(expanded_text)} exceeds {allowed_len}"
        )
        break
else:
    print("✅ All records ingested successfully")

#-------------------------------------------------------------------------------------------------------------

# 11.	Validate that a date string follows YYYY-MM-DD format using slicing.

date = '2025-12-12'
if date[4] == '-' and date[7]=='-':
    print("Valid date format")

# correct

date = '2025-12-12'

valid = True

# length check
if len(date) != 10:
    valid = False

# dash position check
elif date[4] != '-' or date[7] != '-':
    valid = False

# digit checks
elif not (date[:4].isdigit() and date[5:7].isdigit() and date[8:].isdigit()):
    valid = False

# month range
elif not (1 <= int(date[5:7]) <= 12):
    valid = False

# day range
elif not (1 <= int(date[8:]) <= 31):
    valid = False

if valid:
    print("✅ Valid date format (YYYY-MM-DD)")
else:
    print("❌ Invalid date format")

#-------------------------------------------------------------------------------------------------------------

# 12.	Check if product codes start with letters and end with digits.

codes = ['a123','2abd','w45','23','45d']
invalid_codes = []
for code in codes:
    # defensive check (important in real pipelines)
    if len(code) == 0:
        invalid_codes.append(code)
        continue
    if not (code[0].isalpha() and code[-1].isdigit()):
        print(f"❌ Invalid product code: {code}")
        invalid_codes.append(code)

print(f"\nFinal invalid codes list: {invalid_codes}")

#-------------------------------------------------------------------------------------------------------------

# 13.	Reject rows where text fields contain SQL injection characters (;, --, DROP).

rows = ["DROP from table","select ;", "select * from table","insert into --"]
injection = []
for row in rows:
    if ';' in row or '--' in row or 'DROP' in row.upper():
        print(f"❌ sql injection detected - {row}")
        injection.append(row)
print(f"\nDetected injections - {injection}")

#-------------------------------------------------------------------------------------------------------------

# 14.	Ensure at least one contact method (email or phone) is provided using any().

email = ""
phone = "654646"
if any([email,phone]):
    print("Atleast one contact method is available")
else:
    print("Both contact methods are unavailable")

#-------------------------------------------------------------------------------------------------------------

# 15.	Ensure all mandatory fields are present using all().

name = "alphy"
email = ""
phone = "2331321"
if not all([name,email,phone]):
    print("Mandatory fields are missing")
else:
    print("All  details are given")


