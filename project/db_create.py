from views import db
from models import Task
from datetime import date

# create the database and the db table
db.create_all()

# insert dummy data into the table
db.session.add(Task('Finish this tutorial', date(2018, 2, 19), 10, 1))
db.session.add(Task('Finish Real Python', date(2018, 3, 30), 10, 1))

# commit the changes
db.session.commit()
