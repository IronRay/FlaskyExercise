#!/usr/bin/env python3

from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
Manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    Manager.run()
