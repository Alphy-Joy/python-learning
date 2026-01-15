score = 90

result = "Great" if score>=90 else "Good"
print(result)

# OR

print("Great" if score>=90 else "Good")

# we cant use elif in online if-else. so wwrite multiple conditions as follows
score = 70
result = "A+" if score>=90 else "A" if score>=80 else "B"
print(result)

# note
# for simple logic use inline if-else
# for complex logic use classic if else