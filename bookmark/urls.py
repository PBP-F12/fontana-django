from django.urls import path
from bookmark.views import add_bookmark, delete_bookmark, get_bookmark_by_user, delete_bookmark_by_book_id

app_name = 'bookmark'

urlpatterns = [
    path('add/<str:book_id>', add_bookmark, name='add_bookmark'),
    path('delete/<str:bookmark_id>', delete_bookmark, name='delete_bookmark'),
    path('delete/book/<str:book_id>', delete_bookmark_by_book_id, name='delete_bookmark_by_book_id'),
    path('', get_bookmark_by_user, name='get_bookmark_by_user'),
]