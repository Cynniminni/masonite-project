from masonite.controllers import Controller
from masonite.views import View
from masoniteorm.query import QueryBuilder
from masonite.request import Request


class HomeController(Controller):
    def show(self, view: View, request: Request):
        """
        Get all the posts and pass them to the home "/" page.
        """
        controller_method = "HomeController@show"
        print("----------------------")
        print(f"{controller_method}")
        print("----------------------")
        # Get all posts in the database
        builder = QueryBuilder().table("posts")
        builder = builder.join('profiles', 'posts.user_id', '=', 'profiles.user_id')     
        all_posts = builder.table('posts').select(
            'id',
            'profiles.nickname',
            'profiles.handle',            
            'body', 
            'friendly_date', 
            'friendly_time'
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
            'picture',
            'banner'
        ).where(
            'user_id',
            current_user_id
        ).get().first()

        # Create data dictionary to pass to home.html
        data = {
            'posts': all_posts,
            'current_user': current_user
        }

        print(f"Logged in user: {current_user}")
        print(f"Loading posts: {all_posts.count()}")

        # Render the view called posts.html and pass in the posts data
        return view.render("home", data)
