from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from Vange.models import Bug,Category,Publisher
from django.db.models import Count, QuerySet
from Vange.templates.Models import DateEncoder, JsonResult
from django.core import serializers


# varx=("PACS","病床管理","省直单位住房公积金","地铁","大学城","宇宙最强","小毛专属")
def index(request):
    latest_list = Bug.objects.values("category","category_id").annotate(dcount=Count('category'))
    template = loader.get_template('index.html')
    bugs=Bug.objects.values( "category", "publisher", "title", "issue","time")
    context = {
        'latest_list': latest_list,
        'bug_list':bugs
    }
    return HttpResponse(template.render(context, request))


def category(request):
    objects_all = Bug.objects.all()
    assert isinstance(objects_all, QuerySet)
    print(objects_all)
    category_list = Bug.objects.values("category","category_id").annotate(dcount=Count('category'))
    return HttpResponse(JsonResult.success(category_list))


def buglist(request):
    category = request.GET.get("category")
    num = int(request.GET.get("pagenum", default=0))
    size = int(request.GET.get("pagesize", default=10))

    bugs_list = Bug.objects.filter(category=category).values("id", "category", "state", "publisher", "title", "issue","like",
                                                             "time")[num * size:(num + 1) * size]
    return HttpResponse(JsonResult.success(data=bugs_list))


def todo(request):
    objects = Bug.objects.filter(state=0)
    count = objects.count()
    like__count = Bug.objects.filter(state=0, like=1).count()
    list = {"like__count": like__count, "count": count}
    return HttpResponse(JsonResult.success(list))

def like(request):
    id = request.GET.get("id")
    like = request.GET.get("like")
    bug = Bug.objects.get(id=id)
    bug.like=like
    bug.save()
    return HttpResponse(JsonResult.success('"ok"'))

def unsolvelike(request):
    bugs_list = Bug.objects.filter(like=1,state=0).values("id", "category", "state", "publisher", "title", "issue","time","like")
    return HttpResponse(JsonResult.success(data=bugs_list))


def add(request):
    id = request.GET.get("id")
    like = request.GET.get("like")
    bug = Bug.objects.get(id=id)
    bug.like=like
    bug.save()
    return HttpResponse(JsonResult.success('"ok"'))



