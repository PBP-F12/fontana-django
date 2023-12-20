from django.urls import path
from .views import *

urlpatterns = [
    path('<uuid:book_id>/', book_details, name='book_details'),
    path('review/<uuid:book_id>/', get_review_json, name='get_review_json'),
    path('review/add/<uuid:book_id>/', create_review, name='create_review'),
    path('delete_review/<int:review_id>', delete_review, name='delete_review'),
    path('review/addflutter/<uuid:book_id>/',
         create_review_flutter, name='create_review_flutter'),
    path('book/<str:book_id>', get_detail_book, name='get_detail_book')
]
