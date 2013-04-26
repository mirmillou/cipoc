from django.db import models
from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

print('These are your Feed classes')

# Create your models here.
class Feed(models.Model):
    name = models.CharField(_('name'), max_length=30, default='')
    url = models.URLField(_('url'), max_length=200, default='')
    comment = models.CharField(_('comment'), max_length=140, default='', blank=True)
    last_update = models.DateField(_('last_update'), null=True,  blank=True)

    def __str__(self):
        return self.name
       
    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "hello"

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name',  'comment')
    search_fields = ('name', ) 
