from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^users$", views.createUser),
    url(r"^secrets$", views.secrets),
    url(r"^login$", views.login),
    url(r"^logout$", views.logout),
    url(r"^posts$", views.createPost),
]
