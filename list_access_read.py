# Access and Read a list

# indexing - retrieving single item

letters = ['a','b','c','d','e']
print(letters[0])
print(letters[2])
# use negative indexing to access the elements in the last position
print(letters[-1])


matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
print(matrix)
print(matrix[2]) #last row
print(matrix[-1]) #last row
print(matrix[2][2]) #last row,last number
print(matrix[-1][-1]) #last row,last number

# slicing - retrieving multiple items
letters = ['a','b','c','d','e']

print(letters[0:2])
print(letters[0:])
print(letters[:4])
print(letters[2:5])
print(letters[:])

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
print(matrix[1:3])
print(matrix[0:2])
print(matrix[2][0:2])