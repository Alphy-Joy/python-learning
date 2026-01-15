# Email must not be empty
# Email must contain a . one @
# Email must contain exactly one @
# Email must end with .com or .org or .net
# Email must not be longer than 254 characters
# Email must start and end with a letter or digit

email = "--gjgj@fgh.com"


# clean the whitespace before continuing
email = email.strip()
# Email must not be empty
if email == "":
    print("Email cannot be empty")
# Email must contain a . one @
elif not ('.' in email and '@' in email):
    print("Email has . and @")
# Email must contain exactly one @
elif email.count('@') !=1:
    print("Email has more than one @")
# Email must end with .com or .org or .net
elif not email.endswith(('.com','.org','.net')):
    print("Email ends with .com or .org or .net")
# Email must not be longer than 254 characters
elif len(email)>254:
    print("Email must not be longer than 254 characters")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid")

#-----------------------------------------------------------------
email = "gjgj@fgh.com"
valid = True

# clean the whitespace before continuing
email = email.strip()
# Email must not be empty
if email == "":
    print("Email cannot be empty")
    valid = False
# Email must contain a . one @
if not ('.' in email and '@' in email):
    print("Email has . and @")
    valid = False
# Email must contain exactly one @
if email.count('@') !=1:
    print("Email has more than one @")
    valid = False
# Email must end with .com or .org or .net
if not email.endswith(('.com','.org','.net')):
    print("Email ends with .com or .org or .net")
    valid = False
# Email must not be longer than 254 characters
if len(email)>254:
    print("Email must not be longer than 254 characters")
    valid = False
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False
if valid :
    print("Email is valid")
