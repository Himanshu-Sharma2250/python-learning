class ChaiCup:
    size = 200

    def describe(self):
        return f"A {self.size}ml Chai Cup"
    
cup = ChaiCup()
print(cup.describe())
# print(ChaiCup.describe()) # error : missing self args
print(ChaiCup.describe(cup)) # cup : context

cup_2 = ChaiCup()
print(cup_2.describe())
cup_2.size = 100
print(ChaiCup.describe(cup_2))

