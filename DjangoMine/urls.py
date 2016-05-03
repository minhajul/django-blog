"""DjangoMine URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from blog.views import home, blogs, details, contact, login_user

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^post/(?P<id>[0-9]+)/$', details, name = 'details'),
    url(r'^blogs/', blogs, name = 'blogs'),
    url(r'^contact/', contact, name = 'contact'),
    url(r'^login/', login_user, name = 'login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name = 'logout', kwargs={'next_page': '/'}),
    url(r'^admin/', admin.site.urls),
]
