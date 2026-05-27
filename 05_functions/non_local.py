def chai_order():
    chai_type = "Elaichi"
    def change_type():
        nonlocal chai_type
        # using "nonlocal" we can access variables outside the function
        chai_type = "ginger"
    change_type()
    print("after change_type function : ", chai_type)

chai_order()