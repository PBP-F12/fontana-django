from django.urls import URLPattern, URLResolver, path, include


urlpatterns: list[URLPattern | URLResolver] = [
    path('auth/', include(('api.v1.authentication.urls', 'auth'), namespace='v1')),
    path('bookmark/', include(('api.v1.bookmark.urls', 'bookmark'), namespace='bookmark')),
    path('event/', include(('api.v1.event.urls', 'event'), namespace='event')),
    path('forum/', include(('api.v1.forum.urls', 'forum'), namespace='forum')),
    path('main/', include(('api.v1.main.urls', 'main'), namespace='main')),
    path('event/', include(('api.v1.event.urls', 'event'), namespace='event')),
    path('publish/', include(('api.v1.publish.urls', 'publish'), namespace='publish')),
    path('review/', include(('api.v1.review.urls', 'review'), namespace='review')),
]
