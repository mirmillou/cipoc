# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Hello'
        db.delete_table(u'hello_hello')


    def backwards(self, orm):
        # Adding model 'Hello'
        db.create_table(u'hello_hello', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
        ))
        db.send_create_signal('hello', ['Hello'])


    models = {
        
    }

    complete_apps = ['hello']