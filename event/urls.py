from django.urls import path
from .views import *

urlpatterns = [
    path('create-flutter', create_product_flutter, name='create_product_flutter'),
    path('', list_event, name='list_event'),
    path('publish_event/', publish_event, name='publish_event'),
    path('json/', show_json, name='show_json'), 
    path('json/<str:event_id>/', show_json_by_id, name='show_json_by_id'), 
    path('ajax/', list_event_ajax, name='list_event_ajax'),
    path('<str:event_id>/', get_event_details, name='get_event_details'),
]
