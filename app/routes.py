from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.models import User, Deck, Card
from app.forms import LoginForm, RegistrationForm, CardForm, DeckForm
from app import app, db

# INDEX/HOME --------------------------------------
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home') 

# LOGIN --------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # assigning the user from the database
        user = User.query.filter_by(username=form.username.data).first()   
        # check that user exists and password is correct 
        if user is None or not user.check_password(form.password.data):     
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # login the user via the flask_login function
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('user', username=user.username)
        return redirect(next_page)
        #return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# LOGOUT --------------------------------------
@app.route('/logout')
@login_required 
def logout():
    logout_user() # flask_login function
    return redirect(url_for('index')) # redirect to index

# REGISTER --------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # defining the user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        # saving the user to the database and confirming to the user
        db.session.add(user)
        db.session.commit()
        flash('You have been registered with username: {}'.format(user.username))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
 
# USER HOME -------------------------------------- 
@app.route('/user/<username>') 
@login_required 
def user(username): 
    user = User.query.filter_by(username=username).first_or_404() 
    decks = user.decks 
    return render_template('user.html', user=user, decks=decks) 
 

# DECK VIEW -------------------------------------- 
@app.route('/user/<username>/<deck>') 
@login_required 
def deck(username, deck): 
    deck = Deck.query.filter_by(id=deck).first_or_404()
    return render_template('deck.html', deck=deck) 

# CREATE CARD --------------------------------------
@app.route('/<username>/<deck>/create-card', methods=['GET', 'POST'])
@login_required 
def create_card(username, deck):
    form = CardForm()
    if form.validate_on_submit():
        #deck = Deck.query.filter_by(id=deck)
        card = Card(front=form.front.data, back=form.back.data, deck_id=deck.id, user_id=current_user.id)
        db.session.add(card)
        db.session.commit()
        flash('New card created succesfully')
        return redirect(url_for('user', username=current_user.username))
    return render_template('create_card.html', title='New Card', form=form, deck=deck)

# VIEW ALL CARDS --------------------------------------
@app.route('/<username>/<deck>/all-cards', methods=['GET', 'POST'])
@login_required
def view_all_cards(username, deck):
    return render_template('allcards.html', deck=deck)