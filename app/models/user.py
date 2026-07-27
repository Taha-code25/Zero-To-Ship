from datetime import datetime, timezone


class User:
    def __init__(self, id, username, email, hashed_password, created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "hashed_password": self.hashed_password,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            username=data["username"],
            email=data["email"],
            hashed_password=data["hashed_password"],
            created_at=data.get("created_at"),
        )
