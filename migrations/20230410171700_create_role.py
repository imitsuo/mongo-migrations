from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):

        db_admin = self.db.client.get_database("admin")

        role_name = 'clients-crud-role'

        try:
            db_admin.command(
                'createRole', role_name,
                privileges=[
                    {
                        "resource": {
                            "db": "clients",
                            "collection": "domains"
                        },
                        "actions": [
                            "find",
                            "insert",
                            "remove",
                            "update",
                        ]
                    }
                ],
                roles=[]
            )
        except Exception as ex:
            if f'Role "{role_name}@admin" already exists' in str(ex):
                pass

    def downgrade(self):
        pass


# https://www.mongodb.com/docs/manual/reference/method/db.grantPrivilegesToRole/
# https://www.mongodb.com/docs/manual/tutorial/manage-users-and-roles/
