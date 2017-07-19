from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^show/(?P<parameter>\d+)$', views.show),
    url(r'^(?P<parameter>\d+)/edit$', views.edit),
    url(r'^(?P<parameter>\d+)/update$', views.update),
    url(r'^(?P<parameter>\d+)/destroy$', views.destroy),
]
