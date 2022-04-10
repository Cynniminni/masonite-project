"""CreateProfilesTable Migration."""

from masoniteorm.migrations import Migration


class CreateProfilesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("profiles") as table:
            table.increments("id")
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")

            table.string("nickname")
            table.string("handle").unique()
            table.string("bio")  # description
            table.string("picture")  # profile picture
            table.string("banner")  # profile banner
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("profiles")
