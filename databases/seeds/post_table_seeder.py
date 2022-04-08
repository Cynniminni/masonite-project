"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash

from app.models.Post import Post


class PostTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Post.create({
            "author_id": 1,
            "body": "This is a seeded post",
            "friendly_date": "Apr 7, 2022",
            "friendly_time": "8:20PM"
        })
