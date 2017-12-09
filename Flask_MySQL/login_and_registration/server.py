
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = "secret"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/registration', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']
    if len(first_name) < 2 or len(last_name) < 2:
        flash('Invalid Name')
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash('Invalid Email Address')
        return redirect('/')
    elif len(password) < 8:
        flash('Password must be at least 8 characters')
        return redirect('/')
    elif password != confirm:
        flash('Passwords do not match')
        return redirect('/')
    else:
        flash('You are successfully registered')
    pw_hash = bcrypt.generate_password_hash(password)
    query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'pw_hash': pw_hash
    }
    mysql.query_db(query, data)
    return render_template('success.html', user=user[0]['first_name'])


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {
        'email': email
    }
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        flash('You are successfully logged in')
        return render_template('success.html', user=user[0]['first_name'])
    else:
        flash('Incorrect Password')
        return redirect('/')


app.run(debug=True)
