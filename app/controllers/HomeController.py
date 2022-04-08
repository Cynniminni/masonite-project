from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request
from masonite.routes import Route


class HomeController(Controller):
    def show(self, view: View, request: Request):
        """
        Get all the posts and pass them to the home "/" page.
        """
        # Get all posts
        all_posts = Post.all()
        all_posts = {
            'posts': all_posts
        }

        # Render the view called posts.html and pass in the posts data
        return view.render("home", all_posts)
