# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, 'belt_review/index.html')

def register(request):
    error = User.objects.validate_registration(request.POST)
    if len(error):
        for tag, error in error.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(name=name, alias=alias, email=email, password=password)
        request.session['user'] = user.alias
        request.session['id'] = user.id
        return redirect('/books')

def login(request):
    error = User.objects.validate_login(request.POST)
    if len(error):
        for tag, error in error.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user'] = user.alias
        request.session['id'] = user.id
        print request.session['id']
        return redirect('/books')

def books(request):
    review = Review.objects.all().order_by('-id')[:3]
    books = Book.objects.all()
    info = {
        'review':review,
        'books':books
    }
    return render(request, 'belt_review/books.html', info)

def addBook(request):
    return render(request, 'belt_review/addBook.html')

def process(request):
    if request.method == 'POST':
        error = User.objects.validate_review(request.POST)
        if len(error):
            for tag, error in error.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/books')
        else:
            if len(request.POST['author']) < 1:
                author = request.POST['existingAuthor']
                print author
                authorObject = Author.objects.create(name=author)
            else:
                author = request.POST['author']
                authorObject = Author.objects.create(name=author)
            title = request.POST['title']
            try:    
                bookObject = Book.objects.get(title=title)
            except:
                bookObject = Book.objects.create(title=title, author=authorObject)
            content = request.POST['content']
            rating = request.POST['stars']
            print request.session['id']
            userObject = User.objects.get(id=request.session['id'])
            Review.objects.create(content=content, rating=rating, book=bookObject, user=userObject)
            bookId = bookObject.id
            return redirect('/books/{}'.format(bookId))
    else:
        return redirect('/books')

def review(request, id):
    book = Book.objects.get(id=id)
    review = Review.objects.filter(book=book)
    context = {
        'book':book,
        'reviews':review,
    }
    return render(request, 'belt_review/review.html', context)

def viewUser(request, id):
    user = User.objects.annotate(numReviews=Count('reviews')).get(id=id)
    book = Book.objects.filter(reviews__user__id=id).distinct()
    context = {
        'user':user,
        'books':book
    }
    return render(request, 'belt_review/viewUser.html', context)
def processReview(request, id):
    content = request.POST['content']
    rating = request.POST['stars']
    user = User.objects.get(id=id)
    title = request.POST['title']
    bookObject = Book.objects.get(title=title)
    bookId = bookObject.id
    Review.objects.create(content=content, rating=rating, book=bookObject, user=user)
    return redirect('/books/{}'.format(bookId))

def delete(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')