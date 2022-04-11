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
        builder = builder.join('profiles', 'posts.user_id', '=', 'profiles.user_id')
        all_users_posts = builder.table('posts').select(
            "id",
            "profiles.nickname",
            "profiles.handle",
            "body",
            "friendly_date",
            "friendly_time"
        ).where(
            "profiles.handle",
            user_handle
        ).order_by(
            "posts.created_at",
            "desc"
        ).get()

        # Get the current user profile info
        current_user_id = request.user().id
        builder = QueryBuilder().table("profiles")
        builder = builder.join("users", "profiles.user_id", "=", "users.id")
        current_user = builder.table("profiles").select(
            'nickname',
            'handle',
            "bio",
            'picture',
            'banner'
        ).where(
            'user_id',
            current_user_id
        ).get().first()

        data = {
            'all_users_post': all_users_posts,
            # 'nickname': nickname.first()['nickname'],
            'handle': user_handle,
            "current_user": current_user
        }
        return view.render("profile", data)
