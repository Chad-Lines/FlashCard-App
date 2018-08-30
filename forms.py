from flask_wtf import FlaskForm
import wtforms
from db_functions import SQLExec

class FlashCard(wtforms.Form):
    front = wtforms.TextAreaField('Front')
    back = wtforms.TextAreaField('Back')
    deck = wtforms.SelectField (
        'Deck',
        choices=()
    ) 

class Deck(wtforms.Form):
    name = wtforms.StringField('Name')
    description = wtforms.TextAreaField('Description')