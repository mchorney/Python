# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime
import random


def index(request):
    if 'score' not in request.session:
        request.session['score'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'gold/index.html')


def process(request):
    request.session['amount'] = True
    if request.POST['building'] == 'farm':
        earnings = random.randrange(10, 21)
        print earnings
        date = datetime.now().strftime('%Y/%m/%d %I:%M %p')
        request.session['score'] += earnings
        request.session['amount'] = True
        request.session['log'].append(['Earned {} gold from {}! ({})'.format(
            earnings, request.POST['building'], date), True])
    elif request.POST['building'] == 'cave':
        earnings = random.randrange(5, 11)
        print earnings
        date = datetime.now().strftime('%Y/%m/%d %I:%M %p')
        request.session['score'] += earnings
        request.session['amount'] = True
        request.session['log'].append(['Earned {} gold from {}! ({})'.format(
            earnings, request.POST['building'], date), True])
    elif request.POST['building'] == 'house':
        earnings = random.randrange(2, 6)
        print earnings
        date = datetime.now().strftime('%Y/%m/%d %I:%M %p')
        request.session['score'] += earnings
        request.session['amount'] = True
        request.session['log'].append(['Earned {} gold from {}! ({})'.format(
            earnings, request.POST['building'], date), True])
    elif request.POST['building'] == 'casino':
        chance = random.randint(0, 1)
        date = datetime.now().strftime('%Y/%m/%d %I:%M %p')
        if chance == 1:
            earnings = random.randrange(0, 51)
            print earnings
            request.session['score'] += earnings
            request.session['amount'] = True
            request.session['log'].append(['Earned {} gold from {}! ({})'.format(
                earnings, request.POST['building'], date), True])
        elif chance == 0:
            loss = random.randrange(0, 51)
            print loss
            request.session['score'] -= loss
            request.session['amount'] = False
            request.session['log'].append(['Lost {} gold from {}! ({})'.format(
                loss, request.POST['building'], date), False])
    for each in request.session['log']:
        print each
        print each[0]
    return redirect('/')
