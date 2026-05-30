# PURE FUNCTIONS
def pure_order(order):
    return order * 50

# IMPURE FUNCTIONS
total_bill = 20

def impure_order(order):
    global total_bill
    total_bill *= order
    return total_bill

# RECURSIVE FUNCTIONS
def n_to_0(n):
    print(f"n: {n}")
    if (n == 0):
        print(f"End")
        return
    n_to_0(n-1)

# n_to_0(5)

# LAMBDA FUNCTIONS
chais = ["Light", "Kadak", "Green", "Kadak"]

strong_chai = list(filter(lambda chai: chai=="Kadak", chais))

print(f"Strong Chai: {strong_chai}")