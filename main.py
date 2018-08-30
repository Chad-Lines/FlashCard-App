from flask import render_template, request, url_for
from app import app
from db_functions import SQLExec
from forms import FlashCard

@app.route('/')
def index():
    all_decks = SQLExec.get_all_decks()
    deck_list = []
    for deck in all_decks:
        deck_list.append(deck[1][2])
        
    return render_template('index.html', deck_list=deck_list)

@app.route('/create')
def create():
    form = FlashCard()
    return render_template('create.html', form=form)

# Running the app
if __name__ == '__main__':
    app.run(debug=True)