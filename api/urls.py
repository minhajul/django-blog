from django.conf.urls import url
from api.views import PostListView


urlpatterns = [

    url(r'^posts/$', PostListView.as_view(), name = "API Views"),
    url(r'^contact/$', PostListView.as_view(), name = "API Views"),

]
