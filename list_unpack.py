employee = ['Alphy',35,'Data Analyst','Kerala']
#print(employee[0])
#print(employee[1])
#print(employee[2])
#print(employee[3])

name,age,role,place = employee # unpacking . the order should be same as in the list

print(name)
print(role)

# Rest Collector (*) - when we need only few details and ignore all the other unnecessary details 
# (*) stores the rest of the values in a list
name,*details,place = employee
print(name)
print(details)
print(place)

# if you need only the first value
name,*details = employee
print(name)
print(details)
# * collects the left overs. its fine if there are none
numbers = [1]
num,*details = numbers
print(details)
# Rules for unpacking
# No.of variables should match the no.of values - not less,not more
# you can unpack any sequences (list,tuple,string etc)

word = "Hi"
letter, *rest = word
print(letter)
print(rest)

# underscore (_) - skips items
employee = ['Alphy',35,'Data Analyst','Kerala']
name,_,_,place = employee
print(name)

employee = ['Alphy',35,'Data Analyst','Kerala']
*_,place = employee
print(place)