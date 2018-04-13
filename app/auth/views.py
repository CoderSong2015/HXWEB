__author__ = 'Mrsong'

from . import auth
from flask import render_template, redirect,flash,request,url_for
from .forms import LoginForm
from flask_login import login_user,logout_user
from ..models import User
@auth.route('/login/' , methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        #get user info from database
        user = User(3)
        if user is not None :     # and verify password
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            # next_is_valid should check if the user has valid
            # permission to access the `next` url
            ##if not next_is_valid(next):
            ##    return flask.abort(400)

            return redirect(next or url_for('main.index'))
        flash('invalid user name or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout/' , methods=['GET','POST'])
def logout():
    logout_user()
    flash('Log out!')
    return redirect(url_for('main.index'))