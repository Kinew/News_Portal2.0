"""
URL configuration for NewsPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns

from news_portal import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewset)
router.register(r'articles', views.ArticlesViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # path('pages/', include('django.contrib.flatpages.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path("accounts/", include("accounts.urls")),
    # path('', include('news_portal.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    # подключаем встроенные эндопинты для работы с локализацией
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += i18n_patterns(path('', include('news_portal.urls')))
