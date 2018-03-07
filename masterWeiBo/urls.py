from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url('^category', views.category, name='category'),
    url('^articallist', views.articallist, name='articallist'),
    url('^todo', views.todo, name='todo'),
    url('^like', views.like, name='like'),
    url('^getlikelist', views.getlikelist, name='getlikelist'),
]