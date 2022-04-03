"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash

from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            {
                "name": "Admin",
                "email": "radicalcyn@gmail.com",
                "password": Hash.make("MasoniteAdmin2022!!"),
                "nickname": "Masonite Admin",
                "handle": "admin"
            }
        )