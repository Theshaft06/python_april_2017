from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^secrets$', views.home),
    url(r'^add_secret$', views.add_secret),
    #render most popular secrets page
    url(r'^secrets/most_popular$', views.show_most_popular),
    url(r'^/add_like/home$', views.add_like_homepage),
    url(r'^/add_like/popular$', views.add_like_popular_page),
]