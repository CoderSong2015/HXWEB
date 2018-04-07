__author__ = 'Mrsong'

from flask_script import Manager,Shell
from app import create_app


app = create_app('default')
manager = Manager(app)
#test
def make_shell_context():
    return dict(app = app)

manager.add_command("shell", Shell(make_context=make_shell_context))
if __name__ == '__main__':

    #execute python manage.py with parameters -h 0.0.0.0 -p port
    manager.run()