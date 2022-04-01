"""AddFriendlyTimestampToPost Migration."""

from masoniteorm.migrations import Migration


class AddFriendlyTimestampToPost(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("posts") as table:
            table.string("friendly_date").nullable()
            table.string("friendly_time").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        pass
