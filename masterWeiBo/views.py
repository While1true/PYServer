from django.db.models import Count
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.template import loader
from masterWeiBo.models import master
from django.core import serializers
BASE_MODEL='''{{"message":"成功","data":{data},"code":200}}'''

def index(request):
    latest_list = master.objects.order_by('timestr')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_list': latest_list,
    }
    return HttpResponse(template.render(context, request))


def category(request):
    category__annotate = master.objects.values("category").annotate(dcount=Count('category'))

    return HttpResponse(BASE_MODEL.format(data=json.dumps(list(category__annotate))))
