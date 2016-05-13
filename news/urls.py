from django.conf.urls import url
from views import news_views


urlpatterns = [

    url(r'^news/$', news_views, name = "news"),

]
