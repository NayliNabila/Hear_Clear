"""hearclear2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from page import views
#from page.views import SongFileDetailView 
from accounts import views as accounts_views
#from page import songinfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HearClear', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('HearClear/aboutme', views.aboutme),
    path('HearClear/comments', views.comments, name='comments'),
    path('HearClear/upload', views.upload, name = 'upload'),
    path('signup', accounts_views.signup, name='signup'),
    path('HearClear/comments/reply', views.reply, name='reply'),
    #url(r'^songfile/(?P<pk>\d+)/$', views.songdetails, name='songdetails'),
    #path('HearClear/details', views.songdetails, name='songdetails'),
    #path('HearClear/<int:pk>/', SongFileDetailView.as_view(), name='song-detail'),
    path('HearClear/<int:pk>/', views.songdetails, name='song-detail'),
    #path('HearClear/info', views.result, name='info'),
    path('HearClear/testing', views.testing, name='testing'),
    #path('HearClear/<str:song_id>/', views.songs, name='songs'),
    #path('secret/', accounts_views.secret_page, name = 'secret'),
    #url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.upload, name='songs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)