# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse


def register(request):
    response = 'placeholder for users to create a new user record'
    HttpResponse(response)


def login(request):
    response = 'placeholder for users to login'
    HttpResponse(response)


def users(request):
    response = 'placeholder to later display all the list of users'
    HttpResponse(response)
