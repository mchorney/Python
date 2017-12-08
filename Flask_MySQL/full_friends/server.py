from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')
app.secret_key = 'ItIsSecret'


@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html', all_friends=friends)


@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {
        'specific_id': id
    }
    friend = mysql.query_db(query, data)
    print friend
    return render_template('edit.html', one_friend=friend[0])


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)