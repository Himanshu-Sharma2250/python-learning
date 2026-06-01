from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling ", func.__name__)
        result = func(*args, **kwargs)
        print("Finish ", func.__name__)
        return result
    return wrapper

@logger
def chai(type):
    print(f"Preparing {type} chai")

chai("Laal")