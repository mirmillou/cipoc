# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from hello.models import Friend

urlpatterns = patterns('',
#    url(r'^$', 'hello.views.index'),
    url(r'^$', ListView.as_view(
        model=Friend,
    ), name='friends'),

    url(r'^friend/(?P<pk>\d+)/$',
      DetailView.as_view(
        model=Friend,
        template_name='hello/friend_detail.html'), name="friend"),
)
     
