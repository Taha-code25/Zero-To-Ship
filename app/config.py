from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_PATH: str = "tradepost_db.json"
    SECRET_KEY: str = "change-this-to-a-very-long-secret-key-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
