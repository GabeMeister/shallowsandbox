""" The user model """

# pylint: disable=C0103,C0111,C0413,E1101

from shallowsandbox_app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))
