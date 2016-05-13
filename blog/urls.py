from django.conf.urls import url
from blog.views import home, contact, login_user, BlogView, BlogDetailsView

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^login/$', login_user, name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name = 'logout', kwargs={'next_page': '/'}),
    url(r'^blog/$', BlogView.as_view(), name = 'blogs'),
    url(r'^post/(?P<pk>[0-9]+)/$', BlogDetailsView.as_view(), name = 'details'),
    url(r'^contact/$', contact, name = 'contact'),
]
