import os
from _md5 import md5

from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.template import loader
from masterWeiBo.models import master, Like,WordCloud,WordPattern
from django.core import serializers
from django.forms.models import model_to_dict

from masterWeiBo.templates.Models import JsonResult

# BASE_MODEL = '''{{"message":"成功","data":{data},"code":200}}'''


def index(request):
    latest_list = master.objects.order_by('timestr')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_list': latest_list,
    }
    return HttpResponse(template.render(context, request))


def category(request):
    category__annotate = master.objects.values("category").annotate(count=Count('category'))
    return HttpResponse(JsonResult.success(category__annotate))


def articallist(request):
    category = request.GET.get("category")
    like_user = request.GET.get("like_user")
    num = int(request.GET.get("pagenum", default=0))
    size = int(request.GET.get("pagesize", default=10))
    articallist = master.objects.filter(category=category).values('id', 'category', 'content', 'come', 'mid',
                                                                  'hrefStr', 'datelong', 'timestr', 'imgs','href')[
                  num * size:(num + 1) * size]
    listxx = []
    for artical in articallist:
        like_count = Like.objects.filter(like_id=artical['id']).count()
        islike = Like.objects.filter(like_id=artical['id'], like_user=like_user)
        # if(objects_filter):
        if (islike.exists()):
            artical['is_like'] = 1
        artical['like_count'] = like_count
        listxx.append(artical)
    return HttpResponse(JsonResult.success(data=listxx))


def todo(request):
    objects = master.objects.all()
    count = objects.count()
    like__count = Like.objects.all().count()
    list = {"like__count": like__count, "count": count}
    return HttpResponse(JsonResult.success(list))


def like(request):
    like_id = request.GET.get('like_id')
    flag = request.GET.get('flag',default=0)
    like_user = request.GET.get('like_user')
    objects_filter = Like.objects.filter(like_id=like_id, like_user=like_user)
    assert isinstance(objects_filter, QuerySet)
    if (flag == '1'):
        if not objects_filter.exists():
            print("---------------------------------------------------------------")
            like = Like(like_id=like_id, like_user=like_user)
            like.save(force_insert=True)
            return HttpResponse(JsonResult.success('成功'))
    else:
        assert isinstance(objects_filter, QuerySet)
        if (objects_filter.exists()):
            objects_filter.delete()
            return HttpResponse(JsonResult.success('成功'))
    message = ""
    if (flag == '1'):
        message = "已经收藏过了"
    else:
        message = "没有收藏过该博文"
    return HttpResponse(JsonResult.failure(message))

def getlikelist(request):
    like_user = request.GET.get('like_user')
    num = int(request.GET.get("pagenum", default=0))
    size = int(request.GET.get("pagesize", default=10))
    likes=Like.objects.filter(like_user=like_user).values('like_id')[
                  num * size:(num + 1) * size]
    listxx = []
    for like in likes:
        like_id_ = like['like_id']
        artical=master.objects.filter(id=like_id_).values('id', 'category', 'content', 'come', 'mid',
                                                      'hrefStr', 'datelong', 'timestr', 'imgs','href')
        assert isinstance(artical,QuerySet)
        artical=artical.__getitem__(0)
        like_count=Like.objects.filter(like_id=like_id_).count()
        artical['is_like'] = 1
        artical['like_count'] = like_count
        listxx.append(artical)
    return HttpResponse(JsonResult.success(data=listxx))

from masterWeiBo.Utils.WordCloud import generatePic
def getWordCloud(request):
    context = request.GET.get('context')
    id = request.GET.get('id')
    pattern = request.GET.get('pattern',default=None)
    user = request.GET.get('user')
    name= md5((id+context).encode("utf8"))
    pic_url = generatePic(context, name.hexdigest(),pattern)
    filter = WordCloud.objects.filter(user=user, artical_id=id)
    if not filter.exists():
        WordCloud(user=user, artical_id=id, url=pic_url).save(force_insert=True)
    return HttpResponse(JsonResult.success(data=pic_url))

def uploadPattern(request):
    try:
        user = request.POST.get('user')
        name = request.POST.get('name')
        print(user+name+"----")
        pattern = request.FILES.get('pattern', default=None)
        filter = WordCloud.objects.filter(user=user, name=name)
        if not filter.exists():
             WordPattern(user=user,name="/public/media/"+name,img=pattern).save()
        return HttpResponse(JsonResult.success(data="成功"))
    except Exception:
        return HttpResponse(JsonResult.failure(data="失败"))




