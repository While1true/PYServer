from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.template import loader
from masterWeiBo.models import master
from django.core import serializers


def index(request):
    latest_list = master.objects.order_by('timestr')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_list': latest_list,
    }
    return HttpResponse(template.render(context, request))


def category(request):
    latest_list = master.objects.all()
    return HttpResponse(serializers.serialize("json", latest_list))
