# lambda function

# A small, anonymous (no-name) function written in one line
# 📌 Used when:
# The logic is simple
# The function is needed only once
# Cleaner than writing def

# Syntax
# lambda arguments : expression
# 🚨 Rules:
# Only ONE expression
# No return keyword
# Automatically returns result
# No loops (for, while)
# No multiple statements
print('\n------------------LAMBDA()----------------------------\n')

square = lambda x : x*x
print(square(5))
print('\n------------------LAMBDA()----------------------------\n')
add = lambda x,y : x+y # 2 parameters
print(add(10,35))
print('\n------------------LAMBDA()----------------------------\n')
check = lambda i : i in 'Python'
print(check('z'))

print('\n------------------LAMBDA() with MAP()----------------------------\n')

# remove $ sign and also convert these string numbers to actual float numbers
prices = ['$129.9','$111.1','$99.9']
p = '$129.9'
cleaned_p = p.replace('$','')
print(cleaned_p)
print(type(cleaned_p))
float_converted_cleaned_p = float(p.replace('$',''))
print(float_converted_cleaned_p)
print(type(float_converted_cleaned_p))
# now lets go back to our list prices which needs the actual cleaning and transformation
prices = ['$129.9','$111.1','$99.9']
lambda_float_cleaned_p = lambda p : float(p.replace('$',''))
print(lambda_float_cleaned_p('$129.9'))
print(type(lambda_float_cleaned_p))
# now to apply this to all items in the list we use map()

prices = ['$129.9','$111.1','$99.9']
map_lambda_float_cleaned_p = list(map(lambda p : float(p.replace('$','')),prices))
print(map_lambda_float_cleaned_p)
print(type(map_lambda_float_cleaned_p))

print('\n------------------LAMBDA() with FILTER()----------------------------\n')

# remove values below 100 
values = [120,40,350,12]
print(list(filter(lambda p : p>=100,values)))
print('\n------------------LAMBDA() with FILTER()----------------------------\n')
# remove students who scored below 70
students = [['Alphy',60],
            ['Daisy',80],
            ['Joy',85]]
#print(students[0][1]>70)
print(list(filter(lambda row:row[1]>70,students)))

print('\n------------------LAMBDA() with FILTER()----------------------------\n')
# keep students whose name starts with J
students = [['John',60],
            ['Daisy',80],
            ['Joy',85]]
# print(students[1][0].startswith('J'))
print(list(filter(lambda row:row[0].startswith('J'),students)))