# combines multiple boolean expressions

# and - returns true only if all  expressions are true

print("a" == "a" and 5>4)
print("password" == "password" and 20!=20)

# or - returns true any of the expression is true
print("password" == "password" or 20!=20)

# not - reverses True / False
print(not False)
print(not not False)
print(not "a" !="A")

name = "" # false by default
print(not name)
print(not 0)

# order of execution - and has higher priority than or
print(5==5 or 8>4 and 6<4) # returns True
# we can use paranthesis () to control the order of execution
print((5==5 or 8>4) and 6<4) # returns false