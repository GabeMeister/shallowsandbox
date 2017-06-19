""" flask scripts """

# pylint: disable=C0103,C0111,E1101,W0401,C0301

import csv
from datetime import datetime, timedelta
from flask_script import Manager
from shallowsandbox_app import app, db
from shallowsandbox_app.models.post import Post
from shallowsandbox_app.models.user import User
from shallowsandbox_app.models.course import Course
from shallowsandbox_app.models.school import School
from shallowsandbox_app.models.homework import Homework

manager = Manager(app)


@manager.command
def select():
    # posts = Post.query.all()
    # for post in posts:
    #     print post.info() + '\n'

    users = User.query.all()
    for user in users:
        print user.info() + '\n'

    # homeworks = Homework.query.all()
    # for hw in homeworks:
    #     print hw.info() + '\n'

    # courses = Course.query.all()
    # for course in courses:
    #     print course.info() + '\n'

    # schools = School.query.all()
    # for school in schools:
    #     print school.info() + '\n'


@manager.command
def insert():
    college_file_path = '/home/gabe/dev/python/college-generator/college-generator/Accreditation_04_2017.csv'

    colleges = set()
    with open(college_file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            colleges.add(row[1])

    for college_name in colleges:
        new_school = School(full_name=college_name)
        db.session.add(new_school)

    db.session.commit()

    print 'Done!'


@manager.command
def insert_course():
    hw = db.session.query(Homework).order_by(Homework.id.desc()).first()
    school = School.query.first()
    new_course = Course(subject='PHYS',
                        number=112,
                        professor_name='John Williams',
                        course_times='MWF 10:10-11am',
                        school=school)
    new_course.homeworks.append(hw)
    db.session.add(new_course)
    db.session.commit()
    print 'Done!'




if __name__ == "__main__":
    manager.run()
