# take list name and bill and print "name paid bill amount"

customers = ["Himanshu", "Jon", "Kon", "Hen"]
bills = [4000, 2400, 3000, 3400]

# one method
total_customers = len(customers) if len(customers) == len(bills) else 0

# for i in range(total_customers):
#     print(f"Customer {customers[i]} paid ${bills[i]}")

# second method : use "zip" method
for customer, amount in zip(customers, bills):
    print(f"Customer {customer} paid ${amount}")