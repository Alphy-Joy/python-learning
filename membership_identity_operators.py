
# in , not in - membership operators
print("y" in "Python")
print("f" in "Hello")
print("f" not in "Hello")
print(5 in [3,4,5])

#security check - domain banned or not
domain = "gmail.com"
banned_list = ["fake.com","spam.org","bot.net"]
print(domain in banned_list)
print(domain not in banned_list)

# is, is not - indentity operators
# checks if 2 variables are referring to the same object in the memory
x = [1,2,3]
y = [1,2,3]

print(x==y)
print(x is y) # false bcz python creates separate objects that have separate id's for x and y in memory

a = 10
b = 10
print(a==b)
print(a is b) # true because since the values assigned to the variables are easy,python optimizes and 
#only one object is created in the memory for a and b,so they have same id
print(id(a), id(b))


x = [1,2,3]
y = x

print(x==y)
print(x is y) # assigns one variable to the same object that another variable is referring to

x = [1,2]
y = [1,2]

print(id(x), id(y))