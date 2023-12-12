from .views import *
from django.urls import path

urlpatterns = [
    path('', show_main, name='show_main'),
    path('api/book/json', get_book_ajax, name='get_book_ajax'),
    path('json/', show_json, name='show_json'), 
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), 
]