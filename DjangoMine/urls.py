from django.conf.urls import url
from django.contrib import admin
from blog.views import home, contact, login_user, BlogView, BlogDetailsView
from news.views import news_views

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^blog/', BlogView.as_view(), name = 'blogs'),
    url(r'^post/(?P<pk>[0-9]+)/$', BlogDetailsView.as_view(), name = 'details'),
    url(r'^contact/', contact, name = 'contact'),
    url(r'^login/', login_user, name = 'login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name = 'logout', kwargs={'next_page': '/'}),

    url(r'^news/', news_views, name = "news"),

    url(r'^admin/', admin.site.urls),
]
