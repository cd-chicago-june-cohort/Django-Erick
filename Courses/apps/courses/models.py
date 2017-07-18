# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class CoursesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 10:
            errors['name'] = 'name should be longer than 10 characters'
        if len(postData['description']) < 15:
            errors['desc'] = 'description should be longer than 15 characters'
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CoursesManager()
