__author__ = 'Mrsong'
from flask_login import UserMixin
from . import login_manager
class User(UserMixin):
    username = 'xx'
    role_id = 3
    password = 10

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))