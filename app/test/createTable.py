from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import config

app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)
db = SQLAlchemy(app)

db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username