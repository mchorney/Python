# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = 'All Fields are Required'
            if field == 'first_name' or field == 'last_name':
                if not field in errors and len(value) < 2:
                    errors[field] = '{} field must be at least 2 characters'.format(
                        field.replace('_', ''))
        if 'email' not in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Invalid Email'
        else:
            if len(self.filter(email=postData['email'])) > 1:
                errors['email'] = 'Email already in use'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return 'User: {} {}'.format(self.first_name, self.last_name)
