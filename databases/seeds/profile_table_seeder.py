"""ProfileTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Profile import Profile


class ProfileTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        # Profile for Admin
        Profile.create(
            {
                "user_id": 1,
                "nickname": "Masonite Admin",
                "handle": "admin",
                "bio": "The admin for this Masonite project, who calls the shots here.",
                "picture": "/static/pfp_generic_user.png",
                "banner": "/static/banner_leaves.jpg"
            }
        )

        # Profile for cynniminni
        Profile.create(
            {
                "user_id": 2,
                "nickname": "Cynniminni <3",
                "handle": "cynniminni",
                "bio": "An example user, using my own social media as an example.",
                "picture": "/static/pfp_generic_user.png",
                "banner": "/static/banner_leaves.jpg"
            }
        )