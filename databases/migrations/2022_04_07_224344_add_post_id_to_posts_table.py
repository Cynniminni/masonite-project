"""AddPostIdToPostsTable Migration."""

from masoniteorm.migrations import Migration


class AddPostIdToPostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("posts") as table:
            # Drop the posts table
            self.schema.drop("posts")

        with self.schema.create("posts") as table:
            # Recreate the posts table with the post_id as the primary key
            table.increments("post_id").unique().primary()
            table.integer("author_id").unsigned()
            table.foreign("author_id").references("id").on("users")
            table.string("body")
            table.string("friendly_date").nullable()
            table.string("friendly_time").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
