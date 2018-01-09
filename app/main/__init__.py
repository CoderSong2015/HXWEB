__author__ = 'Mrsong'
from flask import Blueprint
main = Blueprint('main', __name__)

#avoid circle import
from . import views, errors

