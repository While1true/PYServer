from django.conf.urls import url

from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^about', views.about, name='about'),


    #以上博客
    url('^category', views.category, name='category'),
    url('^articallist', views.articallist, name='articallist'),
    url('^todo', views.todo, name='todo'),
    url('^like', views.like, name='like'),
    url('^getlikelist', views.getlikelist, name='getlikelist'),
    url('^getWordCloud', views.getWordCloud, name='getWordCloud'),
    url('^uploadPattern', views.uploadPattern, name='uploadPattern'),
    url('^search', views.search, name='search'),
]+static(settings.MEDIA_URL, document_root = settings.STATICFILES_DIRS)