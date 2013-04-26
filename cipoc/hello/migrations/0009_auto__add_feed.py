# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table(u'hello_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('url', self.gf('django.db.models.fields.URLField')(default='', max_length=30)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=140)),
        ))
        db.send_create_signal('hello', ['Feed'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table(u'hello_feed')


    models = {
        'hello.feed': {
            'Meta': {'object_name': 'Feed'},
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '30'})
        },
        'hello.friend': {
            'Meta': {'object_name': 'Friend'},
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['hello']