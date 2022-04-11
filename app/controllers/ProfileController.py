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

        # Check if profile_user is following current_user
        builder = QueryBuilder().table("followings")
        builder = builder.join("users", "followings.user_id", "=", "users.id")
        following_base_query = builder.table("followings").select("*")        
        profile_is_following = following_base_query.where(
            "user_id",
            profile_user["user_id"]
        ).where(
            "following_id",
            current_user["user_id"]
        ).get().first()    
        profile_is_following = True if profile_is_following else False

        # Check if current_user is following profile_user
        current_is_following = following_base_query.where(
            "user_id",
            current_user["user_id"]
        ).where(
            "following_id",
            profile_user["user_id"]
        ).get().first()
        current_is_following = True if current_is_following else False
        print(f"(@{profile_user['handle']} -> @{current_user['handle']}) profile_is_following = {profile_is_following}")
        print(f"(@{current_user['handle']} -> @{profile_user['handle']}) current_is_following = {current_is_following}")
        
        # Get following and follower counts for profile_user
        builder = QueryBuilder().table("followings")
        builder = builder.join('users', "followings.user_id", "=", "users.id")
        following_count = builder.table("followings").select("*").where(
            "user_id",
            profile_user["user_id"]
        ).get().count()
        followers_count = builder.table("followings").select("*").where(
            "following_id",
            profile_user["user_id"]
        ).get().count()
        print(f"@{profile_user['handle']} - {following_count} Following, {followers_count} Followers")

        data = {
            'all_users_post': all_users_posts,
            "profile_user": profile_user,
            "current_user": current_user,
            "profile_is_following": profile_is_following,
            "current_is_following": current_is_following,
            "profile_following_count": following_count,
            "profile_followers_count": followers_count
        }
        return view.render("profile", data)
