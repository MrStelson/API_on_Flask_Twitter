from typing import List
from model.comment import Comment
from model.user import User

twits = []

class Twit():
    
    def __init__(self, id: str,body: str, author: User, comments: List[Comment]):
        self.twit_id = id
        self.body = body
        self.author = author
        self.comments = comments
        
    def to_dict(self):
        comments_dict = dict([(comment.comment_id, ({comment.author : comment.body})) for comment in self.comments])
        return {'twit_id': self.twit_id, 'body' : self.body, "author": self.author["username"], "comments": comments_dict}

def get_twit_by_id(id:str):
    for twit in twits:
        if twit.twit_id == id:
            return twit


def get_comment_by_id(comment_id : str, twit: Twit):
    for comment in twit.comments:
        if comment.comment_id == comment_id:
            return comment