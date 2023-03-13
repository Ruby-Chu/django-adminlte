from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    result = []
    first_items = FIRST_MENU.objects.filter(exist=True)
    for f in first_items:
        item = {
            'name': f.first,
            'url': f.url,
            'second': []
        }
        second_items = SECOND_MENU.objects.filter(first_menu=f)
        if len(second_items) == 0:
            del item['second']
        else:
            for s in second_items:
                item['second'].append(
                    {
                        'name': s.second,
                        'url': s.url
                    }
                )
        result.append(item)
    return render(request, 'index.html', {'webinfo': result})


def demo(request, word):
    return render(request, 'demo.html', {'word': word})

