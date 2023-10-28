from django.urls import path
from .views import *

urlpatterns = [
    path('', list_event, name='list_event'),
    path('publish_event/', publish_event, name='publish_event'),
    path('<str:event_id>/', get_event_details, name='get_event_details')
]
