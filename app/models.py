__author__ = 'Mrsong'
from flask_login import UserMixin
from . import login_manager


class User(UserMixin):
    def __init__(self,Id = None):
        self.id = Id
        pass

    id = 0
    username = 'song'
    email = 'xx@qq.com'
    password = 123
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    print(type(user_id),user_id == '2')
    if user_id == '3':
        print('return User')
        return User(3)
    print('login_manager None')
    return None
    #return User.query.get(int(user_id))