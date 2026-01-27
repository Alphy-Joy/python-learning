# Latest Error Detection
# Scan logs from newest to oldest and stop when the most recent ERROR is found.

statuses = ['INFO','WARNING','INFO','ERROR','INFO']

for pos,status in enumerate(reversed(statuses)):
    if status.lower() == 'error':
        print(f"Error detected at pos {pos}")
        break
print('\n----------------------------------------------\n')

# Rollback Validation
# Given a history of applied patches, validate rollback order using reverse iteration.

patches = ['v1', 'v2', 'v3']

for patch in reversed(patches):
    print(f"Rolling back {patch}")

print('\n----------------------------------------------\n')

# Last Valid Record Retrieval
# From a dataset containing corrupted records, find the last valid entry.
records = [None, None, 'valid1', 'valid2']

for r in reversed(records): # 'valid2' → 'valid1' → None → None
    if r:
        print(r) # Prints the latest valid patch
        break

print('\n----------------------------------------------\n')
# Reverse Trend Analysis
# Analyze declining metrics by processing recent values first.
metrics = [10, 20, 15, 5]

for value in reversed(metrics):
    print(value)
print('\n----------------------------------------------\n')


# Undo Stack Simulation
# Process a list of user actions in reverse order to simulate undo operations.
actions = ['open', 'edit', 'save']

for action in reversed(actions):
    print(f"Undo {action}")
