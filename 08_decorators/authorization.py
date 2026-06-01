from functools import wraps

def require_admin(func):
    wraps(func)
    def wrapper(role):
        if (role != 'admin'):
            print("Access Denied. Admin Only")
        else:
            return func(role)
    return wrapper

@require_admin
def delete_user(role):
    print("User Deleted")

delete_user("user")
delete_user("admin")