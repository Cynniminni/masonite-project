"""RemovePostsTitle Migration."""

from masoniteorm.migrations import Migration


class RemovePostsTitle(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("posts") as table:
            # Remove title column from the table
            table.drop_column("title")

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("posts") as table:
            pass
