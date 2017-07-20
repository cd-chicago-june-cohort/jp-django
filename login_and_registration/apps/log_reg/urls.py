from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration_attempt$', views.register),
    url(r'^login_attempt$', views.login),
    url(r'^success$', views.success),
]