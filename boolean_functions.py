print(True)
print(False)
print(type(True))
print(bool("1"))
print(bool("Hello"))
print(bool(45))
print(bool())
print(bool(""))
print(bool(" "))
print(bool(0))
print(bool(None))

# False values - False, 0, 0.0, "", [], {}, None

# any - returns true if at least one value is given

# eg : user resigtration

email = ""
phone = "123 45646"
password = "abc123"

print(any([email,phone,password]))

# all - returns true only if all values are given
print(all([email,phone,password]))

# isinstance()
print(isinstance("True",bool))
print(isinstance(True,bool))
print(isinstance("True",str))

# endswith() , startswith()
print("Hello".endswith("o"))
print("Hello".startswith("o"))