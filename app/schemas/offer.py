from pydantic import BaseModel


class OfferCreate(BaseModel):
    post_id: int
    offered_item_details: str


class OfferOut(BaseModel):
    offer_id: int
    post_id: int
    proposer_id: int
    offered_item_details: str
    turn_holder_id: int

    class Config:
        from_attributes = True
