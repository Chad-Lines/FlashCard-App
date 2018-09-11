from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app import db
from app.models import User, Deck, Card
from flask_admin import AdminIndexView
from flask import redirect, url_for, flash

class AdminPage(AdminIndexView):
    
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.ADMIN == 1
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))
    