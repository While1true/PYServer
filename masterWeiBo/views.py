from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from masterWeiBo.models import master
def index(request):
    count = master.objects.all()[:1000]
    sx=''
    for s in count:
       sx+=s.__str__()+"\n"
    return HttpResponse(sx)
