# append() - add new items to the end of a list
letters = ['a','b','c']
letters.append('x')
print(letters)
letters.append('y')
print(letters)

# insert() - add new item at specific position in a list
letters = ['a','b','c']
letters.insert(3,'d')
print(letters)
letters.insert(2,'x')
print(letters)


# adding to a matrix

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix.append('x')
print(matrix)

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix.append(['x','x','x'])
print(matrix)

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix[1].append('y')
print(matrix)

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix[0].insert(0,'z')
print(matrix)