# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Price.stone_slinger'
        db.alter_column(u'core_price', 'stone_slinger', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True))

        # Changing field 'Price.tractor_trailer'
        db.alter_column(u'core_price', 'tractor_trailer', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True))

        # Changing field 'Price.tri_axel'
        db.alter_column(u'core_price', 'tri_axel', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True))

    def backwards(self, orm):

        # Changing field 'Price.stone_slinger'
        db.alter_column(u'core_price', 'stone_slinger', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10))

        # Changing field 'Price.tractor_trailer'
        db.alter_column(u'core_price', 'tractor_trailer', self.gf('django.db.models.fields.IntegerField')(default='0', max_length=10))

        # Changing field 'Price.tri_axel'
        db.alter_column(u'core_price', 'tri_axel', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10))

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
            'stone_slinger': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tractor_trailer': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tri_axel': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
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