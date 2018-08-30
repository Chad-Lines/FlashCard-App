from flask import Flask
from config import Configure
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Defining the app
app = Flask(__name__)
app.config.from_object(Configure)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# flask db init
# flask db migrate -m "Desc"