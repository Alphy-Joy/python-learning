# is*() methods

#Real use cases
#Password validation
#Data quality checks
#Input sanitization
text1 = "Python123"
text2 = "12345"
text3 = "Python"
text4 = " "
text5 = "12-34"

print(text1.isalnum())   # True
print(text2.isdigit())   # True
print(text3.isalpha())   # True
print(text4.isspace())   # True
print(text5.isdigit()) #false