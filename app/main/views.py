__author__ = 'Mrsong'

from . import main
from .forms import NameForm
from flask import render_template

#带斜线会默认所有的URL都带斜线
@main.route('/hello/')
def hello():
    return render_template('helloworld.html')

@main.route('/form/' , methods=['GET','POST'])
def form():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('form.html', form=form,name=name)

@main.route('/')
def index():
    return render_template("index.html")