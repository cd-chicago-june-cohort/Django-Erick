# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from models import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors['firstName'] = 'first name should be longer than 2 characters'
        if len(postData['lastName']) < 2:
            errors['lastName'] = 'last name should be longer than 2 characters'
        if len(postData['email']) < 1:
            errors['email'] = 'email is required'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'email must be in valid format'
        if postData['password'] != postData['confirmPassword']:
            errors['confirm'] = 'both passwords must match!'
        if len(postData['password']) < 8:
            errors['password'] = 'password must be greater than 8 characters'
        return errors

    def validate_login(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email'] = 'email is required'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'email must be in valid format'
        if len(postData['password']) < 8:
            errors['password'] = 'password must be greater than 8 characters'
        if len(User.objects.filter(email=postData['email'])) < 1:
            errors['validEmail'] = 'please register before logging in'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
