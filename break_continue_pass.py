names = ["John","Alice","","Ron"]
for name in names:
    print(f"Name is {name}")
# but i want to stop execution when an empty value is found

# break - it stops the loop immediately. it jumps out and ends the loop right away
for name in names:
    if name == "": # checks for empty value
        print("Empty value detected")
        break # stop execution
    print(f"Name is {name}") 

# continue - it skips one loop cycle without stopping the loop. skip this one and go next
# continue skips the bad or empty data without skipping the whole loop
for name in names:
    if name =="":
        print("Empty value detected")
        continue
    print(f"Name = {name}")

# pass - it is a placeholder where nothing happens. for now just keep going. do nothing
for name in names:
    if name =="":
        pass # to do something later when you get the logic
    print(f"Name = {name}")

# when we get the logic, we remove the pass and add our code
for name in names:
    if name =="":
        name = name.replace("","Unknown value")
    print(f"Name = {name}")

# real world application
# loop through a list of days and print only the working days, skipping the weekends

days = ["Mon","Wed","Sat","Thu","Sun","Fri"]
weekends = ["Sat","Sun"]
for day in days:
    if day in weekends:
        continue
    print(f"Working days - {day}")

# for variables use singular
# for sequences use plural
# avoid hardcoding values inside for or if. instead define them as variables.

# Scan emails to block unsafe emails before entering in your system
emails = ["alphy@gmail.com","help@outlook.com","DROP TABLE USERS;","maria@gmail.com"]
for email in emails:
    if ';' in email:
        print("Hacker attack : SQL Injection detected")
        break
    print(f"Scanning emails : {email}")