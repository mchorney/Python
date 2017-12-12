# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    if 'submissions' not in request.session:
        request.session['submissions'] = 0
    return render(request, 'surveys/index.html')


def submit(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')


def result(request):
    request.session['submissions'] += 1
    messages.success(request, 'Thanks for submitting this form! You have submiited this form {} times now.'.format(
        request.session['submissions']))
    return render(request, 'surveys/result.html')
