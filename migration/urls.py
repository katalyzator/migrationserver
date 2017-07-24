"""migration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api
from main.api import *

from migration import settings

v1 = Api(api_name='v1')
v1.register(NewskgResource())
v1.register(NewsruResource())

urlpatterns = patterns('',
                       url(r'^jet/', include('jet.urls', 'jet')),
                       url(r'^admin/', admin.site.urls),
                       url(r'^api/', include(v1.urls)),
                       url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                       url(r'^newsru/$', 'main.views.newsru_view', name='newsru'),
                       url(r'^blacklist/$', 'main.views.blacklist_view', name='blacklist'),
                       url(r'^newskg/$', 'main.views.newskg_view', name='newskg'),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
