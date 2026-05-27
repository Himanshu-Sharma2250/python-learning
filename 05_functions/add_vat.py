def add_vat(price: int, vat_rate: float):
    vat = price * vat_rate
    total_bill = price + vat
    print(f"Your total bill including VAT is {total_bill}")

for i in range(0,3):
    price = int(input("Enter the price: "))
    vat_rate = 0.1
    add_vat(price=price, vat_rate=vat_rate)
