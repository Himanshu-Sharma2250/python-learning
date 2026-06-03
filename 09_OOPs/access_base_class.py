class Chai:
    def __init__(self, price) -> None:
        self.price = price
    
class MasalaChai(Chai):
    def __init__(self, price, spice_level) -> None:
        self.price = price # duplicate value 
        self.spice_level = spice_level

class GingerTea(Chai):
    def __init__(self, price, spice_level) -> None:
        Chai.__init__(self, price) # explicit call of Chai
        self.spice_level = spice_level

class KaliChai(Chai):
    def __init__(self, price, spice_level) -> None:
        super().__init__(price) # super -> base class Chai
        self.spice_level = spice_level