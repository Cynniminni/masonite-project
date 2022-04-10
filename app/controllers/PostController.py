from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request
from masoniteorm.query import QueryBuilder
from datetime import datetime


class PostController(Controller):
    def single(self, view: View, request: Request):
        """
        Display a single post from a user.
        """
        # Get parameters from the request
        user_handle = request.param("handle")
        post_id = request.param("post_id")
        controller_method = "PostController@single"
        print("----------------")
        print(f"{controller_method}")
        print("----------------")
        print(f"user_handle = {user_handle}, post_id: {post_id}")

        # Query posts table to get the post by post_id
        builder = QueryBuilder().table("posts")
        builder = builder.join("users", "posts.author_id", "=", "users.id")
        single_post = builder.table("posts").select(
            "post_id",
            "users.nickname",
            "users.handle",
            "body",
            "friendly_date",
            "friendly_time"
        ).where(
            "users.handle",
            user_handle
        ).where(
            "post_id",
            post_id
        )
        print(f"SQL = {single_post.to_sql()}")

        single_post = single_post.get()
        single_post = {
            "single_post": single_post,
            "post_id": post_id
        }
        print(f"single_post = {single_post}")

        return view.render("single_post", single_post)

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
            body=request.input('body'),
            author_id=request.user().id,
            friendly_date=current_day,
            friendly_time=current_time,
        )

        return f"Post Created for @{request.user().handle} at {current_day} {current_time}"

    def update(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('update', {'post': post})

    def delete(self, request: Request):
        post = Post.find(request.param('id'))
        post.delete()
        return 'post deleted'
