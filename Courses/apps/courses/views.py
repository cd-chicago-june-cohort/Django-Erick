# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages

def index(request):
    courses = Courses.objects.all()
    return render(request, 'courses/index.html', {'courses':courses})

def add(request):
    error = Courses.objects.basic_validator(request.POST)
    if len(error):
        for tag, error in error.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        Courses.objects.create(name=request.POST['name'], desc=request.POST['description'])
        return redirect('/')

def viewDelete(request, id):
    course = Courses.objects.get(id=id)
    return render(request, 'courses/delete.html', {'courses':course})

def delete(request, id):
    course = Courses.objects.get(id=id)
    course.delete()
    return redirect('/')
