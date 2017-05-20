""" Define the views """

# pylint: disable=C0103,C0111,E1101

from flask import render_template, redirect
from flask_login import login_required, login_user, logout_user, current_user
from shallowsandbox_app import app, db
from shallowsandbox_app.models.forms import LoginForm, RegisterForm
from shallowsandbox_app.models.user import User
from werkzeug.security import generate_password_hash


@app.route('/')
@app.route('/index')
def index():
    name = current_user.username if current_user.is_authenticated else ''
    return render_template('index.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect('/')
    return render_template('signup.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
