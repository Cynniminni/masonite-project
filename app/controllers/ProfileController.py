from masonite.request import Request
from masonite.controllers import Controller
from masonite.views import View
from masoniteorm.query import QueryBuilder


class ProfileController(Controller):
    def show(self, view: View, request: Request):
        """
        Display the profile page of the given user handle, and list their posts in descending order by posts.created_at.
        """
        controller_method = "ProfileController@show"
        print("----------------")
        print(f"{controller_method}")
        print("----------------")
        # Get handle of the user
        user_handle = request.param("handle")
        print(f"user_handle = {user_handle}")

        # Get all posts belonging to the current authenticated user
        builder = QueryBuilder().table("posts")
        builder = builder.join('users', 'posts.author_id', '=', 'users.id')
        all_users_posts = builder.table('posts').select(
            "users.nickname",
            "users.handle",
            "body",
            "friendly_date",
            "friendly_time"
        ).where(
            "users.handle",
            user_handle
        ).order_by(
            "posts.created_at",
            "desc"
        ).get()

        # Get given users's nickname
        builder = QueryBuilder().table("users")
        nickname = builder.table("users").select(
            "nickname"
        ).where(
            "users.handle",
            user_handle
        ).get()

        all_users_posts = {
            'all_users_post': all_users_posts,
            'nickname': nickname.first()['nickname'],
            'handle': user_handle
        }
        return view.render("profile", all_users_posts)
