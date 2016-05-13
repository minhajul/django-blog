from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [

    url(r'', include('blog.urls'), name = 'blogs'),

    url(r'', include('news.urls'), name = "news"),

    url(r'^admin/', admin.site.urls),
]
