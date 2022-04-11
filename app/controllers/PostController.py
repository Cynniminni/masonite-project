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
        # Get the single post using handle and post id
        builder = QueryBuilder().table("posts")
        builder = builder.join("profiles", "posts.user_id", "=", "profiles.user_id")
        single_post = builder.table("posts").select(
            "posts.id",
            "profiles.nickname",
            "profiles.handle",
            "body",
            "friendly_date",
            "friendly_time"
        ).where(
            "profiles.handle",
            user_handle
        ).where(
            "posts.id",
            post_id
        ).get().first()

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

        data = {
            "single_post": single_post,
            "current_user": current_user
        }
        print(f"Currently logged in as @{current_user['handle']}")
        print(f"Retrieving single post from @{user_handle} - Post id: {post_id}")
        return view.render("single_post", data)

    def store(self, view: View, request: Request):
        """
        Get the user's input from the request object. This is coming from the <form> in blog.html.
        """
        # TODO: Verify request user is authenticated

        # Get the current date and time
        current_date_time = datetime.now()
        date_time_format = "%b %d, %Y"
        current_day = current_date_time.strftime(date_time_format)
        date_time_format = "%I:%M %p"
        current_time = current_date_time.strftime(date_time_format)

        # Create the post
        Post.create(
            body=request.input('body'),
            author_id=request.user().id,
            friendly_date=current_day,
            friendly_time=current_time,
        )

        # Get all posts in the database
        builder = QueryBuilder().table("posts")
        builder = builder.join('users', 'posts.author_id', '=', 'users.id')
        all_posts = builder.table('posts').select(
            'post_id',
            'users.nickname',
            'users.handle',
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

        # TODO: Redirect to home page if creating post is successful
        return view.render("home", all_posts)

    def update(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('update', {'post': post})

    def delete(self, request: Request):
        """
        Delete a single post
        """
        post = Post.find(request.param('id'))
        post.delete()
        return 'post deleted'
