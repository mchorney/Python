from flask import Flask, render_template, request, redirect, session
import random
import time
app = Flask(__name__)
app.secret_key = 'ninja'


@app.route('/')
def index():
    try:
        session['score'] = session['score']
    except KeyError:
        session['score'] = 0
    try:
        session['log'] != session['log']
    except KeyError:
        session['log'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process():
    session['amount'] = True
    if request.form['building'] == 'farm':
        earnings = random.randrange(10, 21)
        print earnings
        date = time.strftime('%Y/%m/%d %I:%M %p')
        session['score'] += earnings
        session['amount'] = True
        session['log'].append(['Earned {} gold from {}! ({})'.format(
            earnings, request.form['building'], date), True])
    elif request.form['building'] == 'cave':
        earnings = random.randrange(5, 11)
        print earnings
        date = time.strftime('%Y/%m/%d %I:%M %p')
        session['score'] += earnings
        session['amount'] = True
        session['log'].append(['Earned {} gold from {}! ({})'.format(
            earnings, request.form['building'], date), True])
    elif request.form['building'] == 'house':
        earnings = random.randrange(2, 6)
        print earnings
        date = time.strftime('%Y/%m/%d %I:%M %p')
        session['score'] += earnings
        session['amount'] = True
        session['log'].append(['Earned {} gold from {}! ({})'.format(
            earnings, request.form['building'], date), True])
    elif request.form['building'] == 'casino':
        chance = random.randint(0, 1)
        date = time.strftime('%Y/%m/%d %I:%M %p')
        if chance == 1:
            earnings = random.randrange(0, 51)
            print earnings
            session['score'] += earnings
            session['amount'] = True
            session['log'].append(['Earned {} gold from {}! ({})'.format(
                earnings, request.form['building'], date), True])
        elif chance == 0:
            loss = random.randrange(0, 51)
            print loss
            session['score'] -= loss
            session['amount'] = False
            session['log'].append(['Lost {} gold from {}! ({})'.format(
                loss, request.form['building'], date), False])
    for each in session['log']:
        print each
        print each[0]
    return redirect('/')


app.run(debug=True)
