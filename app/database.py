from app.config import settings
from app.storage import json_storage
from app.models.user import User
from app.models.post import TradePost
from app.models.offer import NegotiationOffer

DB_PATH = settings.DATABASE_PATH


def _load_all():
    return json_storage.load_database(DB_PATH)


def _save_all(data):
    json_storage.save_database(DB_PATH, data)


# ── Users ──────────────────────────────────────────
def get_all_users() -> dict[int, User]:
    return json_storage.load_users(DB_PATH)


def save_all_users(users: dict[int, User]):
    json_storage.save_users(DB_PATH, users)


def get_next_user_id() -> int:
    users = get_all_users()
    return max(users.keys(), default=0) + 1


# ── TradePosts ─────────────────────────────────────
def get_all_posts() -> dict[int, TradePost]:
    return json_storage.load_posts(DB_PATH)


def save_all_posts(posts: dict[int, TradePost]):
    json_storage.save_posts(DB_PATH, posts)


def get_next_post_id() -> int:
    posts = get_all_posts()
    return max(posts.keys(), default=0) + 1


# ── NegotiationOffers ──────────────────────────────
def get_all_offers() -> dict[int, NegotiationOffer]:
    return json_storage.load_offers(DB_PATH)


def save_all_offers(offers: dict[int, NegotiationOffer]):
    json_storage.save_offers(DB_PATH, offers)


def get_next_offer_id() -> int:
    offers = get_all_offers()
    return max(offers.keys(), default=0) + 1
