class TradePost:
    def __init__(self, post_id, title, description, owner_id, status):
        self.post_id = post_id
        self.title = title
        self.description = description
        self.owner_id = owner_id
        self.status = status

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'title': self.title,
            'description': self.description,
            'owner_id': self.owner_id,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            post_id=data.get('post_id'),
            title=data.get('title'),
            description=data.get('description'),
            owner_id=data.get('owner_id'),
            status=data.get('status')
        )
