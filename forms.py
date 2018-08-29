from flask_wtf import FlaskForm
import wtforms
from app import db

class FlashCard(wtforms.Form):
    front = wtforms.TextAreaField('Front')
    back = wtforms.TextAreaField('Back')
    deck = wtforms.SelectField (
        'Deck',
        choices=()
    ) 
