"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
#from django.contrib import staticfiles
import django
import views
from user.views import sign_in,success,activate
from comment.views import create_comment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/',include('article.urls')),
    url(r'^$',views.index),
    url(r'^register/',views.register),
    url(r'^signin/',sign_in),
    url(r'^signinsuccess/',success),
    url(r'^activate/(?P<active_code>\w+)$',activate),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^comment/',create_comment),
    url(r'^message/',include('message.urls')),
    url(r'^usercenter/',include('usercenter.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]
