# Data Quality Check
# You receive a list of customer ages.
# 👉 Identify all invalid ages (negative or >120) and report their row positions.

ages = [14,45,33,-10,23,125]

for pos,age in enumerate(ages):
    if age < 0 or age > 120:
        print(f"Invalid age {age} at position {pos}")
print('\n----------------------------------------------\n')
# CSV Row Validation
# While reading a CSV row-by-row (as a list), log the row number where mandatory fields are missing.
employee = [['101','Alphy',None],
            ['102','','HR'],
            ['103','Joy','Finance']
            ]
for pos,emp in enumerate(employee,start=1):
    if '' in emp or None in emp:
                print(f"Missing mandatory data at position {pos}")
print('\n----------------------------------------------\n')

# Log File Auditing
# Given a list of log messages, detect empty or corrupted logs and print the exact line number.
logs = ['INFO Start', '', 'ERROR Failure', None]

for line, log in enumerate(logs):
    if not log:
        print(f"Corrupted log at line {line}")
print('\n----------------------------------------------\n')

# Duplicate Detection with Position
# Find duplicate transaction IDs and print the index of their second occurrence.

transactions = ['T1', 'T2', 'T1', 'T3']
seen = []

for index, t in enumerate(transactions):
    if t in seen:
        print(f"Duplicate {t} at index {index}")
    else:
        seen.append(t)

print('\n----------------------------------------------\n')

# Threshold Breach Tracking
# Given daily sales numbers, detect the day index where sales first exceed a critical threshold.

sales = [232,564,112,899,455]
for day,sale in enumerate(sales,start=1):
     if sale >700:
          print(f"Reached critical threshold on day {day}")
          break