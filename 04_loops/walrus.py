# value = 41
# remainder = value % 5

# if remainder:
#     print(f"Remainder is {remainder}")

value = 88

# if remainder := value % 5:
#     print(f"Remainder is {remainder}")


# cup_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter cup size: ")) in cup_sizes:
#     print(f"Serving {requested_size} cup tea")
# else:
#     print("Unavailable cup size: ", requested_size) 


menu = ["Bread chickpea", "Egg plant", "Tomato Soup"]

print("Available items in menu: ", menu)

while (req_item := input("Enter your order: ")) not in menu:
    print(f"Sorry, {req_item} is not available")