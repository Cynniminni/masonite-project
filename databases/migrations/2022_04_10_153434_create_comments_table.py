"""CreateCommentsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("comments") as table:
            # Primary key
            table.increments("id").unique().primary()

            # Foreign key
            table.integer("post_id").unsigned()
            table.foreign("post_id").references("id").on("posts")

            # User who commented
            table.integer("user_id").unsigned()
            table.string("body")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("comments")
