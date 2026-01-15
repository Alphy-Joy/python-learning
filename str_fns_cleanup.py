# lstrip()
text = " Data Science"
print(len(text))
text = text.lstrip() # remove white space from left side
print(len(text))

# rstrip()
text = "Data Science  "
print(len(text))
text = text.rstrip() # remove white space from right side
print(len(text))

# strip()
text = "  Data Science  "
print(len(text))
text = text.strip() # remove white space from both sides
print(len(text))