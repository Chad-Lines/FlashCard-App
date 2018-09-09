from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, flash, redirect, url_for, request, session
from werkzeug.urls import url_parse
from app.models import User, Deck, Card
from app.forms import *
from app import app, db
import urllib

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
@app.route('/user/<username>', methods=['POST', 'GET']) 
@login_required 
def user(username): 
    user = User.query.filter_by(username=username).first_or_404() 
    decks = user.decks 
    form = DeckForm()
    if form.validate_on_submit():
        deck = Deck(name=form.name.data, user_id=current_user.id)
        db.session.add(deck)
        db.session.commit()
        flash('New deck "{}" created successfully'.format(deck.name))
        return redirect(url_for('user', username=current_user.username))
    return render_template('user.html', user=user, decks=decks, form=form) 

# DECK STUDY VIEW -------------------------------------- 
@app.route('/user/<username>/<deck>') 
@login_required 
def deck(username, deck): 
    deck = Deck.query.filter_by(id=deck).first_or_404()
    card_list = []
    for c in deck.cards:
        card_list.append(c)
    return render_template('study.html', deck=deck, card_list=card_list) 

# CREATE CARD --------------------------------------
@app.route('/<username>/<deck>/create-card', methods=['GET', 'POST'])
@login_required 
def create_card(username, deck):
    form = CardForm()    
    deck = Deck.query.filter_by(id=deck).first_or_404()
    if form.validate_on_submit():
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
    deck = Deck.query.filter_by(id=deck).first_or_404()
    return render_template('allcards.html', deck=deck)

# DELETE CARD --------------------------------------
@app.route('/delete-card/<deck_id>/<card_id>', methods=['GET', 'POST'])
@login_required
def delete_card(card_id, deck_id):
    card = Card.query.filter_by(id=card_id).first_or_404()
    card_front = card.front
    db.session.delete(card)
    db.session.commit()
    flash('Card "{}" has been deleted'.format(card_front))
    return redirect(url_for('view_all_cards', username=current_user.username, deck=deck_id))

# DELETE DECK --------------------------------------
@app.route('/delete-deck/<deck_id>', methods=['GET', 'POST'])
@login_required
def delete_deck(deck_id):
    deck = Deck.query.filter_by(id=deck_id).first_or_404()
    name = deck.name
    # Delete all cards in the deck
    for card in deck.cards:
        db.session.delete(card)
    # Delete the deck and commit changes
    db.session.delete(deck)
    db.session.commit()
    flash('Deck "{}", and all associated cards have been deleted'.format(name))
    return redirect(url_for('user', username=current_user.username))

# EDIT CARD --------------------------------------
@app.route('/edit-card/<deck_id>/<card_id>', methods=['GET', 'POST'])
@login_required
def edit_card(card_id, deck_id):
    deck = Deck.query.filter_by(id=deck_id).first_or_404()
    card = Card.query.filter_by(id=card_id).first_or_404()
    form = CardEdit()
    if form.validate_on_submit():
        card.front = form.front.data
        card.back = form.back.data
        db.session.commit()
        return redirect(url_for('deck', username=current_user.username, deck=deck.id))
    return render_template('edit_card.html', card=card, deck=deck, form=form)

# EDIT DECK  --------------------------------------
@app.route('/rename-deck/<deck_id>', methods=['GET', 'POST'])
@login_required
def edit_deck(deck_id):
    deck = Deck.query.filter_by(id=deck_id).first_or_404()
    form = DeckEdit()
    if form.validate_on_submit():
        deck.name = form.name.data
        db.session.commit()
        return redirect(url_for('user', username=current_user.username))
    return render_template('edit_deck.html', deck=deck, form=form)
