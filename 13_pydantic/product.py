from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

prod_one = Product(id=1, name="Laptop", price=50000, in_stock=True)
prod_two = Product(id=2, name="Pen Drive", price=2000, in_stock=False)
# prod_three = Product(id=3, name="Mouse") # error

print("Product one : ", prod_one)
print("Product two : ", prod_two)
# print("Product three : ", prod_three)