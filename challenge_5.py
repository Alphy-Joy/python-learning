#Salary Cleaning & Formatting

#Remove currency symbol $
#Replace comma , with empty string
#Salary must not be empty after cleaning
#Salary length must be <= 10 characters
#Output formatted sentence using f-string

salary = " $1,234,567,888"
salary = salary.strip()
valid = True

#Remove currency symbol $
#Replace comma , with empty string
salary = salary.replace("$","").replace(",","")

#Salary must not be empty after cleaning
if  salary == "":
    print("Salary must not be empty")
    valid = False

#Salary length must be <= 10 characters
if not len(salary) <= 10:
    print("Salary length must be <= 10 characters")
    valid = False

if valid:
    print(f"Clean salary is {salary}")

#Interview Insight
#This is real-world financial data cleaning
#Chained string methods = clean, readable code