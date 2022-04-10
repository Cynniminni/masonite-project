"""CreateRepliesTable Migration."""

from masoniteorm.migrations import Migration


class CreateRepliesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("replies") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("replies")
