# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'flyer_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'flyer', ['Country'])

        # Adding model 'Province_state'
        db.create_table(u'flyer_province_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Country'])),
            ('Province_state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'flyer', ['Province_state'])

        # Adding model 'Store'
        db.create_table(u'flyer_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Country'])),
            ('province_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Province_state'])),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('zip_postalcode', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'flyer', ['Store'])

        # Adding model 'Flyer'
        db.create_table(u'flyer_flyer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flyer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Store'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'flyer', ['Flyer'])

        # Adding model 'Product'
        db.create_table(u'flyer_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flyer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Flyer'])),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('units', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'flyer', ['Product'])

        # Adding model 'Saving'
        db.create_table(u'flyer_saving', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Product'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'flyer', ['Saving'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'flyer_country')

        # Deleting model 'Province_state'
        db.delete_table(u'flyer_province_state')

        # Deleting model 'Store'
        db.delete_table(u'flyer_store')

        # Deleting model 'Flyer'
        db.delete_table(u'flyer_flyer')

        # Deleting model 'Product'
        db.delete_table(u'flyer_product')

        # Deleting model 'Saving'
        db.delete_table(u'flyer_saving')


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