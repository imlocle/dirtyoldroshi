from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sketch', views.sketch),
    url(r'^paint', views.paint),
]
