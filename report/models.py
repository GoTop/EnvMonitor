# coding=utf-8
from django.db import models
from company.models import Station
# Create your models here.


class HourReport(models.Model):
    #小时报表
    #id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('Station', db_column='mn')  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    factor = models.CharField(max_length=10, blank=True)
    value = models.IntegerField(blank=True, null=True)
    is_adnormal = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'HourReport'


class Standard(models.Model):
    #排放标准
    #id = models.CharField(primary_key=True, max_length=10)
    mn = models.ForeignKey('Station', db_column='mn')  # Field name made lowercase.
    factor = models.CharField(max_length=10, blank=True)
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