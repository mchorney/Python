# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib.messages import error
from django.core.urlresolvers import reverse


def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/index.html', context)


def new(request):
    return render(request, 'users/new_user.html')


def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for tag, message in errors.iteritems():
            error(request, message, extra_tags=tag)
        return render(request, 'users/new_user.html')
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email']
    )
    return redirect('/')


def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'users/show.html', context)


def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'users/edit.html', context)


def update(request, id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for tag, message in errors.iteritems():
            error(request, message, extra_tags=tag)
        return redirect('/users/{}/edit'.format(id))
    update_user = User.objects.get(id=id)
    update_user.first_name = request.POST['first_name']
    update_user.last_name = request.POST['last_name']
    update_user.email = request.POST['email']
    update_user.save()
    return redirect(reverse('show'))


def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect(reverse('home'))
