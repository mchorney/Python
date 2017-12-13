# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User


def index(request):
    print "Got to index"
    return render(request, 'user_login/index.html')
