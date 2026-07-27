# Zero-To-Ship

A FastAPI-based trade-post and negotiation-offer management system with JWT authentication and JSON file persistence.

## Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.10
- **Auth:** JWT (python-jose) + bcrypt password hashing
- **Validation:** Pydantic v2
- **Persistence:** JSON flat-file (`tradepost_db.json`)

## Project Structure

```
├── main.py                       # Legacy CLI driver
├── app/
│   ├── main.py                   # FastAPI app entry point
│   ├── config.py                 # Settings (SECRET_KEY, expiry, etc.)
│   ├── database.py               # JSON read/write helpers
│   ├── models/                   # Domain models (User, Post, Offer)
│   ├── schemas/                  # Pydantic request/response schemas
│   ├── routers/                  # API route handlers
│   │   ├── auth.py               # Register, login, /me
│   │   ├── posts.py              # CRUD on posts
│   │   └── offers.py             # Offers (if implemented)
│   ├── security/
│   │   └── auth.py               # bcrypt hashing, JWT create/decode
│   └── dependencies/
│       └── auth.py               # get_current_user dependency
├── requirements.txt
├── tradepost_db.json             # JSON database (gitignored)
└── TradePost API.postman_collection.json  # Postman test collection
```

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

API docs available at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Auth
| Method | Path       | Description            |
|--------|------------|------------------------|
| POST   | /register  | Create a new user      |
| POST   | /login     | Login, receive JWT     |
| GET    | /me        | Get current user info  |

### Posts (JWT required)
| Method | Path         | Description              |
|--------|--------------|--------------------------|
| POST   | /posts       | Create a post            |
| GET    | /posts       | List all posts           |
| PUT    | /posts/{id}  | Update own post          |
| DELETE | /posts/{id}  | Delete own post          |

## Auth Flow

1. `POST /register` with `{username, email, password}` (password max 72 bytes)
2. `POST /login` with `{username, password}` → receive JWT
3. Include `Authorization: Bearer <token>` in protected endpoints

Users can only update/delete their own posts (403 otherwise).
