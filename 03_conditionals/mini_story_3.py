# calculate price based on input

cup_size = input("Enter the cup size for tea: ").lower()

if cup_size == "small":
    print("That will be $10")
elif cup_size == "medium":
    print("That will be $15")
elif cup_size == "large":
    print("That will be $20")
else:
    print("Kya bak rahe ho mactherchos")