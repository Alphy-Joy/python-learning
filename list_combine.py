# combining
letters = ['a','b','c']
numbers = [1,2,3]
comb = letters + numbers # here we are combining 2 lists and making a new list
print(comb)

print(letters * 3) # multiply operator

comb = [letters,numbers]
print(comb)
# extend()
# it extends an existing list by adding a new list to it instead of creating a new list
letters = ['a','b','c']
numbers = [1,2,3]
numbers.extend(letters)
print(numbers)
print(letters)

# zip()
# zip() combines multiple iterables element-by-element into pairs (or tuples).
# zip() returns an iterator, not a list
# very important - zip() stops at the shortest iterable
letters = ['a','b','c']
numbers = [1,2,3,4]
comb = list(zip(letters,numbers)) 
print(comb)
comb = list(zip(letters,numbers,'Hi'))
print(comb)