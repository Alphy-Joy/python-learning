# challenge
# clean text = "968-Maria,  ( D@t@ Engineer ) ;;  27y " to name: maria | role: data engineer | age: 27

text = "968-Maria,  ( D@t@ Engineer ) ;;  27y "

# extract name
name = text[4:9].lower()

# extract role
#role = text.split("(")
#role = text.split("(")[1]
role = text.split("(")[1].split(")")[0]
role = role.replace("@", "a").strip().lower()
print(role)

age = text.split(";;")
print(age)