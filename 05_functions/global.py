chaiType = "ginger"
print("Chai order: ", chaiType)

def chaiOrder():
    def changeType():
        global chaiType
        # get the global variable and can change it if want
        chaiType = "Black"
    changeType()

chaiOrder()
print("Chai order now: ", chaiType)