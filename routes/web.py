from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    # Home page - Redirect to login page if user isn't logged in
    Route.get("/", "HomeController@show").middleware('auth').name("home"),

    # User Profile - Show all posts from the given user handle in desc created_at order
    Route.get("/@handle", "ProfileController@show"),

    # Show a page with a form to create a single post
    Route.get("/blog", "BlogController@show"),

    # Create a post
    Route.post("/blog/create", "BlogController@store"),

    # Show all posts
    Route.get("/posts", "PostController@show"),

    # Show a single post
    Route.get("/post/@id", "PostController@single"),

    # Show a page with a form to update a single post
    Route.get('post/@id/update', 'PostController@update'),

    # Update and save a post in the db
    Route.post('post/@id/update', 'PostController@store'),

    # Delete a post
    Route.get('post/@id/delete', 'PostController@delete')
]

ROUTES += Auth.routes()
