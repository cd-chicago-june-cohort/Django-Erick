from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)$', views.view),
    url(r'^(?P<id>\d+)/edit$', views.viewEdit),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.update),
]