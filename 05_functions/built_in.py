def chai(flavor='Masala'):
    """Return the masala""" # __doc__  must be first line of function and if not it will not work like value of __doc__ will be NONE
    return flavor # __name__

print(chai.__doc__)
print(chai.__name__)