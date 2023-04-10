# mongo-migrations

This project use https://github.com/DoubleCiti/mongodb-migrations

# How to use it

1. create a fold named `migrations`
2. create a python file with name in form of `TIMESTAMP_description.py` , i.e.`20160320145400_description.py`, otherwise migration file won't be found.
3. in `20160320145400_description.py` create a class named `Migration` and extends `BaseMigration`
4. implement `upgrade` method
5. use cli `mongodb-migrate` to run migrations
6. `metastore` is an optional parameter of collection name where it stores the previous migrations

**Now there is an easier way to create a migration file, command `mongodb-migrate-create --description <description>` will create an empty migration file in `migrations` folder or the folder provided by `--migrations`.**
