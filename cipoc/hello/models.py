from django.db import models

# Create your models here.
class Hello(models.Model):
    name = models.CharField(max_length=30, default='')
    print('These are your classes as you start building real apps')

    def __str__(self):
        return self.name
       
    def __unicode__(self):
        return self.name

    class Admin:
        list_display = ('name')
        search_fields = ('name', ) 
