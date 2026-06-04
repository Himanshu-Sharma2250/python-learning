class OutOfIngredients(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredients("Either Milk or Sugar is not available")
    print("Chai is ready!")

make_chai(0,0)