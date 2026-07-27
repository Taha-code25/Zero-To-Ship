from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, UserOut
from app.models.user import User
from app.dependencies.auth import get_current_user
from app.security.auth import hash_password, verify_password, create_access_token
from app.database import get_all_users, save_all_users, get_next_user_id

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(body: RegisterRequest):
    users = get_all_users()

    if any(u.username == body.username for u in users.values()):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken",
        )
    if any(u.email == body.email for u in users.values()):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    uid = get_next_user_id()
    user = User(
        id=uid,
        username=body.username,
        email=body.email,
        hashed_password=hash_password(body.password),
    )
    users[uid] = user
    save_all_users(users)
    return user


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest):
    users = get_all_users()
    user = next((u for u in users.values() if u.username == body.username), None)

    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token({"sub": user.username})
    return TokenResponse(access_token=token)


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
