# indexing


# positive indexing 
# 0  1  2  3  4
# H  E  L  L  O

# negative indexing
# -5  -4  -3  -2  -1
# H   E   L   L   O

# print E
text = "HELLO"
print(text[1]) #positive indexing
print(text[-4]) #negative indexing


# slicing

#print HEL
print(text[0:3]) #positive indexing
print(text[-5:-2]) #negative indexing

date = "2025-12-22"
#extract year
print(date[0:4])

# open ended slicing
print(date[:4])
print(date[8:])

# Note - if you want to extract from the start use positive indexing or 
# if you want to extract from the end of the string use negative indexing
print(date[-2:])

# with steps
print(text[0:8:2])
