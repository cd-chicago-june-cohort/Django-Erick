# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = 'name should be longer than 2 characters'
        if len(postData['alias']) < 2:
            errors['alias'] = 'last name should be longer than 2 characters'
        if len(postData['email']) < 1:
            errors['email'] = 'email is required'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'email must be in valid format'
        if len(User.objects.filter(email=postData['email'])) >= 1:
            errors['validEmail'] = 'email already in use'
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
        else:
            password = postData['password']
            email = postData['email']
            print password
            user = User.objects.get(email=email)
            print user.password
            hashed = user.password
            if not bcrypt.checkpw(password.encode(), hashed.encode()):
                errors['validPassword'] = 'please enter the correct password'
        return errors

    def validate_review(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = 'title must be entered'
        if len(postData['content']) < 1:
            errors['content'] = 'review must be entered'
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)   

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews')
    user = models.ForeignKey(User, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)