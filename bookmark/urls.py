from django.urls import path
from bookmark.views import add_bookmark, delete_bookmark, get_bookmark_by_user

app_name = 'bookmark'

urlpatterns = [
    path('add/<str:book_id>', add_bookmark, name='add_bookmark'),
    path('delete/', delete_bookmark, name='delete_bookmark'),
    path('', get_bookmark_by_user, name='get_bookmark_by_user'),
]