"""
URL configuration for bookshelve_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'), namespace='main')),
    path('auth/', include(('auths.urls', 'auths'), namespace='auths')),
    path('book/', include(('publish.urls', 'publish'), namespace='publish')),
    path('forum/', include(('forum.urls', 'forum'), namespace='forum')),
    path('bookmark/', include(('bookmark.urls', 'bookmark'), namespace='bookmark')),
    path('event/', include(('event.urls', 'event'), namespace='event')),
    path('details/', include(('review.urls', 'review'), namespace='review')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
