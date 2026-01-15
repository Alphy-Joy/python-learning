
# sort - asc by default
letters = ['c','b','a']
letters.sort() # method not a function
print(letters)
# to sort in desc order
letters.sort(reverse=True)
print(letters)

# matrix 
matrix = [['g','h','i'],
          ['d','e','f'],
          ['a','b','c']]
matrix.sort() # python doesnt compare all the elements in the matrix. it checks the first element of each row and sort accordigly
print(matrix)

matrix = [['a','h','i'],
          ['d','e','f'],
          ['a','b','c']]
matrix.sort() # python doesnt compare all the elements in the matrix. it checks the first element of each row and sort accordigly
print(matrix)

# sorted() - function . creates a new list without changing the original list

letters = ['c','b','a','d']
new_list = sorted(letters)
reversed_new_list = sorted(letters,reverse = True)
print(f'old list - {letters}')
print(f'new list - {new_list}')
print(f'new list reversed - {reversed_new_list}')


# reversed() - flip the list. doesnt sort the items - it creates an iterator object not a list. so we should convert it to a list manually
letters = ['c','b','a','d']
reversed_letters = reversed(letters)
reversed_letters = list(reversed(letters))
print(reversed_letters)