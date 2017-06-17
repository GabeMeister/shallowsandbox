""" The homework model """

# pylint: disable=C0103,C0111,C0413,E1101

from shallowsandbox_app import db
from sqlalchemy.orm import relationship

class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    posts = relationship('Post', back_populates='homework')


    def __str__(self):
        return self.title


    def info(self):
        buf = self.title
        buf += 'Posts:\n'
        for post in self.posts:
            buf += str(post)

        return buf
