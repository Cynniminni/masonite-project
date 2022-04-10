"""CreateLikesTable Migration."""

from masoniteorm.migrations import Migration


class CreateLikesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("likes") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("likes")
