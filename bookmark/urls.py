from django.urls import path
from bookmark.views import add_bookmark, delete_bookmark, get_bookmark_by_user, delete_bookmark_by_book_id, get_bookmark_by_user_ajax, add_bookmark_ajax, delete_bookmark_by_book_id_ajax

app_name = 'bookmark'

urlpatterns = [
    path('api/add/<str:book_id>', add_bookmark_ajax, name='add_bookmark_ajax'),
    path('api/delete/<str:book_id>', delete_bookmark_by_book_id_ajax, name='delete_bookmark_by_book_id_ajax'),
    path('add/<str:book_id>', add_bookmark, name='add_bookmark'),
    path('delete/<str:bookmark_id>', delete_bookmark, name='delete_bookmark'),
    path('delete/book/<str:book_id>', delete_bookmark_by_book_id,
         name='delete_bookmark_by_book_id'),
    path('', get_bookmark_by_user, name='get_bookmark_by_user'),
    path('ajax/', get_bookmark_by_user_ajax, name='get_bookmark_by_user_ajax')
]
