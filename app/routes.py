from flask import render_template, request, url_for
from app import app
from app.forms import FlashCard

@app.route('/')
def index():       
    
    return render_template('index.html')

@app.route('/create')
def create():
    form = FlashCard()
    return render_template('create.html', form=form)

