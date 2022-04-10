"""CreateResharesTable Migration."""

from masoniteorm.migrations import Migration


class CreateResharesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("reshares") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("reshares")
