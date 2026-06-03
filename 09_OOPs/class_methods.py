class ChaiOrder:
    def __int__(self, tea_type, sweetness, cup):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.cup = cup

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["cup"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, cup = order_string.split("-")
        return cls(tea_type, sweetness, cup)
    
order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": "Medium", "cup": "small"})
order2 = ChaiOrder.from_string("Normal-medium-small")

print(order1.__dict__)