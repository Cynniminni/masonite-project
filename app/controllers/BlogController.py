from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request
from datetime import datetime


class BlogController(Controller):
    def show(self, view: View):
        return view.render("blog")

    def store(self, request: Request):
        """
        Get the user's input from the request object. This is coming from the <form> in blog.html.
        """
        # Get the current date and time
        current_date_time = datetime.now()
        date_time_format = "%b %d, %Y"
        current_day = current_date_time.strftime(date_time_format)
        date_time_format = "%I:%M %p"
        current_time = current_date_time.strftime(date_time_format)

        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            author_id=request.user().id,
            friendly_date=current_day,
            friendly_time=current_time,
        )

        return f"Post Created for @{request.user().handle} at {current_day} {current_time}"
