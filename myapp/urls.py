from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('demo1', demo1, name='demo1'),
    path('demo2', demo2, name='demo2'),
]
