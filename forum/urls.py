from django.urls import path
from .views import *

urlpatterns = [
    path('', display_all_forum, name='display_all_forum'),
    path('create/', create_forum, name='create_forum'),
    path('api', display_all_forums_ajax, name='display_all_forums_ajax'),
    path('api/create', create_forum_ajax, name='create_forum_ajax'),
    path('ajax/<str:forum_id>', display_forum_by_id_ajax,
         name='display_forum_by_id_ajax'),
    path('ajax/reply/<str:forum_id>', add_reply_to_forum_ajax,
         name='add_reply_to_forum_ajax'),
    path('<str:forum_id>/', display_forum_by_id, name='display_forum_by_id'),
]
