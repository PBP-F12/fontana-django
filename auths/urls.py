from django.urls import path
from .views import *

urlpatterns = [
    path('register/reader/', register_as_reader, name='register_as_reader'),
    path('register/author/', register_as_author, name='register_as_author'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user/<int:user_id>', get_user_by_id, name='get_user_by_id')
]
