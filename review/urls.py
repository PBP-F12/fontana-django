from django.urls import path
from .views import *

urlpatterns = [
    path('<str:book_title>/', book_details, name='book_details'),
    path('', show_mainbruh, name='show_main'),
    path('review/<str:book_title>/', get_review_json, name='get_review_json'),
    path('review/add/<str:book_title>/', create_review, name='create_review'),
]
