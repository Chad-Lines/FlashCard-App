# Within the system shell
# ---------------------------------
# Initializing and migrating the database
flask db init
flask db migrate -m "Desc"
flask db upgrade

# Within the Python shell
# ---------------------------------
# Imports
from app import db
from app.models import User

# Creating a user
u = User(username='chad', email='chad.lines1@gmail.com')
db.session.add(u)
db.session.commit()

# Testing that the user exists
User.query.get(1)
