#coding=utf-8
__author__ = 'Mrsong'

from flask_script import Manager,Shell
from app import create_app


app = create_app('default')
#manager = Manager(app)


#db.create_all()
print('asd')
#test
def make_shell_context():
    return dict(app = app)

#manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':

    #execute python manage.py with parameters 'runserver -h 0.0.0.0 -p port
    # pycharm: Run->Edit Configurations->parameters'
    #manager.run()
    app.run(host='0.0.0.0', port=12301)
