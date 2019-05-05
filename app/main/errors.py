#coding=utf-8
__author__ = 'Mrsong'

from flask import render_template
from . import main

#错误处理如果是errorhandler修饰则只有蓝本中的错误才能触发处理程序，全局需要app来处理
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
