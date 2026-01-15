# Transformations

# 1. replace() - use case eg : clean numeric formats
price = "345,889"
print(price.replace(",","."))

# use case - change phone number format
phone = "234-566-745"
print(phone.replace("-"," "))

# chained methods - executes left to right
price = "$55,99"
print(price.replace("$","").replace(",","."))

#challenge
phone = "+49 (178) 123-567" #expected o/p - 0049178123567
print(phone.replace("+","00").replace(" ","").replace("(","").replace(")","").replace("-",""))

#===================================================================================================

# 2. Concatenation (+)
first_name = "Alphy"
last_name = "Joy"
full_name = first_name +" "+ last_name
print(full_name)

#use case - build file path
folder = "C:/Users/Alphy"
file = "dataset.csv"
file_path = folder+"/"+file
print(file_path)

#===================================================================================================

# 3. fstring - formatted string - formats and build string

name = "Alphy"
age = 35
is_student = False
print("My name is "+name+", I am "+str(age)+" years old and my student status is "+str(is_student)+".") # hard to read
print(f"My name is {name}, I am {age} years old and my student status is {is_student}.") # easy -no concats,no conversions
print(f"2 + 3 = {2+3}")

#===================================================================================================

# 4. split()

t_stamp = "22-12-2025 14:28"
print(t_stamp.split(" ")) #list
date = "22-12-2025"
print(date.split("-")) #list

# 5. String repetition (*)

print("="*40)