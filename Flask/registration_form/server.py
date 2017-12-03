from flask import Flask, render_template, redirect, request, session, flash
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PW_REGEX = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$")
app = Flask(__name__)
app.secret_key = 'ThisIsSecret!'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def submit():
    presentDate = datetime.today()
    inputDate = datetime.strptime(request.form['dateOfBirth'], '%Y-%m-%d')
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm']) < 1:
        flash('All fields are required!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid Email Address!', 'error')
    elif len(request.form['password']) < 8:
        flash(u'Password must be at least 8 characters!', 'error')
    elif request.form['password'] != request.form['confirm']:
        flash(u'Passwords do not match!', error)
    elif not PW_REGEX.match(request.form['password']):
        flash(u'Password must contain 1 uppercase letter and 1 numeric value!', 'error')
    elif not (request.form['first_name']).isalpha():
        flash(u'Name cannot contain numbers!', 'error')
    elif not (request.form['last_name']).isalpha():
        flash(u'Name cannot contain numbers!', 'error')
    elif inputDate > presentDate:
        flash(u'Invalid Date of Birth!', 'error')
    else:
        flash(u'Success!', 'success')
    return redirect('/')


app.run(debug=True)
