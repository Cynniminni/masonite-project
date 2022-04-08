from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request
from masoniteorm.query import QueryBuilder
import logging


class PostController(Controller):
    def single(self, view: View, request: Request):
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

    # def single(self, view: View, request: Request):
    #     post = Post.find(request.param('id'))
    #
    #     # Render the view called single.html and pass in the post data
    #     return view.render("single", {"post": post})

    def update(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('update', {'post': post})

    def store(self, request: Request):
        post = Post.find(request.param('id'))
        post.title = request.input('title')
        post.body = request.input('body')
        post.save()
        return 'post updated'

    def delete(self, request: Request):
        post = Post.find(request.param('id'))
        post.delete()
        return 'post deleted'
