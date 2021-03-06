# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hello'
        db.create_table(u'hello_hello', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('firstname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
        ))
        db.send_create_signal('hello', ['Hello'])


    def backwards(self, orm):
        # Deleting model 'Hello'
        db.delete_table(u'hello_hello')


    models = {
        'hello.hello': {
            'Meta': {'object_name': 'Hello'},
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['hello']