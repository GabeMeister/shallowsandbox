""" Initialize the package """

# pylint: disable=C0103,C0111,C0413,C0412

# The application
from shallowsandbox_app.application import create_app
app = create_app()
app.config.from_pyfile('config.py')


# The database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from shallowsandbox_app.models.post import Post
from shallowsandbox_app.models.user import User
from shallowsandbox_app.models.homework import Homework
from shallowsandbox_app.models.course import Course
from shallowsandbox_app.models.school import School


# The login manager
from flask_login import LoginManager
login_manager = LoginManager()
import shallowsandbox_app.models.login


# The views
from shallowsandbox_app import views
