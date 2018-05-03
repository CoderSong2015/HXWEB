__author__ = 'Mrsong'

from . import main
from .forms import NameForm
from flask import render_template, jsonify,send_from_directory
from  flask_login import login_required
from flask import request
import os
from  common.markdownCMD import convertMDtoHTML
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

@main.route('/api/articleInfo')
def htmltest():
    s = [ { 'name':'test1', 'id':1},{ 'name':'test2', 'id':2}]
    return jsonify(s)


@main.route('/api/article')
def articleInfo():
    articleid = (request.args.get('articleid'))
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\static")  # html是个文件夹
    fileurl = root +  '\\test.md'
    print(fileurl)
    return convertMDtoHTML(fileurl)