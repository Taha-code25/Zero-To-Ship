import json

from app.models.post import TradePost
from app.models.offer import NegotiationOffer
from app.models.user import User


def load_database(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"posts": {}, "offers": {}, "users": {}}


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
    database["posts"] = {str(k): v.to_dict() for k, v in posts.items()}
    save_database(filename, database)


def load_offers(filename):
    database = load_database(filename)
    offers = {}
    for offer_id, offer_data in database.get("offers", {}).items():
        offers[int(offer_id)] = NegotiationOffer.from_dict(offer_data)
    return offers


def save_offers(filename, offers):
    database = load_database(filename)
    database["offers"] = {str(k): v.to_dict() for k, v in offers.items()}
    save_database(filename, database)


def load_users(filename):
    database = load_database(filename)
    users = {}
    for uid, udata in database.get("users", {}).items():
        users[int(uid)] = User.from_dict(udata)
    return users


def save_users(filename, users):
    database = load_database(filename)
    database["users"] = {str(k): v.to_dict() for k, v in users.items()}
    save_database(filename, database)
