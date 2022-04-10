"""CreateRepliesTable Migration."""

from masoniteorm.migrations import Migration


class CreateRepliesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("replies") as table:
            # Primary key
            table.increments("id").unique().primary()
            
            # Foreign key
            table.integer("comment_id").unsigned()
            table.foreign("comment_id").references("id").on("comments")
            
            # Reply id, if it is a reply to a reply
            table.integer("replied_to_id").nullable()

            # User who replied
            table.integer("user_replied_id").unsigned()
            table.string("user_replied_body")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("replies")
