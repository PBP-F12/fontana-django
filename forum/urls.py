from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_forum, name='create_forum'),
    path('', display_all_forum, name='display_all_forum'),
    path('ajax/', display_all_forums_ajax, name='display_all_forums_ajax'),
    path('<str:forum_id>/', display_forum_by_id, name='display_forum_by_id'),
]
