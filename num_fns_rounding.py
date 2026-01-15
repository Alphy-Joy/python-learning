import math

# abs() - inbuilt fn
print(abs(5-10))

# round() - inbuilt fn
# round() is best for data analysis to clean up numbers for reports or save space
print(round(1.3)) 
print(round(1.5)) # .5 round to nearest even. known as bankers rounding
print(round(2.5)) # nearest even is 2
print(round(37.1234,2))

# math.floor() - not inbuilt. Math fn
print(math.floor(23.3))
print(math.floor(23.7))

# math.ceil() - not inbuilt. Math fn
# ceil() is best for data engg . it can be used to split data into batches or pages
print(math.ceil(1.7))
print(math.ceil(1.3))

# math.trunc() - cuts off decimal part and keeps the whole number
price = 171.8889
print(math.trunc(price))

# int() also gives same result as trunc(). If math module is not already imported you can use int() as well