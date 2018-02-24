from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url('category', views.category, name='category')
]