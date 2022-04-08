""" User Model """

from masoniteorm.models import Model


class Following(Model):
    """Following Model"""
    __fillable__ = [
        "user_id",
        "following_id",
        "following_handle",
        "following_nickname"
    ]

    @belongs_to('user_id', 'id')
    def author(self):
        from app.models.User import User
        return User
