class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {
        "masala chai": 20,
        "kali chai": 10
    }
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"We don't serve {flavor} chai")
        if not isinstance("cups", int):
            raise TypeError("Cups value must be Numberic value")
        total = menu[flavor] * cups
        print("Total bill: ", total)
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thanking for visiting")

bill("masala", 2)
bill("masala chai", 1)
bill("Oolong", "3")
    