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

        # Get all posts belonging to the given user handle
        builder = QueryBuilder().table("posts")
        builder = builder.join('profiles', 'posts.user_id', '=', 'profiles.user_id')
        all_users_posts = builder.table('posts').select(
            "id",
            "profiles.nickname",
            "profiles.handle",
            "profiles.picture",
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
            '*'
        ).where(
            'user_id',
            current_user_id
        ).get().first()

        # Get profile of given user handle
        builder = QueryBuilder().table("profiles")
        profile_user = builder.table("profiles").select(
            "*"
        ).where(
            "handle",
            user_handle
        ).get().first()
        print(f"Accessing profile of @{user_handle}")
        print(profile_user)

        data = {
            'all_users_post': all_users_posts,
            "profile_user": profile_user,
            "current_user": current_user
        }
        return view.render("profile", data)
