from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    all_web = webdb.objects.filter(exist=True)
    output = {}
    for a in all_web:
        output.update({a.name: a.url})
    return render(request, 'index.html', {'webinfo': output})

def demo1(request):
    return render(request, 'demo1.html')

def demo2(request):
    return render(request, 'demo2.html')

