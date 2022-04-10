""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

class Profile(Model):
    """Profile Model"""
    __fillable__ = [
        "user_id",
        "nickname",
        "handle",
        "bio",
        "picture",
        "banner"
    ]

    @belongs_to('user_id', 'id')
    def author(self):
        from app.models.User import User
        return User
