for x in (1,2,3):
    for y in (1,2):
        print(f"({x},{y})")

# USECASES
# 1 - cross and combine

colors = ['red','blue','green','white']
sizes = ['L','M','S']
for color in colors:
    for size in sizes:
        print(f"{color} - Size {size}")

# 2 - navigate/drill into heirarchy
years = ['2026','2027']
months = ['Jan','Feb']
days = range(1,19)
for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")


# select count(*) from table where col IS NULL
tables = ['users','customers','products','orders']
columns = ['Id','creation_date']
for t in tables:
    for c in columns:
        print(f"select count(*) from {t} where {c} IS NULL")