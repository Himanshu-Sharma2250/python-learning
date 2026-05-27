def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

def order():
    cup_size = input("Enter cup size: ")
    total_cups = int(input("Enter total cups: "))

    prices_per_size = {
        "small": 20,
        "medium": 50,
        "large": 80
    }

    total_bill = calculate_bill(total_cups, prices_per_size[cup_size])

    print(f"Your total bill is {total_bill}")


order()
