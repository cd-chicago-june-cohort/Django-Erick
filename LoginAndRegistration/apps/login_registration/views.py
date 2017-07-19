# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    error = User.objects.validate_registration(request.POST)
    if len(error):
        for tag, error in error.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        fName = request.POST['firstName']
        lName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        password = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
        User.objects.create(first_name=fName, last_name=lName, email=email, password=password)
        return redirect('/success')

def login(request):
    error = User.objects.validate_login(request.POST)
    if len(error):
        for tag, error in error.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user'] = user.first_name
        return redirect('/success')

def success(request):
    return render(request, 'login_registration/user.html')
