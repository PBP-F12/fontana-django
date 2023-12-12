from django.urls import path
from .views import *

urlpatterns = [
    path('register/reader/', register_as_reader, name='register_as_reader'),
    path('register/author/', register_as_author, name='register_as_author'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user/<int:user_id>', get_user_by_id, name='get_user_by_id'),
    path('api/logout', logout_user_api, name='logout_user_api'),
    path('api/login', login_user_api, name='login_api'),
    path('api/register/reader', register_as_reader_api,
         name='register_as_reader_api'),
    path('api/register/author', register_as_author_api,
         name='register_as_author_api'),
]
