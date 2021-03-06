# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    logged_in_user = get_logged_in_user(request)
    context = {
        'logged_in': logged_in(request)
    }
    return render(request, 'users/index.html', context)


def login_action(request):
    if len(request.POST['password']) < 1 or len(request.POST['email']) < 1:
        return login_fail(request)

    try:
        user_to_check = User.objects.get(email=request.POST['email'])
    except User.DoesNotExist:
        return login_fail(request)

    password = request.POST['password'].encode("utf-8")

    if bcrypt.checkpw(password, user_to_check.password_hash.encode("utf-8")):
        request.session['id'] = user_to_check.id
        return redirect('/book')
    else:
        return login_fail(request)


def login_fail(request):
    messages.error(request, "Login Failed")
    return redirect('/')


def register_action(request):
    errors = User.objects.user_validation(request.POST)
    print 'error len', len(errors)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    else:
        new_hash = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt())
        print new_hash
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                        email=request.POST['email'], password_hash=new_hash)
        new_user.save()
        request.session['id'] = new_user.id
        return redirect('/book')


def get_logged_in_user(request):
    try:
        request.session['id']
    except KeyError:
        return None

    return User.objects.get(id=request.session['id'])


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return redirect('/')


def logged_in(request):
    if not get_logged_in_user(request) == None:
        return True
    else:
        return False
