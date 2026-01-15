# string is immutable
# Immutability of strings (VERY IMPORTANT)
text = "Hello"
# text[0] = "Y"  ❌ ERROR

text = "Y" + text[1:]  # ✅ Correct
print(text)