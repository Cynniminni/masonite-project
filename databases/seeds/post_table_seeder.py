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

        for i in range(10):
            # Refresh time
            current_time = current_date_time.strftime(date_time_format)

            if i % 2:
                author_id = 2  # simple_admin
            else:
                author_id = 1  # admin

            Post.create({
                "author_id": author_id,
                "body": f"This is a seeded post: {i}",
                "friendly_date": current_day,
                "friendly_time": current_time
            })
