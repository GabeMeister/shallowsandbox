"""
Define the app object, and all the routes
"""

from flask import render_template
from shallowsandbox import app

@app.route('/')
@app.route('/index')
def index():
    """ The index page """
    user = {'nickname': 'Gabe'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'I like lighting things on fire.'
        },
        {
            'author': {'nickname': 'Bob'},
            'body': 'Jim Gaffigan is my spirit animal.'
        },
        {
            'author': {'nickname': 'Freddy'},
            'body': 'I can eat an entire cow.'
        }
    ]

    return render_template('index.html', user=user, posts=posts)

@app.route('/about')
def about():
    """ The about page """
    return render_template('about.html')
