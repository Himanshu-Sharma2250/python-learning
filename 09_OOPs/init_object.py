class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def profile(self):
        return f"User {self.name} with email {self.email}"

himanshu = User("Himanshu", "him@gmail.com")
print(himanshu.profile())

hitesh = User("Hitesh", "hit@gmail.com")
print(hitesh.profile())