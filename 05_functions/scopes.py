def server_chai(): 
    chaiType = "Black" # local scope
    print(f"Chai type (inside function) is {chaiType}")

chaiType = "Ginger" # gobal scope
# server_chai()
# print(f"Outside function => {chaiType}")

def chai_counter():
    chai_order = "Black"
    def print_order():
        chai_order = "Ginger"
        print("Inner: ", chai_order)
    print_order()
    print("Outer: ", chai_order)    

chai_counter()