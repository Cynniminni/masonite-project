from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request


class BlogController(Controller):
    def show(self, view: View):
        return view.render("blog")

    def store(self, request: Request):
        """
        Get the user's input from the request object. This is coming from the <form> in blog.html.
        """
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            author_id=request.user().id
        )

        return 'post created'
