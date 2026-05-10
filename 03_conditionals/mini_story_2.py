# suggestion system, if samosa and cookies present, proceed with order or else not available

snackInput = input("What snack do you want? ")

snack = snackInput.lower()

if snack == "samosa" or snack == "cookies":
    print("Order confirmed")
else:
    print("This snack is unavailable. We only serve samosa and cookies")