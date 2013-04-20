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
        ))
        db.send_create_signal(u'hello', ['Hello'])


    def backwards(self, orm):
        # Deleting model 'Hello'
        db.delete_table(u'hello_hello')


    models = {
        u'hello.hello': {
            'Meta': {'object_name': 'Hello'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['hello']