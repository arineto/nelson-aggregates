# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Price'
        db.create_table(u'core_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quarry', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('tri_axel', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('tractor_trailer', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('stone_slinger', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'core', ['Price'])

        # Adding model 'Polygon'
        db.create_table(u'core_polygon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('points', self.gf('django.db.models.fields.CharField')(max_length=100000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Polygon'])

        # Adding M2M table for field prices on 'Polygon'
        m2m_table_name = db.shorten_name(u'core_polygon_prices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('polygon', models.ForeignKey(orm[u'core.polygon'], null=False)),
            ('price', models.ForeignKey(orm[u'core.price'], null=False))
        ))
        db.create_unique(m2m_table_name, ['polygon_id', 'price_id'])

        # Adding model 'Quarry'
        db.create_table(u'core_quarry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('delivery_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mailing_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('office', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('toll', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sales', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['Quarry'])


    def backwards(self, orm):
        # Deleting model 'Price'
        db.delete_table(u'core_price')

        # Deleting model 'Polygon'
        db.delete_table(u'core_polygon')

        # Removing M2M table for field prices on 'Polygon'
        db.delete_table(db.shorten_name(u'core_polygon_prices'))

        # Deleting model 'Quarry'
        db.delete_table(u'core_quarry')


    models = {
        u'core.polygon': {
            'Meta': {'object_name': 'Polygon'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.CharField', [], {'max_length': '100000'}),
            'prices': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Price']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'core.price': {
            'Meta': {'object_name': 'Price'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quarry': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'stone_slinger': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'tractor_trailer': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'tri_axel': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'core.quarry': {
            'Meta': {'object_name': 'Quarry'},
            'delivery_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mailing_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sales': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'toll': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['core']