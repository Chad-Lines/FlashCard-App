from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    decks = db.relationship('Deck', backref='owner', lazy='dynamic')
    cards = db.relationship('Card', backref='owner', lazy='dynamic')

    def __repr__(self):
        return 'User: {}'.format(self.username)

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cards = db.relationship('Card', backref='deck', lazy='dynamic')

    def __repr__(self):
        return 'Card: {}'.format(self.front)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(1000))
    back = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'))

    def __repr__(self):
        return 'Card: {}'.format(self.front)