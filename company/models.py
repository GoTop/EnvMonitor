from __future__ import unicode_literals
#coding=utf8
from django.db import models
from db_baise_models import *

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.


class Company(models.Model):
    #企业信息

    #监测点位
    DISTRICT_CHOICES = (
        (u'右江区', '右江区'),
        (u'田阳', '田阳'),
        (u'田东', '田东'),
        (u'平果', '平果'),
        (u'德保', '德保'),
        (u'靖西', '靖西'),
        (u'那坡', '那坡'),
        (u'凌云', '凌云'),
        (u'乐业', '乐业'),
        (u'田林', '田林'),
        (u'隆林', '隆林'),
        (u'西林', '西林'),
    )

    #行业
    TRADE_CHOICES = (
        (u'糖厂', '糖厂'),
        (u'造纸厂', '造纸厂'),
        (u'酒精厂', '酒精厂'),
        (u'淀粉厂', '淀粉厂'),
        (u'水泥厂', '水泥厂'),
        (u'化工厂', '化工厂'),
        (u'污水处理厂', '污水处理厂'),
        (u'垃圾填埋厂', '垃圾填埋厂'),
        (u'其他', '其他'),
    )

    #company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)  # Field name made lowercase.
    district = models.CharField(max_length=6, choices=DISTRICT_CHOICES)
    tel = models.TextField(blank=True)  # Field name made lowercase.
    organ_code = models.TextField(blank=True)  # Field name made lowercase.
    fax = models.TextField(blank=True)  # Field name made lowercase.
    post_code = models.TextField(blank=True)  # Field name made lowercase.
    law_person = models.CharField(max_length=10, blank=True)  # Field name made lowercase.
    email = models.TextField(blank=True)  # Field name made lowercase.
    setup_time = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(max_length=10, blank=True)  # Field name made lowercase.
    address = models.CharField(max_length=80, blank=True)  # Field name made lowercase.
    trade = models.CharField(max_length=6, choices=TRADE_CHOICES)

    class Meta:
        db_table = 'Company'


class MaintainCompany(models.Model):
    #运维商
    #maintain_company_id = models.CharField(max_length=10)  # Field name made lowercase.
    name = models.TextField(blank=True)

    class Meta:
        db_table = 'MaintainCompany'


class Station(models.Model):
    #监测点位
    TYPE_CHOICES = (
        (u'water', '废水'),
        (u'gas', '废气'),
        (u'metal ', '重金属'),
    )
    PORT_CHOICES = (
        (u'in', '进口'),
        (u'out', '出口'),
    )
    mn = models.CharField(primary_key=True, max_length=14)  # Field name made lowercase.
    type = models.CharField(max_length=10, blank=True, choices=TYPE_CHOICES)
    company = models.ForeignKey(Company, blank=True)
    name = models.TextField(blank=True)
    in_or_out = models.CharField(max_length=10, blank=True, choices=PORT_CHOICES, default='出口')
    maintain_company = models.ForeignKey(MaintainCompany, db_column='maintain_company_id')  # Field name made lowercase.

    class Meta:
        db_table = 'Station'


class Datavalidation(models.Model):
    #数据有效性审核
    #id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('Station', db_column='MN')  # Field name made lowercase.
    year = models.CharField(max_length=10, blank=True)
    season = models.CharField(max_length=10, blank=True)
    exam_date = models.DateTimeField(blank=True, null=True)
    is_exam_pass = models.CharField(max_length=10, blank=True)
    field_field = models.DateTimeField(blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'DataValidation'


class Equipment(models.Model):
    #分析仪
    #equipment_id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('Station')  # Field name made lowercase.
    equipment_code = models.CharField(max_length=10, blank=True)
    monitor_factor = models.CharField(max_length=10, blank=True)
    manufacturer = models.CharField(max_length=10, blank=True)
    acceptance_date = models.DateTimeField(blank=True, null=True)
    is_use = models.CharField(max_length=10, blank=True)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'Equipment'


class ShutdownDate(models.Model):
    #停运时间
    #id = models.CharField(primary_key=True, max_length=10)
    company = models.ForeignKey(Company)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'ShutDownDate'


class SpecialSuprevision(models.Model):
    #国控信息
    TYPE_CHOICES = (
        (u'water', '废水'),
        (u'gas', '废气'),
        (u'metal ', '重金属'),
        (u'wastewater_treatment_plant ', '污水处理厂'),
    )
    id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('Station', db_column='mn')  # Field name made lowercase.
    year = models.CharField(max_length=10, blank=True, choices=TYPE_CHOICES)
    type = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'SpecialSuprevision'
