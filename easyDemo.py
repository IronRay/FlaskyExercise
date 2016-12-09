#!/usr/bin/env python3

from datetime import datetime

from flask import Flask, render_template, url_for
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    age = '27'
    url = url_for('age', age=age, _external=True)
    return render_template('user.html', name=name, url=url)


@app.route('/age/<age>')
def age(age):
    return render_template('age.html', age=age)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
