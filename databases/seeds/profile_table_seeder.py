"""ProfileTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Profile import Profile


class ProfileTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Profile.create(
            {
                "user_id": "",
                "nickname": "PLACEHOLDER_NICKNAME",
                "handle": "PLACEHOLDER_HANDLE",
                "bio": "PLACEHOLDER_BIO",
                "picture": "/static/pfp_generic_user.png",
                "banner": "/static/banner_leaves.jpg"
            }
        )