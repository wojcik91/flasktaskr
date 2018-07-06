from project import db
from project.models import Task, User
from datetime import date

# create the database and the db table
db.create_all()

# insert dummy data into the table
db.session.add(User('admin', 'admin@admin.com', 'admin', 'admin'))
db.session.add(Task('Finish this tutorial', date(2018, 2, 19), 10,
                    date(2018, 2, 19), 1, 1))
db.session.add(Task('Finish Real Python', date(2018, 3, 30), 10,
                    date(2018, 3, 30), 1, 1))

# commit the changes
db.session.commit()
