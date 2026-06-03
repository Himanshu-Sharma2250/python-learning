class ChaiUtils:
    @staticmethod
    def cleanIngredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = "Water,     Milk      ,  Tea Leaves,     Sugar"

cleaned = ChaiUtils.cleanIngredients(raw)
print(cleaned)