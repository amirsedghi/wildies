from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^loginreg$', views.loginreg),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^preferences/(?P<id>\d+)$', views.preferences),
    url(r'^main$', views.main),
    url(r'^wildrecord$', views.wildrecord),
    url(r'^record$', views.record),
]
