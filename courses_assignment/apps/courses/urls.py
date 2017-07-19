from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^delete_page/(?P<parameter>\d+)$', views.delete_page),
    url(r'^destroy/(?P<parameter>\d+)$', views.destroy),
]