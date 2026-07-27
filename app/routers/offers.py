from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.offer import OfferCreate, OfferOut
from app.models.offer import NegotiationOffer
from app.models.user import User
from app.dependencies.auth import get_current_user
from app.database import get_all_offers, save_all_offers, get_next_offer_id, get_all_posts

router = APIRouter(prefix="/offers", tags=["offers"])


@router.get("", response_model=List[OfferOut])
def list_offers():
    offers = get_all_offers()
    return list(offers.values())


@router.post("", response_model=OfferOut, status_code=status.HTTP_201_CREATED)
def create_offer(body: OfferCreate, current_user: User = Depends(get_current_user)):
    posts = get_all_posts()
    post = posts.get(body.post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    offers = get_all_offers()
    oid = get_next_offer_id()
    offer = NegotiationOffer(
        offer_id=oid,
        post_id=body.post_id,
        proposer_id=current_user.id,
        offered_item_details=body.offered_item_details,
        turn_holder_id=post.owner_id,
    )
    offers[oid] = offer
    save_all_offers(offers)
    return offer
