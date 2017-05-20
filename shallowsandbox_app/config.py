"""Configuration details for the app"""

# pylint: disable=C0103,C0111

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'waffles steak flash drive'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'shallowsandbox.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
