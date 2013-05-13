# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from hello.models import Friend,  Feed
from hello.views import FeedList,  FeedDetail

urlpatterns = patterns('',
   url(r'^$', 'hello.views.index',  name='front'),
   url(r'^friends/$', ListView.as_view(
        model=Friend,
    ), name='friends'),

    url(r'^friends/(?P<pk>\d+)/$',
      DetailView.as_view(
        model=Friend,
        template_name='hello/friend_detail.html'), name="friend"),
        
    url(r'^feeds/$', FeedList.as_view(),  name='feeds'),
    url(r'^feeds/(?P<pk>\d+)/$', FeedDetail.as_view(),  name='feed'),
)
