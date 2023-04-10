from mongodb_migrations.cli import MigrationManager

if __name__ == '__main__':
    manager = MigrationManager()
    manager.config.config_file = "config.ini"
    manager.config._from_ini()
    manager.run()
