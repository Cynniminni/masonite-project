"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .user_table_seeder import UserTableSeeder
from .post_table_seeder import PostTableSeeder
from .profile_table_seeder import ProfileTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)  # Populate users table
        self.call(ProfileTableSeeder)  # Create profile for each user
        self.call(PostTableSeeder)  # Populate posts table