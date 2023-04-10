from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):

        db_admin = self.db.client.get_database("admin")

        role_name = 'clients-crud-role'

        db_admin.command(
            'grantPrivilegesToRole', role_name,
            privileges=[
                {
                    "resource": {
                        "db": "clients",
                        "collection": "emails"
                    },
                    "actions": [
                        "find",
                        "insert",
                        "remove",
                        "update",
                    ]
                }
            ]
        )

    def downgrade(self):
        db_admin = self.db.client.get_database("admin")

        role_name = 'clients-crud-role'

        db_admin.command(
            'revokePrivilegesFromRole', role_name,
            privileges=[
                {
                    "resource": {
                        "db": "clients",
                        "collection": "emails"
                    },
                    "actions": [
                        "find",
                        "insert",
                        "remove",
                        "update",
                    ]
                }
            ]
        )


# https://www.mongodb.com/docs/manual/reference/method/db.grantPrivilegesToRole/
# https://www.mongodb.com/docs/manual/tutorial/manage-users-and-roles/
