def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greeting():
    print("Greetings! My fellow human beings")

greeting()