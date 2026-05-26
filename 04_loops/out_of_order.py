menu = ["Chole Bhature", "Chole Chawal", "Samosa", "Pani Puri"]

for item in menu:
    print("Item is ", item)
    if (item == "Samosa"):
        print(item, ": Discontinued")
        break
    elif (item == "Chole Chawal"):
        print(item, ": Out of Stock")
        continue