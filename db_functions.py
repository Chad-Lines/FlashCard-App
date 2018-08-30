import psycopg2
from psycopg2 import sql
from datetime import datetime

class SQLExec():
    # Setting up the database
    conn = psycopg2.connect("dbname='flashcard' user='chad' host='localhost' password='Passw0rd'")
    global db = conn.cursor()

    # Function to retrieve a list of all deck
    def get_all_decks():
        global db
        return db.execute("SELECT * FROM deck")