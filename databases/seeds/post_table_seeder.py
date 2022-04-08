"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from app.models.Post import Post
from datetime import datetime


class PostTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
                # Get the current date and time
        current_date_time = datetime.now()        
        date_time_format = "%b %d, %Y"
        current_day = current_date_time.strftime(date_time_format)
        date_time_format = "%I:%M %p"
        current_time = current_date_time.strftime(date_time_format)

        Post.create({
            "author_id": 1,
            "body": "This is a seeded post",
            "friendly_date": current_day,
            "friendly_time": current_time
        })

        Post.create({
            "author_id": 1,
            "body": "This is a seeded post 2",
            "friendly_date": current_day,
            "friendly_time": current_time
        })

        Post.create({
            "author_id": 1,
            "body": "This is a seeded post 3",
            "friendly_date": current_day,
            "friendly_time": current_time
        })

        Post.create({
            "author_id": 1,
            "body": "This is a seeded post 4",
            "friendly_date": current_day,
            "friendly_time": current_time
        })

        Post.create({
            "author_id": 1,
            "body": "This is a seeded post 5",
            "friendly_date": current_day,
            "friendly_time": current_time
        })

        Post.create({
            "author_id": 1,
            "body": "This is a seeded post 6",
            "friendly_date": current_day,
            "friendly_time": current_time
        })