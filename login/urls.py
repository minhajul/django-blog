from django.conf.urls import url
from login.views import login_user

urlpatterns = [
    url(r'^login/$', login_user, name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name = 'logout', kwargs={'next_page': '/'}),
]
