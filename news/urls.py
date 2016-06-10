from django.conf.urls import url
from news.views import news_views


urlpatterns = [

    url(r'^news/$', news_views, name = "news"),

]
