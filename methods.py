text = "Hello"
number = 50
# specific data type classes.An instance method of that object’s class
print(text.upper())
#print(number.upper()) # error bcz its a string class instance method . 
print(number.to_bytes())
#print(text.to_bytes()) # error bcz its an integer class instance method
text = "hello alphy. how are you"
print(text.title()) # capitalize first letter of each word

print(text.capitalize()) # capitalise first letter of first word
