for i in range(5):
    print(i)
else: # here else is useless. bcz it will execute when the loop ends. even without else the last print statement will be executed
    print("Loop completed")

# we use else in for loop when break statement is used.

# check for even numbers
items = [1,3,5,7,9]
for item in items:
    if item%2 == 0:
        print(f"Found an even number: {item}")
        break
else:
    print("All numbers are odd")

# usecase : Search and validate
# searching for a missing name

names = ["John","Monica",None,"Jade"]
for name in names:
    if name is None:
        print("Name is missing")
        break
else:
    print("All names are found")



files = ["data.csv","report.pdf","sales.csv"]
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a csv")
        break
else:
    print("All files are csv")

# cannot use continue with else

files = ["data.csv","report.pdf","job.txt","sales.csv"]
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a csv")
        continue
else:
    print("All files are csv") # this is useless

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
for file in file_list:
    if file_list.count(file) > 1:
        print(f"Duplicate found: {file}")
        break
else:
    print("All files are unique")