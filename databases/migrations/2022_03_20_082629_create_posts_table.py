"""CreatePostsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.increments("id").unique()
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")
            table.string("body")
            table.string("friendly_date")
            table.string("friendly_time")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
