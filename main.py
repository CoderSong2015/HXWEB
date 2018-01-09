__author__ = 'Mrsong'

from flask import Flask,render_template,send_from_directory,template_rendered
from flask_bootstrap import Bootstrap
from __init__ import create_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  Required,DataRequired
import os

class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
bootstrap=Bootstrap(app)
build  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build")
@app.route('/')
def index():
    return render_template("index.html")

#带斜线会默认所有的URL都带斜线
@app.route('/hello/')
def hello():
    return render_template('helloworld.html')

@app.route('/form/' , methods=['GET','POST'])
def form():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('form.html', form=form,name=name)

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internalError(e):
    return render_template('500.html'), 505


if __name__=='__main__':
    #app.debug = True
    app.config['SECRET_KEY'] = 'xxx'
    app.run(host='0.0.0.0',port=9999)

    #create_app('xx', app)

