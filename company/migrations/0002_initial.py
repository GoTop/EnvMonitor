# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manufacturer'
        db.create_table(u'Manufacturer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column=u'ManufacturerID')),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=30, db_column=u'Remark', blank=True)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, db_column=u'LinkMan', blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, db_column=u'Phone', blank=True)),
            ('is_have_run_ipmp', self.gf('django.db.models.fields.NullBooleanField')(null=True, db_column=u'IsHaveRunIpmp', blank=True)),
        ))
        db.send_create_signal(u'company', ['Manufacturer'])

        # Adding model 'Company'
        db.create_table(u'Company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('organ_code', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('post_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('law_person', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('setup_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('trade', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'company', ['Company'])

        # Adding unique constraint on 'Company', fields ['name', 'organ_code', 'district', 'trade']
        db.create_unique(u'Company', ['name', 'organ_code', 'district', 'trade'])

        # Adding model 'MaintainCompany'
        db.create_table(u'MaintainCompany', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'company', ['MaintainCompany'])

        # Adding model 'Station'
        db.create_table(u'Station', (
            ('station_id', self.gf('django.db.models.fields.CharField')(max_length=14, primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default=u'water', max_length=10, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Company'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_or_out', self.gf('django.db.models.fields.CharField')(default=u'out', max_length=10, blank=True)),
            ('maintain_company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.MaintainCompany'], null=True)),
        ))
        db.send_create_signal(u'company', ['Station'])

        # Adding model 'DataValidation'
        db.create_table(u'DataValidation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Station'])),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('examine_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_examine_pass', self.gf('django.db.models.fields.BooleanField')()),
            ('examine_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('analyze_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_analyze_pass', self.gf('django.db.models.fields.BooleanField')(max_length=10)),
            ('analyze_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'company', ['DataValidation'])

        # Adding model 'EquipmentModel'
        db.create_table(u'EquipmentModel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'company', ['EquipmentModel'])

        # Adding model 'Equipment'
        db.create_table(u'Equipment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Station'])),
            ('equipment_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.EquipmentModel'], null=True, blank=True)),
            ('data_param', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.DataParam'], null=True, blank=True)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Manufacturer'], null=True, blank=True)),
            ('acceptance_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_use', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'company', ['Equipment'])

        # Adding model 'ShutdownDate'
        db.create_table(u'ShutDownDate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['company.Company'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'company', ['ShutdownDate'])

        # Adding model 'NationSuprevise'
        db.create_table(u'NationSuprevise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['company.Station'], unique=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal(u'company', ['NationSuprevise'])


    def backwards(self, orm):
        # Removing unique constraint on 'Company', fields ['name', 'organ_code', 'district', 'trade']
        db.delete_unique(u'Company', ['name', 'organ_code', 'district', 'trade'])

        # Deleting model 'Manufacturer'
        db.delete_table(u'Manufacturer')

        # Deleting model 'Company'
        db.delete_table(u'Company')

        # Deleting model 'MaintainCompany'
        db.delete_table(u'MaintainCompany')

        # Deleting model 'Station'
        db.delete_table(u'Station')

        # Deleting model 'DataValidation'
        db.delete_table(u'DataValidation')

        # Deleting model 'EquipmentModel'
        db.delete_table(u'EquipmentModel')

        # Deleting model 'Equipment'
        db.delete_table(u'Equipment')

        # Deleting model 'ShutdownDate'
        db.delete_table(u'ShutDownDate')

        # Deleting model 'NationSuprevise'
        db.delete_table(u'NationSuprevise')


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
        u'company.datavalidation': {
            'Meta': {'object_name': 'DataValidation', 'db_table': "u'DataValidation'"},
            'analyze_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'analyze_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examine_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examine_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_analyze_pass': ('django.db.models.fields.BooleanField', [], {'max_length': '10'}),
            'is_examine_pass': ('django.db.models.fields.BooleanField', [], {}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Station']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'company.equipment': {
            'Meta': {'object_name': 'Equipment', 'db_table': "u'Equipment'"},
            'acceptance_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'data_param': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.DataParam']", 'null': 'True', 'blank': 'True'}),
            'equipment_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.EquipmentModel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_use': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Manufacturer']", 'null': 'True', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Station']"})
        },
        u'company.equipmentmodel': {
            'Meta': {'object_name': 'EquipmentModel', 'db_table': "u'EquipmentModel'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'company.maintaincompany': {
            'Meta': {'object_name': 'MaintainCompany', 'db_table': "u'MaintainCompany'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'company.manufacturer': {
            'Meta': {'object_name': 'Manufacturer', 'db_table': "u'Manufacturer'"},
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'LinkMan'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'ManufacturerID'"}),
            'is_have_run_ipmp': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "u'IsHaveRunIpmp'", 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'Phone'", 'blank': 'True'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "u'Remark'", 'blank': 'True'})
        },
        u'company.nationsuprevise': {
            'Meta': {'object_name': 'NationSuprevise', 'db_table': "u'NationSuprevise'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['company.Station']", 'unique': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'company.shutdowndate': {
            'Meta': {'object_name': 'ShutdownDate', 'db_table': "u'ShutDownDate'"},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Company']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
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
        u'company.t_admin_area': {
            'Meta': {'object_name': 'T_Admin_area', 'db_table': "'T_AdminArea'", 'managed': 'False'},
            'area_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'AreaID'"}),
            'area_name': ('django.db.models.fields.TextField', [], {'db_column': "'AreaName'"}),
            'client_x': ('django.db.models.fields.TextField', [], {'db_column': "'ClientX'", 'blank': 'True'}),
            'client_y': ('django.db.models.fields.TextField', [], {'db_column': "'ClientY'", 'blank': 'True'}),
            'higherareaid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'HigherAreaID'", 'blank': 'True'}),
            'zoom_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'ZoomLevel'", 'blank': 'True'})
        },
        u'company.t_all_station': {
            'Meta': {'object_name': 'T_All_station', 'db_table': "'T_AllStation'", 'managed': 'False'},
            'comp_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'CompID'", 'blank': 'True'}),
            'higher_out_id': ('django.db.models.fields.TextField', [], {'db_column': "'HigherOutID'", 'blank': 'True'}),
            'ionline': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'IOnline'", 'blank': 'True'}),
            'is_1015building': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'Is1015Building'", 'blank': 'True'}),
            'is_country_control': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsCountryControl'", 'blank': 'True'}),
            'is_emergency': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsEmergency'", 'blank': 'True'}),
            'is_facility': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsFacility'", 'blank': 'True'}),
            'is_import_export': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'IsImportexport'", 'blank': 'True'}),
            'is_pass_accept': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsPassAccept'", 'blank': 'True'}),
            'is_show': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsShow'", 'blank': 'True'}),
            'lat_warp': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'LatWarp'", 'decimal_places': '9', 'max_digits': '12'}),
            'latitude': ('django.db.models.fields.TextField', [], {'db_column': "'Latitude'", 'blank': 'True'}),
            'long_warp': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'LongWarp'", 'decimal_places': '9', 'max_digits': '12'}),
            'longitude': ('django.db.models.fields.TextField', [], {'db_column': "'Longitude'", 'blank': 'True'}),
            'mn_pwd': ('django.db.models.fields.TextField', [], {'db_column': "'MNPwd'", 'blank': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'OrderID'", 'blank': 'True'}),
            'param_codes': ('django.db.models.fields.TextField', [], {'db_column': "'ParamCodes'", 'blank': 'True'}),
            'pass_accept_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'PassAcceptTime'", 'blank': 'True'}),
            'pollute_level_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'PolluteLevelIndex'", 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "'ShortName'", 'blank': 'True'}),
            'standard_demo': ('django.db.models.fields.TextField', [], {'db_column': "'StandardDemo'", 'blank': 'True'}),
            'state_year': ('django.db.models.fields.TextField', [], {'db_column': "'StateYear'", 'blank': 'True'}),
            'station_id': ('django.db.models.fields.TextField', [], {'primary_key': 'True', 'db_column': "'StationID'"}),
            'station_name': ('django.db.models.fields.TextField', [], {'db_column': "'StationName'", 'blank': 'True'}),
            't_admin_area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Admin_area']", 'null': 'True', 'db_column': "'AreaID'", 'blank': 'True'}),
            't_attend_degree': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Attend_degree']", 'null': 'True', 'db_column': "'AttendID'", 'blank': 'True'}),
            't_station_kind': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Station_kind']", 'null': 'True', 'db_column': "'KindID'", 'blank': 'True'}),
            't_trade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Trade']", 'null': 'True', 'db_column': "'TradeID'", 'blank': 'True'}),
            't_transfers': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Transfers']", 'null': 'True', 'db_column': "'TransfersID'", 'blank': 'True'}),
            't_water_shed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Water_shed']", 'null': 'True', 'db_column': "'WaterShedID'", 'blank': 'True'})
        },
        u'company.t_attend_degree': {
            'Meta': {'object_name': 'T_Attend_degree', 'db_table': "'T_AttendDegree'", 'managed': 'False'},
            'attend_id': ('django.db.models.fields.IntegerField', [], {'db_column': "'AttendID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'db_column': "'Remark'", 'blank': 'True'})
        },
        u'company.t_comp_info': {
            'Meta': {'object_name': 'T_Comp_info', 'db_table': "'T_CompInfo'", 'managed': 'False'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'AddTime'"}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '160', 'db_column': "'Address'", 'blank': 'True'}),
            'area_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'AreaID'", 'blank': 'True'}),
            'boiler_coal': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'BoilerCoal'", 'decimal_places': '6', 'max_digits': '18'}),
            'boiler_cou': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'BoilerCou'", 'blank': 'True'}),
            'boiler_have_decoke': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'BoilerHaveDecoke'", 'blank': 'True'}),
            'boiler_is_run': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'BoilerIsRun'", 'blank': 'True'}),
            'boiler_ton': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'BoilerTon'", 'decimal_places': '6', 'max_digits': '18'}),
            'boiler_type': ('django.db.models.fields.TextField', [], {'db_column': "'BoilerType'", 'blank': 'True'}),
            'build_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'BuildTime'", 'blank': 'True'}),
            'comp_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'CompID'"}),
            'comp_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'CompName'"}),
            'comp_properties': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'CompProperties'", 'blank': 'True'}),
            'contact_man': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_column': "'ContactMan'", 'blank': 'True'}),
            'contact_man_phone': ('django.db.models.fields.TextField', [], {'db_column': "'ContactManPhone'", 'blank': 'True'}),
            'country_attribute': ('django.db.models.fields.TextField', [], {'db_column': "'CountryAttribute'", 'blank': 'True'}),
            'demo': ('django.db.models.fields.TextField', [], {'db_column': "'Demo'", 'blank': 'True'}),
            'dispose_ability': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'DisposeAbility'", 'decimal_places': '0', 'max_digits': '9'}),
            'email': ('django.db.models.fields.TextField', [], {'db_column': "'Email'", 'blank': 'True'}),
            'factory_area': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'FactoryArea'", 'decimal_places': '2', 'max_digits': '10'}),
            'fax': ('django.db.models.fields.TextField', [], {'db_column': "'Fax'", 'blank': 'True'}),
            'function_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'FunctionID'", 'blank': 'True'}),
            'hs_ename': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_column': "'HsEName'", 'blank': 'True'}),
            'idnkiln_cou': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'IdnkilnCou'", 'blank': 'True'}),
            'img_save_path': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'ImgSavePath'", 'blank': 'True'}),
            'industry_park_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'IndustryParkName'", 'blank': 'True'}),
            'is_facility': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsFacility'", 'blank': 'True'}),
            'is_gb_judge': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsGBJudge'", 'blank': 'True'}),
            'is_have_jury_project': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsHaveJuryProject'", 'blank': 'True'}),
            'is_occur_jury': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsOccurJury'", 'blank': 'True'}),
            'issuing_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'IssuingTime'", 'blank': 'True'}),
            'jury_demo': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'db_column': "'JuryDemo'", 'blank': 'True'}),
            'kiln_coal': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'KilnCoal'", 'decimal_places': '6', 'max_digits': '18'}),
            'kiln_have_decoke': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'KilnHaveDecoke'", 'blank': 'True'}),
            'kiln_is_run': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'KilnIsRun'", 'blank': 'True'}),
            'kiln_type': ('django.db.models.fields.TextField', [], {'db_column': "'kilnType'", 'blank': 'True'}),
            'last_year_fine_money': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'LastYearFineMoney'", 'decimal_places': '0', 'max_digits': '9'}),
            'last_year_pay_money': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'LastYearPayMoney'", 'decimal_places': '0', 'max_digits': '9'}),
            'latitude': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'law_person': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'LawPerson'", 'blank': 'True'}),
            'law_person_mum': ('django.db.models.fields.TextField', [], {'db_column': "'LawPersonMum'", 'blank': 'True'}),
            'link_man': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'LinkMan'", 'blank': 'True'}),
            'linkman_phone': ('django.db.models.fields.TextField', [], {'db_column': "'LinkManPhone'", 'blank': 'True'}),
            'longitude': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organ_code': ('django.db.models.fields.TextField', [], {'db_column': "'OrganCode'", 'blank': 'True'}),
            'out_where_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_column': "'OutWhereCode'", 'blank': 'True'}),
            'pollute_level_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'PolluteLevelIndex'", 'blank': 'True'}),
            'post_code': ('django.db.models.fields.TextField', [], {'db_column': "'Postcode'", 'blank': 'True'}),
            'reg_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_column': "'RegType'", 'blank': 'True'}),
            'setup_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'SetUpTime'", 'blank': 'True'}),
            'sew_fac_cou': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SewFacCou'", 'blank': 'True'}),
            'sfexploit_va': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'SFexploitVa'", 'decimal_places': '0', 'max_digits': '9'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'ShortName'", 'blank': 'True'}),
            'site_url': ('django.db.models.fields.TextField', [], {'db_column': "'SiteUrl'", 'blank': 'True'}),
            'tel': ('django.db.models.fields.TextField', [], {'db_column': "'Tel'", 'blank': 'True'}),
            'tel_code_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'TelCodeID'", 'blank': 'True'}),
            'tlfac_cap': ('django.db.models.fields.TextField', [], {'db_column': "'TLFacCap'", 'blank': 'True'}),
            'tlfac_cou': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'TLFacCou'", 'blank': 'True'}),
            'trade_id': ('django.db.models.fields.TextField', [], {'db_column': "'TradeID'", 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_column': "'UserID'"}),
            'waste_emission_id': ('django.db.models.fields.TextField', [], {'db_column': "'WasteEmissionID'", 'blank': 'True'}),
            'water_shed_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'WaterShedID'", 'blank': 'True'})
        },
        u'company.t_data_param': {
            'Meta': {'object_name': 'T_Data_param', 'db_table': "'T_DataParam'", 'managed': 'False'},
            'app_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'AppValue'", 'decimal_places': '5', 'max_digits': '18'}),
            'data_precision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'DataPrecision'", 'blank': 'True'}),
            'is_have_cou': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsHaveCou'", 'blank': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'OrderID'", 'blank': 'True'}),
            'param_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "'ParamCode'"}),
            'param_kind': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'ParamKind'", 'blank': 'True'}),
            'param_remark': ('django.db.models.fields.TextField', [], {'db_column': "'ParamRemark'", 'blank': 'True'}),
            'param_unit': ('django.db.models.fields.TextField', [], {'db_column': "'ParamUnit'", 'blank': 'True'}),
            'standard_code': ('django.db.models.fields.TextField', [], {'db_column': "'StandardCode'", 'blank': 'True'}),
            'standard_values': ('django.db.models.fields.TextField', [], {'db_column': "'StandardValues'", 'blank': 'True'})
        },
        u'company.t_datatype': {
            'Meta': {'object_name': 'T_Datatype', 'db_table': "'T_DataType'", 'managed': 'False'},
            'data_type': ('django.db.models.fields.TextField', [], {'db_column': "'DataType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'db_column': "'Remark'", 'blank': 'True'})
        },
        u'company.t_exam_project': {
            'Meta': {'object_name': 'T_Exam_project', 'db_table': "'T_ExamProject'", 'managed': 'False'},
            'analyse_id': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'db_column': "'AnalyseID'", 'blank': 'True'}),
            'asc_id': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'AscID'", 'blank': 'True'}),
            'd_max_limit': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'dMaxLimit'", 'decimal_places': '6', 'max_digits': '18'}),
            'd_min_limit': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'dMinLimit'", 'decimal_places': '6', 'max_digits': '18'}),
            'data_precision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'DataPrecision'", 'blank': 'True'}),
            'error_max_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'ErrorMaxValue'", 'decimal_places': '4', 'max_digits': '10'}),
            'error_min_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'ErrorMinValue'", 'decimal_places': '4', 'max_digits': '10'}),
            'exam_parm_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'ExamParmID'"}),
            'high_limit_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'HighLimitValue'", 'decimal_places': '4', 'max_digits': '18'}),
            'is_enable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsEnable'", 'blank': 'True'}),
            'is_main': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsMain'", 'blank': 'True'}),
            'is_send': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsSend'", 'blank': 'True'}),
            'is_used': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsUsed'", 'blank': 'True'}),
            'k_unit': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'kUnit'", 'decimal_places': '2', 'max_digits': '8'}),
            'low_limit_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'LowLimitValue'", 'decimal_places': '4', 'max_digits': '18'}),
            'minimum_level': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'MinimumLevel'", 'decimal_places': '4', 'max_digits': '18'}),
            'model': ('django.db.models.fields.TextField', [], {'db_column': "'Model'", 'blank': 'True'}),
            'number': ('django.db.models.fields.TextField', [], {'db_column': "'Number'", 'blank': 'True'}),
            'param_unit': ('django.db.models.fields.TextField', [], {'db_column': "'ParamUnit'", 'blank': 'True'}),
            'sort_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'SortID'", 'blank': 'True'}),
            't_all_station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_All_station']", 'db_column': "'StationID'"}),
            't_data_param': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Data_param']", 'null': 'True', 'db_column': "'ParamCode'", 'blank': 'True'}),
            't_manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Manufacturer']", 'null': 'True', 'db_column': "'ManufacturerID'", 'blank': 'True'}),
            'total_unit': ('django.db.models.fields.TextField', [], {'db_column': "'TotalUnit'", 'blank': 'True'})
        },
        u'company.t_manufacturer': {
            'Meta': {'object_name': 'T_Manufacturer', 'db_table': "'T_Manufacturer'", 'managed': 'False'},
            'is_have_run_ipmp': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsHaveRunIpmp'", 'blank': 'True'}),
            'link_man': ('django.db.models.fields.TextField', [], {'db_column': "'LinkMan'", 'blank': 'True'}),
            'manufacturer_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'ManufacturerID'"}),
            'phone': ('django.db.models.fields.TextField', [], {'db_column': "'Phone'", 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'db_column': "'Remark'", 'blank': 'True'})
        },
        u'company.t_station_kind': {
            'Meta': {'object_name': 'T_Station_kind', 'db_table': "'T_StationKind'", 'managed': 'False'},
            'is_mobile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsMobile'", 'blank': 'True'}),
            'kind_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'KindID'"}),
            'kind_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'KindName'", 'blank': 'True'})
        },
        u'company.t_superscale': {
            'Meta': {'object_name': 'T_Superscale', 'db_table': "'T_Superscale'", 'managed': 'False'},
            'exam_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'ExamID'"}),
            'is_apply': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsApply'", 'blank': 'True'}),
            'level_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'LevelID'", 'blank': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'MaxValue'", 'blank': 'True'}),
            's': ('django.db.models.fields.TextField', [], {'db_column': "'DataType'", 'blank': 'True'}),
            'standard_demo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'StandardDemo'", 'blank': 'True'}),
            'standard_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'StandardValue'", 'blank': 'True'}),
            't_exam_project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.T_Exam_project']", 'db_column': "'ExamParmID'"})
        },
        u'company.t_trade': {
            'Meta': {'object_name': 'T_Trade', 'db_table': "'T_Trade'", 'managed': 'False'},
            'higher_trade_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "'HigherTradeID'", 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'db_column': "'Remark'", 'blank': 'True'}),
            'trade_demo': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'db_column': "'TradeDemo'", 'blank': 'True'}),
            'trade_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'TradeID'"})
        },
        u'company.t_transfers': {
            'Meta': {'object_name': 'T_Transfers', 'db_table': "'T_Transfers'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'db_column': "'Remark'", 'blank': 'True'}),
            'transfers_id': ('django.db.models.fields.IntegerField', [], {'db_column': "'TransfersID'"})
        },
        u'company.t_water_shed': {
            'Meta': {'object_name': 'T_Water_shed', 'db_table': "'T_Watershed'", 'managed': 'False'},
            'day_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'DayValue'", 'decimal_places': '0', 'max_digits': '9'}),
            'direction_index': ('django.db.models.fields.TextField', [], {'db_column': "'DirectionIndex'", 'blank': 'True'}),
            'font_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'FontType'", 'blank': 'True'}),
            'higher_water_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "'HigherWaterID'", 'blank': 'True'}),
            'hour_value': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'HourValue'", 'decimal_places': '0', 'max_digits': '9'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_load': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'IsLoad'", 'blank': 'True'}),
            'lat': ('django.db.models.fields.TextField', [], {'db_column': "'Lat'", 'blank': 'True'}),
            'long': ('django.db.models.fields.TextField', [], {'db_column': "'Long'", 'blank': 'True'}),
            'long_lats': ('django.db.models.fields.TextField', [], {'db_column': "'LongLats'", 'blank': 'True'}),
            'name_lng_lat': ('django.db.models.fields.TextField', [], {'db_column': "'NameLngLat'", 'blank': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'OrderID'", 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'db_column': "'Remark'", 'blank': 'True'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'db_column': "'Speed'", 'decimal_places': '2', 'max_digits': '10'}),
            'water_border': ('django.db.models.fields.TextField', [], {'db_column': "'WaterBorder'", 'blank': 'True'}),
            'water_shed_id': ('django.db.models.fields.IntegerField', [], {'db_column': "'WaterShedID'"})
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
        }
    }

    complete_apps = ['company']