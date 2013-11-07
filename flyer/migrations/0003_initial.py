# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table(u'flyer_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('flyer_crawl', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Store'])

        # Adding model 'Location'
        db.create_table(u'flyer_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Store'])),
            ('flyer_crawl', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postalcode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Location'])

        # Adding model 'Flyer'
        db.create_table(u'flyer_flyer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flyer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Location'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Flyer'])

        # Adding model 'Product'
        db.create_table(u'flyer_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Product'])

        # Adding model 'Brand'
        db.create_table(u'flyer_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Brand'])

        # Adding model 'Category'
        db.create_table(u'flyer_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Category'])

        # Adding model 'Sale'
        db.create_table(u'flyer_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Product'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Brand'], blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Category'], blank=True)),
            ('flyer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Flyer'])),
            ('price_sale', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price_reg', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Sale'])

        # Adding model 'Saving'
        db.create_table(u'flyer_saving', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flyer.Sale'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('saving', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'flyer', ['Saving'])


    def backwards(self, orm):
        # Deleting model 'Store'
        db.delete_table(u'flyer_store')

        # Deleting model 'Location'
        db.delete_table(u'flyer_location')

        # Deleting model 'Flyer'
        db.delete_table(u'flyer_flyer')

        # Deleting model 'Product'
        db.delete_table(u'flyer_product')

        # Deleting model 'Brand'
        db.delete_table(u'flyer_brand')

        # Deleting model 'Category'
        db.delete_table(u'flyer_category')

        # Deleting model 'Sale'
        db.delete_table(u'flyer_sale')

        # Deleting model 'Saving'
        db.delete_table(u'flyer_saving')


    models = {
        u'flyer.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'flyer.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'flyer.flyer': {
            'Meta': {'object_name': 'Flyer'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'flyer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Location']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'flyer.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flyer_crawl': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Store']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'flyer.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'flyer.sale': {
            'Meta': {'object_name': 'Sale'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Brand']", 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Category']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'flyer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Flyer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'price_reg': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price_sale': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Product']"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'flyer.saving': {
            'Meta': {'object_name': 'Saving'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flyer.Sale']"}),
            'saving': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'flyer.store': {
            'Meta': {'object_name': 'Store'},
            'flyer_crawl': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['flyer']