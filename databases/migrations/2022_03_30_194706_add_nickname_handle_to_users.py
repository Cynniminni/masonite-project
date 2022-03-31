"""AddNicknameHandleToUsers Migration."""

from masoniteorm.migrations import Migration


class AddNicknameHandleToUsers(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.string("nickname").nullable()
            table.string("handle").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        pass
