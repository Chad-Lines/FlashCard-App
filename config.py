

class Configure(object):
    DEBUG = True
    SECRET_KEY = 'Passw0rd'
    SQLALCHEMY_DATABASE_URI = 'postgres://chad:Passw0rd@localhost:5432/flashcard'
    SQLALCHEMY_TRACK_MODIFICATIONS = False