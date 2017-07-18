# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    return render(request, 'users/index.html', {'users':User.objects.all()})

def new(request):
    return render(request, 'users/new.html')

def create(request):
    User.objects.create(first_name=request.POST['firstName'], last_name=request.POST['lastName'], email=request.POST['email'])
    return redirect('/users')

def view(request, id):
    user = User.objects.get(id=id)
    return render(request, 'users/view.html', {'user':user})

def viewEdit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'users/edit.html', {'user':user})

def update(request, id):
    user = User.objects.get(id=id)
    user.first_name = request.POST['firstName']
    user.last_name = request.POST['lastName']
    user.email = request.POST['email']
    user.save()
    return redirect('/users')

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')
