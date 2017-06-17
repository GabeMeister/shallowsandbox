""" flask scripts """

# pylint: disable=C0103,C0111,E1101

from flask_script import Manager
from shallowsandbox_app import app, db
from shallowsandbox_app.models.post import Post
from shallowsandbox_app.models.user import User
from shallowsandbox_app.models.homework import Homework
from datetime import datetime

manager = Manager(app)

@manager.command
def select():
    # posts = Post.query.all()
    # for post in posts:
    #     print post.info() + '\n'

    # users = User.query.all()
    # for user in users:
    #     print user.info() + '\n'

    homeworks = Homework.query.all()
    for hw in homeworks:
        print hw.info() + '\n'


@manager.command
def insert():
    user = User.query.first()
    hw = Homework(title='mastering physics day 6')
    now = datetime.now()
    post = Post(question='this is another post',
                answer='yet ANOTHER answer',
                creation_date=now,
                last_edit_date=now,
                user=user,
                homework=hw)
    db.session.add(post)
    db.session.commit()
    print 'Done!'


if __name__ == "__main__":
    manager.run()
