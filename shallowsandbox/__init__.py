"""
Initialize the application
"""
# pylint: disable=C0103,C0413

from flask import Flask
app = Flask(__name__)

import shallowsandbox.views
