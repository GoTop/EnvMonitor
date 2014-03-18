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

class Manufacturer(models.Model):
    id = models.IntegerField(db_column='ManufacturerID', primary_key=True)  # Field name made lowercase.
    #厂商名称
    remark = models.TextField(db_column='Remark', blank=True)  # Field name made lowercase.
    link_man = models.TextField(db_column='LinkMan', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    #是否有运营资格
    is_have_run_ipmp = models.NullBooleanField(db_column='IsHaveRunIpmp', blank=True,
                                               null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Manufacturer'


class Company(models.Model):
    #企业信息

    #监测点位
    DISTRICT_CHOICES = (
        ('右江区', '右江区'),
        ('田阳', '田阳'),
        ('田东', '田东'),
        ('平果', '平果'),
        ('德保', '德保'),
        ('靖西', '靖西'),
        ('那坡', '那坡'),
        ('凌云', '凌云'),
        ('乐业', '乐业'),
        ('田林', '田林'),
        ('隆林', '隆林'),
        ('西林', '西林'),
    )

    #行业
    TRADE_CHOICES = (
        ('sugar_factory', '糖厂'),
        ('paper_mill', '造纸厂'),
        ('alcohol_plant', '酒精厂'),
        ('starch_plant', '淀粉厂'),
        ('cement_plant', '水泥厂'),
        ('chemical_plant', '化工厂'),
        ('wastewater_treatment_plant', '污水处理厂'),
        ('landfills', '垃圾填埋厂'),
        ('metal', '重金属'),
        ('other', '其他'),
    )

    #company_id = models.IntegerField(primary_key=True)
    #企业名称
    name = models.CharField(max_length=50)  # Field name made lowercase.
    #地区
    district = models.CharField(max_length=6, choices=DISTRICT_CHOICES)
    #联系电话
    tel = models.TextField(blank=True)  # Field name made lowercase.
    #组织机构代码
    organ_code = models.TextField(blank=True)  # Field name made lowercase.
    fax = models.TextField(blank=True)  # Field name made lowercase.
    #邮政编码
    post_code = models.TextField(blank=True)  # Field name made lowercase.
    #法人代表
    law_person = models.CharField(max_length=10, blank=True)  # Field name made lowercase.

    email = models.EmailField(blank=True)  # Field name made lowercase.
    #投产日期
    setup_time = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    contact = models.CharField(max_length=10, blank=True)  # Field name made lowercase.
    #地址
    address = models.CharField(max_length=80, blank=True)  # Field name made lowercase.
    #行业类型
    trade = models.CharField(max_length=6, choices=TRADE_CHOICES)

    class Meta:
        db_table = 'Company'
        verbose_name = '企业'
        verbose_name_plural = '企业'


class MaintainCompany(models.Model):
    #运维商
    #maintain_company_id = models.CharField(max_length=10)  # Field name made lowercase.
    name = models.TextField(blank=True)

    class Meta:
        db_table = 'MaintainCompany'
        verbose_name = '运维商'
        verbose_name_plural = '运维商'


class Station(models.Model):
    #监测点位
    TYPE_CHOICES = (
        ('water', '废水'),
        ('gas', '废气'),
        ('metal ', '重金属'),
    )
    PORT_CHOICES = (
        ('in', '进口'),
        ('out', '出口'),
    )
    mn = models.CharField(primary_key=True, max_length=14)  # Field name made lowercase.
    #水或气
    type = models.CharField(max_length=10, blank=True, choices=TYPE_CHOICES, default='water')
    #企业
    company = models.ForeignKey(Company, blank=True, null=True)
    #监测点位名称
    name = models.CharField(max_length=50)
    #进口或出口，窑头或窑尾
    in_or_out = models.CharField(max_length=10, blank=True, choices=PORT_CHOICES, default='out')
    #运维单位
    maintain_company = models.ForeignKey(MaintainCompany, db_column='maintain_company_id',
                                         null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Station'
        verbose_name = '监控点位'
        verbose_name_plural = '监控点位'


class DataValidation(models.Model):
    #数据有效性审核
    YEAR_CHOICES = (
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
    )
    SEASON_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    #id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('Station', db_column='MN')  # Field name made lowercase.
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, blank=True)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES, blank=True)
    #检查日期
    examine_date = models.DateTimeField(blank=True, null=True)
    is_examine_pass = models.BooleanField(blank=True)
    examine_comment = models.TextField(blank=True)
    #比对监测日期
    analyze_date = models.DateTimeField(blank=True, null=True)
    is_analyze_pass = models.BooleanField(max_length=10, blank=True)
    analyze_comment = models.TextField(blank=True)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'DataValidation'
        verbose_name = '数据有效性审核'
        verbose_name_plural = '数据有效性审核'


class Equipment(models.Model):
    #分析仪

    #equipment_id = models.CharField(primary_key=True, max_length=10)
    station = models.ForeignKey('Station')  # Field name made lowercase.
    #设备型号
    equipment_model = models.CharField(max_length=10, blank=True)
    #data_param = models.ForeignKey('company.DataParam')
    #生成商
    manufacturer = models.ForeignKey(Manufacturer)
    #验收日期
    acceptance_date = models.DateTimeField(blank=True, null=True)
    #是否在用
    is_use = models.BooleanField(blank=True)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'Equipment'
        verbose_name = '分析仪'
        verbose_name_plural = '分析仪'


class ShutdownDate(models.Model):
    #停运时间
    #id = models.CharField(primary_key=True, max_length=10)
    company = models.ForeignKey('Company')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'ShutDownDate'
        verbose_name = '停运时间'
        verbose_name_plural = '停运时间'


class SpecialSuprevision(models.Model):
    #国控信息
    TYPE_CHOICES = (
        ('water', '废水'),
        ('gas', '废气'),
        ('metal', '重金属'),
        ('wastewater_treatment_plant', '污水处理厂'),
        ('landfills', '垃圾填埋厂'),
    )

    YEAR_CHOICES = (
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
    )

    #id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('Station', db_column='mn')  # Field name made lowercase.
    year = models.CharField(max_length=4, blank=True, choices=YEAR_CHOICES)
    type = models.CharField(max_length=10, blank=True, choices=TYPE_CHOICES)

    class Meta:
        db_table = 'SpecialSuprevision'
        verbose_name = '国控信息'
        verbose_name_plural = '国控信息'
