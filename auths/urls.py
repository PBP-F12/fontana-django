from django.urls import path
from . import views

urlpatterns = [
    path('register/reader/', views.register_as_reader, name='register_as_reader'),
    path('register/author/', views.register_as_author, name='register_as_author'),
    path('login/', views.login_user, name='login')
]
