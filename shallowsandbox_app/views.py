""" Define the views """

# pylint: disable=C0103,C0111,E1101

from datetime import datetime
from flask import render_template, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from shallowsandbox_app import app, db
from shallowsandbox_app.models.forms import LoginForm, RegisterForm, NewPostForm, EditPostForm
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

        return redirect('/')
    return render_template('newpost.html', form=form)

@app.route('/editpost/<post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    if not post_id.isdigit():
        # Redirect to home page if garbage input
        return redirect('/')

    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        # Redirect to home page if we didn't find the correct post
        return redirect('/')

    form = EditPostForm()

    # Check if user is initially loading the form
    if request.method == 'GET':
        form.question.data = post.question
        form.answer.data = post.answer

    if form.validate_on_submit():
        form.populate_obj(post)

        # Don't need db.session.add() here because post was already added
        db.session.commit()
        return redirect('/')

    return render_template('editpost.html', form=form, post=post)


@app.route('/deletepost')
@login_required
def delete_post():
    return redirect('/')
