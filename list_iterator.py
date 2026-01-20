# iterator 
# for containers like  like list,tuple ,set, string etc python creates objects for each in memory
# if the containers carry huge data it will consume huge memory
# in most of the cases we dont need the enitre data, we only need subsets or few data
# where as iterators Generates values only when needed. it wont store everything in memory
# An iterator is an object that returns elements one at a time using next() and raises StopIteration when exhausted.
# iterators are used to loop through data, saves memory and increase speed and flexibility
# An iterator: - Produces values one at a time - Uses next() - Gets exhausted
# eg - range(), zip(), map(), filter()



# Iterable
# An iterable is something you can loop over.
# eg - list, tuple, string, set, dict, range

letters = ['a','b','c'] # iterables
#num = 123133 # not iterable . its an integer
for l in letters:
    print(l)

print('\n----------------------------------------------\n')
letters = ['a','b','c'] # iterables
new_list = []
for l in letters:
    new_list.append(l.upper())
print(new_list)    
print('\n---------------------ENUMERATE()-------------------------\n')

# enumerate()
# enumerate() is a built-in Python function that returns both index (position) and value (element) at the same time while looping
# Each value is a tuple (index, element)
# usecase - find the exact position of a bad data

letters = ['a','b','c'] # iterables
for index,value in enumerate(letters):
    print(index,value)
print('\n----------------------------------------------\n')

letters = ['a','b','c'] # iterables
print(list(enumerate(letters)))
print(list(enumerate(letters,start=2))) # we can give starting index position
print('\n----------------------------------------------\n')

letters = ['a','','c'] # iterables
for index,value in enumerate(letters):
    print(index,value) # find bad value
print('\n------------------REVERSED()----------------------------\n')

# reversed()
# reversed() is a built-in Python function that returns an iterator which gives elements in reverse order.
# It does NOT change the original data.
letters = ['a','b','c'] # iterables
print(reversed(letters))
print(list(reversed(letters))) # Very Important: reversed() Returns an Iterator
print('\n------------------REVERSED()----------------------------\n')
letters = ['a','b','c'] # iterables
for l in reversed(letters):
    print(l)


# zip()
# comines two or more sequences into pairs() tuples 
# Each tuple = one record (row)
# zip() Returns an Iterator (Important)
# zip() stops at the shortest iterable - important interview question
print('\n------------------ZIP()----------------------------\n')
letters = ['a','b','c']
numbers = [1,2,3]
print(zip(letters,numbers))# iterables
print(list(zip(letters,numbers)))
for l,n in zip(letters,numbers):
    print(l,n)
comb = list(zip(letters,numbers,'Hi')) # stops at the shortest iterable
print(comb)
print('\n------------------MAP()----------------------------\n')

# map()
# map() applies a function to every item in an iterable and returns the result.
# “Take each value → apply logic → return transformed values”
# syntax - map(function, iterable)
# clean and easiest way to do data transformations
letters = ['a','b','c']
print(map(str.upper,letters)) # iterator object
print(list(map(str.upper,letters)))

print('\n------------------MAP()----------------------------\n')

numbers = ['1','2','3'] # num as string
print(list(map(int,numbers))) #numbers

print('\n------------------MAP()----------------------------\n')
# remove whitespace

names = [' Alphy ','Daisy  ','  Joy']
print(list(map(str.strip,names)))

print('\n------------------MAP()----------------------------\n')
names = ['Alphy','Daisy','Joy']
for name in map(str.upper,names):
    print(name)
    print(type(name))

print('\n------------------FILTER()----------------------------\n')

# filter()
# filter() keeps only the values that satisfy a condition.
# “Check each item → keep it OR discard it”
# filter(function, iterable)
# returns a iterator object
# perfect for cleaning up data

# remove invalid data
names = ['Alphy',"",'Daisy',None,'Joy',False]
print(list(filter(None,names))) # None removes all the falsy values
print(list(filter(bool,names))) # bool also removes all the falsy values
print('\n------------------FILTER()----------------------------\n')

# keep only alphabets
items = ['sql','123','python','']
print(list(filter(str.isalpha,items)))
print('\n------------------FILTER()----------------------------\n')
items = ['sql','123','python','']
for item in filter(str.isalpha,items):
    print(item)