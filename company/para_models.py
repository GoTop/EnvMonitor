# coding=utf-8
__author__ = 'GoTop'
from django.db import models
from company.models import *
from company.db_baise_models import *


class T_Water_shed(models.Model):
    water_shed_id = models.IntegerField(db_column='WaterShedID')  # Field name made lowercase.
    higher_water_id = models.BigIntegerField(db_column='HigherWaterID', blank=True,
                                             null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True)  # Field name made lowercase.
    hour_value = models.DecimalField(db_column='HourValue', max_digits=9, decimal_places=0, blank=True,
                                     null=True)  # Field name made lowercase.
    day_value = models.DecimalField(db_column='DayValue', max_digits=9, decimal_places=0, blank=True,
                                    null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    long = models.TextField(db_column='Long', blank=True)  # Field name made lowercase.
    lat = models.TextField(db_column='Lat', blank=True)  # Field name made lowercase.
    speed = models.DecimalField(db_column='Speed', max_digits=10, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    long_lats = models.TextField(db_column='LongLats',
                                 blank=True)  # Field name made lowercase. This field type is a guess.
    direction_index = models.TextField(db_column='DirectionIndex', blank=True)  # Field name made lowercase.
    is_load = models.NullBooleanField(db_column='IsLoad', blank=True, null=True)  # Field name made lowercase.
    name_lng_lat = models.TextField(db_column='NameLngLat',
                                    blank=True)  # Field name made lowercase. This field type is a guess.
    font_type = models.IntegerField(db_column='FontType', blank=True, null=True)  # Field name made lowercase.
    water_border = models.TextField(db_column='WaterBorder',
                                    blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'T_Watershed'


class T_Station_kind(models.Model):
    kind_id = models.IntegerField(db_column='KindID', primary_key=True)  # Field name made lowercase.
    kind_name = models.CharField(db_column='KindName', max_length=30, blank=True)  # Field name made lowercase.
    is_mobile = models.NullBooleanField(db_column='IsMobile', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_StationKind'


class T_Attend_degree(models.Model):
    attend_id = models.IntegerField(db_column='AttendID')  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_AttendDegree'


class T_Transfers(models.Model):
    transfers_id = models.IntegerField(db_column='TransfersID')  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Transfers'


class T_Trade(models.Model):
    #行业信息
    trade_id = models.IntegerField(db_column='TradeID', primary_key=True)  # Field name made lowercase.
    higher_trade_id = models.BigIntegerField(db_column='HigherTradeID', blank=True,
                                             null=True)  # Field name made lowercase.
    #行业名称
    remark = models.TextField(db_column='Remark', blank=True)  # Field name made lowercase.
    trade_demo = models.CharField(db_column='TradeDemo', max_length=1000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Trade'


class T_Manufacturer(models.Model):
    manufacturer_id = models.IntegerField(db_column='ManufacturerID', primary_key=True)  # Field name made lowercase.
    #厂商名称
    remark = models.TextField(db_column='Remark', blank=True)  # Field name made lowercase.
    link_man = models.TextField(db_column='LinkMan', blank=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True)  # Field name made lowercase.
    #是否有运营资格
    is_have_run_ipmp = models.NullBooleanField(db_column='IsHaveRunIpmp', blank=True,
                                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Manufacturer'




