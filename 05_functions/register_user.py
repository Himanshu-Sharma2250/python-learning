def get_input():
    username = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    return (username, email, password)

def validate_input(username, email, password):
    print("User input is validated")

def save_to_db():
    print("Saving to DB")
    print("Save Done")

def register_user():
    username, email, password = get_input()
    validate_input(username=username, email=email, password=password)
    save_to_db()

register_user()