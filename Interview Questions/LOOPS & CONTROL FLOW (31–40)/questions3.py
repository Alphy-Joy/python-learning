# LOOPS & CONTROL FLOW (31–40)

#---------------------------------------------------------------------------------------------------

# 31.	Retry user input validation up to 3 times using while.

# attempt = 0
# while attempt < 3:
#     user_input = input("Enter yes/no? ")

#     if user_input == 'yes':
#         print("✅ Input accepted")
#         break

#     attempt += 1
# else:
#     print("❌ Reached maximum attempts")

# print("Program ended")
# else runs only if the loop finishes naturally
# else does NOT run if break is executed

#---------------------------------------------------------------------------------------------------

# 32.	Loop through records and stop execution if a critical threshold is exceeded.

values = ['10','12','15','17','101','21']
for value in values:
    print(f"processing value... {value}")
    if int(value)>100:
        print("critical threshold is exceeded")
        break
else:
    print("Values are valid")

#---------------------------------------------------------------------------------------------------

# 33.	Process rows until a termination keyword (END) is encountered.

rows = ['wait','continue','end','pass']
for row in rows:
    print(f"processing row... {row}")
    if row.lower() == 'end':
        print("reached termination keyword end")
        break
else:
    print("Processed all rows")

#---------------------------------------------------------------------------------------------------

# 34.	Skip weekend records while processing daily sales data.

sales = ['Mon','Tue','Sat','Sun','Fri']
for sale in sales:
    print(f"processing daily sales... {sale}")
    if sale in ['Sat','Sun']:
        print("Weekend sales skipped")
        continue
        print(f"Psales days {sale}")

#---------------------------------------------------------------------------------------------------

# 35.	Generate report filenames for the last 30 days using range().

file_name = 'report'
for i in range(31):
    print(f"{file_name}_jan_{i}.csv")

#---------------------------------------------------------------------------------------------------

# 36.	Compare actual vs expected counts and break when mismatch occurs.

expected_counts = [10, 15, 20, 25]
actual_counts   = [10, 15, 18, 25]

for index in range(len(expected_counts)):
    expected = expected_counts[index]
    actual = actual_counts[index]

    print(f"\nChecking record {index}")
    print(f"Expected = {expected}, Actual = {actual}")

    if actual != expected:
        print("❌ Count mismatch detected")
        break
else:
    print("✅ All counts match expected values")

#---------------------------------------------------------------------------------------------------

# 37.	Use nested loops to generate cross-combinations of regions and products.

regions = ['north','south','east','west']
products = ['kurta','jeans']

for region in regions:
    for product in products:
        print(f"Product : Region - {product} : {region}")
print("All combinations are generated")

#---------------------------------------------------------------------------------------------------

# 38.	Drill into year → month → day data folders and generate file paths.

years = ['2024','2025']
months = ['Oct','Nov','Dec']
days = ['20','21','22']
for year in years:
    for month in months:
        for day in days:
            print(f"report_{day}_{month}_{year}")

#---------------------------------------------------------------------------------------------------

# 39.	Identify missing values in hierarchical data using nested loops.

classes = {
    "Class A": ["John", "Alice", ""],
    "Class B": ["Maria", None, "David"]
}
for class_name, students in classes.items():      # level 1
    for position, student in enumerate(students): # level 2
        if student == "" or student is None:
            print(f"❌ Missing student in {class_name} at position {position}")

#---------------------------------------------------------------------------------------------------

# 40.	Validate multiple tables and columns using nested loops.

tables = ["users"]
columns = ["id", "date"]

for t in tables:
    for c in columns:
        print(f"Checking {t}.{c}")

