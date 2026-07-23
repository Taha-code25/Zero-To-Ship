import json
from models.post import TradePost
from models.offer import NegotiationOffer


import json

def load_database(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "posts": {},
            "offers": {}
        }


def save_database(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_posts(filename):
    database = load_database(filename)

    posts = {}

    for post_id, post_data in database.get("posts", {}).items():
        posts[int(post_id)] = TradePost.from_dict(post_data)

    return posts

def save_posts(filename, posts):
    database = load_database(filename)

    database["posts"] = {
        str(post_id): post.to_dict()
        for post_id, post in posts.items()
    }

    save_database(filename, database)


def load_offers(filename):
    database = load_database(filename)

    offers = {}

    for offer_id, offer_data in database.get("offers", {}).items():
        offers[int(offer_id)] = NegotiationOffer.from_dict(offer_data)

    return offers


def save_offers(filename, offers):
    database = load_database(filename)

    database["offers"] = {
        str(offer_id): offer.to_dict()
        for offer_id, offer in offers.items()
    }

    save_database(filename, database)