from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.template import loader
from masterWeiBo.models import master,Like
from django.core import serializers

from masterWeiBo.templates.Models import JsonResult

BASE_MODEL='''{{"message":"成功","data":{data},"code":200}}'''

def index(request):
    latest_list = master.objects.order_by('timestr')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_list': latest_list,
    }
    return HttpResponse(template.render(context, request))


def category(request):
    category__annotate = master.objects.values("category").annotate(count=Count('category'))
    return HttpResponse(BASE_MODEL.format(data=json.dumps(list(category__annotate))))

def articallist(request):
    category = request.GET.get("category")
    like_user = request.GET.get("like_user")
    num = int(request.GET.get("pagenum", default=0))
    size = int(request.GET.get("pagesize", default=10))
    articallist = master.objects.filter(category=category).values('id','category','content','come','mid',
                                                                  'hrefStr','datelong','imgs')[num * size:(num + 1) * size]
    listxx=[]
    for artical in articallist:
        print(type(artical))
        like_count = Like.objects.filter(like_id=artical['id']).count()
        islike = Like.objects.filter(like_id=artical['id'],like_user=like_user)
        # if(objects_filter):
        if(islike):
            artical['islike']=1
        artical['like_count']=like_count
        listxx.append(artical)
    return HttpResponse(JsonResult.success(data=listxx))

def todo(request):
    objects = master.objects.all()
    count = objects.count()
    like__count = Like.objects.all().count()
    list = {"like__count": like__count, "count": count}
    return HttpResponse(JsonResult.success(list))