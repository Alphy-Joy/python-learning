letters = ['a','b','c','d']
print(type(letters))
print(letters)
letters[1] = 'X'
print(letters)
letters[2] = 'Y'
print(letters)
letters = 'Z'
print(type(letters)) # changed to str class after a string is assigned

#matrix
matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix[-1] = ['X','Y','Z']
print(matrix)
matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix[0][0] = 'A'
print(matrix)
