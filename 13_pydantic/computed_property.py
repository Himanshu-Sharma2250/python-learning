from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field( ..., ge=1 )
    rate_per_night: float

    @computed_field # used to compute the values using the values of class 
    @property
    def total_bill(self) -> float:
        return self.rate_per_night * self.nights
    
hotel_book = Booking(user_id=1, room_id=4, nights=4, rate_per_night=1000.00)
print("hotel ", hotel_book.total_bill) # gives the total bill
print(hotel_book.model_dump())
print(hotel_book)