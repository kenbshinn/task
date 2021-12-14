from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from flask_sqlalchemy import SQLAlchemy
import os
import re


PG_DB_SERVER = os.environ.get('DB_SERVER')
PG_DATABASE = os.environ.get('DATABASE')
PG_DB_USER = os.environ.get('DB_USER')
PG_DB_PASS = os.environ.get('DB_PASS')
PG_DB_PORT = os.environ.get('DB_PORT')
PG_DB_URI = os.environ.get('DB_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = SECRET_KEY

# Enter your database connection details below
app.config['SQLALCHEMY_DATABASE_URI'] = PG_DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config['PGSQL_USER'] = PG_DB_USER
#app.config['PGSQL_PASSWORD'] = PG_DB_PASS
#app.config['PGSQL_DB'] = PG_DATABASE

# Intialize MySQL
db = SQLAlchemy(app)


# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    return render_template('index.html', msg='')

app.run(debug=True)