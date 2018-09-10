from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    decks = db.relationship('Deck', backref='owner', lazy='dynamic')
    cards = db.relationship('Card', backref='owner', lazy='dynamic')

    def __repr__(self):
        return 'User: {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cards = db.relationship('Card', backref='deck', lazy='dynamic')

    def __repr__(self):
        return 'Deck: {}'.format(self.name) 

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(1000))
    back = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # days_till defines how much time between study dates
    # 0 = .now() (Same day)
    # 1 = .now() + 1 (next day)
    # 2 = .now() + 2 (following day)
    # etc...
    days_till = db.Column(db.Integer) 
    due_date = db.Column(db.DateTime, index=True, default=datetime.utcnow) #When cards are due to study
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'))

    def __repr__(self):
        return 'Card: {}'.format(self.front)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))