from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app import db
from app.models import User, Deck, Card
from flask_admin import Admin
from flask import redirect, url_for, flash

class AdminPage(Admin):
    
    def is_accessible(self):
        return current_user.ADMIN == 1

    def inaccessible_callback(self, name, **kwargs):
        flash('Access Denied')
        return redirect(url_for('index'))
    