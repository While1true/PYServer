from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url('^category', views.category, name='category'),
    url('^buglist', views.buglist, name='buglist'),
    url('^todo', views.todo, name='todo'),
    url('^like', views.like, name='like'),
    url('^unsolvelike', views.unsolvelike, name='unsolvelike'),
    url('^add', views.add, name='add'),
]