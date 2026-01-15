answer = ""
while answer != 'yes':
    answer = input("Do you agree, yes/no? ")
print("Thank you")

#-------------------------------------------

while True:
    answer = input("Do you agree, yes/no? ")
    if answer == 'yes':
        break
print("Thank you")

#-------------------------------------------

attempt = 0
while attempt < 3:
    answer = input("Do you agree, yes/no? ")
    if answer == 'yes':
        print("Glad we are on the same page")
        break
    attempt += 1
else:    
    print("3 strikes! You are out")