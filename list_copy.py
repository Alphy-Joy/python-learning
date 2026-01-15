import copy

list_og = ['a','b','c']
print(f"OG list is - {list_og}")
# we are assigning the og list to a variable. here a new copy is not made. 
# both the variables are pointed to the same reference of the list created in the memory. 
# so if we make a change in copy ,it will be reflected in the og list also
list_copy = list_og 
print(f"List copy is - {list_copy}")
list_copy.append('x')
print(f"List copy after adding an element in copy - {list_copy}")
print(f"OG List after adding an element in copy - {list_og}")
print("------------------------------------------------------------")
# shallow copy - for top level
list_og = ['a','b','c']
print(f"OG list is - {list_og}")

list_copy = list_og.copy() # a copy is made . here change will  be made only in copy 
print(f"List copy is - {list_copy}")
list_copy.append('x')
print(f"List copy after adding an element in copy - {list_copy}")
print(f"OG List after adding an element in copy - {list_og}")
print("\n----------------------------------\n")

# matrix

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix_copy = matrix.copy() # shallow copy
print(f"OG matrix - {matrix}")
print(f" Matrix copy - {matrix_copy}")
matrix_copy.pop()
print(f"OG matrix after removing - {matrix}") # no changes since the operation was on top level not deep
print(f" Matrix copy after removing - {matrix_copy}")
matrix_copy[1].append('X')
print(f"OG matrix after appending - {matrix}") # X is appended in OG matrix too. means shallow copy doesnt work for deeper level . for that we should use deepcopy()
print(f" Matrix copy after appending - {matrix_copy}")
print("\n----------------------------------\n")

# deep copy
# for a shallow copy, any changes in deeper level will affect the og list also. so we use deep copy
# for that we need to import copy library
matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix_copy = copy.deepcopy(matrix)
print(f"OG matrix - {matrix}")
print(f" Matrix deep copy - {matrix_copy}")
matrix_copy.pop()
print(f"OG matrix after removing - {matrix}") # no changes
print(f" Matrix deep copy after removing - {matrix_copy}")
matrix_copy[1].append('X')
print(f"OG matrix after appending - {matrix}") # unlike the shallow copy, here OG list isnt affected when the matrix deep copy was altered
print(f" Matrix deep copy after appending - {matrix_copy}")
#copy.deepcopy() creates a true independent copy for all levels

print("\n----------------------------------\n")

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix_copy = copy.copy(matrix)
print(f"OG matrix - {matrix}")
print(f" Matrix  copy - {matrix_copy}")
matrix_copy.pop()
print(f"OG matrix after removing - {matrix}") #  no changes
print(f" Matrix  copy after removing - {matrix_copy}")
matrix_copy[1].append('X')
print(f"OG matrix after appending - {matrix}") # changes - just like shallow copy
print(f" Matrix  copy after appending - {matrix_copy}")
