country = "India"

if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Canada":
    print("CA")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("DE")
else:
    print("Unknown country")

# using match case we can rewrite this
# We can use this only if we are matching values
country = "USA"
match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Canada":
        print("CA")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown country")