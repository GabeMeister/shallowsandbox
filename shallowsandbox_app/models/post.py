"""
The post model

A question and an answer make a post.
"""

# pylint: disable=C0103,C0111,C0413,E1101

from shallowsandbox_app import db
from shallowsandbox_app.models.user import User
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.BLOB, nullable=False)
    answer = db.Column(db.BLOB, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    last_edit_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = relationship(User)

    def __str__(self):
        strbuf = """
Question: {0}
Answer: {1}
Created: {2}
Last Edited: {3}
User: {4}""".format(self.question,
                    self.answer,
                    self.creation_date,
                    self.last_edit_date,
                    self.user)
        return strbuf
