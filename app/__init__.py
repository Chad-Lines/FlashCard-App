from flask import Flask, session
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
from app.models import User, Deck, Card
from app.model_views import AdminPage
# Adding the admin pages
admin = Admin(app, name="FlashCard Admin", index_view=AdminPage())
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Deck, db.session))
admin.add_view(ModelView(Card, db.session))

