# max()
numbers = [4,9,3,12,34,2]
print(max(numbers))
# min()
print(min(numbers))
# sum()
print(sum(numbers))
# len()
print(len(numbers))

# all() - returns true if all items are true
print('All : ', all(numbers))
print('All : ', all([1,0,3,5])) # considers 0 as missing value
print('All : ', all(['a','','b','c'])) # empty string is considered as a missing value

# any() - returns true if any of the item is true
print('Any : ', any(numbers))
print('Any : ', any([1,0,3,5])) 
print('Any : ', any(['a','','b','c']))

# count() - returns the occurence of an item in a list
print('Count : ', numbers.count(3))

# index() - returns the position of first occurence of an item in a list
print('Index : ',numbers.index(12))