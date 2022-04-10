from distutils.command.build import build
from masonite.controllers import Controller
from masonite.views import View
from masoniteorm.query import QueryBuilder


class HomeController(Controller):
    def show(self, view: View):
        """
        Get all the posts and pass them to the home "/" page.
        """
        controller_method = "HomeController@show"
        print("----------------------")
        print(f"{controller_method}")
        print("----------------------")
        # Get all posts in the database
        builder = QueryBuilder().table("posts")
        builder = builder.join('users', 'posts.user_id', '=', 'users.id')
        builder = builder.join('profiles', 'posts.user_id', '=', 'profiles.user_id')     
        all_posts = builder.table('posts').select(
            'profiles.nickname',
            'profiles.handle',            
            'body', 
            'friendly_date', 
            'friendly_time'
        ).order_by(
            "posts.created_at",
            "desc"
        ).get()
        
        all_posts = {
            'posts': all_posts
        }

        print(f"all_posts: {all_posts}")

        # Render the view called posts.html and pass in the posts data
        return view.render("home", all_posts)
