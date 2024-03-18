from django.urls import URLPattern, URLResolver, include, path


urlpatterns: list[URLPattern | URLResolver] = [
    path('v1/', include(('api.v1.urls', 'v1'), namespace='v1'))
]
