""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class Post(Model):
    """Post Model"""
    __fillable__ = [
        "user_id",
        "body",
        "friendly_date",
        "friendly_time"
    ]

    @belongs_to('user_id', 'id')
    def author(self):
        from app.models.User import User
        return User
