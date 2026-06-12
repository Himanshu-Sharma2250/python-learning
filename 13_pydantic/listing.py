from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    image_url: Optional[str] = None

cart = Cart(id=1, items=["apple"], quantities={"apple": 2})
print("cart : ", cart)

blog_one = BlogPost(id=1, title="Pydantic and How it works", content="Pydantic is used to type safety and validation")
blog_two = BlogPost(id=1, title="Pydantic and How it works", content="Pydantic is used to type safety and validation", image_url="https://image.com/png")

print("Blog one :", blog_one)
print("Blog two :", blog_two)