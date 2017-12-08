from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = 'ThisIsSecret!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    flash('The email address you entered is a VALID email address! Thank you!')
    query = "SELECT * from email"
    emails = mysql.query_db(query)
    print emails
    return render_template('success.html', all_emails=emails)


@app.route('/add_email', methods=['POST'])
def add_email():
    if len(request.form['email']) < 1:
        flash('Email cannot be blank!')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        return redirect('/')
    query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/success')


app.run(debug=True)
