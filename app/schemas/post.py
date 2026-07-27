from pydantic import BaseModel
from typing import Optional


class PostCreate(BaseModel):
    title: str
    description: str
    status: Optional[str] = "Open"


class PostUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class PostOut(BaseModel):
    post_id: int
    title: str
    description: str
    owner_id: int
    status: str

    class Config:
        from_attributes = True
