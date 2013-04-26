# -*- coding: utf-8 -*-
from django.contrib import admin
from hello.models import Friend,  FriendAdmin,  Feed,  FeedAdmin
 
admin.site.register(Friend,  FriendAdmin)
admin.site.register(Feed, FeedAdmin)
