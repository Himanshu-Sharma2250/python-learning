def local_chai():
    yield "Kali Chai"
    yield "Masala Chai"

def imported_chai():
    yield "Macha Tea"
    yield "Oolong Tea"

def full_chai_menu():
    yield from local_chai()
    yield from imported_chai()

# for chai in full_chai_menu():
#     print(chai)

# Closing the generator
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed")
    
stall = chai_stall()
print(next(stall))
stall.close() # clean up