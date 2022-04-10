"""CreateLikesTable Migration."""

from masoniteorm.migrations import Migration


class CreateLikesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("likes") as table:
            # Primary key
            table.increments("id").unique().primary()

            # Foreign key - post_id from posts table
            table.integer("post_id").unsigned()
            table.foreign("post_id").references("id").on("posts")

            # Id of user that liked the post - id from users table
            table.integer("user_liked_id").unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("likes")
