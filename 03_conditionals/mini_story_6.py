# Railway ticket system. show seat feature based on the inout of user

seat_input = input("Enter your seat (General/AC/Sleeper/Luxury): ").lower()

match seat_input:
    case "general":
        print("No seat guarantee")
    case "sleeper":
        print("Seat guarantee but no AC")
    case "ac":
        print("Seat guarantee and AC available")
    case "luxury":
        print("Seat with AC and private cabine and free food")
    case _:
        print("Seat Unavailable")