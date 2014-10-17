# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataParam'
        db.create_table('DataParam', (
            ('param_code', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column='ParamCode')),
            ('standard_code', self.gf('django.db.models.fields.TextField')(db_column='StandardCode', blank=True)),
            ('param_remark', self.gf('django.db.models.fields.TextField')(db_column='ParamRemark', blank=True)),
            ('param_kind', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='ParamKind', blank=True)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='OrderID', blank=True)),
            ('param_unit', self.gf('django.db.models.fields.TextField')(null=True, db_column='ParamUnit', blank=True)),
            ('data_precision', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='DataPrecision', blank=True)),
            ('is_have_cou', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column='IsHaveCou', blank=True)),
            ('standard_values', self.gf('django.db.models.fields.TextField')(null=True, db_column='StandardValues', blank=True)),
            ('app_value', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column='AppValue', decimal_places=5, max_digits=18)),
        ))
        db.send_create_signal(u'report', ['DataParam'])

        # Adding model 'HourReport'
        db.create_table('HourReport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Station'], db_column='mn')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_param', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.DataParam'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_abnormal', self.gf('django.db.models.fields.BooleanField')(max_length=10)),
        ))
        db.send_create_signal(u'report', ['HourReport'])

        # Adding model 'Standard'
        db.create_table('Standard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Station'], db_column='mn')),
            ('data_param', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.DataParam'])),
            ('upper_limit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lower_limit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['Standard'])

        # Adding model 'Revise'
        db.create_table('Revise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hour_report_id', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'report', ['Revise'])

        # Adding model 'Message'
        db.create_table('Message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sent_to', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sent_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mn', self.gf('django.db.models.fields.CharField')(max_length=10, db_column='MN', blank=True)),
        ))
        db.send_create_signal(u'report', ['Message'])

        # Adding model 'AbnormalData'
        db.create_table('AbnormalData', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_time', self.gf('django.db.models.fields.DateTimeField')(db_column='DataTime')),
            ('mn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Station'], db_column='mn')),
            ('param_code', self.gf('django.db.models.fields.CharField')(max_length=3, db_column='ParamCode')),
            ('data_type', self.gf('django.db.models.fields.CharField')(max_length=5, db_column='DataType')),
            ('original_value', self.gf('django.db.models.fields.DecimalField')(db_column='original_value', decimal_places=4, max_digits=18)),
            ('modify_value', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, db_column='modify_value', decimal_places=4, max_digits=18)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column='modify_time', blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='user_id', blank=True)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=500, db_column='remark', blank=True)),
        ))
        db.send_create_signal(u'report', ['AbnormalData'])

        # Adding unique constraint on 'AbnormalData', fields ['data_time', 'mn', 'param_code', 'data_type']
        db.create_unique('AbnormalData', ['DataTime', 'mn', 'ParamCode', 'DataType'])


    def backwards(self, orm):
        # Removing unique constraint on 'AbnormalData', fields ['data_time', 'mn', 'param_code', 'data_type']
        db.delete_unique('AbnormalData', ['DataTime', 'mn', 'ParamCode', 'DataType'])

        # Deleting model 'DataParam'
        db.delete_table('DataParam')

        # Deleting model 'HourReport'
        db.delete_table('HourReport')

        # Deleting model 'Standard'
        db.delete_table('Standard')

        # Deleting model 'Revise'
        db.delete_table('Revise')

        # Deleting model 'Message'
        db.delete_table('Message')

        # Deleting model 'AbnormalData'
        db.delete_table('AbnormalData')


    models = {
        u'company.company': {
            'Meta': {'unique_together': "((u'name', u'organ_code', u'district', u'trade'),)", 'object_name': 'Company', 'db_table': "u'Company'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'law_person': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'organ_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'setup_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trade': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'company.maintaincompany': {
            'Meta': {'object_name': 'MaintainCompany', 'db_table': "u'MaintainCompany'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'company.station': {
            'Meta': {'object_name': 'Station', 'db_table': "u'Station'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Company']", 'null': 'True', 'blank': 'True'}),
            'in_or_out': ('django.db.models.fields.CharField', [], {'default': "u'out'", 'max_length': '10', 'blank': 'True'}),
            'maintain_company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.MaintainCompany']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'station_id': ('django.db.models.fields.CharField', [], {'max_length': '14', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "u'water'", 'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'report.abnormaldata': {
            'Meta': {'unique_together': "(('data_time', 'mn', 'param_code', 'data_type'),)", 'object_name': 'AbnormalData', 'db_table': "'AbnormalData'"},
            'data_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'DataTime'"}),
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_column': "'DataType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Station']", 'db_column': "'mn'"}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'modify_time'", 'blank': 'True'}),
            'modify_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'modify_value'", 'decimal_places': '4', 'max_digits': '18'}),
            'original_value': ('django.db.models.fields.DecimalField', [], {'db_column': "'original_value'", 'decimal_places': '4', 'max_digits': '18'}),
            'param_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'ParamCode'"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'remark'", 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'user_id'", 'blank': 'True'})
        },
        u'report.dataparam': {
            'Meta': {'object_name': 'DataParam', 'db_table': "'DataParam'"},
            'app_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'AppValue'", 'decimal_places': '5', 'max_digits': '18'}),
            'data_precision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'DataPrecision'", 'blank': 'True'}),
            'is_have_cou': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsHaveCou'", 'blank': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'OrderID'", 'blank': 'True'}),
            'param_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "'ParamCode'"}),
            'param_kind': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'ParamKind'", 'blank': 'True'}),
            'param_remark': ('django.db.models.fields.TextField', [], {'db_column': "'ParamRemark'", 'blank': 'True'}),
            'param_unit': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'ParamUnit'", 'blank': 'True'}),
            'standard_code': ('django.db.models.fields.TextField', [], {'db_column': "'StandardCode'", 'blank': 'True'}),
            'standard_values': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'StandardValues'", 'blank': 'True'})
        },
        u'report.hourreport': {
            'Meta': {'object_name': 'HourReport', 'db_table': "'HourReport'"},
            'data_param': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.DataParam']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_abnormal': ('django.db.models.fields.BooleanField', [], {'max_length': '10'}),
            'mn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Station']", 'db_column': "'mn'"}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'report.message': {
            'Meta': {'object_name': 'Message', 'db_table': "'Message'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mn': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_column': "'MN'", 'blank': 'True'}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sent_to': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'report.revise': {
            'Meta': {'object_name': 'Revise', 'db_table': "'Revise'"},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'hour_report_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'report.standard': {
            'Meta': {'object_name': 'Standard', 'db_table': "'Standard'"},
            'data_param': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.DataParam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lower_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Station']", 'db_column': "'mn'"}),
            'upper_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['report']