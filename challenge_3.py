#Username Validation . Case-insensitive comparison is VERY IMPORTANT in real systems

# Must not be empty
# Must be between 5 and 15 characters
# Must not contain spaces
# Must start with a letter
# Must end with a letter or digit
# Must be case-insensitive unique (assume existing username = "AdminUser")
username = "adminUser1"
username = username.strip()
existing_username = "AdminUser"
existing_username = existing_username.strip()
valid = True

# Must not be empty
if  username=="":
    print("Username must not be empty")
    valid = False
# Must be between 5 and 15 characters
if not(len(username)>5 and len(username)<15): # if not (5 <= len(username) <= 15):
    print("Username length should be between 5 and 15 characters")
    valid = False
# Must not contain spaces
if ' ' in username:
    print("Username must not contain spaces")
    valid = False
# Must start with a letter
if not username[0].isalpha():
    print("Username must start with a letter")
    valid = False
# Must end with a letter or digit
if not username[-1].isalnum():
    print("Username must end with a letter or digit")
    valid = False
# Must be case-insensitive unique (assume existing username = "AdminUser")
if  username.lower() == existing_username.lower():
    print("Username already exists")
    valid = False
# if valid = True
if valid:
    print("Username is valid")