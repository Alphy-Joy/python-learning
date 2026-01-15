
# clear() - remove all the elements and returns an empty list 
numbers = [1,2,3,4,5]
numbers.clear()
print(numbers)

# remove() - remove by value. remove only the first occurence of the value in the list 
letters = ['a','b','a','d','a']
letters.remove('a')
print(letters)

# pop() - remove by position. remove item at a specific position. if the position is not mentioned it removes the last element in the list
# also pop returns the removed value.

letters = ['a','b','a','d','a']
removed_item = letters.pop() # removes last element
print(letters)
print(f'Removed Item - {removed_item}')

letters = ['a','b','a','d','a']
removed_item = letters.pop(1)# removes  element at position 1
print(letters)
print(f'Removed Item - {removed_item}')

# removing items from matrix

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix.clear()
print(matrix)

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix.remove(['d','e','f'])
print(matrix)

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix[0].remove('c')
print(matrix)

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
removed_item = matrix.pop() # removes the last row
print(matrix)
print(f'Removed Item - {removed_item}')

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
removed_item = matrix.pop(0) 
print(matrix)
print(f'Removed Item - {removed_item}')

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
removed_item = matrix[-1].pop(2)
print(matrix)
print(f'Removed Item - {removed_item}')