from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.newsList, name='newsList'),
    url(r'^sources', views.news_sources, name='news_sources'),


]