class BaseChai:
    def __init__(self, type_) -> None:
        self.type = type_
    
    def prepare(self):
        print(f"Preparing {self.type} chai")
    
class MasalaChai(BaseChai): # inheritance
    def add_spices(self):
        print("Adding Kali Mirch, Ginger")
    
class ChaiShop:
    chai_cls = BaseChai # composition

    def __init__(self) -> None:
        self.chai = self.chai_cls("Normal")
    
    def serve(self):
        self.chai.prepare()
        print(f"Serving {self.chai.type} chai")
    
class FancyShop(ChaiShop): # inheritance
    chai_cls = MasalaChai # composition

shop = ChaiShop()
fancy = FancyShop()

shop.serve()
# fancy.chai_cls.add_spices()  # error: missing arg self
fancy.chai.add_spices() # showing red swigly lines but it gives correct output