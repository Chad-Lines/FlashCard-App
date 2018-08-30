from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db
from app import login

class User(UserMixin, db.Model):                                     
    id = db.Column(db.Integer, primary_key=True)                      
    username = db.Column(db.String(64), index=True, nullable=False, unique=True)      
    email = db.Column(db.String(120), index=True, nullable=False, unique=True)         
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
    name = db.Column(db.String(100), index=True, nullable=False)
    description = db.Column(db.String(500))
    cards = db.relationship('Card', backref='deck', lazy='dynamic')
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):             
        return 'Deck: {}'.format(self.name)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(1000), nullable=False)
    back = db.Column(db.String(1000), nullable=False)
    owner = db.Column(db.Integer, ForeignKey('user.id'))

    def __repr__(self):             
        return 'Card: {}'.format(self.front)