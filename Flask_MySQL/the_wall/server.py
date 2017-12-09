from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'the_wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = 'secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']
    if not EMAIL_REGEX.match(email):
        flash('Invalid Email Address')
    elif len(password) < 8:
        flash('Password must be at least 8 characters')
    elif password != confirm:
        flash('Passwords do not match')
    else:
        flash('You are successfully registered. You may now login.')
        pw_hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'pw_hash': pw_hash
        }
        mysql.query_db(query, data)
    return redirect('/')


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
        session['id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        session['last_name'] = user[0]['last_name']
        return redirect('/the_wall')
    else:
        flash('Incorrect Password')
        return redirect('/')


@app.route('/the_wall')
def the_wall():
    msg_query = "SELECT CONCAT(users.first_name, ' ', users.last_name) as author, DATE_FORMAT(messages.created_at, '%M %d, %Y, %h:%i %p') as time_created, messages.id, messages.message FROM messages LEFT JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC"
    all_msgs = mysql.query_db(msg_query)

    comment_query = ("SELECT comments.id, comments.message_id, comments.comment, DATE_FORMAT(comments.created_at, '%M %d, %Y, %h:%i %p') as time_created, CONCAT(users.first_name, ' ', users.last_name) as commenter FROM comments "
                     "JOIN users ON comments.user_id = users.id "
                     "ORDER BY comments.created_at ASC")
    all_comments = mysql.query_db(comment_query)
    return render_template('the_wall.html', all_msgs=all_msgs, all_comments=all_comments)


@app.route('/postmessage', methods=['POST'])
def post_message():
    message = request.form['message']
    user_id = session['id']
    post_msg_query = "INSERT INTO messages (user_id, message, created_at) VALUES (:user_id, :message, NOW())"
    data = {
        'message': message,
        'user_id': user_id
    }
    mysql.query_db(post_msg_query, data)
    return redirect('/the_wall')


@app.route('/postcomment', methods=['POST'])
def post_comment():
    comment = request.form['comment']
    user_id = session['id']
    message_id = request.form['message_id']
    post_comment_query = "INSERT INTO comments (message_id, user_id, comment, created_at) VALUES (:message_id, :user_id, :comment, NOW())"
    data = {
        'message_id': message_id,
        'user_id': user_id,
        'comment': comment
    }
    mysql.query_db(post_comment_query, data)
    return redirect('/the_wall')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
