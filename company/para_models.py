__author__ = 'GoTop'
from django.db import models

class TWatershed(models.Model):
    watershedid = models.IntegerField(db_column='WaterShedID')  # Field name made lowercase.
    higherwaterid = models.BigIntegerField(db_column='HigherWaterID', blank=True,
                                           null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True)  # Field name made lowercase.
    hourvalue = models.DecimalField(db_column='HourValue', max_digits=9, decimal_places=0, blank=True,
                                    null=True)  # Field name made lowercase.
    dayvalue = models.DecimalField(db_column='DayValue', max_digits=9, decimal_places=0, blank=True,
                                   null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    long = models.TextField(db_column='Long', blank=True)  # Field name made lowercase.
    lat = models.TextField(db_column='Lat', blank=True)  # Field name made lowercase.
    speed = models.DecimalField(db_column='Speed', max_digits=10, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    longlats = models.TextField(db_column='LongLats',
                                blank=True)  # Field name made lowercase. This field type is a guess.
    directionindex = models.TextField(db_column='DirectionIndex', blank=True)  # Field name made lowercase.
    isload = models.NullBooleanField(db_column='IsLoad', blank=True, null=True)  # Field name made lowercase.
    namelnglat = models.TextField(db_column='NameLngLat',
                                  blank=True)  # Field name made lowercase. This field type is a guess.
    fonttype = models.IntegerField(db_column='FontType', blank=True, null=True)  # Field name made lowercase.
    waterborder = models.TextField(db_column='WaterBorder',
                                   blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'T_Watershed'


class TStationkind(models.Model):
    kindid = models.IntegerField(db_column='KindID', primary_key=True)  # Field name made lowercase.
    kindname = models.CharField(db_column='KindName', max_length=30, blank=True)  # Field name made lowercase.
    ismobile = models.NullBooleanField(db_column='IsMobile', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_StationKind'

class TAttenddegree(models.Model):
    attendid = models.IntegerField(db_column='AttendID') # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AttendDegree'

class TTransfers(models.Model):
    transfersid = models.IntegerField(db_column='TransfersID') # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Transfers'

class TTrade(models.Model):
    tradeid = models.IntegerField(db_column='TradeID') # Field name made lowercase.
    highertradeid = models.BigIntegerField(db_column='HigherTradeID', blank=True, null=True) # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    tradedemo = models.CharField(db_column='TradeDemo', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Trade'
