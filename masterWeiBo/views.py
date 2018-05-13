import os
from _md5 import md5

from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.template import loader
from masterWeiBo.models import master, Like, WordCloud, WordPattern, Statistics, Science
from django.core import serializers

from masterWeiBo.templates.Models import JsonResult


# BASE_MODEL = '''{{"message":"成功","data":{data},"code":200}}'''


def index(request):
    # 获取文章列表
    page = int(request.GET.get("page", 1))
    if (page < 1):
        page = 1
    categoryxx = request.GET.get("category")
    come = request.GET.get("come")
    objects = master.objects
    if (categoryxx):
        objects = objects.filter(category=categoryxx)

    if (come):
        objects = objects.filter(come=come)

    artical_list = objects.order_by('-timestr')[(page * 10):((1 + page) * 10)]

    # 获取分类
    category_list = master.objects.values("category").annotate(count=Count('category'))

    # 获取来源
    come_list = master.objects.values("come").annotate(count=Count('come'))

    context = {
        'artical_list': artical_list,
        'pre': page if (page <= 1) else (page - 1),
        'next': page + 1,
        'category_list': category_list,
        'come_list': come_list,

    }
    if (come):
        context['come'] = come
    if (categoryxx):
        context['category'] = categoryxx

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def about(request):
    return HttpResponse(loader.get_template('about.html').render())


# 以上博客
# --------------------------------------------------------


def category(request):
    category__annotate = master.objects.values("category").annotate(count=Count('category'))
    return HttpResponse(JsonResult.success(category__annotate))


def articallist(request):
    category = request.GET.get("category")
    like_user = request.GET.get("like_user")
    num = int(request.GET.get("pagenum", default=1))
    size = int(request.GET.get("pagesize", default=10))
    articallist = master.objects.filter(category=category).values('id', 'category', 'content', 'come', 'mid',
                                                                  'hrefStr', 'datelong', 'timestr', 'imgs',
                                                                  'href').order_by("-datelong")[
                  (num - 1) * size: num * size]
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
    like_user = request.GET.get('like_user')
    objects = master.objects.all()
    count = objects.count()
    like__count = Like.objects.filter(like_user=like_user).all().count()
    list = {"like__count": like__count, "count": count}
    return HttpResponse(JsonResult.success(list))


def like(request):
    like_id = request.GET.get('like_id')
    flag = request.GET.get('flag', default=0)
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
    num = int(request.GET.get("pagenum", default=1))
    size = int(request.GET.get("pagesize", default=10))
    likes = Like.objects.filter(like_user=like_user).values('like_id')[
            (num - 1) * size:num * size]
    listxx = []
    for like in likes:
        like_id_ = like['like_id']
        artical = master.objects.filter(id=like_id_).values('id', 'category', 'content', 'come', 'mid',
                                                            'hrefStr', 'datelong', 'timestr', 'imgs', 'href')
        assert isinstance(artical, QuerySet)
        artical = artical.__getitem__(0)
        like_count = Like.objects.filter(like_id=like_id_).count()
        artical['is_like'] = 1
        artical['like_count'] = like_count
        listxx.append(artical)
    return HttpResponse(JsonResult.success(data=listxx))


from masterWeiBo.Utils.WordCloud import generatePic


def getWordCloud(request):
    context = request.GET.get('context')
    id = request.GET.get('id')
    pattern = request.GET.get('pattern', default=None)
    user = request.GET.get('user')
    name = md5((id + context).encode("utf8"))
    pic_url = generatePic(context, name.hexdigest(), pattern)
    filter = WordCloud.objects.filter(user=user, artical_id=id)
    if not filter.exists():
        WordCloud(user=user, artical_id=id, url=pic_url).save(force_insert=True)
    return HttpResponse(JsonResult.success(data=pic_url))


from django.views.decorators.csrf import csrf_exempt
from static.GLOBAVARS import UPLOAD_IMG_HOST as host


@csrf_exempt
def uploadPattern(request):
    try:
        user = request.GET.get('user')
        name = request.GET.get('name')
        print(user + name + "----")
        pattern = request.FILES.get('pattern', default=None)

        filter = WordPattern.objects.filter(user=user, name=host + name)
        if not filter.exists():
            WordPattern(user=user, name=host + name, img=pattern).save()
        return HttpResponse(JsonResult.success(data="成功"))
    except Exception:
        return HttpResponse(JsonResult.failure(data="失败"))


import jieba
from django.db.models import Q


def search(request):
    category = request.GET.get("category")
    words = request.GET.get("words")
    cut = jieba.cut(words)
    like_user = request.GET.get("like_user")
    num = int(request.GET.get("pagenum", default=1))
    size = int(request.GET.get("pagesize", default=10))
    articallist = master.objects;
    print(category)
    if (category):
        articallist = articallist.filter(category=category)
    for word in cut:
        print(word.strip())
        if (word.strip()):
            articallist = articallist.filter(
                Q(content__icontains=word) | Q(come__icontains=word) | Q(timestr__icontains=word))

    articallist = articallist.values('id', 'category', 'content', 'come', 'mid', 'hrefStr', 'datelong', 'timestr',
                                     'imgs', 'href').order_by("-datelong")[
                  (num - 1) * size:num * size]
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


import random


def latestSplash(r):
    type = r.GET.get('type')
    # 1.最近的文章
    randindex = random.randint(0, 5)
    artical = \
    master.objects.order_by("-datelong").values('id', 'category', 'content', 'come', 'mid', 'hrefStr', 'datelong',
                                                'timestr', 'imgs', 'href')[randindex]
    return HttpResponse(JsonResult.success(data=artical))


import time


def statistics(r):
    try:
        user = r.GET.get('user')
        if("HTTP_X_FORWARDED_FOR" in r.META):
            ip=r.META["HTTP_X_FORWARDED_FOR"]
        else:
            ip=r.META['REMOTE_ADDR']
        objects_filter = Statistics.objects.filter(user=user)
        count = objects_filter.count()
        result = {}
        result['count'] = count
        lastlogin = objects_filter.order_by("-date")
        if (lastlogin):
            lastlogin = lastlogin[:1][0]
            result['ip']=lastlogin.ip
            result['lasttime'] = lastlogin.date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            result['lasttime'] = "这是您的初次登陆"
        Statistics(user=user,ip=ip).save(force_insert=True)
    except:
        return HttpResponse(JsonResult.failure(data=None))
    print(result)
    return HttpResponse(JsonResult.success(data=result))

from static import GLOBAVARS
def science(r):
    values = Science.objects.order_by('-date').values('name', 'description', 'packageName', 'mainActivity', 'url' ,'date','icon')
    for value in values:
        icon_ = value['icon']
        url_ = value['url']
        assert  isinstance(icon_,str)
        replace = icon_.replace("static/media/", GLOBAVARS.UPLOAD_IMG_HOST)
        replace_file = url_.replace("static/", GLOBAVARS.CURRENT_HOST)
        value['url']=replace_file
        value['icon'] =replace
        if(url_):
            value['size'] =os.path.getsize(url_)
    return HttpResponse(JsonResult.success(data=values))

def getHistory100(r):
    user = r.GET.get('user')
    historys = Statistics.objects.filter(user=user).order_by('-date').values('date','ip')[:100]
    return HttpResponse(JsonResult.success(data=historys))

def getMycloud100(r):
    user = r.GET.get('user')
    historys = WordCloud.objects.filter(user=user).order_by('-date').values('date','url')[:100]
    return HttpResponse(JsonResult.success(data=historys))

