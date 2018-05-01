__author__ = 'Mrsong'

from . import main
from .forms import NameForm
from flask import render_template, jsonify
from  flask_login import login_required
#带斜线会默认所有的URL都带斜线

@main.route('/hello/')
@login_required
def hello():
    #return 'login requereifesf'
    return render_template('helloworld.html')

@main.route('/form/' , methods=['GET','POST'])
def form():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('form.html', form=form,name=name)


@main.route('/',defaults = {'path':''})

def index(path):
    return render_template("index.html")


##rest api?

@main.route('/api/random')
def randomNumber():
    response = {
        'randomNumber': 233
    }
    response = jsonify(response)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response