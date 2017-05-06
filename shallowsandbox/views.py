"""
Define the app object, and all the routes
"""

from shallowsandbox import app

@app.route('/')
@app.route('/index')
def home():
    """ The home page """
    return "Hello World!"
