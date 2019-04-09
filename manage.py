"""Module to handle application migrations."""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import app

from api.common.models import db


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
