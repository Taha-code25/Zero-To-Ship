from fastapi import FastAPI

from app.routers import auth, posts, offers

app = FastAPI(title="TradePost Negotiation API", version="1.0.0")

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(offers.router)
