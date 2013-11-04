# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Store.flyer_url'
        db.add_column(u'flyer_store', 'flyer_url',
                      self.gf('django.db.models.fields.CharField')(default='NULL', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Store.flyer_url'
        db.delete_column(u'flyer_store', 'flyer_url')


    models = {
        u'flyer.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'flyer.flyer': {
            'Meta': {'object_name': 'Flyer'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'flyer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Store']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'flyer.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'flyer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Flyer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'flyer.province_state': {
            'Meta': {'object_name': 'Province_state'},
            'Province_state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'flyer.saving': {
            'Meta': {'object_name': 'Saving'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Product']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'flyer.store': {
            'Meta': {'object_name': 'Store'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Country']"}),
            'flyer_url': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'province_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Province_state']"}),
            'store': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['flyer']