from django.conf.urls import url
from api.views import PostListView
from api.views import ContactListView
from api.views import UserListView


urlpatterns = [
    url(r'^posts/$', PostListView.as_view(), name = "Posts List View"),
    url(r'^contact/$', ContactListView.as_view(), name = "Contact List View"),
    url(r'^users/$', UserListView.as_view(), name = "Users Lift View"),
]
