from .views import show_main
from django.urls import path

urlpatterns = [
    path('', show_main)
]
