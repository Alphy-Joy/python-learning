# A list comprehension is a compact way to create a new list by:
# •	looping over a sequence
# •	optionally filtering data
# •	optionally transforming data

# syntax= [
#     # Data Transformation
#     # for loop
#     # Data Filtering
# ]

domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.YOUTUBE.COM']
cleaned = [
    # Data Transformation
    d.lower().replace('www.','') # if no transformation is required just write the item in the iterable . here d
    # for loop
    for d in domains
    # Data Filtering
    if '.' in d # optional
]
print(cleaned)
print('\n------------------without transformation----------------------------\n')

cleaned = [
    # Data Transformation
    d # if no transformation is required just write the item in the iterable . here d
    # for loop
    for d in domains
    # Data Filtering
    if '.' in d # optional
]
print(cleaned)
print('\n------------------without transformation and filtering----------------------------\n')

cleaned = [
    # Data Transformation
    d # if no transformation is required just write the item in the iterable . here d
    # for loop
    for d in domains
]
print(cleaned)
print('\n------------------FILTER and LOOP - For each number → keep it only if it’s even----------------------------\n')
numbers = [1,2,3,4,5,6]

evens = [n 
         for n in numbers 
         if n % 2 == 0
         ]
print(evens)
print('\n------------------TRANSFORM + FILTER TOGETHER - square only even numbers----------------------------\n')
numbers = [1,2,3,4,5,6]

result = [n*n for n in numbers if n % 2 == 0]
print(result)
print('\n------------------IF–ELSE inside List Comprehension (VERY IMPORTANT)----------------------------\n')
numbers = [-3, 4, -1, 5]

labels = ['positive' 
          if n > 0 
          else 'negative' 
          for n in numbers]
print(labels)
print('\n------------------Flatten a matrix----------------------------\n')

matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
# Read it like:
# for each row → for each number → collect number
print(flat)

print('\n------------------Using range()----------------------------\n')

squares = [
    n*n
    for n in range(1,9)
    if n%2==0
]
print(squares)
print('\n------------------Flagged values ----------------------------\n')

values = [12, -5, 8, -1]
flagged = ['invalid' 
           if v < 0 
           else 'valid' 
           for v in values]
print(flagged)
print('\n------------------MULTIPLE CONDITIONS----------------------------\n')

nums = [10, 25, 30, 5]
filtered = [n 
            for n in nums 
            if n > 10 and n % 5 == 0]
print(filtered)