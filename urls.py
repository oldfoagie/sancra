from django.conf.urls import url
from . import views

#This file lets django know which file to call when user types in an url
#This file is at /blog/urls.py

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'home$', views.home),
    url(r'board$', views.board),
    url(r'cities$', views.cities),
    url(r'orgs$', views.orgs),
    ]
