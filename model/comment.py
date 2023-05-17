from model.user import User


class Comment():
    
    def __init__(self, id: str, body: str, author: User):
        self.comment_id = id
        self.body = body
        self.author = author
        