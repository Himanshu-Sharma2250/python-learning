from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(
    id=1,
    content="first comment",
    replies=[
        Comment( id=2, content="first reply" ),
        Comment( id=3, content="second reply", replies=[
                Comment( id=4, content="first reply of second reply" )
            ]
        ),
    ]
)

print(comment)