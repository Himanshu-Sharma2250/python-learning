def waiter():
    print("Welcome! What would you like to order?") # executes when generator starts
    order = yield # stores value that is given
    print("Order when sending value: ", order)
    while True:
        print(f"Preparing: {order}")
        order = yield
        print("Order when after value: ", order)

customer1 = waiter() # stores the ref of waiter() in customer1
next(customer1) # starts the generator

customer1.send("Chilli Potato") # gives the value to generator
customer1.send("Pizza") # gives the value to generator