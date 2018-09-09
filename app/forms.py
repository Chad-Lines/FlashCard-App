from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from app.models import User, Card, Deck
from flask_login import current_user

# Existing user login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# New user registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already in use')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already in use')

# Creating a new card
class CardForm(FlaskForm):
    front = TextAreaField('Front', validators=[DataRequired(), Length(min=1, max=500)])
    back = TextAreaField('Back', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Create')

# Creating a new deck
class DeckForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create')

# Edit a card
class CardEdit(FlaskForm):
    front = TextAreaField('Front', validators=[DataRequired(), Length(min=1, max=500)])
    back = TextAreaField('Back', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Save')

# Edit a deck
class DeckEdit(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Save')