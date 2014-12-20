from __future__ import unicode_literals
#coding=utf8
import time
from django.core.urlresolvers import reverse
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
    #因为是从DB_baise导出的表，必须设置db_column
    id = models.AutoField(db_column='ManufacturerID', primary_key=True)  # Field name made lowercase.
    #厂商名称
    remark = models.CharField(db_column='Remark', max_length=30, blank=True)  # Field name made lowercase.
    #联系人
    contact_person = models.CharField(db_column='LinkMan', max_length=30, blank=True,
                                      null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    #是否有运营资格
    is_have_run_ipmp = models.NullBooleanField(db_column='IsHaveRunIpmp', blank=True,
                                               null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Manufacturer'

        verbose_name = '设备制造商'
        verbose_name_plural = '设备制造商'
    def __unicode__(self):
        return self.remark

class District(models.Model):
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
    name = models.CharField(max_length=6, choices=DISTRICT_CHOICES)

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
        ('糖厂', '糖厂'),
        ('造纸厂', '造纸厂'),
        ('酒精厂', '酒精厂'),
        ('淀粉厂', '淀粉厂'),
        ('水泥厂', '水泥厂'),
        ('化工厂', '化工厂'),
        ('污水处理厂', '污水处理厂'),
        ('垃圾填埋厂', '垃圾填埋厂'),
        ('重金属', '重金属'),
        ('其他', '其他'),
    )

    #company_id = models.IntegerField(primary_key=True)
    #企业名称
    name = models.CharField(max_length=50, unique=True)  # Field name made lowercase.
    #地区
    district = models.CharField(max_length=6, choices=DISTRICT_CHOICES)
    #district = models.ForeignKey(District, blank=True, null=True)

    #联系电话
    tel = models.CharField(max_length=30, blank=True)  # Field name made lowercase.
    #组织机构代码
    organ_code = models.CharField(max_length=15, blank=True)  # Field name made lowercase.
    fax = models.CharField(max_length=20, blank=True)  # Field name made lowercase.
    #邮政编码
    post_code = models.CharField(max_length=10, blank=True)  # Field name made lowercase.
    #法人代表
    law_person = models.CharField(max_length=10, blank=True)  # Field name made lowercase.

    email = models.EmailField(blank=True)  # Field name made lowercase.
    #投产日期
    setup_time = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    contact = models.CharField(max_length=10, blank=True)  # Field name made lowercase.
    #地址
    address = models.CharField(max_length=80, blank=True)  # Field name made lowercase.
    #行业类型
    trade = models.CharField(max_length=20, choices=TRADE_CHOICES, blank=True, null=True)

    is_use = models.BooleanField(default=True)

    class Meta:
        db_table = 'Company'
        verbose_name = '企业'
        verbose_name_plural = '企业'
        unique_together = (("name", "organ_code", "district", "trade"))

    def __unicode__(self):
        return self.name


class MaintainCompany(models.Model):
    #运维商
    #maintain_company_id = models.CharField(max_length=10)  # Field name made lowercase.
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'MaintainCompany'
        verbose_name = '运维商'
        verbose_name_plural = '运维商'

    def __unicode__(self):
        return self.name


class Station(models.Model):
    #监测点位
    TYPE_CHOICES = (
        ('废水', '废水'),
        ('废气', '废气')
    )
    PORT_CHOICES = (
        ('进口', '进口'),
        ('排放口', '排放口'),
    )
    station_id = models.CharField(primary_key=True, max_length=14)  # Field name made lowercase.
    #水或气
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='废水', blank=True, null=True)
    #监测点位所属的企业
    company = models.ForeignKey(Company, blank=True, null=True)
    #监测点位名称
    name = models.CharField(max_length=50)
    #进口或出口，窑头或窑尾
    in_or_out = models.CharField(max_length=10, blank=True, choices=PORT_CHOICES, default='排放口')
    #运维单位
    maintain_company = models.ForeignKey(MaintainCompany, null=True)  # Field name made lowercase.

    is_use = models.BooleanField(default=True)

    #显示
    def district(self):
        """
        显示该监控点位的所属的县区
        """
        try:
            district = self.company.district
        except AttributeError:
            district = ''
        return district

    district.short_description = '县区'


    def report_url(self):
        '''
        生成显示当天小时数据的连接
        '''
        date = time.strftime("%Y%m%d")
        html = "<a href='%s' target='_blank'>Report</a>" % reverse("station_day_report_url",
                                                                   args=[self.station_id, date])
        return html

    report_url.short_description = 'Report'
    report_url.allow_tags = True


    class Meta:
        db_table = 'Station'
        verbose_name = '监控点位'
        verbose_name_plural = '监控点位'

    def __unicode__(self):
        return self.name


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
    station = models.ForeignKey('Station')  # Field name made lowercase.
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


class EquipmentModel(models.Model):
    model = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'EquipmentModel'
        verbose_name = '分析仪型号'
        verbose_name_plural = '分析仪型号'

    def __unicode__(self):
        return self.model


class Equipment(models.Model):
    #分析仪

    #equipment_id = models.CharField(primary_key=True, max_length=10)
    station = models.ForeignKey('Station')  # Field name made lowercase.
    #设备型号
    equipment_model = models.ForeignKey(EquipmentModel, blank=True, null=True)
    #监控因子
    data_param = models.ForeignKey('report.DataParam', blank=True, null=True)
    #生成商
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
    #验收日期
    acceptance_date = models.DateTimeField(blank=True, null=True)
    #是否在用
    is_use = models.NullBooleanField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Equipment'
        verbose_name = '分析仪'
        verbose_name_plural = '分析仪'

    def __unicode__(self):
        return self.equipment_model.model


class ShutdownDate(models.Model):
    #停运时间
    #id = models.CharField(primary_key=True, max_length=10)
    station = models.ForeignKey('Station')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'ShutDownDate'
        verbose_name = '停运时间'
        verbose_name_plural = '停运时间'

    def __unicode__(self):
        return self.station.name + ' 从'+ self.start_date.strftime('%Y-%m-%d %H:%M:%S')+\
               '至' + self.end_date.strftime('%Y-%m-%d %H:%M:%S')


class NationSuprevise(models.Model):
    #国控信息
    TYPE_CHOICES = (
        ('废水', '废水'),
        ('废气', '废气'),
        ('重金属', '重金属'),
        ('污水处理厂', '污水处理厂'),
        ('垃圾填埋厂', '垃圾填埋厂'),
    )

    YEAR_CHOICES = (
        ('2011', '2011年'),
        ('2012', '2012年'),
        ('2013', '2013年'),
        ('2014', '2014年'),
    )

    #id = models.CharField(primary_key=True, max_length=10)
    station = models.OneToOneField('Station')  # Field name made lowercase.
    year = models.CharField(max_length=4, blank=True, choices=YEAR_CHOICES)
    type = models.CharField(max_length=15, blank=True, choices=TYPE_CHOICES)

    class Meta:
        db_table = 'NationSuprevise'
        verbose_name = '国控信息'
        verbose_name_plural = '国控信息'

class StationList(models.Model):
    station = models.ForeignKey('Station')  # Field name made lowercase.
    datetime = models.DateTimeField( blank=True)