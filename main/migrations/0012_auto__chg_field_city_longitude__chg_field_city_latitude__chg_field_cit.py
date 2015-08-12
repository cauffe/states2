# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'City.longitude'
        db.alter_column(u'main_city', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'City.latitude'
        db.alter_column(u'main_city', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'City.zip_code'
        db.alter_column(u'main_city', 'zip_code', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'City.longitude'
        raise RuntimeError("Cannot reverse this migration. 'City.longitude' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'City.longitude'
        db.alter_column(u'main_city', 'longitude', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'City.latitude'
        raise RuntimeError("Cannot reverse this migration. 'City.latitude' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'City.latitude'
        db.alter_column(u'main_city', 'latitude', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'City.zip_code'
        raise RuntimeError("Cannot reverse this migration. 'City.zip_code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'City.zip_code'
        db.alter_column(u'main_city', 'zip_code', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'main.city': {
            'Meta': {'object_name': 'City'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.State']", 'null': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'main.statecapital': {
            'Meta': {'object_name': 'StateCapital'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.State']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['main']