from flask import Flask
import psycopg2
from psycopg2 import sql
from datetime import datetime

# Setting up the database
conn = psycopg2.connect("dbname='flashcard' user='chad' host='localhost' password='Passw0rd'")
db = conn.cursor()

# Defining the app
app = Flask(__name__)