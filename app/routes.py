from flask import render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import FlashCard

@app.route('/')
@app.route('/index')
@login_required
def index():  
    return render_template('index.html')

@app.route('/create')
def create():
    form = FlashCard()
    return render_template('create.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))