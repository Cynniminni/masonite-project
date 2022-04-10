"""CreateResharesTable Migration."""

from masoniteorm.migrations import Migration


class CreateResharesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("reshares") as table:
            # Primary key
            table.increments("id").unique().primary()
            
            # Foreign key
            table.integer("post_id").unsigned()
            table.foreign("post_id").references("id").on("posts")
            
            # User who reshared
            table.integer("user_reshared_id")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("reshares")
