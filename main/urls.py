from .views import *
from django.urls import path

urlpatterns = [
    path('', show_main, name='show_main')
]
