# delivery fee waiver system

order_amount = int(input("The total order amount is "))

delivery_fee = 0 if order_amount > 300 else 30

if delivery_fee == 0:
    print(f"Free Delivery. Total cost: ${order_amount}")
else:
    print(f"Delivery fee is $30. Total cost: ${order_amount + 30}")