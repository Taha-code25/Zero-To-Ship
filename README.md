# Zero-To-Ship

A minimal Python-based trade-post and negotiation-offer management system. Built as a learning project for modeling trade posts, negotiation offers, and JSON file persistence.

## Tech Stack

- **Language:** Python 3.10
- **Persistence:** JSON flat-file (`tradepost_db.json`)
- **Dependencies:** None (standard library only)

## Project Structure

```
├── main.py                   # Entry point / driver script
├── tradepost_db.json         # JSON database (ignored by git)
├── models/
│   ├── post.py               # TradePost class
│   └── offer.py              # NegotiationOffer class
└── storage/
    └── json_storage.py       # JSON read/write helpers
```

## Models

### TradePost (`models/post.py`)
- **Fields:** `post_id`, `title`, `description`, `owner_id`, `status`
- **Methods:** `to_dict()`, `from_dict()`

### NegotiationOffer (`models/offer.py`)
- **Fields:** `offer_id`, `post_id`, `proposer_id`, `offered_item_details`, `turn_holder_id`
- **Methods:** `to_dict()`, `from_dict()`

## Storage

`storage/json_storage.py` provides functions to load/save the entire database or individual collections (posts/offers) to a JSON file.

## Usage

```bash
python main.py
```

The driver loads existing data, creates sample posts and offers, saves them, and prints both collections.

## Status

Early prototype — Phase 1 complete (core models + JSON persistence).