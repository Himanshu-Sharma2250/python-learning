# smart thermostate alert system

temperature = 330
user_input = input("Want to activate the thermostate: ").lower()

device_status = "Inactive"

if user_input == "yes":
    device_status = "Active"
else:   
    device_status = "Inactive"

if device_status == "Active":
    if temperature > 35:
        print("Warning! High temperature detected. Please on AC")
    else:
        print("Normal temperature")
else:
    print("Thermostate is inactive")