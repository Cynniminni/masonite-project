"""CreateFollowingsTable Migration."""

from masoniteorm.migrations import Migration


class CreateFollowingsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("followings") as table:
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")        
            table.integer("following_id")
            table.string("following_handle")
            table.string("following_nickname")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("followings")
