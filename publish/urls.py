from django.urls import path
from .views import *

urlpatterns = [
    path('publish/', publish_book, name='publish_book'),
    path('author/', get_book_by_author, name='get_book_by_author')
]
