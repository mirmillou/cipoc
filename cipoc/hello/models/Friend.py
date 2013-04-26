from django.db import models
from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

print('These are your Friend classes')

# Create your models here.
class Friend(models.Model):
    name = models.CharField(_('name'), max_length=30, default='')
    firstname = models.CharField(_('firstname'), max_length=30, default='')

    def __str__(self):
        return self.name
       
    def __unicode__(self):
        return self.name+' '+self.firstname

    class Meta:
        app_label = "hello"

class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'firstname')
    search_fields = ('name', ) 
