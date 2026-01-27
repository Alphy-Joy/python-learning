# Type Normalization
# Convert string-based numeric columns to integers before aggregation.

numbers = ['344','12','889']
print(list(map(int,numbers)))
print('\n----------------------------------------------\n')

# Text Standardization
# Normalize names (uppercase, trimmed) before deduplication.
names = [' alphy ','joy  ',' maRia']
#print(list(map(str.upper().strip(),names))) # upper() and strip() are methods, not standalone functions. You are calling them immediately, instead of passing them to map
cleaned_names = list(map(lambda x: x.strip().upper(), names))
print(cleaned_names)
print('\n----------------------------------------------\n')

# Date Parsing
# Convert raw date strings into a consistent YYYY-MM-DD format.
dates = ['2025/01/01', '2025/02/01']
formatted = list(map(lambda d: d.replace('/', '-'), dates))
print(formatted)
print('\n----------------------------------------------\n')

# Currency Conversion
# Apply a conversion rate to all price values in a dataset.
prices = [100, 200, 300]
converted = list(map(lambda p: p * 82, prices))
print(converted)
print('\n----------------------------------------------\n')
# Feature Engineering
# Transform raw numeric values into scaled or categorized values for analytics.
values = [10, 20, 30]
scaled = list(map(lambda x: x / max(values), values))
print(scaled)