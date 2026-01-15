# CSV Column Name Cleaner (Very Important for Data Analysts)
# Rules

# Remove leading/trailing spaces
# Convert to lowercase
# Replace spaces with _
# Column name must not be empty
# Column name must not start or end with _

column = "  Total Sales Amount  "
valid = True

# Remove leading/trailing spaces
column = column.strip()
# Convert to lowercase
column = column.lower()
# Replace spaces with _
column = column.replace(" ","_")
# Column name must not be empty
if  column == "":
    print("Column name must not be empty")
    valid = False
# Column name must not start or end with _
if column[0].startswith("_") and column[-1].endswith("_"):
    print("Column name must not start or end with _")
    valid = False

if valid:
    print(f"clean column name: {column}")