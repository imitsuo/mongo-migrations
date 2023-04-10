from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):

        collection = self.db.get_collection("test_coll")
        collection.insert_one({"abc": 1})

    def downgrade(self):
        self.db.test_collection.update_many(
            {}, {"$unset": {"new_column1": ""}})
