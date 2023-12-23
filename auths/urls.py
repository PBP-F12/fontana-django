from django.urls import path
from .views import register_as_reader, register_as_author, login_user, logout_user, get_user_by_id, logout_user_api, login_user_api, register_as_reader_api, register_as_author_api, get_user_data, upload_profile_picture

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
    path('api/user', get_user_data, name='get_user_data'),
    path('api/user/picture', upload_profile_picture,
         name='upload_profile_picture')
]
