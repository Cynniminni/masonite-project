from masonite.request import Request
from masonite.controllers import Controller
from masonite.views import View
from masoniteorm.query import QueryBuilder
from masonite.authentication import Auth


class ProfileController(Controller):
    def show(self, view: View, auth: Auth):
        """
        Display the profile page of the current authenticated user, and list their posts in descending order by posts.created_at.
        """
        # Get id of current authenticated user
        current_user_id = auth.user().id

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
            "posts.author_id",
            current_user_id
        ).order_by(
            "posts.created_at",
            "desc"
        ).get()
        all_users_posts = {
            'all_users_post': all_users_posts
        }
        return view.render("profile", all_users_posts)
    
    def show_other_user_profile(self, view: View, request: Request):
        """
        Display the profile page of another user based on the handle passed in the url, and list their posts in descending order by posts.created_at.
        """
        # Get user handle value from url
        user_handle = request.param("handle")
        
        # Get all posts belonging to the user handle
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
        all_users_posts = {
            'all_users_post': all_users_posts
        }
        return view.render("profile", all_users_posts)
