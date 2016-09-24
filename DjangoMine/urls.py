from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'', include('blog.urls'), name = 'blog'),
    url(r'', include('news.urls'), name = "news"),
    url(r'', include('login.urls'), name = 'login'),
    url(r'^api/', include('api.urls'), name = 'api'),
    url(r'^admin/', admin.site.urls),
]
