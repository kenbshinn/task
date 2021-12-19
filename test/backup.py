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
app.secret_key = 'k37gF6kw4KQ9QsZjIuQrQw'

# Enter your database connection details below
app.config['SQLALCHEMY_DATABASE_URI'] = PG_DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config['PGSQL_USER'] = PG_DB_USER
#app.config['PGSQL_PASSWORD'] = PG_DB_PASS
#app.config['PGSQL_DB'] = PG_DATABASE

conn = psycopg2.connect(
    database=PG_DATABASE, user=PG_DB_USER, password=PG_DB_PASS, host=PG_DB_SERVER, port=PG_DB_PORT
) 

# Intialize MySQL
db = SQLAlchemy(app)

# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        #cursor = db.connection.cursor(db.cursors.DictCursor)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
    return render_template('index.html', msg='')

app.run(debug=True)