from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('demo/<str:word>', demo, name='demo'),
]
