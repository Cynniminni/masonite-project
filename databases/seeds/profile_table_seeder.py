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
                "nickname": "PLACEHOLDER_NICKNAME",
                "handle": "admin",
                "bio": "PLACEHOLDER_BIO",
                "picture": "/static/pfp_generic_user.png",
                "banner": "/static/banner_leaves.jpg"
            }
        )

        # Profile for cynniminni
        Profile.create(
            {
                "user_id": 2,
                "nickname": "PLACEHOLDER_NICKNAME",
                "handle": "cynniminni",
                "bio": "PLACEHOLDER_BIO",
                "picture": "/static/pfp_generic_user.png",
                "banner": "/static/banner_leaves.jpg"
            }
        )