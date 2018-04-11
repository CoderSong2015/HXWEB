__author__ = 'Mrsong'

from . import auth
from flask import render_template
from .forms import LoginForm


@auth.route('/login/' , methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
    return render_template('auth/login.html', form=form)

