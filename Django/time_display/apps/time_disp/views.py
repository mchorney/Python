# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse


def index(request):
    context = {
        'time': datetime.now()
    }
    return render(request, 'time_disp/index.html', context)
