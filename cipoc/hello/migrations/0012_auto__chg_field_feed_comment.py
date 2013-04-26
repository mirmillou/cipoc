# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feed.comment'
        db.alter_column(u'hello_feed', 'comment', self.gf('django.db.models.fields.CharField')(default='', max_length=140))

    def backwards(self, orm):

        # Changing field 'Feed.comment'
        db.alter_column(u'hello_feed', 'comment', self.gf('django.db.models.fields.CharField')(max_length=140, null=True))

    models = {
        'hello.feed': {
            'Meta': {'object_name': 'Feed'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'})
        },
        'hello.friend': {
            'Meta': {'object_name': 'Friend'},
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['hello']