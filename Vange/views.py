from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from Vange.models import Bug
from django.db.models import Count, QuerySet
from Vange.templates.Models import BASE_MODEL, DateEncoder
from django.core import serializers


# varx=("PACS","病床管理","省直单位住房公积金","地铁","大学城","宇宙最强","小毛专属")
def index(request):
    latest_list = Bug.objects.values("category").annotate(dcount=Count('category'))
    template = loader.get_template('index.html')
    context = {
        'latest_list': latest_list,
    }
    return HttpResponse(template.render(context, request))


def category(request):
    category_list = Bug.objects.values("category").annotate(dcount=Count('category'))
    return HttpResponse(BASE_MODEL.format(data=json.dumps(list(category_list))))


def buglist(request):
    assert isinstance(request, HttpRequest)
    category = request.GET.get("category")
    assert isinstance(Bug.objects.filter(category=category), QuerySet)
    bugs_list = Bug.objects.filter(category=category).values("category", "state", "publisher", "issue", "time")
    return HttpResponse(BASE_MODEL.format(data=json.dumps(list(bugs_list), cls=DateEncoder)))
