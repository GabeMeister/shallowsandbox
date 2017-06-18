""" The course model """

# pylint: disable=C0103,C0111,C0413,E1101

from shallowsandbox_app import db
from sqlalchemy.orm import relationship


class Course(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    subject = db.Column('subject', db.String(100), nullable=False)
    number = db.Column('number', db.Integer, nullable=False)
    professor_name = db.Column('professor_name', db.String(200), nullable=False)
    course_times = db.Column('course_times', db.String(100), nullable=False)
    homeworks = relationship('Homework', back_populates='course')


    def __str__(self):
        return '{0} {1} on {2}-- {3}'.format(self.subject,
                                             self.number,
                                             self.professor_name,
                                             self.course_times)


    def info(self):
        buf = self.__str__()
        buf += 'Posts:\n'
        for post in self.posts:
            buf += str(post)

        return buf
