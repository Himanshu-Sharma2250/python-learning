def order(drinks, main_dish, deserts):
    print(f"Drinks: {drinks} - Main Dish: {main_dish} - Desserts: {deserts}")

# postional args
# order("Water", "Daal Chawal", "Gulab Jamun")
# key word args
# order(drinks="Water", deserts="Rosgulla", main_dish="Briyani")

def special_chai(*ingredients, **extras):
    print("Ingredients: ", ingredients)
    print("Extra Ingredients: ", extras)

# *args == *ingredients
# **kwargs == **extras

# special_chai("Oolong", "Macha", sweetner="Brown Sugar", foam="No")
# answer : Ingredients:  ('Oolong', 'Macha')
#          Extra Ingredients:  {'sweetner': 'Brown Sugar', 'foam': 'No'}

# special_chai("Oolong", "Macha", "Brown Sugar", "No")
# answer : Ingredients:  ('Oolong', 'Macha', 'Brown Sugar', 'No')
#          Extra Ingredients:  {}

def print_list(order=[]):
    order.append("Kala Chai")
    print(order)

# print_list()
# print_list()

def print_list_(order=None):
    if order is None:
        order = []
        order.append("Green Tea")
    
    print(order)

print_list_()
print_list_()