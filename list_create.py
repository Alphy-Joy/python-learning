# create a list

# empty list
empty_list = []
print(empty_list)
print(type(empty_list))

# list

vowels = ['a','e','i','o','u'] # python creates an object for each values in memory
print(vowels)
print(type(vowels))
numbers = [1,2,3,4,5]
print(numbers)
mixed_list = [2,'w',None,True]
print(mixed_list)

lang = "Python"
lang = list("Python") # another way to create a list
print(lang)

num = list(range(5))
print(num)

# nested list (matrix)

matrix = [['a','b','c'],
          [1,2,3],
          [True]]
print(matrix)
print(type(matrix))

