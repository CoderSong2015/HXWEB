__author__ = 'Mrsong'

from flask_script import Manager,Shell
from app import create_app
from app.models import User
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
app = create_app('default')
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)

db.create_all()
print('asd')
#test
def make_shell_context():
    return dict(app = app, db=db,User = User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':

    #execute python manage.py with parameters 'runserver -h 0.0.0.0 -p port'
    manager.run()