
# if
score = 90
if score>=90:
    print("Great Job!") #indendation is important

# if - else
score = 65
if score>=90:
    print("Great Job!")
else:
    print("Better luck next time")

# if - elif - else
score = 80
if score>=90:
    print("Great Job!")
elif score>=80:
    print("Good")
else:
    print("Better luck next time")

# nested if
score = 92
submitted_project = True
if score>=90:
    if submitted_project:
        print("Grade A+. Great Job")
    else:
        print("Grade A.Great Job!")
elif score>=80:
    print("Good")
else:
    print("Better luck next time")

# logical operator
score = 90
submitted_project = True
if score>=90 and submitted_project:
    print("Grade A+. Great Job!!")
elif score>=80:
    print("Good")
else:
    print("Better luck next time")