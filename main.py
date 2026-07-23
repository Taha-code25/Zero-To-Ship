from models.post import TradePost
from models.offer import NegotiationOffer

from storage.json_storage import (
    load_posts,
    save_posts,
    load_offers,
    save_offers
)

DATABASE = "tradepost_db.json"

posts = load_posts(DATABASE)

posts[1] = TradePost(
    post_id=1,
    title="Gaming Laptop",
    description="RTX 3060",
    owner_id=15,
    status="Open"
)

posts[2] = TradePost(
    post_id=2,
    title="iPhone 13",
    description="128GB Blue",
    owner_id=7,
    status="Open"
)

save_posts(DATABASE, posts)

posts = load_posts(DATABASE)

print("Posts:")
for post in posts.values():
    print(post.to_dict())


offers = load_offers(DATABASE)

offers[101] = NegotiationOffer(
    offer_id=101,
    post_id=1,              
    proposer_id=20,
    offered_item_details="PlayStation 5 + Controller",
    turn_holder_id=15
)

offers[102] = NegotiationOffer(
    offer_id=102,
    post_id=1,
    proposer_id=25,
    offered_item_details="MacBook Air M1",
    turn_holder_id=15
)

save_offers(DATABASE, offers)

offers = load_offers(DATABASE)

print("\nOffers:")
for offer in offers.values():
    print(offer.to_dict())