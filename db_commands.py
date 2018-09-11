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
from app.models import User, Deck, Card

# Creating a user
u = User(username='john', email='john@example.com')
db.session.add(u)
db.session.commit()

# Testing that the user exists
User.query.get(1)

# Adding a card to a user
u = User.query.get(1)
c = Card(front='Hello', back='Talofa', owner=u)
db.session.add(c)
db.session.commit()

# Getting all cards belonging to user u
u.cards.all()

# Creating a user with a password
u = User(username='Don', email='don@example.com')
u.set_password('Passw0rd')
db.session.add(u)
db.session.commit()

# Creating a deck 
d = Deck(name='Samoan Language', user_id=u.id) 
 
# Adding a card to a deck 
c = Card.query.get(1) 
c.deck_id = 1

# 9/11: Set an admin user
# Migrate and update db, then:
users = User.query.all()
for u in users:
    u.ADMIN = 0

user[3].ADMIN = 1