# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Friend'
        db.create_table(u'hello_friend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('firstname', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
        ))
        db.send_create_signal('hello', ['Friend'])


    def backwards(self, orm):
        # Deleting model 'Friend'
        db.delete_table(u'hello_friend')


    models = {
        'hello.friend': {
            'Meta': {'object_name': 'Friend'},
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['hello']