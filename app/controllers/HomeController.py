from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from app.models.User import User
from masonite.request import Request


class HomeController(Controller):
    def show(self, view: View, request: Request):
        """
        Get all the posts and pass them to the home "/" page.
        """
        # Get all posts belonging to the current authenticated user
        all_posts = Post.where('author_id', request.user().id).get()
        all_posts = {
            'posts': all_posts
        }

        # Render the view called posts.html and pass in the posts data
        return view.render("home", all_posts)
