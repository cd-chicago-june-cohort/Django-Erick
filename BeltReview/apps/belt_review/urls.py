from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^books/add$', views.addBook),
    url(r'^books/process$', views.process),
    url(r'^books/process/(?P<id>\d+)$', views.processReview),
    url(r'^books/(?P<id>\d+)$', views.review),
    url(r'^users/(?P<id>\d+)$', views.viewUser),
    url(r'^books/delete/(?P<id>\d+)$', views.delete),
]