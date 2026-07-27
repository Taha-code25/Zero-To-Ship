from pydantic import BaseModel, field_validator


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

    @field_validator("password")
    @classmethod
    def password_not_too_long(cls, v: str) -> str:
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password must not exceed 72 bytes")
        return v


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    created_at: str

    class Config:
        from_attributes = True
