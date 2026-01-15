# Password Quality Check
    # Must not be empty
    # Must be atleast 8 characters long
    # Must include atleast one uppercase
    # Must include atleast one lowercase
    # Must not be same as email
    # Must not contain any spaces
    # Must start and end with a letter or digit

password = "12311A4567n"
#password = password.strip()
email = "123A4567n"
email = email.strip()
valid = True

# Must not be empty
if password == "":
    print("Password must not be empty")
    valid = False
# Must be atleast 8 characters long
if len(password)<8:
    print("Password must be atleast 8 characters long")
    valid = False
# Must include atleast one uppercase
if password == password.lower():
    print("Password must include at least one uppercase")
    valid = False
 # Must include atleast one lowercase 
if password == password.upper():
    print("Password must include at least one lowercase")
    valid = False
# Must not be same as email
if  password == email:
    print("Password must not be same as email")
    valid = False
# Must not contain any spaces
if ' ' in password: # because strip only removes spaces from both ends
    print("Password must not contain any spaces")
    valid = False
# Must start and end with a letter or digit
if password[0].isalnum() and password[-1].isalnum():
    print("Password must start and end with a letter or digit")
    valid = False
if valid:
    print("Password is valid")
