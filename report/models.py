# coding=utf-8
from django.db import models
from company.models import Station
# Create your models here.

class DataParam(models.Model):
    """
    与DB_baise数据库中的T_Data_param表相同
    因为Django不支持不同的数据库之间建立外键，所以将T_Data_param表复制到EnvMonitor数据库中
    """
    param_code = models.CharField(db_column='ParamCode', max_length=3, primary_key=True)  # Field name made lowercase.
    standard_code = models.TextField(db_column='StandardCode', blank=True)  # Field name made lowercase.
    param_remark = models.TextField(db_column='ParamRemark', blank=True)  # Field name made lowercase.
    param_kind = models.IntegerField(db_column='ParamKind', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    param_unit = models.TextField(db_column='ParamUnit', blank=True)  # Field name made lowercase.
    data_precision = models.IntegerField(db_column='DataPrecision', blank=True, null=True)  # Field name made lowercase.
    is_have_cou = models.NullBooleanField(db_column='IsHaveCou')  # Field name made lowercase.
    standard_values = models.TextField(db_column='StandardValues', blank=True)  # Field name made lowercase.
    app_value = models.DecimalField(db_column='AppValue', max_digits=18, decimal_places=5, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataParam'


class HourReport(models.Model):
    #小时报表
    #id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('company.Station', db_column='mn')  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    data_param = models.ForeignKey('DataParam')
    value = models.IntegerField(blank=True, null=True)
    is_abnormal = models.BooleanField(max_length=10, blank=True)

    class Meta:
        db_table = 'HourReport'


class Standard(models.Model):
    #排放标准
    #id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('company.Station', db_column='mn')  # Field name made lowercase.
    data_param = models.ForeignKey('DataParam')
    upper_limit = models.IntegerField(blank=True, null=True)
    lower_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Standard'


class Revise(models.Model):
    #修约
    #id = models.ForeignKey(Hourreport, db_column='id', primary_key=True)
    hour_report_id = models.CharField(max_length=10, blank=True)
    value = models.CharField(max_length=10, blank=True)
    comment = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'Revise'


class Message(models.Model):
    #短信
    #id = models.ForeignKey(Hourreport, db_column='id', primary_key=True)
    sent_to = models.IntegerField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True)
    mn = models.CharField(db_column='MN', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Message'