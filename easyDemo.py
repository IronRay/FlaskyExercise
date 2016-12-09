#!/usr/bin/env python3

from datetime import datetime

from flask import Flask, render_template, url_for, redirect, session, flash
from flask_script import Manager
from flask_wtf import Form
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guss string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField("What's your name?", validators=[Required()])
    Submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')

        if (old_name is not None) and (old_name != form.name.data):
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('user', name=session['name']))

    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    # age = '27'
    # url = url_for('age', age=age, _external=True)
    return render_template('user.html', name=name)


# @app.route('/age/<age>')
# def age(age):
#     return render_template('age.html', age=age)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
