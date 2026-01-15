# startswith()
number = "+92 7523423424"
print(number.startswith("91"))

#in
email = "alphy@gmail.com"
print('@' in email)

# endswith()

file = 'datset.csv'
print(file.endswith(".csv"))

# find()
phone1 = "+48-534-5464"
phone2 = "+123-532-7756"
phone3 = "0034-123-6765"
# imagine we want to extract the phone number without the country code.
# we cant use slicing here since each time the length of country code may vary.
# so we use find() along with slicing to identify the starting position of the number.
print(phone1[4:])
print(phone1[phone1.find("-")+1:])
print(phone2[5:])
print(phone2[phone2.find("-")+1:])

#find() vs index() (classic interview trap)
# index() returns error if the search string is not found
text = "Python Programming"

print(text.find("Pro"))    # 7
print(text.find("Java"))   # -1

#print(text.index("Java")) # ERROR