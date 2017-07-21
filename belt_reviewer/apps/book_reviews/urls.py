from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration_attempt$', views.register),
    url(r'^login_attempt$', views.login),
    url(r'^success$', views.success),
    url(r'^books/add$', views.add),
    url(r'^make_book_entry$', views.make_book_entry),
    url(r'^book/(?P<parameter>\d+)$', views.display_book),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home),
    url(r'^user/(?P<parameter>\d+)$', views.show_user),
    url(r'^destroy/(?P<parameter>\d+)/(?P<book_id>\d+)$', views.destroy),
    url(r'^add_review$', views.add_review),
]
