def process_order(item, amount):
    try:
        price = {"masala": 50}[item]
        cost = price * amount
        print(f"Total cost of order is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Amount must be numberic")

process_order("ginger", 20)
process_order("masala", 20)
process_order("masala", "1")