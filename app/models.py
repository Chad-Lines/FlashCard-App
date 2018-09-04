from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):             
    __tablename__ = 'User'                        
    id = db.Column(db.Integer, primary_key=True)                      
    username = db.Column(db.String(64), index=True, nullable=False, unique=True)      
    email = db.Column(db.String(120), index=True, nullable=False, unique=True)         
    password_hash = db.Column(db.String(128))
    decks = db.relationship('Deck')
    cards = db.relationship('Card')
    schema = 'omni'

    def __repr__(self):             
        return 'User: {}'.format(self.username)

    def set_password(self, password):                            
        self.password_hash = generate_password_hash(password)      

    def check_password(self, password):                          
        return check_password_hash(self.password_hash, password)    

class Deck(db.Model):
    __tablename__ = 'Deck'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    description = db.Column(db.String(500))
    owner = db.Column(db.Integer, db.ForeignKey('User.id'))
    # cards = db.relationship('Card')
    schema = 'omni'
    
    def __repr__(self):             
        return 'Deck: {}'.format(self.name)

class Card(db.Model):
    __tablename__ = 'Card'
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(1000), nullable=False)
    back = db.Column(db.String(1000), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('User.id'))
    deck = db.Column(db.Integer, db.ForeignKey('Deck.id'))
    schema = 'omni'

    def __repr__(self):             
        return 'Card: {}'.format(self.front)
