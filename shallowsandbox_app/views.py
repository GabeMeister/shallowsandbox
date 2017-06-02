""" Define the views """

# pylint: disable=C0103,C0111,E1101

from datetime import datetime
from flask import render_template, redirect
from flask_login import login_required, login_user, logout_user, current_user
from shallowsandbox_app import app, db
from shallowsandbox_app.models.forms import LoginForm, RegisterForm, NewPostForm
from shallowsandbox_app.models.user import User
from shallowsandbox_app.models.post import Post
from werkzeug.security import generate_password_hash


@app.route('/')
@app.route('/index')
def index():
    name = ''
    posts = []
    if current_user.is_authenticated:
        name = current_user.username
        posts = Post.query.all()
    return render_template('index.html', name=name, posts=posts)


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

@app.route('/newpost', methods=['GET', 'POST'])
@login_required
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        now = datetime.now()
        post = Post(question=form.question.data,\
                    answer=form.answer.data,\
                    creation_date=now,\
                    last_edit_date=now,\
                    user=current_user)
        db.session.add(post)
        db.session.commit()

        test_post = Post.query.filter_by(creation_date=now).first()
        print test_post
        if test_post.answer == post.answer:
            print 'they match!'
        else:
            print 'nope nope nope'

        return redirect('/')
    return render_template('newpost.html', form=form)
