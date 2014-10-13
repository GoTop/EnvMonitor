# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Day45007760002007(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Day_45007760002007'

class Day45007760002601(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Day_45007760002601'

class Day45007760002801(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Day_45007760002801'

class Day45007760003001(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Day_45007760003001'

class Day45007760006501(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Day_45007760006501'

class Hour45007760002007(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Hour_45007760002007'

class Hour45007760002801(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Hour_45007760002801'

class Hour45007760003001(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Hour_45007760003001'

class Modify45007760002007(models.Model):
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='ModifyTime', blank=True, null=True) # Field name made lowercase.
    flag = models.TextField(db_column='Flag', blank=True) # Field name made lowercase.
    sipaddress = models.TextField(db_column='sIPAddress', blank=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    swhys = models.CharField(db_column='sWhys', max_length=500, blank=True) # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True) # Field name made lowercase.
    id = models.TextField(db_column='ID', blank=True) # Field name made lowercase.
    isactive = models.NullBooleanField(db_column='IsActive', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Modify_45007760002007'

class TAdjust(models.Model):
    adjustid = models.CharField(db_column='AdjustID', max_length=20) # Field name made lowercase.
    recodeid = models.ForeignKey('TAdjustrecord', db_column='RecodeID') # Field name made lowercase.
    adjustreason = models.CharField(db_column='AdjustReason', max_length=1000, blank=True) # Field name made lowercase.
    adjustsource = models.TextField(db_column='AdjustSource', blank=True) # Field name made lowercase.
    adjuststarttime = models.DateTimeField(db_column='AdjustStartTime', blank=True, null=True) # Field name made lowercase.
    adjustendtime = models.DateTimeField(db_column='AdjustEndTime', blank=True, null=True) # Field name made lowercase.
    rangeset = models.DecimalField(db_column='RangeSet', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    adjustperson = models.CharField(db_column='AdjustPerson', max_length=30, blank=True) # Field name made lowercase.
    linear = models.CharField(db_column='Linear', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Adjust'

class TAdjustrecord(models.Model):
    recodeid = models.CharField(db_column='RecodeID', max_length=20) # Field name made lowercase.
    stationid = models.ForeignKey('TAllstation', db_column='StationID') # Field name made lowercase.
    checker = models.CharField(db_column='Checker', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AdjustRecord'

class TAdminarea(models.Model):
    areaid = models.IntegerField(db_column='AreaID') # Field name made lowercase.
    higherareaid = models.IntegerField(db_column='HigherAreaID', blank=True, null=True) # Field name made lowercase.
    areaname = models.TextField(db_column='AreaName') # Field name made lowercase.
    clientx = models.TextField(db_column='ClientX', blank=True) # Field name made lowercase.
    clienty = models.TextField(db_column='ClientY', blank=True) # Field name made lowercase.
    zoomlevel = models.IntegerField(db_column='ZoomLevel', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AdminArea'

class TAirparamset(models.Model):
    airparamsetid = models.IntegerField(db_column='AirParamSetID') # Field name made lowercase.
    airstandardcurve = models.TextField(db_column='AirStandardCurve', blank=True) # Field name made lowercase.
    airstandardcurvedemo = models.CharField(db_column='AirStandardCurveDemo', max_length=100, blank=True) # Field name made lowercase.
    fluesection = models.TextField(db_column='FlueSection', blank=True) # Field name made lowercase.
    fluesectiondemo = models.CharField(db_column='FlueSectionDemo', max_length=100, blank=True) # Field name made lowercase.
    excessivecoe = models.TextField(db_column='ExcessiveCoe', blank=True) # Field name made lowercase.
    excessivecoedemo = models.CharField(db_column='ExcessiveCoeDemo', max_length=100, blank=True) # Field name made lowercase.
    speedcoe = models.TextField(db_column='SpeedCoe', blank=True) # Field name made lowercase.
    speedcoedemo = models.CharField(db_column='SpeedCoeDemo', max_length=100, blank=True) # Field name made lowercase.
    pipecoe = models.TextField(db_column='PipeCoe', blank=True) # Field name made lowercase.
    pipecoedemo = models.CharField(db_column='PipeCoeDemo', max_length=100, blank=True) # Field name made lowercase.
    sootcoe = models.TextField(db_column='SootCoe', blank=True) # Field name made lowercase.
    sootcoedemo = models.CharField(db_column='SootCoeDemo', max_length=100, blank=True) # Field name made lowercase.
    so2range = models.TextField(db_column='SO2Range', blank=True) # Field name made lowercase.
    so2rangedemo = models.CharField(db_column='SO2RangeDemo', max_length=100, blank=True) # Field name made lowercase.
    noxrange = models.TextField(db_column='NOXRange', blank=True) # Field name made lowercase.
    noxrangedemo = models.CharField(db_column='NOXRangeDemo', max_length=100, blank=True) # Field name made lowercase.
    grainrange = models.TextField(db_column='GrainRange', blank=True) # Field name made lowercase.
    grainrangedemo = models.CharField(db_column='GrainRangeDemo', max_length=100, blank=True) # Field name made lowercase.
    o2range = models.TextField(db_column='O2Range', blank=True) # Field name made lowercase.
    o2rangedemo = models.CharField(db_column='O2RangeDemo', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AirParamSet'

class TAlarmlevel(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.TextField(db_column='ParamCode') # Field name made lowercase.
    levelitemid = models.ForeignKey('TLevelitem', db_column='LevelItemID') # Field name made lowercase.
    isalarm = models.NullBooleanField(db_column='IsAlarm', blank=True, null=True) # Field name made lowercase.
    lowvalue = models.DecimalField(db_column='LowValue', max_digits=18, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    heightvalue = models.DecimalField(db_column='HeightValue', max_digits=18, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    levelonedemo = models.CharField(db_column='LevelOneDemo', max_length=50, blank=True) # Field name made lowercase.
    leveltwovalue = models.DecimalField(db_column='LevelTwoValue', max_digits=18, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    leveltwodemo = models.TextField(db_column='LevelTwoDemo', blank=True) # Field name made lowercase.
    levelthreevalue = models.DecimalField(db_column='LevelThreeValue', max_digits=18, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    levelthreedemo = models.CharField(db_column='LevelThreeDemo', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AlarmLevel'

class TAlarmlog(models.Model):
    logid = models.IntegerField(db_column='LogID') # Field name made lowercase.
    alarmtime = models.DateTimeField(db_column='AlarmTime', blank=True, null=True) # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    paramcode = models.TextField(db_column='ParamCode', blank=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    sendkeyid = models.TextField(db_column='SendKeyID', blank=True) # Field name made lowercase.
    systemtag = models.TextField(db_column='SystemTag', blank=True) # Field name made lowercase.
    eventtag = models.TextField(db_column='EventTag', blank=True) # Field name made lowercase.
    messagcontent = models.CharField(db_column='MessagContent', max_length=200, blank=True) # Field name made lowercase.
    issuccess = models.NullBooleanField(db_column='IsSuccess', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AlarmLog'

class TAlarmquery(models.Model):
    queryid = models.IntegerField(db_column='QueryID') # Field name made lowercase.
    surcenum = models.TextField(db_column='SurceNum', blank=True) # Field name made lowercase.
    revtime = models.DateTimeField(db_column='RevTime', blank=True, null=True) # Field name made lowercase.
    revcontent = models.TextField(db_column='RevContent', blank=True) # Field name made lowercase.
    isright = models.NullBooleanField(db_column='IsRight', blank=True, null=True) # Field name made lowercase.
    rettime = models.DateTimeField(db_column='RetTime', blank=True, null=True) # Field name made lowercase.
    contentlen = models.TextField(db_column='ContentLen', blank=True) # Field name made lowercase.
    isretsucess = models.NullBooleanField(db_column='IsRetSucess', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AlarmQuery'

class TAlarmset(models.Model):
    alarmindex = models.IntegerField(db_column='AlarmIndex') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID', blank=True, null=True) # Field name made lowercase.
    examparmid = models.ForeignKey('TExamproject', db_column='ExamParmID', blank=True, null=True) # Field name made lowercase.
    alarmscope = models.IntegerField(db_column='AlarmScope', blank=True, null=True) # Field name made lowercase.
    maxvalue = models.DecimalField(db_column='MaxValue', max_digits=18, decimal_places=8, blank=True, null=True) # Field name made lowercase.
    adddemo = models.CharField(db_column='AddDemo', max_length=50, blank=True) # Field name made lowercase.
    isalarm = models.NullBooleanField(db_column='IsAlarm', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AlarmSet'

class TAlarmuser(models.Model):
    stationid = models.ForeignKey(TAlarmlevel, db_column='StationID') # Field name made lowercase.
    paramcode = models.ForeignKey(TAlarmlevel, db_column='ParamCode') # Field name made lowercase.
    levelitemid = models.ForeignKey(TAlarmlevel, db_column='LevelItemID') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID') # Field name made lowercase.
    isused = models.NullBooleanField(db_column='IsUsed', blank=True, null=True) # Field name made lowercase.
    isacceptegzmessage = models.NullBooleanField(db_column='IsAccepteGZMessage', blank=True, null=True) # Field name made lowercase.
    isacceptdelaymessage = models.NullBooleanField(db_column='IsAcceptDelayMessage', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AlarmUser'

class TAllstation(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    kindid = models.ForeignKey('TStationkind', db_column='KindID', blank=True, null=True) # Field name made lowercase.
    watershedid = models.ForeignKey('TWatershed', db_column='WaterShedID', blank=True, null=True) # Field name made lowercase.
    attendid = models.ForeignKey('TAttenddegree', db_column='AttendID', blank=True, null=True) # Field name made lowercase.
    transfersid = models.ForeignKey('TTransfers', db_column='TransfersID', blank=True, null=True) # Field name made lowercase.
    areaid = models.ForeignKey(TAdminarea, db_column='AreaID', blank=True, null=True) # Field name made lowercase.
    stationname = models.TextField(db_column='StationName', blank=True) # Field name made lowercase.
    tradeid = models.ForeignKey('TTrade', db_column='TradeID', blank=True, null=True) # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True) # Field name made lowercase.
    ionline = models.IntegerField(db_column='IOnline', blank=True, null=True) # Field name made lowercase.
    compid = models.IntegerField(db_column='CompID', blank=True, null=True) # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=60, blank=True) # Field name made lowercase.
    mnpwd = models.TextField(db_column='MNPwd', blank=True) # Field name made lowercase.
    standarddemo = models.TextField(db_column='StandardDemo', blank=True) # Field name made lowercase.
    higheroutid = models.TextField(db_column='HigherOutID', blank=True) # Field name made lowercase.
    isfacility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True) # Field name made lowercase.
    isemergency = models.NullBooleanField(db_column='IsEmergency', blank=True, null=True) # Field name made lowercase.
    isshow = models.NullBooleanField(db_column='IsShow', blank=True, null=True) # Field name made lowercase.
    longitude = models.TextField(db_column='Longitude', blank=True) # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True) # Field name made lowercase.
    isimportexport = models.IntegerField(db_column='IsImportexport', blank=True, null=True) # Field name made lowercase.
    paramcodes = models.TextField(db_column='ParamCodes', blank=True) # Field name made lowercase.
    pollutelevelindex = models.IntegerField(db_column='PolluteLevelIndex', blank=True, null=True) # Field name made lowercase.
    longwarp = models.DecimalField(db_column='LongWarp', max_digits=12, decimal_places=9, blank=True, null=True) # Field name made lowercase.
    latwarp = models.DecimalField(db_column='LatWarp', max_digits=12, decimal_places=9, blank=True, null=True) # Field name made lowercase.
    iscountrycontrol = models.NullBooleanField(db_column='IsCountryControl', blank=True, null=True) # Field name made lowercase.
    is1015building = models.NullBooleanField(db_column='Is1015Building', blank=True, null=True) # Field name made lowercase.
    ispassaccept = models.NullBooleanField(db_column='IsPassAccept', blank=True, null=True) # Field name made lowercase.
    passaccepttime = models.DateTimeField(db_column='PassAcceptTime', blank=True, null=True) # Field name made lowercase.
    stateyear = models.TextField(db_column='StateYear', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AllStation'

class TAnalysemethod(models.Model):
    analyseid = models.IntegerField(db_column='AnalyseID') # Field name made lowercase.
    analysename = models.CharField(db_column='AnalyseName', max_length=30) # Field name made lowercase.
    workelements = models.CharField(db_column='WorkElements', max_length=500, blank=True) # Field name made lowercase.
    paramnames = models.CharField(db_column='ParamNames', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AnalyseMethod'

class TAreaserverid(models.Model):
    areaserverid = models.IntegerField(db_column='AreaServerID') # Field name made lowercase.
    areaid = models.ForeignKey(TAdminarea, db_column='AreaID') # Field name made lowercase.
    areaservernumber = models.TextField(db_column='AreaServerNumber') # Field name made lowercase.
    distinctionid = models.TextField(db_column='DistinctionID', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AreaServerID'

class TAreatelcode(models.Model):
    telcodeid = models.IntegerField(db_column='TelCodeID') # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True) # Field name made lowercase.
    cityname = models.TextField(db_column='CityName') # Field name made lowercase.
    telcode = models.TextField(db_column='TelCode', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AreaTelCode'

class TArtificial(models.Model):
    artificialid = models.CharField(db_column='ArtificialID', max_length=20) # Field name made lowercase.
    replacemonid = models.ForeignKey('TReplacemon', db_column='ReplaceMonID') # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=50, blank=True) # Field name made lowercase.
    sampling = models.DateTimeField(db_column='Sampling', blank=True, null=True) # Field name made lowercase.
    analysis = models.CharField(db_column='Analysis', max_length=50, blank=True) # Field name made lowercase.
    analysismethord = models.CharField(db_column='AnalysisMethord', max_length=50, blank=True) # Field name made lowercase.
    samplingperson = models.CharField(db_column='SamplingPerson', max_length=30, blank=True) # Field name made lowercase.
    analysisperson = models.CharField(db_column='AnalysisPerson', max_length=30, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Artificial'

class TAttenddegree(models.Model):
    attendid = models.IntegerField(db_column='AttendID') # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_AttendDegree'

class TBaseset(models.Model):
    belongs = models.TextField(db_column='Belongs') # Field name made lowercase.
    confer = models.TextField(db_column='Confer') # Field name made lowercase.
    copyright = models.TextField(db_column='CopyRight') # Field name made lowercase.
    isshowmap = models.NullBooleanField(db_column='IsShowMap') # Field name made lowercase.
    ishavemap = models.NullBooleanField(db_column='IsHaveMap') # Field name made lowercase.
    isautocollect = models.NullBooleanField(db_column='IsAutoCollect') # Field name made lowercase.
    alarmid = models.TextField(db_column='AlarmID') # Field name made lowercase.
    showformat = models.SmallIntegerField(db_column='ShowFormat') # Field name made lowercase.
    configid = models.BigIntegerField(db_column='ConfigID', blank=True, null=True) # Field name made lowercase.
    namebase = models.CharField(db_column='NameBase', max_length=100, blank=True) # Field name made lowercase.
    namedataapply = models.CharField(db_column='NameDataApply', max_length=100, blank=True) # Field name made lowercase.
    namece = models.CharField(db_column='NameCE', max_length=100, blank=True) # Field name made lowercase.
    namedisplay = models.CharField(db_column='NameDisplay', max_length=100, blank=True) # Field name made lowercase.
    namepda = models.CharField(db_column='NamePDA', max_length=100, blank=True) # Field name made lowercase.
    namealarm = models.CharField(db_column='NameAlarm', max_length=100, blank=True) # Field name made lowercase.
    namelhclient = models.CharField(db_column='NameLHClient', max_length=100, blank=True) # Field name made lowercase.
    lwcenter = models.TextField(db_column='LWCenter', blank=True) # Field name made lowercase.
    lwkey = models.TextField(db_column='LWKey', blank=True) # Field name made lowercase.
    nzoomlevel = models.FloatField(db_column='NZoomLevel', blank=True, null=True) # Field name made lowercase.
    wwcenter = models.TextField(db_column='WWCenter', blank=True) # Field name made lowercase.
    wwkey = models.TextField(db_column='WWKey', blank=True) # Field name made lowercase.
    wzoomlevel = models.FloatField(db_column='WZoomLevel', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_BaseSet'

class TBus(models.Model):
    stationid = models.CharField(db_column='StationID', max_length=14) # Field name made lowercase.
    licenseplate = models.TextField(db_column='LicensePlate', blank=True) # Field name made lowercase.
    simnumber = models.TextField(db_column='SIMNumber', blank=True) # Field name made lowercase.
    variety = models.CharField(db_column='Variety', max_length=50, blank=True) # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True) # Field name made lowercase.
    driverman = models.CharField(db_column='DriverMan', max_length=10, blank=True) # Field name made lowercase.
    manmobile = models.TextField(db_column='ManMobile', blank=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=200, blank=True) # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True) # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Bus'

class TCecenter(models.Model):
    centerindex = models.TextField(db_column='CenterIndex') # Field name made lowercase.
    centername = models.CharField(db_column='CenterName', max_length=200, blank=True) # Field name made lowercase.
    longlat = models.TextField(db_column='LongLat', blank=True) # Field name made lowercase.
    chiefname = models.CharField(db_column='ChiefName', max_length=50, blank=True) # Field name made lowercase.
    assistantnames = models.CharField(db_column='AssistantNames', max_length=200, blank=True) # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_CECenter'

class TCeeventplan(models.Model):
    ceventindex = models.TextField(db_column='CEventIndex') # Field name made lowercase.
    generalplanindex = models.TextField(db_column='GeneralPlanIndex') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CEEventPlan'

class TCegroup(models.Model):
    groupindex = models.TextField(db_column='GroupIndex') # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=200, blank=True) # Field name made lowercase.
    gooff = models.DateTimeField(db_column='GoOff', blank=True, null=True) # Field name made lowercase.
    arrivedtime = models.DateTimeField(db_column='ArrivedTime', blank=True, null=True) # Field name made lowercase.
    factarrivedtime = models.DateTimeField(db_column='FactArrivedTime', blank=True, null=True) # Field name made lowercase.
    taskdemo = models.TextField(db_column='TaskDemo', blank=True) # Field name made lowercase. This field type is a guess.
    grouppath = models.TextField(db_column='GroupPath', blank=True) # Field name made lowercase. This field type is a guess.
    watershedid = models.IntegerField(db_column='WaterShedID', blank=True, null=True) # Field name made lowercase.
    groupnumber = models.IntegerField(db_column='GroupNumber', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CEGroup'

class TCeelement(models.Model):
    celementsindex = models.TextField(db_column='CElementsIndex') # Field name made lowercase.
    elementid = models.TextField(db_column='ElementID', blank=True) # Field name made lowercase.
    usernames = models.CharField(db_column='UserNames', max_length=1000, blank=True) # Field name made lowercase.
    ismen = models.NullBooleanField(db_column='IsMen', blank=True, null=True) # Field name made lowercase.
    longlat = models.TextField(db_column='LongLat', blank=True) # Field name made lowercase.
    groupindex = models.ForeignKey(TCegroup, db_column='GroupIndex', blank=True, null=True) # Field name made lowercase.
    sampleaddress = models.CharField(db_column='SampleAddress', max_length=500, blank=True) # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=2000, blank=True) # Field name made lowercase.
    orderid = models.CharField(db_column='OrderID', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CEelement'

class TChangebakparts(models.Model):
    bakpartid = models.CharField(db_column='BakPartID', max_length=20) # Field name made lowercase.
    serviceid = models.ForeignKey('TServicerecord', db_column='ServiceID') # Field name made lowercase.
    bakpartname = models.CharField(db_column='BakPartName', max_length=50, blank=True) # Field name made lowercase.
    bakpartscount = models.IntegerField(db_column='BakPartsCount', blank=True, null=True) # Field name made lowercase.
    bakpartbrand = models.CharField(db_column='BakPartBrand', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ChangeBakParts'

class TChangereagent(models.Model):
    changereagentid = models.CharField(db_column='ChangeReagentID', max_length=20) # Field name made lowercase.
    serviceid = models.ForeignKey('TServicerecord', db_column='ServiceID') # Field name made lowercase.
    reagentname = models.CharField(db_column='ReagentName', max_length=50, blank=True) # Field name made lowercase.
    reagentsource = models.TextField(db_column='ReagentSource', blank=True) # Field name made lowercase.
    normaltime = models.DateTimeField(db_column='NormalTime', blank=True, null=True) # Field name made lowercase.
    concentration = models.CharField(db_column='Concentration', max_length=20, blank=True) # Field name made lowercase.
    reagentcount = models.IntegerField(db_column='ReagentCount', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ChangeReagent'

class TChatmsglog(models.Model):
    logindex = models.IntegerField(db_column='LogIndex') # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=14, blank=True) # Field name made lowercase.
    centerid = models.CharField(db_column='CenterID', max_length=14, blank=True) # Field name made lowercase.
    revtime = models.DateTimeField(db_column='RevTime', blank=True, null=True) # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime', blank=True, null=True) # Field name made lowercase.
    msgcontent = models.CharField(db_column='MsgContent', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ChatMsgLog'

class TChildsystem(models.Model):
    childsystemid = models.CharField(db_column='ChildSystemID', max_length=20) # Field name made lowercase.
    repairid = models.ForeignKey('TRepairfault', db_column='RepairID') # Field name made lowercase.
    childsystemname = models.CharField(db_column='ChildSystemName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ChildSystem'

class TClasstype(models.Model):
    classtypeid = models.IntegerField(db_column='ClassTypeID') # Field name made lowercase.
    classname = models.TextField(db_column='ClassName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ClassType'

class TCommonitorreport(models.Model):
    commonitorreportid = models.TextField(db_column='ComMonitorReportID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    commonitortime = models.DateTimeField(db_column='ComMonitorTime') # Field name made lowercase.
    years = models.IntegerField(db_column='Years') # Field name made lowercase.
    season = models.SmallIntegerField(db_column='Season') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ComMonitorReport'

class TCommunicationmsg(models.Model):
    msgindex = models.TextField(db_column='MsgIndex') # Field name made lowercase.
    msgtime = models.DateTimeField(db_column='MsgTime', blank=True, null=True) # Field name made lowercase.
    commanduserid = models.IntegerField(db_column='CommandUserID', blank=True, null=True) # Field name made lowercase.
    usheruserid = models.IntegerField(db_column='UsherUserID', blank=True, null=True) # Field name made lowercase.
    receiveduserid = models.IntegerField(db_column='ReceivedUserID', blank=True, null=True) # Field name made lowercase.
    msgcontenet = models.TextField(db_column='MsgContenet', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_CommunicationMsg'

class TCompcplan(models.Model):
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    generalplanindex = models.TextField(db_column='GeneralPlanIndex') # Field name made lowercase.
    isused = models.NullBooleanField(db_column='IsUsed', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompCPlan'

class TCompinfo(models.Model):
    compid = models.IntegerField(db_column='CompID') # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=100) # Field name made lowercase.
    tel = models.TextField(db_column='Tel', blank=True) # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True) # Field name made lowercase.
    postcode = models.TextField(db_column='Postcode', blank=True) # Field name made lowercase.
    lawperson = models.CharField(db_column='LawPerson', max_length=20, blank=True) # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True) # Field name made lowercase.
    setuptime = models.DateTimeField(db_column='SetUpTime', blank=True, null=True) # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=20, blank=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=160, blank=True) # Field name made lowercase.
    longitude = models.TextField(blank=True)
    latitude = models.TextField(blank=True)
    hsename = models.CharField(db_column='HsEName', max_length=40, blank=True) # Field name made lowercase.
    regtype = models.CharField(db_column='RegType', max_length=40, blank=True) # Field name made lowercase.
    sewfaccou = models.IntegerField(db_column='SewFacCou', blank=True, null=True) # Field name made lowercase.
    sfexploitva = models.DecimalField(db_column='SFexploitVa', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    disposeability = models.DecimalField(db_column='DisposeAbility', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    tlfaccou = models.IntegerField(db_column='TLFacCou', blank=True, null=True) # Field name made lowercase.
    idnkilncou = models.IntegerField(db_column='IdnkilnCou', blank=True, null=True) # Field name made lowercase.
    tlfaccap = models.TextField(db_column='TLFacCap', blank=True) # Field name made lowercase.
    lastyearfinemoney = models.DecimalField(db_column='LastYearFineMoney', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    lastyearpaymoney = models.DecimalField(db_column='LastYearPayMoney', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    wasteemissionid = models.TextField(db_column='WasteEmissionID', blank=True) # Field name made lowercase.
    issuingtime = models.DateTimeField(db_column='IssuingTime', blank=True, null=True) # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True) # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200, blank=True) # Field name made lowercase.
    telcodeid = models.IntegerField(db_column='TelCodeID', blank=True, null=True) # Field name made lowercase.
    tradeid = models.TextField(db_column='TradeID', blank=True) # Field name made lowercase.
    countryattribute = models.TextField(db_column='CountryAttribute', blank=True) # Field name made lowercase.
    watershedid = models.IntegerField(db_column='WaterShedID', blank=True, null=True) # Field name made lowercase.
    pollutelevelindex = models.IntegerField(db_column='PolluteLevelIndex', blank=True, null=True) # Field name made lowercase.
    isfacility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True) # Field name made lowercase.
    organcode = models.TextField(db_column='OrganCode', blank=True) # Field name made lowercase.
    buildtime = models.DateTimeField(db_column='BuildTime', blank=True, null=True) # Field name made lowercase.
    factoryarea = models.DecimalField(db_column='FactoryArea', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    lawpersonmum = models.TextField(db_column='LawPersonMum', blank=True) # Field name made lowercase.
    siteurl = models.TextField(db_column='SiteUrl', blank=True) # Field name made lowercase.
    compproperties = models.CharField(db_column='CompProperties', max_length=500, blank=True) # Field name made lowercase.
    linkmanphone = models.TextField(db_column='LinkManPhone', blank=True) # Field name made lowercase.
    contactman = models.CharField(db_column='ContactMan', max_length=10, blank=True) # Field name made lowercase.
    contactmanphone = models.TextField(db_column='ContactManPhone', blank=True) # Field name made lowercase.
    industryparkname = models.CharField(db_column='IndustryParkName', max_length=200, blank=True) # Field name made lowercase.
    ishavejuryproject = models.NullBooleanField(db_column='IsHaveJuryProject', blank=True, null=True) # Field name made lowercase.
    isgbjudge = models.NullBooleanField(db_column='IsGBJudge', blank=True, null=True) # Field name made lowercase.
    isoccurjury = models.NullBooleanField(db_column='IsOccurJury', blank=True, null=True) # Field name made lowercase.
    jurydemo = models.CharField(db_column='JuryDemo', max_length=1000, blank=True) # Field name made lowercase.
    kilntype = models.TextField(db_column='kilnType', blank=True) # Field name made lowercase.
    kilnhavedecoke = models.NullBooleanField(db_column='KilnHaveDecoke', blank=True, null=True) # Field name made lowercase.
    kilnisrun = models.NullBooleanField(db_column='KilnIsRun', blank=True, null=True) # Field name made lowercase.
    kilncoal = models.DecimalField(db_column='KilnCoal', max_digits=18, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    boilercou = models.IntegerField(db_column='BoilerCou', blank=True, null=True) # Field name made lowercase.
    boilerton = models.DecimalField(db_column='BoilerTon', max_digits=18, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    boilertype = models.TextField(db_column='BoilerType', blank=True) # Field name made lowercase.
    boilerhavedecoke = models.NullBooleanField(db_column='BoilerHaveDecoke', blank=True, null=True) # Field name made lowercase.
    boilerisrun = models.NullBooleanField(db_column='BoilerIsRun', blank=True, null=True) # Field name made lowercase.
    boilercoal = models.DecimalField(db_column='BoilerCoal', max_digits=18, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    imgsavepath = models.CharField(db_column='ImgSavePath', max_length=500, blank=True) # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase. This field type is a guess.
    outwherecode = models.CharField(db_column='OutWhereCode', max_length=10, blank=True) # Field name made lowercase.
    functionid = models.IntegerField(db_column='FunctionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompInfo'

class TCompinfoextend(models.Model):
    compextendid = models.IntegerField(db_column='CompExtendID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    compinvest = models.DecimalField(db_column='CompInvest', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    mainmaterial = models.TextField(db_column='mainMaterial', blank=True) # Field name made lowercase.
    usedgross = models.CharField(db_column='UsedGross', max_length=50, blank=True) # Field name made lowercase.
    mainproduct = models.TextField(db_column='MainProduct', blank=True) # Field name made lowercase.
    totaloutput = models.TextField(db_column='TotalOutput', blank=True) # Field name made lowercase.
    yearproducttime = models.IntegerField(db_column='YearProductTime', blank=True, null=True) # Field name made lowercase.
    grossmoney = models.DecimalField(db_column='GrossMoney', max_digits=10, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    ishaveprocedure = models.NullBooleanField(db_column='IsHaveProcedure', blank=True, null=True) # Field name made lowercase.
    postiltime = models.DateTimeField(db_column='PostilTime', blank=True, null=True) # Field name made lowercase.
    postildept = models.TextField(db_column='postilDept', blank=True) # Field name made lowercase.
    isvalidate = models.NullBooleanField(db_column='IsValidate', blank=True, null=True) # Field name made lowercase.
    validatetime = models.DateTimeField(db_column='validateTime', blank=True, null=True) # Field name made lowercase.
    validatedept = models.TextField(db_column='validateDept', blank=True) # Field name made lowercase.
    producttechnical = models.TextField(db_column='ProductTechnical', blank=True) # Field name made lowercase.
    ishaveammeter = models.NullBooleanField(db_column='IsHaveAmmeter', blank=True, null=True) # Field name made lowercase.
    polluteattribute = models.TextField(db_column='polluteAttribute', blank=True) # Field name made lowercase.
    ishavepunish = models.NullBooleanField(db_column='IsHavePunish', blank=True, null=True) # Field name made lowercase.
    finishtime = models.DateTimeField(db_column='finishTime', blank=True, null=True) # Field name made lowercase.
    publishsum = models.DecimalField(db_column='publishSum', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    isstop = models.NullBooleanField(db_column='IsStop', blank=True, null=True) # Field name made lowercase.
    ispermission = models.TextField(db_column='IsPermission', blank=True) # Field name made lowercase.
    isonschedule = models.NullBooleanField(db_column='IsOnschedule', blank=True, null=True) # Field name made lowercase.
    workedtechnicalid = models.IntegerField(db_column='workedTechnicalID', blank=True, null=True) # Field name made lowercase.
    dayoutwater = models.DecimalField(db_column='DayOutWater', max_digits=18, decimal_places=8, blank=True, null=True) # Field name made lowercase.
    hbinvest = models.DecimalField(db_column='HBInvest', max_digits=18, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompInfoExtend'

class TCompkeys(models.Model):
    keyprojectindex = models.ForeignKey('TKeyprojects', db_column='KeyProjectIndex') # Field name made lowercase.
    compid = models.IntegerField(db_column='CompID') # Field name made lowercase.
    apartdistance = models.DecimalField(db_column='ApartDistance', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    arrivedtime = models.IntegerField(db_column='ArrivedTime', blank=True, null=True) # Field name made lowercase.
    speed = models.DecimalField(db_column='Speed', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    directionindex = models.ForeignKey('TDirection', db_column='DirectionIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompKeys'

class TCompmold(models.Model):
    comptypeid = models.IntegerField(db_column='CompTypeID') # Field name made lowercase.
    comptypename = models.CharField(db_column='CompTypeName', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompMold'

class TCompparams(models.Model):
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    distance = models.DecimalField(db_column='Distance', max_digits=18, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompParams'

class TCompsewage(models.Model):
    stationid = models.CharField(db_column='StationID', max_length=14) # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompSewage'

class TComptype(models.Model):
    comptypeid = models.IntegerField(db_column='CompTypeID') # Field name made lowercase.
    comptypename = models.CharField(db_column='CompTypeName', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompType'

class TComptyperel(models.Model):
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    comptypeid = models.IntegerField(db_column='CompTypeID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompTypeRel'

class TComparedata(models.Model):
    comparedataid = models.IntegerField(db_column='CompareDataID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.TextField(db_column='ParamCode') # Field name made lowercase.
    sampletypeid = models.ForeignKey('TComparesampletype', db_column='SampleTypeID', blank=True, null=True) # Field name made lowercase.
    cause = models.CharField(db_column='Cause', max_length=400, blank=True) # Field name made lowercase.
    sampletime = models.DateTimeField(db_column='SampleTime') # Field name made lowercase.
    comparetime = models.DateTimeField(db_column='CompareTime', blank=True, null=True) # Field name made lowercase.
    factvalue = models.DecimalField(db_column='FactValue', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    testvalue = models.DecimalField(db_column='TestValue', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    errorrate = models.DecimalField(db_column='ErrorRate', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    isacross = models.NullBooleanField(db_column='IsAcross', blank=True, null=True) # Field name made lowercase.
    approachmsg = models.TextField(db_column='ApproachMsg', blank=True) # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID', blank=True, null=True) # Field name made lowercase.
    writetime = models.DateTimeField(db_column='WriteTime', blank=True, null=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=1000, blank=True) # Field name made lowercase.
    comparefactid = models.ForeignKey('TComparefact', db_column='CompareFactID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompareData'

class TComparefact(models.Model):
    comparefactid = models.IntegerField(db_column='CompareFactID') # Field name made lowercase.
    comparefactname = models.CharField(db_column='CompareFactName', max_length=400, blank=True) # Field name made lowercase.
    highercomparefactid = models.IntegerField(db_column='HigherCompareFactID', blank=True, null=True) # Field name made lowercase.
    comparefactaddress = models.CharField(db_column='CompareFactAddress', max_length=500, blank=True) # Field name made lowercase.
    postnumber = models.TextField(db_column='PostNumber', blank=True) # Field name made lowercase.
    superman = models.CharField(db_column='SuperMan', max_length=50, blank=True) # Field name made lowercase.
    telephonenum = models.TextField(db_column='TelephoneNum', blank=True) # Field name made lowercase.
    comptypeid = models.IntegerField(db_column='CompTypeID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompareFact'

class TComparesampletype(models.Model):
    sampletypeid = models.IntegerField(db_column='SampleTypeID') # Field name made lowercase.
    sampletypename = models.CharField(db_column='SampleTypeName', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_CompareSampleType'

class TConcentration(models.Model):
    groupid = models.CharField(db_column='GroupID', max_length=20) # Field name made lowercase.
    recodeid = models.ForeignKey(TAdjustrecord, db_column='RecodeID') # Field name made lowercase.
    one = models.DecimalField(db_column='One', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    two = models.DecimalField(db_column='Two', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    three = models.DecimalField(db_column='Three', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    four = models.DecimalField(db_column='Four', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    five = models.DecimalField(db_column='Five', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    six = models.DecimalField(db_column='Six', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    seven = models.DecimalField(db_column='Seven', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Concentration'

class TContingencyevent(models.Model):
    ceventindex = models.TextField(db_column='CEventIndex') # Field name made lowercase.
    ceventname = models.CharField(db_column='CEventName', max_length=200, blank=True) # Field name made lowercase.
    ceventaddress = models.CharField(db_column='CEventAddress', max_length=200, blank=True) # Field name made lowercase.
    occurtime = models.DateTimeField(db_column='OccurTime', blank=True, null=True) # Field name made lowercase.
    warningmen = models.CharField(db_column='WarningMen', max_length=30, blank=True) # Field name made lowercase.
    longlat = models.TextField(db_column='LongLat', blank=True) # Field name made lowercase.
    warningtime = models.DateTimeField(db_column='WarningTime', blank=True, null=True) # Field name made lowercase.
    receivedmen = models.CharField(db_column='ReceivedMen', max_length=30, blank=True) # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3, blank=True) # Field name made lowercase.
    pollutelevel = models.IntegerField(db_column='PolluteLevel', blank=True, null=True) # Field name made lowercase.
    pollutearea = models.TextField(db_column='PolluteArea', blank=True) # Field name made lowercase. This field type is a guess.
    eventdemo = models.CharField(db_column='EventDemo', max_length=500, blank=True) # Field name made lowercase.
    stoptime = models.DateTimeField(db_column='StopTime', blank=True, null=True) # Field name made lowercase.
    isautorev = models.NullBooleanField(db_column='IsAutoRev', blank=True, null=True) # Field name made lowercase.
    watershedid = models.IntegerField(db_column='WaterShedID', blank=True, null=True) # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=14, blank=True) # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    centerindex = models.ForeignKey(TCecenter, db_column='CenterIndex', blank=True, null=True) # Field name made lowercase.
    childcenterid = models.CharField(db_column='ChildCenterID', max_length=14, blank=True) # Field name made lowercase.
    typeid = models.ForeignKey('TContingencytype', db_column='TypeID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ContingencyEvent'

class TContingencygroup(models.Model):
    ceventindex = models.ForeignKey(TContingencyevent, db_column='CEventIndex') # Field name made lowercase.
    groupindex = models.ForeignKey(TCegroup, db_column='GroupIndex') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ContingencyGroup'

class TContingencyplan(models.Model):
    generalplanindex = models.TextField(db_column='GeneralPlanIndex') # Field name made lowercase.
    plannumber = models.IntegerField(db_column='PlanNumber', blank=True, null=True) # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=200, blank=True) # Field name made lowercase.
    typeindex = models.IntegerField(db_column='TypeIndex', blank=True, null=True) # Field name made lowercase.
    simpledemo = models.CharField(db_column='SimpleDemo', max_length=50, blank=True) # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True) # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=1000, blank=True) # Field name made lowercase.
    relatedoc = models.TextField(db_column='RelateDoc', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_ContingencyPlan'

class TContingencytype(models.Model):
    typeid = models.IntegerField(db_column='TypeID') # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=500, blank=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=2000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ContingencyType'

class TDangermarktype(models.Model):
    marktypeid = models.IntegerField(db_column='MarkTypeID') # Field name made lowercase.
    markname = models.TextField(db_column='MarkName', blank=True) # Field name made lowercase.
    mark = models.BinaryField(db_column='Mark', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DangerMarkType'

class TDatapage(models.Model):
    pageid = models.IntegerField(db_column='PageID') # Field name made lowercase.
    revtime = models.DateTimeField(db_column='RevTime', blank=True, null=True) # Field name made lowercase.
    msgfromid = models.TextField(db_column='MsgFromID', blank=True) # Field name made lowercase.
    pagecontent = models.TextField(db_column='PageContent', blank=True) # Field name made lowercase.
    isprase = models.NullBooleanField(db_column='IsPrase', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DataPage'

class TDataparam(models.Model):
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    standardcode = models.TextField(db_column='StandardCode', blank=True) # Field name made lowercase.
    paramremark = models.TextField(db_column='ParamRemark', blank=True) # Field name made lowercase.
    paramkind = models.IntegerField(db_column='ParamKind', blank=True, null=True) # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True) # Field name made lowercase.
    paramunit = models.TextField(db_column='ParamUnit', blank=True) # Field name made lowercase.
    dataprecision = models.IntegerField(db_column='DataPrecision', blank=True, null=True) # Field name made lowercase.
    ishavecou = models.NullBooleanField(db_column='IsHaveCou') # Field name made lowercase.
    standardvalues = models.TextField(db_column='StandardValues', blank=True) # Field name made lowercase.
    appvalue = models.DecimalField(db_column='AppValue', max_digits=18, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DataParam'

class TDatatype(models.Model):
    datatype = models.TextField(db_column='DataType') # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DataType'

class TDataverifylist(models.Model):
    dataverifyid = models.IntegerField(db_column='DataVerifyID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    begtime = models.DateTimeField(db_column='BegTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime') # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType') # Field name made lowercase.
    isresult = models.NullBooleanField(db_column='IsResult', blank=True, null=True) # Field name made lowercase.
    explain = models.TextField(db_column='Explain') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DataVerifyList'

class TDefenseitem(models.Model):
    defenseid = models.BigIntegerField(db_column='DefenseID') # Field name made lowercase.
    defensename = models.CharField(db_column='DefenseName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DefenseItem'

class TDefenserelation(models.Model):
    defenselistid = models.TextField(db_column='DefenseListID') # Field name made lowercase.
    keyid = models.TextField(db_column='KeyID', blank=True) # Field name made lowercase.
    keyname = models.CharField(db_column='KeyName', max_length=100, blank=True) # Field name made lowercase.
    defenseid = models.ForeignKey(TDefenseitem, db_column='DefenseID', blank=True, null=True) # Field name made lowercase.
    nextdefenselistid = models.TextField(db_column='NextDefenseListID', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DefenseRelation'

class TDefensetxtimage(models.Model):
    txtimageid = models.TextField(db_column='TxtImageID') # Field name made lowercase.
    defenselistid = models.ForeignKey(TDefenserelation, db_column='DefenseListID', blank=True, null=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=500, blank=True) # Field name made lowercase.
    savepath = models.CharField(db_column='SavePath', max_length=500, blank=True) # Field name made lowercase.
    txtcontent = models.TextField(db_column='TxtContent', blank=True) # Field name made lowercase. This field type is a guess.
    sortindex = models.IntegerField(db_column='SortIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DefenseTxtImage'

class TDelmnpwd(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    delmnpwd = models.TextField(db_column='DelMNPwd') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DelMNPwd'

class TDemosteep(models.Model):
    steepid = models.TextField(db_column='SteepID') # Field name made lowercase.
    steepname = models.CharField(db_column='SteepName', max_length=200, blank=True) # Field name made lowercase.
    xsteep = models.IntegerField(db_column='XSteep', blank=True, null=True) # Field name made lowercase.
    steepdemo = models.CharField(db_column='SteepDemo', max_length=2000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DemoSteep'

class TDepartments(models.Model):
    departid = models.IntegerField(db_column='DepartID') # Field name made lowercase.
    higherdepartid = models.IntegerField(db_column='HigherDepartID', blank=True, null=True) # Field name made lowercase.
    departname = models.CharField(db_column='DepartName', max_length=200, blank=True) # Field name made lowercase.
    comparefactid = models.IntegerField(db_column='CompareFactID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Departments'

class TDirection(models.Model):
    directionindex = models.TextField(db_column='DirectionIndex') # Field name made lowercase.
    directionname = models.CharField(db_column='DirectionName', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Direction'

class TDiscuss(models.Model):
    discussid = models.TextField(db_column='DiscussID') # Field name made lowercase.
    messageid = models.ForeignKey('TMessage', db_column='MessageID') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID') # Field name made lowercase.
    discusstime = models.DateTimeField(db_column='DiscussTime', blank=True, null=True) # Field name made lowercase.
    discusscontent = models.TextField(db_column='DiscussContent', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_Discuss'

class TDrillingtype(models.Model):
    typeid = models.IntegerField(db_column='TypeID') # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=500, blank=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DrillingType'

class TDuty(models.Model):
    dutyid = models.IntegerField(db_column='DutyID') # Field name made lowercase.
    dutyname = models.TextField(db_column='DutyName') # Field name made lowercase.
    higherdutyid = models.IntegerField(db_column='HigherDutyID', blank=True, null=True) # Field name made lowercase.
    specialname = models.TextField(db_column='SpecialName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Duty'

class TDykes(models.Model):
    dykeindex = models.TextField(db_column='DykeIndex') # Field name made lowercase.
    typeid = models.ForeignKey('TWaterkeytype', db_column='TypeID', blank=True, null=True) # Field name made lowercase.
    watershedid = models.ForeignKey('TWatershed', db_column='WaterShedID', blank=True, null=True) # Field name made lowercase.
    dykename = models.CharField(db_column='DykeName', max_length=200, blank=True) # Field name made lowercase.
    latlong = models.TextField(db_column='LatLong', blank=True) # Field name made lowercase.
    long = models.TextField(db_column='Long', blank=True) # Field name made lowercase.
    lat = models.TextField(db_column='Lat', blank=True) # Field name made lowercase.
    orderid = models.TextField(db_column='OrderID', blank=True) # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase. This field type is a guess.
    directionindex = models.ForeignKey(TDirection, db_column='DirectionIndex', blank=True, null=True) # Field name made lowercase.
    isload = models.NullBooleanField(db_column='IsLoad', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Dykes'

class TEnvcheck(models.Model):
    logid = models.ForeignKey('TRunlogbyuser', db_column='LogID') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID', blank=True, null=True) # Field name made lowercase.
    checktime = models.DateTimeField(db_column='CheckTime', blank=True, null=True) # Field name made lowercase.
    checkdemo = models.CharField(db_column='CheckDemo', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_EnvCheck'

class TEventlog(models.Model):
    eventlogindex = models.TextField(db_column='EventLogIndex') # Field name made lowercase.
    ceventindex = models.ForeignKey(TContingencyevent, db_column='CEventIndex', blank=True, null=True) # Field name made lowercase.
    showtitle = models.CharField(db_column='ShowTitle', max_length=2000, blank=True) # Field name made lowercase.
    showcontent = models.CharField(db_column='ShowContent', max_length=2000, blank=True) # Field name made lowercase.
    iskey = models.NullBooleanField(db_column='IsKey', blank=True, null=True) # Field name made lowercase.
    stepindex = models.IntegerField(db_column='StepIndex', blank=True, null=True) # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime', blank=True, null=True) # Field name made lowercase.
    logmen = models.CharField(db_column='LogMen', max_length=50, blank=True) # Field name made lowercase.
    logcontent = models.CharField(db_column='LogContent', max_length=2000, blank=True) # Field name made lowercase.
    fornext = models.CharField(db_column='ForNext', max_length=2000, blank=True) # Field name made lowercase.
    msgcontent = models.CharField(db_column='MsgContent', max_length=1000, blank=True) # Field name made lowercase.
    formname = models.TextField(db_column='FormName', blank=True) # Field name made lowercase.
    screenimage = models.BinaryField(db_column='ScreenImage', blank=True, null=True) # Field name made lowercase.
    isreback = models.NullBooleanField(db_column='IsReback', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_EventLog'

class TExamproject(models.Model):
    examparmid = models.IntegerField(db_column='ExamParmID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode', blank=True, null=True) # Field name made lowercase.
    manufacturerid = models.ForeignKey('TManufacturer', db_column='ManufacturerID', blank=True, null=True) # Field name made lowercase.
    lowlimitvalue = models.DecimalField(db_column='LowLimitValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    highlimitvalue = models.DecimalField(db_column='HighLimitValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    dataprecision = models.IntegerField(db_column='DataPrecision', blank=True, null=True) # Field name made lowercase.
    paramunit = models.TextField(db_column='ParamUnit', blank=True) # Field name made lowercase.
    kunit = models.DecimalField(db_column='kUnit', max_digits=8, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    issend = models.NullBooleanField(db_column='IsSend', blank=True, null=True) # Field name made lowercase.
    totalunit = models.TextField(db_column='TotalUnit', blank=True) # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortID', blank=True, null=True) # Field name made lowercase.
    isused = models.NullBooleanField(db_column='IsUsed', blank=True, null=True) # Field name made lowercase.
    ascid = models.NullBooleanField(db_column='AscID', blank=True, null=True) # Field name made lowercase.
    analyseid = models.SmallIntegerField(db_column='AnalyseID', blank=True, null=True) # Field name made lowercase.
    model = models.TextField(db_column='Model', blank=True) # Field name made lowercase.
    number = models.TextField(db_column='Number', blank=True) # Field name made lowercase.
    minimumlevel = models.DecimalField(db_column='MinimumLevel', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    errormaxvalue = models.DecimalField(db_column='ErrorMaxValue', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    errorminvalue = models.DecimalField(db_column='ErrorMinValue', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    isenable = models.NullBooleanField(db_column='IsEnable', blank=True, null=True) # Field name made lowercase.
    dminlimit = models.DecimalField(db_column='dMinLimit', max_digits=18, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    dmaxlimit = models.DecimalField(db_column='dMaxLimit', max_digits=18, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    ismain = models.NullBooleanField(db_column='IsMain', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ExamProject'

class TExpertlevel(models.Model):
    levelindex = models.TextField(db_column='LevelIndex') # Field name made lowercase.
    levelname = models.CharField(db_column='LevelName', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ExpertLevel'

class TExpertstrongkind(models.Model):
    typeindex = models.IntegerField(db_column='TypeIndex') # Field name made lowercase.
    expertid = models.TextField(db_column='ExpertID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ExpertStrongKind'

class TExperts(models.Model):
    expertid = models.TextField(db_column='ExpertID') # Field name made lowercase.
    expertname = models.CharField(db_column='ExpertName', max_length=20, blank=True) # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=10, blank=True) # Field name made lowercase.
    expernumber = models.TextField(db_column='ExperNumber', blank=True) # Field name made lowercase.
    ascription = models.TextField(db_column='Ascription', blank=True) # Field name made lowercase.
    tradeid = models.CharField(db_column='TradeID', max_length=10, blank=True) # Field name made lowercase.
    birthtime = models.DateTimeField(db_column='BirthTime', blank=True, null=True) # Field name made lowercase.
    contactaddress = models.CharField(db_column='ContactAddress', max_length=200, blank=True) # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=20, blank=True) # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=20, blank=True) # Field name made lowercase.
    resume = models.TextField(db_column='Resume', blank=True) # Field name made lowercase. This field type is a guess.
    comparefactid = models.IntegerField(db_column='CompareFactID', blank=True, null=True) # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=50, blank=True) # Field name made lowercase.
    degree = models.CharField(db_column='Degree', max_length=10, blank=True) # Field name made lowercase.
    strong = models.CharField(db_column='Strong', max_length=200, blank=True) # Field name made lowercase.
    strongkey = models.CharField(db_column='StrongKey', max_length=50, blank=True) # Field name made lowercase.
    expertdemo = models.TextField(db_column='ExpertDemo', blank=True) # Field name made lowercase. This field type is a guess.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True) # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True) # Field name made lowercase.
    levelindex = models.ForeignKey(TExpertlevel, db_column='LevelIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Experts'

class TFjalaexcessiveparam(models.Model):
    alaexcessiveparamid = models.IntegerField(db_column='AlaExcessiveParamID') # Field name made lowercase.
    watawsaladisrecordid = models.ForeignKey('TFjwatawsaladisrecord', db_column='WatAWSAlaDisRecordID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    superscalenotes = models.CharField(db_column='SuperscaleNotes', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlaExcessiveParam'

class TFjalareceiptrecord(models.Model):
    alareceiptrecordid = models.IntegerField(db_column='AlaReceiptRecordID') # Field name made lowercase.
    watawsaladisrecordid = models.ForeignKey('TFjwatawsaladisrecord', db_column='WatAWSAlaDisRecordID') # Field name made lowercase.
    alareceiptdept = models.TextField(db_column='AlaReceiptDept', blank=True) # Field name made lowercase.
    alarecname = models.TextField(db_column='AlaRecName', blank=True) # Field name made lowercase.
    alarectime = models.DateTimeField(db_column='AlaRecTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlaReceiptRecord'

class TFjalarmaccountpersonnel(models.Model):
    accountpersonnelid = models.IntegerField(db_column='AccountPersonnelID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    dutytype = models.IntegerField(db_column='DutyType', blank=True, null=True) # Field name made lowercase.
    username = models.TextField(db_column='UserName') # Field name made lowercase.
    tel = models.TextField(db_column='Tel') # Field name made lowercase.
    isresult = models.NullBooleanField(db_column='IsResult') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmAccountPersonnel'

class TFjalarmdisposerecord(models.Model):
    alarmdisposerecordid = models.IntegerField(db_column='AlarmDisposeRecordID') # Field name made lowercase.
    watawsaladisrecordid = models.ForeignKey('TFjnewwatawsaladisrecord', db_column='WatAWSAlaDisRecordID') # Field name made lowercase.
    parentid = models.BigIntegerField(db_column='ParentID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    disposetime = models.DateTimeField(db_column='DisposeTime', blank=True, null=True) # Field name made lowercase.
    disposeopinion = models.TextField(db_column='DisposeOpinion', blank=True) # Field name made lowercase.
    isresult = models.NullBooleanField(db_column='IsResult') # Field name made lowercase.
    isendstate = models.NullBooleanField(db_column='IsEndState', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmDisposeRecord'

class TFjalarmlevelsameset(models.Model):
    ideid = models.IntegerField(db_column='ideID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmLevelSameSet'

class TFjalarmoosrecords(models.Model):
    alarmoosrecordsid = models.IntegerField(db_column='AlarmOosRecordsID') # Field name made lowercase.
    watawsaladisrecordid = models.ForeignKey('TFjnewwatawsaladisrecord', db_column='WatAWSAlaDisRecordID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=4) # Field name made lowercase.
    ooscircs = models.TextField(db_column='OosCircs', blank=True) # Field name made lowercase.
    flagtype = models.CharField(db_column='FlagType', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmOosRecords'

class TFjalarmparamset(models.Model):
    aralmparamsetid = models.IntegerField(db_column='AralmParamSetID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    standardlevel = models.IntegerField(db_column='StandardLevel', blank=True, null=True) # Field name made lowercase.
    degree = models.IntegerField(db_column='Degree', blank=True, null=True) # Field name made lowercase.
    multiple = models.IntegerField(db_column='Multiple', blank=True, null=True) # Field name made lowercase.
    isaralmauditing = models.NullBooleanField(db_column='IsAralmAuditing', blank=True, null=True) # Field name made lowercase.
    isalarm = models.NullBooleanField(db_column='IsAlarm', blank=True, null=True) # Field name made lowercase.
    standardvalue = models.DecimalField(db_column='StandardValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    maxvalue = models.DecimalField(db_column='MaxValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmParamSet'

class TFjalarmsmssendrecord(models.Model):
    smssendid = models.IntegerField(db_column='SMSSendID') # Field name made lowercase.
    watawsaladisrecordid = models.TextField(db_column='WatAWSAlaDisRecordID', blank=True) # Field name made lowercase.
    mobilenum = models.TextField(db_column='MobileNum') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    smscontent = models.TextField(db_column='SMSContent') # Field name made lowercase.
    isresult = models.NullBooleanField(db_column='IsResult') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSMSSendRecord'

class TFjalarmsetcreateday(models.Model):
    createdayid = models.IntegerField(db_column='CreateDayID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    createday = models.IntegerField(db_column='CreateDay') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSetCreateDay'

class TFjalarmsetfourleveltime(models.Model):
    setfourleveltimeid = models.IntegerField(db_column='SetFourLevelTimeID') # Field name made lowercase.
    setfourleveltime = models.FloatField(db_column='SetFourLevelTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSetFourLevelTime'

class TFjalarmsetlevel(models.Model):
    alarmsetlevelid = models.IntegerField(db_column='AlarmSetLevelID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    onelevel = models.NullBooleanField(db_column='OneLevel', blank=True, null=True) # Field name made lowercase.
    twolevel = models.NullBooleanField(db_column='TwoLevel', blank=True, null=True) # Field name made lowercase.
    threelevel = models.NullBooleanField(db_column='ThreeLevel', blank=True, null=True) # Field name made lowercase.
    fourlevel = models.NullBooleanField(db_column='FourLevel', blank=True, null=True) # Field name made lowercase.
    fivelevel = models.NullBooleanField(db_column='FiveLevel', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSetLevel'

class TFjalarmsetoossuccsend(models.Model):
    succsendid = models.IntegerField(db_column='SuccSendID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    isstate = models.NullBooleanField(db_column='IsState') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSetOosSuccSend'

class TFjalarmsetpresstime(models.Model):
    setpresstimeid = models.IntegerField(db_column='SetPressTimeID') # Field name made lowercase.
    alarmsetlevelid = models.ForeignKey(TFjalarmsetlevel, db_column='AlarmSetLevelID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    levels = models.IntegerField(db_column='Levels') # Field name made lowercase.
    pressnum = models.IntegerField(db_column='PressNum') # Field name made lowercase.
    timelimit = models.FloatField(db_column='TimeLimit') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSetPressTime'

class TFjalarmsetsupervisetime(models.Model):
    setsupervisetimeid = models.IntegerField(db_column='SetSuperviseTimeID') # Field name made lowercase.
    supervisetime = models.FloatField(db_column='SuperviseTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSetSuperviseTime'

class TFjalarmsitesetsection(models.Model):
    setsectionid = models.IntegerField(db_column='SetSectionID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    isinterfixsection = models.NullBooleanField(db_column='IsInterfixSection') # Field name made lowercase.
    upstream = models.TextField(db_column='Upstream', blank=True) # Field name made lowercase.
    downstream = models.TextField(db_column='Downstream', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmSiteSetSection'

class TFjalarmstationsetuser(models.Model):
    alarmstationsetuserid = models.IntegerField(db_column='AlarmStationSetUserID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    leveltype = models.IntegerField(db_column='LevelType', blank=True, null=True) # Field name made lowercase.
    usertype = models.IntegerField(db_column='UserType', blank=True, null=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmStationSetUser'

class TFjalarmuserset(models.Model):
    alarmusersetid = models.IntegerField(db_column='AlarmUserSetID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3, blank=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJAlarmUserSet'

class TFjdutycities(models.Model):
    dutycitiesid = models.IntegerField(db_column='DutyCitiesID') # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID') # Field name made lowercase.
    citiesname = models.TextField(db_column='CitiesName') # Field name made lowercase.
    telephonecode = models.TextField(db_column='TelephoneCode', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJDutyCities'

class TFjdutylog(models.Model):
    dutylogid = models.IntegerField(db_column='DutyLogID') # Field name made lowercase.
    dutypersonnelid = models.ForeignKey('TFjdutypersonnel', db_column='DutyPersonnelID') # Field name made lowercase.
    dutyweeks = models.IntegerField(db_column='DutyWeeks') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJDutyLog'

class TFjdutypersonnel(models.Model):
    dutypersonnelid = models.IntegerField(db_column='DutyPersonnelID') # Field name made lowercase.
    dutycitiesid = models.ForeignKey(TFjdutycities, db_column='DutyCitiesID') # Field name made lowercase.
    username = models.TextField(db_column='UserName') # Field name made lowercase.
    regulatorytype = models.SmallIntegerField(db_column='RegulatoryType') # Field name made lowercase.
    tel = models.TextField(db_column='Tel', blank=True) # Field name made lowercase.
    mobile = models.TextField(db_column='Mobile', blank=True) # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJDutyPersonnel'

class TFjnewwatawsaladisrecord(models.Model):
    watawsaladisrecordid = models.TextField(db_column='WatAWSAlaDisRecordID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    isnormal = models.NullBooleanField(db_column='IsNormal', blank=True, null=True) # Field name made lowercase.
    isverify = models.NullBooleanField(db_column='IsVerify', blank=True, null=True) # Field name made lowercase.
    isavailability = models.NullBooleanField(db_column='IsAvailability', blank=True, null=True) # Field name made lowercase.
    makeid = models.TextField(db_column='MakeID', blank=True) # Field name made lowercase.
    supervisedept = models.TextField(db_column='SuperviseDept', blank=True) # Field name made lowercase.
    isinterfixsection = models.NullBooleanField(db_column='IsInterfixSection', blank=True, null=True) # Field name made lowercase.
    upstream = models.TextField(db_column='Upstream', blank=True) # Field name made lowercase.
    downstream = models.TextField(db_column='Downstream', blank=True) # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    sitecircs = models.TextField(db_column='SiteCircs', blank=True) # Field name made lowercase.
    appchecircs = models.TextField(db_column='AppCheCircs', blank=True) # Field name made lowercase.
    operationpersonnel = models.TextField(db_column='OperationPersonnel', blank=True) # Field name made lowercase.
    operationuserid = models.IntegerField(db_column='OperationUserID', blank=True, null=True) # Field name made lowercase.
    operationaddtime = models.DateTimeField(db_column='OperationAddTime', blank=True, null=True) # Field name made lowercase.
    operationstate = models.NullBooleanField(db_column='OperationState', blank=True, null=True) # Field name made lowercase.
    localpersonnel = models.TextField(db_column='LocalPersonnel', blank=True) # Field name made lowercase.
    localuserid = models.IntegerField(db_column='LocalUserID', blank=True, null=True) # Field name made lowercase.
    localsupeaddtime = models.DateTimeField(db_column='LocalSupeAddTime', blank=True, null=True) # Field name made lowercase.
    localsupedeptopinion = models.TextField(db_column='LocalSupeDeptOpinion', blank=True) # Field name made lowercase.
    localstate = models.NullBooleanField(db_column='LocalState', blank=True, null=True) # Field name made lowercase.
    upstreampersonnel = models.TextField(db_column='UpstreamPersonnel', blank=True) # Field name made lowercase.
    upstreamuserid = models.IntegerField(db_column='UpstreamUserID', blank=True, null=True) # Field name made lowercase.
    upstreamaddtime = models.DateTimeField(db_column='UpstreamAddTime', blank=True, null=True) # Field name made lowercase.
    upstreamdeptopinion = models.TextField(db_column='UpstreamDeptOpinion', blank=True) # Field name made lowercase.
    upstreamstate = models.NullBooleanField(db_column='UpstreamState', blank=True, null=True) # Field name made lowercase.
    citylevelpersonnel = models.TextField(db_column='CityLevelPersonnel', blank=True) # Field name made lowercase.
    cityleveluserid = models.IntegerField(db_column='CityLevelUserID', blank=True, null=True) # Field name made lowercase.
    cityleveladdtime = models.DateTimeField(db_column='CityLevelAddTime', blank=True, null=True) # Field name made lowercase.
    citylevelopinion = models.TextField(db_column='CityLevelOpinion', blank=True) # Field name made lowercase.
    citylevelstate = models.NullBooleanField(db_column='CityLevelState', blank=True, null=True) # Field name made lowercase.
    provincialpersonnel = models.TextField(db_column='ProvincialPersonnel', blank=True) # Field name made lowercase.
    provincialuserid = models.IntegerField(db_column='ProvincialUserID', blank=True, null=True) # Field name made lowercase.
    provincialaddtime = models.DateTimeField(db_column='ProvincialAddTime', blank=True, null=True) # Field name made lowercase.
    provincialopinion = models.TextField(db_column='ProvincialOpinion', blank=True) # Field name made lowercase.
    provincialstate = models.NullBooleanField(db_column='ProvincialState', blank=True, null=True) # Field name made lowercase.
    isresult = models.NullBooleanField(db_column='IsResult', blank=True, null=True) # Field name made lowercase.
    smsstate = models.NullBooleanField(db_column='SMSState', blank=True, null=True) # Field name made lowercase.
    keymessage = models.TextField(db_column='KeyMessage', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJNewWatAWSAlaDisRecord'

class TFjwatawsaladisrecord(models.Model):
    watawsaladisrecordid = models.TextField(db_column='WatAWSAlaDisRecordID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    makeid = models.TextField(db_column='MakeID') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    supervisedept = models.TextField(db_column='SuperviseDept', blank=True) # Field name made lowercase.
    sectioncircs = models.TextField(db_column='SectionCircs', blank=True) # Field name made lowercase.
    isinterfixsection = models.NullBooleanField(db_column='IsInterfixSection', blank=True, null=True) # Field name made lowercase.
    upstream = models.TextField(db_column='Upstream', blank=True) # Field name made lowercase.
    downstream = models.TextField(db_column='Downstream', blank=True) # Field name made lowercase.
    findtime = models.DateTimeField(db_column='FindTime', blank=True, null=True) # Field name made lowercase.
    sitecircs = models.TextField(db_column='SiteCircs', blank=True) # Field name made lowercase.
    appchecircs = models.TextField(db_column='AppCheCircs', blank=True) # Field name made lowercase.
    maintaincircs = models.TextField(db_column='MaintainCircs', blank=True) # Field name made lowercase.
    relieftime = models.DateTimeField(db_column='ReliefTime', blank=True, null=True) # Field name made lowercase.
    operationpersonnel = models.TextField(db_column='OperationPersonnel', blank=True) # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True) # Field name made lowercase.
    operationstate = models.SmallIntegerField(db_column='OperationState', blank=True, null=True) # Field name made lowercase.
    operationuserid = models.IntegerField(db_column='OperationUserID', blank=True, null=True) # Field name made lowercase.
    localsupedeptopinion = models.TextField(db_column='LocalSupeDeptOpinion', blank=True) # Field name made lowercase.
    localpersonnel = models.TextField(db_column='LocalPersonnel', blank=True) # Field name made lowercase.
    localsupeaddtime = models.DateTimeField(db_column='LocalSupeAddTime', blank=True, null=True) # Field name made lowercase.
    localuserid = models.IntegerField(db_column='LocalUserID', blank=True, null=True) # Field name made lowercase.
    localstate = models.SmallIntegerField(db_column='LocalState', blank=True, null=True) # Field name made lowercase.
    upstreamdeptopinion = models.TextField(db_column='UpstreamDeptOpinion', blank=True) # Field name made lowercase.
    upstreampersonnel = models.TextField(db_column='UpstreamPersonnel', blank=True) # Field name made lowercase.
    upstreamaddtime = models.DateTimeField(db_column='UpstreamAddTime', blank=True, null=True) # Field name made lowercase.
    upstreamuserid = models.IntegerField(db_column='UpstreamUserID', blank=True, null=True) # Field name made lowercase.
    upstreamstate = models.SmallIntegerField(db_column='UpstreamState', blank=True, null=True) # Field name made lowercase.
    citylevelopinion = models.TextField(db_column='CityLevelOpinion', blank=True) # Field name made lowercase.
    citylevelpersonnel = models.TextField(db_column='CityLevelPersonnel', blank=True) # Field name made lowercase.
    cityleveladdtime = models.DateTimeField(db_column='CityLevelAddTime', blank=True, null=True) # Field name made lowercase.
    cityleveluserid = models.IntegerField(db_column='CityLevelUserID', blank=True, null=True) # Field name made lowercase.
    citylevelstate = models.SmallIntegerField(db_column='CityLevelState', blank=True, null=True) # Field name made lowercase.
    provincialopinion = models.TextField(db_column='ProvincialOpinion', blank=True) # Field name made lowercase.
    provincialpersonnel = models.TextField(db_column='ProvincialPersonnel', blank=True) # Field name made lowercase.
    provincialaddtime = models.DateTimeField(db_column='ProvincialAddTime', blank=True, null=True) # Field name made lowercase.
    provincialuserid = models.IntegerField(db_column='ProvincialUserID', blank=True, null=True) # Field name made lowercase.
    provincialstate = models.SmallIntegerField(db_column='ProvincialState', blank=True, null=True) # Field name made lowercase.
    isresult = models.NullBooleanField(db_column='IsResult', blank=True, null=True) # Field name made lowercase.
    isverify = models.NullBooleanField(db_column='IsVerify', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FJWatAWSAlaDisRecord'

class TFacilitiesoperateratedata(models.Model):
    facilitiesoperaterateid = models.IntegerField(db_column='FacilitiesOperateRateID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    begtime = models.DateTimeField(db_column='BegTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    userid = models.BigIntegerField(db_column='UserID') # Field name made lowercase.
    idetype = models.SmallIntegerField(db_column='IdeType') # Field name made lowercase.
    outagecause = models.TextField(db_column='OutageCause') # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_FacilitiesOperateRateData'

class TFactrecord(models.Model):
    recordid = models.IntegerField(db_column='RecordID') # Field name made lowercase.
    rectifyrecordid = models.TextField(db_column='RectifyRecordID') # Field name made lowercase.
    moniday = models.DateTimeField(db_column='MoniDay', blank=True, null=True) # Field name made lowercase.
    collectiontime = models.DateTimeField(db_column='CollectionTime', blank=True, null=True) # Field name made lowercase.
    labvalue = models.DecimalField(db_column='LabValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    machinevalue = models.DecimalField(db_column='MachineValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    errorpersent = models.CharField(db_column='ErrorPersent', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FactRecord'

class TFaltpoint(models.Model):
    faltid = models.CharField(db_column='FaltID', max_length=20) # Field name made lowercase.
    childsystemid = models.ForeignKey(TChildsystem, db_column='ChildSystemID') # Field name made lowercase.
    faltpointname = models.CharField(db_column='FaltPointName', max_length=50, blank=True) # Field name made lowercase.
    casediscript = models.CharField(db_column='CaseDIsCript', max_length=1000, blank=True) # Field name made lowercase.
    faltcount = models.IntegerField(db_column='FaltCount', blank=True, null=True) # Field name made lowercase.
    solutions = models.CharField(db_column='Solutions', max_length=1000, blank=True) # Field name made lowercase.
    normaldate = models.DateTimeField(db_column='NormalDate', blank=True, null=True) # Field name made lowercase.
    applyname = models.CharField(db_column='ApplyName', max_length=50, blank=True) # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FaltPoint'

class TFault(models.Model):
    faultid = models.CharField(db_column='FaultID', max_length=20) # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    faultstarttime = models.DateTimeField(db_column='FaultStartTime', blank=True, null=True) # Field name made lowercase.
    faultcase = models.CharField(db_column='FaultCase', max_length=1000, blank=True) # Field name made lowercase.
    artificialmoncase = models.CharField(db_column='ArtificialMonCase', max_length=1000, blank=True) # Field name made lowercase.
    normaltime = models.DateTimeField(db_column='NormalTime', blank=True, null=True) # Field name made lowercase.
    aftermachinecase = models.CharField(db_column='AfterMachineCase', max_length=1000, blank=True) # Field name made lowercase.
    afteradjustcase = models.CharField(db_column='AfterAdjustCase', max_length=1000, blank=True) # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Fault'

class TFluegascoualarmerror(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    errorrate = models.DecimalField(db_column='ErrorRate', max_digits=12, decimal_places=4) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FlueGasCouAlarmError'

class TFluegascoualarmuser(models.Model):
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_FlueGasCouAlarmUser'

class TFonts(models.Model):
    fonttype = models.IntegerField(db_column='FontType') # Field name made lowercase.
    fontname = models.CharField(db_column='FontName', max_length=50, blank=True) # Field name made lowercase.
    fontcolor = models.TextField(db_column='FontColor', blank=True) # Field name made lowercase.
    fontsize = models.IntegerField(db_column='FontSize', blank=True, null=True) # Field name made lowercase.
    fontdemo = models.CharField(db_column='FontDemo', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Fonts'

class TFunc(models.Model):
    funid = models.IntegerField(db_column='FunID') # Field name made lowercase.
    funhigherid = models.IntegerField(db_column='FunHigherID', blank=True, null=True) # Field name made lowercase.
    funname = models.TextField(db_column='FunName') # Field name made lowercase.
    fundemo = models.CharField(db_column='FunDemo', max_length=500, blank=True) # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=2, blank=True) # Field name made lowercase.
    pageurl = models.TextField(db_column='PageUrl', blank=True) # Field name made lowercase.
    indexs = models.TextField(db_column='Indexs', blank=True) # Field name made lowercase.
    isflag = models.SmallIntegerField(db_column='IsFlag') # Field name made lowercase.
    picaddress = models.TextField(db_column='PicAddress', blank=True) # Field name made lowercase.
    systemid = models.CharField(db_column='SystemID', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Func'

class TGpslog(models.Model):
    gpsid = models.IntegerField(db_column='GPSID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID', blank=True, null=True) # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime', blank=True, null=True) # Field name made lowercase.
    longitude = models.TextField(db_column='Longitude', blank=True) # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GPSLog'

class TGasdistributed(models.Model):
    distributedid = models.IntegerField(db_column='DistributedID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    functionid = models.IntegerField(db_column='FunctionID', blank=True, null=True) # Field name made lowercase.
    protectid = models.IntegerField(db_column='ProtectID', blank=True, null=True) # Field name made lowercase.
    counts = models.IntegerField(db_column='Counts', blank=True, null=True) # Field name made lowercase.
    targetname = models.TextField(db_column='TargetName', blank=True) # Field name made lowercase.
    longitude = models.TextField(db_column='Longitude', blank=True) # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True) # Field name made lowercase.
    distance = models.FloatField(db_column='Distance', blank=True, null=True) # Field name made lowercase.
    cpersonname = models.TextField(db_column='CpersonName', blank=True) # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True) # Field name made lowercase.
    directionindex = models.TextField(db_column='DirectionIndex', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GasDistributed'

class TGasfunction(models.Model):
    functionid = models.IntegerField(db_column='FunctionID') # Field name made lowercase.
    functionname = models.TextField(db_column='FunctionName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GasFunction'

class TGasmonirecord(models.Model):
    recordid = models.IntegerField(db_column='RecordID') # Field name made lowercase.
    rectifyrecordid = models.TextField(db_column='RectifyRecordID') # Field name made lowercase.
    monitime = models.DateTimeField(db_column='MoniTime', blank=True, null=True) # Field name made lowercase.
    methoda = models.DecimalField(db_column='MethodA', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    methodb = models.DecimalField(db_column='MethodB', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    compareab = models.DecimalField(db_column='CompareAB', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GasMoniRecord'

class TGasprotect(models.Model):
    protectid = models.IntegerField(db_column='ProtectID') # Field name made lowercase.
    protectname = models.TextField(db_column='ProtectName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GasProtect'

class TGradecontent(models.Model):
    gradecontentid = models.IntegerField(db_column='GradeContentID') # Field name made lowercase.
    grageitemid = models.ForeignKey('TGradeitem', db_column='GrageItemID', blank=True, null=True) # Field name made lowercase.
    gradecontent = models.TextField(db_column='GradeContent', blank=True) # Field name made lowercase. This field type is a guess.
    detail = models.CharField(db_column='Detail', max_length=200, blank=True) # Field name made lowercase.
    iswaterorair = models.IntegerField(db_column='IsWaterOrAir', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GradeContent'

class TGradeitem(models.Model):
    grageitemid = models.IntegerField(db_column='GrageItemID') # Field name made lowercase.
    grageitemname = models.CharField(db_column='GrageItemName', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GradeItem'

class TGradelog(models.Model):
    gradelogid = models.IntegerField(db_column='GradeLogID') # Field name made lowercase.
    comparefactid = models.IntegerField(db_column='CompareFactID', blank=True, null=True) # Field name made lowercase.
    accout = models.FloatField(db_column='Accout', blank=True, null=True) # Field name made lowercase.
    cause = models.CharField(db_column='Cause', max_length=1000, blank=True) # Field name made lowercase.
    gradecontentid = models.IntegerField(db_column='GradeContentID', blank=True, null=True) # Field name made lowercase.
    gradetotallogid = models.BigIntegerField(db_column='GradeTotalLogID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GradeLog'

class TGradetotallog(models.Model):
    gradetotallogid = models.IntegerField(db_column='GradeTotalLogID') # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=14) # Field name made lowercase.
    daytime = models.DateTimeField(db_column='DayTime', blank=True, null=True) # Field name made lowercase.
    totalcent = models.FloatField(db_column='TotalCent', blank=True, null=True) # Field name made lowercase.
    years = models.IntegerField(db_column='Years', blank=True, null=True) # Field name made lowercase.
    isseason = models.SmallIntegerField(db_column='IsSeason', blank=True, null=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_GradeTotalLog'

class TJurymaterials(models.Model):
    materialsindex = models.TextField(db_column='MaterialsIndex') # Field name made lowercase.
    materialsname = models.CharField(db_column='MaterialsName', max_length=100, blank=True) # Field name made lowercase.
    chemname = models.CharField(db_column='ChemName', max_length=100, blank=True) # Field name made lowercase.
    compid = models.IntegerField(db_column='CompID', blank=True, null=True) # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    minstock = models.DecimalField(db_column='MinStock', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    maxstock = models.DecimalField(db_column='MaxStock', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=10, blank=True) # Field name made lowercase.
    manname = models.CharField(db_column='ManName', max_length=10, blank=True) # Field name made lowercase.
    manmobile = models.TextField(db_column='ManMobile', blank=True) # Field name made lowercase.
    manphone = models.TextField(db_column='ManPhone', blank=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True) # Field name made lowercase.
    long = models.CharField(db_column='Long', max_length=12, blank=True) # Field name made lowercase.
    lat = models.CharField(db_column='Lat', max_length=12, blank=True) # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase. This field type is a guess.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True) # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_JuryMaterials'

class TJuryprocess(models.Model):
    processid = models.TextField(db_column='ProcessID') # Field name made lowercase.
    typeid = models.ForeignKey(TDrillingtype, db_column='TypeID', blank=True, null=True) # Field name made lowercase.
    processindex = models.IntegerField(db_column='ProcessIndex', blank=True, null=True) # Field name made lowercase.
    processname = models.CharField(db_column='ProcessName', max_length=500, blank=True) # Field name made lowercase.
    commandcode = models.CharField(db_column='CommandCode', max_length=10, blank=True) # Field name made lowercase.
    param = models.CharField(db_column='Param', max_length=10, blank=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=1000, blank=True) # Field name made lowercase.
    screenindex = models.ForeignKey('TScreenenum', db_column='ScreenIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_JuryProcess'

class TKeymessage(models.Model):
    keymessageid = models.IntegerField(db_column='KeyMessageID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    releasetime = models.DateTimeField(db_column='ReleaseTime', blank=True, null=True) # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=400, blank=True) # Field name made lowercase.
    ipaddress = models.TextField(db_column='IPAddress', blank=True) # Field name made lowercase.
    releasecontent = models.CharField(db_column='ReleaseContent', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_KeyMessage'

class TKeyparams(models.Model):
    keyprojectindex = models.ForeignKey('TKeyprojects', db_column='KeyProjectIndex') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_KeyParams'

class TKeyprojects(models.Model):
    keyprojectindex = models.TextField(db_column='KeyProjectIndex') # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=200, blank=True) # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True) # Field name made lowercase.
    long = models.TextField(db_column='Long', blank=True) # Field name made lowercase.
    lat = models.TextField(db_column='Lat', blank=True) # Field name made lowercase.
    borderline = models.TextField(db_column='BorderLine', blank=True) # Field name made lowercase. This field type is a guess.
    keytypeindex = models.ForeignKey('TKeytype', db_column='KeyTypeIndex', blank=True, null=True) # Field name made lowercase.
    mancounts = models.DecimalField(db_column='ManCounts', max_digits=18, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    animalscounts = models.DecimalField(db_column='AnimalsCounts', max_digits=18, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    projectdemo = models.CharField(db_column='ProjectDemo', max_length=500, blank=True) # Field name made lowercase.
    iskeypoint = models.NullBooleanField(db_column='IsKeyPoint', blank=True, null=True) # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True) # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True) # Field name made lowercase.
    isload = models.NullBooleanField(db_column='IsLoad', blank=True, null=True) # Field name made lowercase.
    namelnglat = models.TextField(db_column='NameLngLat', blank=True) # Field name made lowercase. This field type is a guess.
    fonttype = models.ForeignKey(TFonts, db_column='FontType', blank=True, null=True) # Field name made lowercase.
    colors = models.CharField(db_column='Colors', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_KeyProjects'

class TKeytype(models.Model):
    keytypeindex = models.TextField(db_column='KeyTypeIndex') # Field name made lowercase.
    keytypename = models.CharField(db_column='KeyTypeName', max_length=100, blank=True) # Field name made lowercase.
    keytypedemo = models.CharField(db_column='KeyTypeDemo', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_KeyType'

class TLevelitem(models.Model):
    levelitemid = models.IntegerField(db_column='LevelItemID') # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_LevelItem'

class TLocaltestdata(models.Model):
    celementsindex = models.ForeignKey(TCeelement, db_column='CElementsIndex') # Field name made lowercase.
    sampletime = models.DateTimeField(db_column='SampleTime') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=18, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    sampleaddress = models.CharField(db_column='SampleAddress', max_length=500, blank=True) # Field name made lowercase.
    sampledeep = models.DecimalField(db_column='SampleDeep', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    testtime = models.DateTimeField(db_column='TestTime', blank=True, null=True) # Field name made lowercase.
    testvalue = models.DecimalField(db_column='TestValue', max_digits=18, decimal_places=5, blank=True, null=True) # Field name made lowercase.
    menname = models.CharField(db_column='MenName', max_length=50, blank=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=2000, blank=True) # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True) # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_LocalTestData'

class TLog(models.Model):
    num = models.IntegerField(db_column='Num') # Field name made lowercase.
    logtype = models.SmallIntegerField(db_column='LogType') # Field name made lowercase.
    loglevel = models.SmallIntegerField(db_column='LogLevel') # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True) # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True) # Field name made lowercase.
    logtitle = models.CharField(db_column='LogTitle', max_length=50) # Field name made lowercase.
    logtext = models.TextField(db_column='LogText', blank=True) # Field name made lowercase. This field type is a guess.
    writetime = models.DateTimeField(db_column='WriteTime', blank=True, null=True) # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID', blank=True, null=True) # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID', blank=True, null=True) # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Log'

class TLogdict(models.Model):
    logid = models.TextField(db_column='LogID') # Field name made lowercase.
    logrange = models.CharField(db_column='LogRange', max_length=2, blank=True) # Field name made lowercase.
    logtype = models.CharField(db_column='LogType', max_length=2, blank=True) # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_LogDict'

class TMachinetype(models.Model):
    typeid = models.IntegerField(db_column='TypeID') # Field name made lowercase.
    typename = models.TextField(db_column='TypeName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MachineType'

class TMainproduct(models.Model):
    productid = models.TextField(db_column='ProductID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    pstorwayid = models.IntegerField(db_column='PstorWayID', blank=True, null=True) # Field name made lowercase.
    sstorwayid = models.IntegerField(db_column='SstorWayID', blank=True, null=True) # Field name made lowercase.
    mstateid = models.IntegerField(db_column='MstateID', blank=True, null=True) # Field name made lowercase.
    productwayid = models.IntegerField(db_column='ProductWayID', blank=True, null=True) # Field name made lowercase.
    stateindex = models.TextField(db_column='StateIndex', blank=True) # Field name made lowercase.
    transport = models.TextField(db_column='Transport', blank=True) # Field name made lowercase.
    classtype = models.TextField(db_column='ClassType', blank=True) # Field name made lowercase.
    productname = models.TextField(db_column='ProductName', blank=True) # Field name made lowercase.
    functions = models.TextField(db_column='Functions', blank=True) # Field name made lowercase.
    saleincount = models.DecimalField(db_column='SaleInCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    saleoutcount = models.DecimalField(db_column='SaleOutCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    pareastorcount = models.DecimalField(db_column='PareaStorCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    sareastorcount = models.DecimalField(db_column='SareaStorCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    chemistryname = models.TextField(db_column='ChemistryName', blank=True) # Field name made lowercase.
    casnumber = models.CharField(db_column='CASNumber', max_length=10, blank=True) # Field name made lowercase.
    pability = models.DecimalField(db_column='Pability', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    factproduct = models.DecimalField(db_column='FactProduct', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MainProduct'

class TMangpslog(models.Model):
    mangpgsindex = models.IntegerField(db_column='ManGPGSIndex') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='UploadTime', blank=True, null=True) # Field name made lowercase.
    longlat = models.TextField(db_column='LongLat', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ManGPSLog'

class TManufacturer(models.Model):
    manufacturerid = models.IntegerField(db_column='ManufacturerID') # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    linkman = models.TextField(db_column='LinkMan', blank=True) # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase.
    ishaverunipmp = models.NullBooleanField(db_column='IsHaveRunIpmp', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Manufacturer'

class TMapmark(models.Model):
    markindex = models.TextField(db_column='MarkIndex') # Field name made lowercase.
    markname = models.CharField(db_column='MarkName', max_length=200, blank=True) # Field name made lowercase.
    marklevel = models.IntegerField(db_column='MarkLevel', blank=True, null=True) # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3, blank=True) # Field name made lowercase.
    markvalue = models.DecimalField(db_column='MarkValue', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    longlat = models.TextField(db_column='LongLat', blank=True) # Field name made lowercase.
    longlats = models.TextField(db_column='LongLats', blank=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase. This field type is a guess.
    marktime = models.DateTimeField(db_column='MarkTime', blank=True, null=True) # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True) # Field name made lowercase.
    ceventindex = models.ForeignKey(TContingencyevent, db_column='CEventIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MapMark'

class TMaterial(models.Model):
    materialid = models.IntegerField(db_column='MaterialID') # Field name made lowercase.
    productid = models.TextField(db_column='ProductID', blank=True) # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    pstorwayid = models.IntegerField(db_column='PstorWayID', blank=True, null=True) # Field name made lowercase.
    sstorwayid = models.IntegerField(db_column='SstorWayID', blank=True, null=True) # Field name made lowercase.
    materialname = models.TextField(db_column='MaterialName', blank=True) # Field name made lowercase.
    chemistryname = models.TextField(db_column='ChemistryName', blank=True) # Field name made lowercase.
    casnumber = models.CharField(db_column='CASNumber', max_length=10, blank=True) # Field name made lowercase.
    usecount = models.DecimalField(db_column='UseCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    singlecount = models.DecimalField(db_column='SingleCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    pareastorcount = models.DecimalField(db_column='PareaStorCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    sareastorcount = models.DecimalField(db_column='SareaStorCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    stateindex = models.TextField(db_column='StateIndex', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Material'

class TMaterialspollutekind(models.Model):
    typeindex = models.IntegerField(db_column='TypeIndex') # Field name made lowercase.
    materialsindex = models.TextField(db_column='MaterialsIndex') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MaterialsPolluteKind'

class TMeasure(models.Model):
    measureid = models.IntegerField(db_column='MeasureID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    waterpathid = models.IntegerField(db_column='WaterPathID', blank=True, null=True) # Field name made lowercase.
    mainchemistryname = models.TextField(db_column='MainChemistryName', blank=True) # Field name made lowercase.
    measurename = models.TextField(db_column='MeasureName', blank=True) # Field name made lowercase.
    chemistrycount = models.DecimalField(db_column='ChemistryCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    chemistrymaxcount = models.DecimalField(db_column='ChemistryMaxCount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    condition = models.TextField(db_column='Condition', blank=True) # Field name made lowercase.
    feature = models.TextField(db_column='Feature', blank=True) # Field name made lowercase.
    leakage = models.TextField(db_column='Leakage', blank=True) # Field name made lowercase.
    orther = models.TextField(db_column='Orther', blank=True) # Field name made lowercase.
    bhavefence = models.NullBooleanField(db_column='bHaveFence', blank=True, null=True) # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True) # Field name made lowercase.
    bhavetube = models.NullBooleanField(db_column='bHaveTube', blank=True, null=True) # Field name made lowercase.
    materialname = models.TextField(db_column='MaterialName', blank=True) # Field name made lowercase.
    bhavealarm = models.NullBooleanField(db_column='bHaveAlarm', blank=True, null=True) # Field name made lowercase.
    monitornet = models.TextField(db_column='MonitorNet', blank=True) # Field name made lowercase.
    absorbname = models.TextField(db_column='AbsorbName', blank=True) # Field name made lowercase.
    evolume = models.FloatField(db_column='Evolume', blank=True, null=True) # Field name made lowercase.
    bhavevalve = models.NullBooleanField(db_column='bHaveValve', blank=True, null=True) # Field name made lowercase.
    dvolume = models.FloatField(db_column='Dvolume', blank=True, null=True) # Field name made lowercase.
    outwherecode = models.CharField(db_column='OutWhereCode', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Measure'

class TMensendsms(models.Model):
    mensendsmsid = models.IntegerField(db_column='MenSendSMSID') # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', blank=True) # Field name made lowercase.
    smscontent = models.CharField(db_column='SmsContent', max_length=1000, blank=True) # Field name made lowercase.
    issuccess = models.NullBooleanField(db_column='IsSuccess', blank=True, null=True) # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MenSendSMS'

class TMessage(models.Model):
    messageid = models.TextField(db_column='MessageID') # Field name made lowercase.
    typeid = models.ForeignKey('TMessagetype', db_column='TypeID') # Field name made lowercase.
    publisher = models.IntegerField(db_column='Publisher') # Field name made lowercase.
    verifyperson = models.IntegerField(db_column='VerifyPerson', blank=True, null=True) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True) # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=1000, blank=True) # Field name made lowercase.
    publishtime = models.DateTimeField(db_column='PublishTime', blank=True, null=True) # Field name made lowercase.
    messagecontent = models.TextField(db_column='MessageContent', blank=True) # Field name made lowercase. This field type is a guess.
    validity = models.DateTimeField(db_column='Validity', blank=True, null=True) # Field name made lowercase.
    verifytime = models.DateTimeField(db_column='VerifyTime', blank=True, null=True) # Field name made lowercase.
    replycontent = models.CharField(db_column='ReplyContent', max_length=1000, blank=True) # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255, blank=True) # Field name made lowercase.
    bdiscuss = models.NullBooleanField(db_column='BDiscuss', blank=True, null=True) # Field name made lowercase.
    clickcount = models.IntegerField(db_column='ClickCount', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Message'

class TMessagetype(models.Model):
    typeid = models.IntegerField(db_column='TypeID') # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MessageType'

class TMobileevent(models.Model):
    eventid = models.IntegerField(db_column='EventID') # Field name made lowercase.
    busaddress = models.CharField(db_column='BusAddress', max_length=200, blank=True) # Field name made lowercase.
    moveevgs = models.CharField(db_column='MoveEvgs', max_length=200, blank=True) # Field name made lowercase.
    eventtime = models.DateTimeField(db_column='EventTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MobileEvent'

class TMoniconclusion(models.Model):
    conclusionid = models.IntegerField(db_column='ConclusionID') # Field name made lowercase.
    recordid = models.ForeignKey('TMonireportcontent', db_column='RecordID', blank=True, null=True) # Field name made lowercase.
    commonitorreportid = models.ForeignKey(TCommonitorreport, db_column='ComMonitorReportID', blank=True, null=True) # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=14, blank=True) # Field name made lowercase.
    conclusioncontent = models.CharField(db_column='ConclusionContent', max_length=1000, blank=True) # Field name made lowercase.
    monitime = models.DateTimeField(db_column='MoniTime', blank=True, null=True) # Field name made lowercase.
    creater = models.CharField(db_column='Creater', max_length=50, blank=True) # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True) # Field name made lowercase.
    updateusername = models.CharField(db_column='UpdateUserName', max_length=50, blank=True) # Field name made lowercase.
    years = models.IntegerField(db_column='Years', blank=True, null=True) # Field name made lowercase.
    season = models.SmallIntegerField(db_column='Season', blank=True, null=True) # Field name made lowercase.
    ischeckout = models.SmallIntegerField(db_column='IsCheckOut', blank=True, null=True) # Field name made lowercase.
    isupfile = models.NullBooleanField(db_column='IsUpFile') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MoniConclusion'

class TMonireportcontent(models.Model):
    recordid = models.IntegerField(db_column='RecordID') # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=14, blank=True) # Field name made lowercase.
    recordcontent = models.TextField(db_column='RecordContent', blank=True) # Field name made lowercase. This field type is a guess.
    newrecordcontent = models.TextField(db_column='NewRecordContent', blank=True) # Field name made lowercase. This field type is a guess.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True) # Field name made lowercase.
    adduser = models.CharField(db_column='AddUser', max_length=50, blank=True) # Field name made lowercase.
    updateusername = models.CharField(db_column='UpdateUserName', max_length=50, blank=True) # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True) # Field name made lowercase.
    season = models.SmallIntegerField(db_column='Season', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MoniReportContent'

class TMonitornolaunchcause(models.Model):
    nolaunchcauseid = models.IntegerField(db_column='NoLaunchCauseID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=20) # Field name made lowercase.
    years = models.IntegerField(db_column='Years') # Field name made lowercase.
    isseason = models.IntegerField(db_column='IsSeason') # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType') # Field name made lowercase.
    cause = models.TextField(db_column='Cause') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MonitorNoLaunchCause'

class TMonitorparamreport(models.Model):
    monitorparamreportid = models.TextField(db_column='MonitorParamReportID') # Field name made lowercase.
    monitortime = models.DateTimeField(db_column='MonitorTime') # Field name made lowercase.
    commonitorreportid = models.ForeignKey(TCommonitorreport, db_column='ComMonitorReportID') # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode') # Field name made lowercase.
    monitorvalue = models.DecimalField(db_column='MonitorValue', max_digits=12, decimal_places=4) # Field name made lowercase.
    colindex = models.IntegerField(db_column='ColIndex', blank=True, null=True) # Field name made lowercase.
    rowindex = models.IntegerField(db_column='RowIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MonitorParamReport'

class TMonitorparamresult(models.Model):
    commonitorreportid = models.ForeignKey(TCommonitorreport, db_column='ComMonitorReportID') # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode') # Field name made lowercase.
    monitorresult = models.IntegerField(db_column='MonitorResult') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_MonitorParamResult'

class TMonitorrecord(models.Model):
    recordid = models.IntegerField(db_column='RecordID') # Field name made lowercase.
    rectifyrecordid = models.TextField(db_column='RectifyRecordID') # Field name made lowercase.
    monititime = models.DateTimeField(db_column='MonitiTime', blank=True, null=True) # Field name made lowercase.
    monitoringcontent = models.TextField(db_column='MonitoringContent', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_MonitorRecord'

class TMstate(models.Model):
    mstateid = models.IntegerField(db_column='MstateID') # Field name made lowercase.
    statename = models.TextField(db_column='StateName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Mstate'

class TNvzsstation(models.Model):
    nvzsid = models.ForeignKey('TSetnvzs', db_column='NvzsID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_NvzsStation'

class TOnlineinfo(models.Model):
    areaid = models.ForeignKey(TAdminarea, db_column='AreaID') # Field name made lowercase.
    netcounts = models.IntegerField(db_column='NetCounts', blank=True, null=True) # Field name made lowercase.
    onlinecount = models.IntegerField(db_column='OnlineCount', blank=True, null=True) # Field name made lowercase.
    onlinerate = models.FloatField(db_column='OnlineRate', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OnlineInfo'

class TOosdisposal(models.Model):
    oosid = models.IntegerField(db_column='OosID') # Field name made lowercase.
    parentid = models.ForeignKey('self', db_column='ParentID', blank=True, null=True) # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID', blank=True, null=True) # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True) # Field name made lowercase.
    isremind = models.SmallIntegerField(db_column='IsRemind') # Field name made lowercase.
    isresult = models.SmallIntegerField(db_column='IsResult') # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=300, blank=True) # Field name made lowercase.
    isadopt = models.SmallIntegerField(db_column='IsAdopt') # Field name made lowercase.
    begtime = models.DateTimeField(db_column='BegTime', blank=True, null=True) # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True) # Field name made lowercase.
    mergeid = models.TextField(db_column='MergeID', blank=True) # Field name made lowercase.
    finishtime = models.DateTimeField(db_column='FinishTime', blank=True, null=True) # Field name made lowercase.
    againremind = models.NullBooleanField(db_column='AgainRemind', blank=True, null=True) # Field name made lowercase.
    mobilenum = models.TextField(db_column='MobileNum', blank=True) # Field name made lowercase.
    smscontent = models.TextField(db_column='SMSContent', blank=True) # Field name made lowercase.
    reviewstate = models.NullBooleanField(db_column='ReviewState', blank=True, null=True) # Field name made lowercase.
    iseventend = models.NullBooleanField(db_column='IsEventEnd') # Field name made lowercase.
    isfinish = models.NullBooleanField(db_column='IsFinish', blank=True, null=True) # Field name made lowercase.
    isconclusion = models.NullBooleanField(db_column='IsConclusion') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OosDisposal'

class TOoseventsmslog(models.Model):
    logid = models.IntegerField(db_column='logID') # Field name made lowercase.
    rcvuserid = models.IntegerField(db_column='RcvUserID') # Field name made lowercase.
    mobilenum = models.TextField(db_column='MobileNum') # Field name made lowercase.
    topparentoosid = models.IntegerField(db_column='TopParentOosID') # Field name made lowercase.
    parentoosid = models.IntegerField(db_column='ParentOosID') # Field name made lowercase.
    curoosid = models.IntegerField(db_column='CurOosID') # Field name made lowercase.
    inserttime = models.DateTimeField(db_column='InsertTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OosEventSmsLog'

class TOosjointhearingstat(models.Model):
    oj_id = models.IntegerField(db_column='OJ_ID') # Field name made lowercase.
    datatype = models.SmallIntegerField(db_column='DataType') # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID') # Field name made lowercase.
    weekindex = models.SmallIntegerField(db_column='WeekIndex', blank=True, null=True) # Field name made lowercase.
    datastartdate = models.DateTimeField(db_column='DataStartDate', blank=True, null=True) # Field name made lowercase.
    dataenddate = models.DateTimeField(db_column='DataEndDate', blank=True, null=True) # Field name made lowercase.
    wateroosnum = models.IntegerField(db_column='WaterOosNum', blank=True, null=True) # Field name made lowercase.
    airoosnum = models.IntegerField(db_column='AirOosNum', blank=True, null=True) # Field name made lowercase.
    startoosnum = models.IntegerField(db_column='StartOosNum', blank=True, null=True) # Field name made lowercase.
    starteventnum = models.IntegerField(db_column='StartEventNum', blank=True, null=True) # Field name made lowercase.
    surveyoosnum = models.IntegerField(db_column='SurveyOosNum', blank=True, null=True) # Field name made lowercase.
    surveyeventnum = models.IntegerField(db_column='SurveyEventNum', blank=True, null=True) # Field name made lowercase.
    jointoosnum = models.IntegerField(db_column='JointOosNum', blank=True, null=True) # Field name made lowercase.
    jointeventnum = models.IntegerField(db_column='JointEventNum', blank=True, null=True) # Field name made lowercase.
    supervisionunfinish = models.IntegerField(db_column='SupervisionUnfinish', blank=True, null=True) # Field name made lowercase.
    supervisionfinish = models.IntegerField(db_column='SupervisionFinish', blank=True, null=True) # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OosJoinThearingStat'

class TOosrecord(models.Model):
    oosreid = models.IntegerField(db_column='OosReID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode') # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime') # Field name made lowercase.
    datatab = models.SmallIntegerField(db_column='DataTab') # Field name made lowercase.
    datatype = models.TextField(db_column='DataType', blank=True) # Field name made lowercase.
    dvalue = models.DecimalField(db_column='dValue', max_digits=9, decimal_places=0) # Field name made lowercase.
    isresult = models.SmallIntegerField(db_column='IsResult', blank=True, null=True) # Field name made lowercase.
    ismerge = models.BigIntegerField(db_column='IsMerge') # Field name made lowercase.
    mergeid = models.TextField(db_column='MergeID', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OosRecord'

class TOutwhere(models.Model):
    outwherecode = models.CharField(db_column='OutWhereCode', max_length=10) # Field name made lowercase.
    outwhere = models.CharField(db_column='OutWhere', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OutWhere'

class TOutagemarkingdata(models.Model):
    markingdataid = models.IntegerField(db_column='MarkingDataID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    datatype = models.CharField(db_column='DataType', max_length=8) # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    userid = models.BigIntegerField(db_column='UserID') # Field name made lowercase.
    outagecause = models.TextField(db_column='OutageCause') # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_OutageMarkingData'

class TOutagetimeinterval(models.Model):
    outagetimeintervalid = models.IntegerField(db_column='OutageTimeIntervalID') # Field name made lowercase.
    plantshssfid = models.ForeignKey('TPlantshssfdesurun', db_column='PlantShssfID') # Field name made lowercase.
    begtime = models.DateTimeField(db_column='BegTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime') # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType') # Field name made lowercase.
    causes = models.TextField(db_column='Causes', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OutageTimeInterval'

class TOverproofaviso(models.Model):
    overproofavisoid = models.IntegerField(db_column='OverproofAvisoID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode') # Field name made lowercase.
    years = models.IntegerField(db_column='Years') # Field name made lowercase.
    quarters = models.IntegerField(db_column='Quarters') # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType') # Field name made lowercase.
    overproofcou = models.IntegerField(db_column='OverProofCou') # Field name made lowercase.
    lastquerytime = models.DateTimeField(db_column='LastQueryTime', blank=True, null=True) # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_OverproofAviso'

class TPdafunc(models.Model):
    funid = models.IntegerField(db_column='FunID') # Field name made lowercase.
    funname = models.TextField(db_column='FunName') # Field name made lowercase.
    fundemo = models.CharField(db_column='FunDemo', max_length=500, blank=True) # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True) # Field name made lowercase.
    pageurl = models.TextField(db_column='PageUrl', blank=True) # Field name made lowercase.
    indexs = models.TextField(db_column='Indexs', blank=True) # Field name made lowercase.
    isflag = models.SmallIntegerField(db_column='IsFlag') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PDAFunc'

class TPdarolefun(models.Model):
    roleid = models.IntegerField(db_column='RoleID') # Field name made lowercase.
    funid = models.IntegerField(db_column='FunID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PDARoleFun'

class TParamstatus(models.Model):
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True) # Field name made lowercase.
    lastchenger = models.CharField(db_column='LastChenger', max_length=20, blank=True) # Field name made lowercase.
    chengetime = models.DateTimeField(db_column='ChengeTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ParamStatus'

class TPart(models.Model):
    partid = models.CharField(db_column='PartID', max_length=20) # Field name made lowercase.
    repairid = models.ForeignKey('TRepairfault', db_column='RepairID') # Field name made lowercase.
    partname = models.CharField(db_column='PartName', max_length=50, blank=True) # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True) # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    arrivetime = models.DateTimeField(db_column='ArriveTime', blank=True, null=True) # Field name made lowercase.
    reciveperson = models.CharField(db_column='RecivePerson', max_length=30, blank=True) # Field name made lowercase.
    riceiver = models.CharField(db_column='Riceiver', max_length=50, blank=True) # Field name made lowercase.
    reciveaddress = models.TextField(db_column='ReciveAddress', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Part'

class TPlanmaterial(models.Model):
    generalplanindex = models.TextField(db_column='GeneralPlanIndex') # Field name made lowercase.
    materialsindex = models.TextField(db_column='MaterialsIndex') # Field name made lowercase.
    useddemo = models.CharField(db_column='UsedDemo', max_length=500, blank=True) # Field name made lowercase.
    replacername = models.CharField(db_column='ReplacerName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PlanMaterial'

class TPlanparams(models.Model):
    paramcode = models.CharField(db_column='ParamCode', max_length=3) # Field name made lowercase.
    generalplanindex = models.TextField(db_column='GeneralPlanIndex') # Field name made lowercase.
    limitvalue = models.DecimalField(db_column='LimitValue', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    ismain = models.NullBooleanField(db_column='IsMain', blank=True, null=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PlanParams'

class TPlantrunlog(models.Model):
    daytime = models.DateTimeField(db_column='DayTime') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    powerstoptime = models.TextField(db_column='PowerStopTime', blank=True) # Field name made lowercase.
    desulfurizationstoptime = models.TextField(db_column='DesulfurizationStopTime', blank=True) # Field name made lowercase.
    powerdegrees = models.IntegerField(db_column='PowerDegrees', blank=True, null=True) # Field name made lowercase.
    coalconsumption = models.DecimalField(db_column='CoalConsumption', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    sulfurratio = models.DecimalField(db_column='SulfurRatio', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    inputtime = models.DateTimeField(db_column='InputTime', blank=True, null=True) # Field name made lowercase.
    ismodify = models.NullBooleanField(db_column='IsModify', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PlantRunLog'

class TPlantshssfdesurun(models.Model):
    plantshssfid = models.TextField(db_column='PlantShssfID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    runstate = models.NullBooleanField(db_column='RunState', blank=True, null=True) # Field name made lowercase.
    dayadds = models.DateTimeField(db_column='DayAdds') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True) # Field name made lowercase.
    generatedenergy = models.DecimalField(db_column='GeneratedEnergy', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    aircrewload = models.DecimalField(db_column='AircrewLoad', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    actualconsumecoal = models.DecimalField(db_column='ActualConsumeCoal', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    originallyconsumecoal = models.DecimalField(db_column='OriginallyConsumeCoal', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    coalavgsulfurcontent = models.DecimalField(db_column='CoalAvgSulfurContent', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    dynamorunduration = models.DecimalField(db_column='DynamoRunDuration', max_digits=12, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    machineoutagething = models.TextField(db_column='MachineOutageThing', blank=True) # Field name made lowercase.
    calciumcurrentpcnt = models.DecimalField(db_column='CalciumCurrentPcnt', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    tlrunduration = models.DecimalField(db_column='TLRunDuration', max_digits=12, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    tlrunthing = models.TextField(db_column='TLRunThing', blank=True) # Field name made lowercase.
    onlinemonitoryfumes = models.DecimalField(db_column='OnlineMonitorYFumes', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    onlineyscalarcouval = models.DecimalField(db_column='OnlineYScalarCouVal', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    onlinemonitorjfumes = models.DecimalField(db_column='OnlineMonitorJFumes', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    onlinejscalarcouval = models.DecimalField(db_column='OnlineJScalarCouVal', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    equitableso2zschroma = models.DecimalField(db_column='EquitableSO2ZsChroma', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    equitablecleanso2zschroma = models.DecimalField(db_column='EquitableCleanSO2ZsChroma', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    shsreleasequantity = models.DecimalField(db_column='SHSReleaseQuantity', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    yshsreleasequantity = models.DecimalField(db_column='YSHSReleaseQuantity', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    shscalccarbcontent = models.DecimalField(db_column='ShsCalcCarbContent', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    yhsgypsumfactvalue = models.DecimalField(db_column='YhsGypsumFactValue', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    hsgypsumoutput = models.DecimalField(db_column='HsGypsumOutput', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    gypsumwatercontent = models.DecimalField(db_column='GypsumWaterContent', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    bypassopenduration = models.DecimalField(db_column='ByPassOpenDuration', max_digits=12, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    bypassopenthing = models.TextField(db_column='ByPassOpenThing', blank=True) # Field name made lowercase.
    openbypassgendur = models.DecimalField(db_column='OpenByPassGenDur', max_digits=12, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    jyqcommissduration = models.DecimalField(db_column='JYQCommissDuration', max_digits=12, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    jyqcommissthing = models.TextField(db_column='JYQCommissThing', blank=True) # Field name made lowercase.
    yyqcommissduration = models.DecimalField(db_column='YYQCommissDuration', max_digits=12, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    yyqcommissthing = models.TextField(db_column='YYQCommissThing', blank=True) # Field name made lowercase.
    zxjcdatadesulfidation = models.DecimalField(db_column='ZXJCDataDesulfidation', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    matterdesulphur = models.DecimalField(db_column='Matterdesulphur', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    decokeefficiency = models.DecimalField(db_column='DecokeEfficiency', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    matterdesulphurefficiency = models.DecimalField(db_column='MatterdesulphurEfficiency', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    handiworksetefficiency = models.DecimalField(db_column='HandiworkSetEfficiency', max_digits=12, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    onlinegascou = models.DecimalField(db_column='OnlineGasCou', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    jlgascou = models.DecimalField(db_column='JLGasCou', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    isfinish = models.NullBooleanField(db_column='IsFinish', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PlantShssfDesuRun'

class TPollutefactlog(models.Model):
    pollutefactlogid = models.TextField(db_column='PolluteFactLogID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime') # Field name made lowercase.
    begtime = models.DateTimeField(db_column='BegTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime') # Field name made lowercase.
    paramcode = models.TextField(db_column='ParamCode') # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase. This field type is a guess.
    isresult = models.NullBooleanField(db_column='IsResult') # Field name made lowercase.
    transactorid = models.IntegerField(db_column='TransactorID', blank=True, null=True) # Field name made lowercase.
    transactortime = models.DateTimeField(db_column='TransactorTime', blank=True, null=True) # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True) # Field name made lowercase. This field type is a guess.
    isidentify = models.NullBooleanField(db_column='IsIdentify', blank=True, null=True) # Field name made lowercase.
    isflag = models.SmallIntegerField(db_column='IsFlag') # Field name made lowercase.
    isenabled = models.NullBooleanField(db_column='IsEnabled', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PolluteFactLog'

class TPollutelevel(models.Model):
    pollutelevelindex = models.IntegerField(db_column='PolluteLevelIndex') # Field name made lowercase.
    pollutelevelname = models.CharField(db_column='PolluteLevelName', max_length=50, blank=True) # Field name made lowercase.
    polluteleveldemo = models.CharField(db_column='PolluteLevelDemo', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PolluteLevel'

class TPolluteresult(models.Model):
    polluteresultid = models.IntegerField(db_column='PolluteResultID') # Field name made lowercase.
    conclusionid = models.BigIntegerField(db_column='ConclusionID', blank=True, null=True) # Field name made lowercase.
    superviseconclusionid = models.BigIntegerField(db_column='SuperviseConclusionID', blank=True, null=True) # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True) # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=14, blank=True) # Field name made lowercase.
    isaccess = models.NullBooleanField(db_column='IsAccess', blank=True, null=True) # Field name made lowercase.
    years = models.IntegerField(db_column='Years', blank=True, null=True) # Field name made lowercase.
    isseason = models.SmallIntegerField(db_column='IsSeason', blank=True, null=True) # Field name made lowercase.
    conclusioncontent = models.TextField(db_column='ConclusionContent', blank=True) # Field name made lowercase. This field type is a guess.
    transactor = models.CharField(db_column='Transactor', max_length=50, blank=True) # Field name made lowercase.
    isdonewith = models.NullBooleanField(db_column='IsDoneWith', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PolluteResult'

class TPollutetype(models.Model):
    typeindex = models.IntegerField(db_column='TypeIndex') # Field name made lowercase.
    highertypeid = models.IntegerField(db_column='HigherTypeID', blank=True, null=True) # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=200, blank=True) # Field name made lowercase.
    typedemo = models.CharField(db_column='TypeDemo', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PolluteType'

class TProcessparam(models.Model):
    processid = models.CharField(db_column='ProcessID', max_length=36) # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ProcessParam'

class TProdmanaattribute(models.Model):
    prodmanaattributeid = models.IntegerField(db_column='ProdManaAttributeID') # Field name made lowercase.
    producesysmanageid = models.TextField(db_column='ProduceSysManageID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    inoutflag = models.IntegerField(db_column='InOutFlag') # Field name made lowercase.
    installedcapacity = models.DecimalField(db_column='InstalledCapacity', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ProdManaAttribute'

class TProducesysmanage(models.Model):
    producesysmanageid = models.TextField(db_column='ProduceSysManageID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    producesysname = models.TextField(db_column='ProduceSysName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ProduceSysManage'

class TProductway(models.Model):
    productwayid = models.IntegerField(db_column='ProductWayID') # Field name made lowercase.
    wayname = models.TextField(db_column='WayName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ProductWay'

class TPublicverifyone(models.Model):
    verifyid = models.IntegerField(db_column='VerifyID') # Field name made lowercase.
    verifytime = models.DateTimeField(db_column='VerifyTime', blank=True, null=True) # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    facilitymodel = models.TextField(db_column='FacilityModel', blank=True) # Field name made lowercase.
    lawperson = models.TextField(db_column='LawPerson', blank=True) # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=10, blank=True) # Field name made lowercase.
    comparefactid = models.IntegerField(db_column='CompareFactID', blank=True, null=True) # Field name made lowercase.
    ischeckup = models.NullBooleanField(db_column='IsCheckUp', blank=True, null=True) # Field name made lowercase.
    checkupdemo = models.CharField(db_column='CheckUpDemo', max_length=500, blank=True) # Field name made lowercase.
    maintain = models.TextField(db_column='Maintain', blank=True) # Field name made lowercase.
    perambulate = models.TextField(db_column='Perambulate', blank=True) # Field name made lowercase.
    checkandadjust = models.TextField(db_column='CheckAndAdjust', blank=True) # Field name made lowercase.
    replaces = models.TextField(db_column='Replaces', blank=True) # Field name made lowercase.
    exceptiondealwith = models.TextField(db_column='ExceptionDealWith', blank=True) # Field name made lowercase.
    havecertificate = models.TextField(db_column='HaveCertificate', blank=True) # Field name made lowercase.
    potency = models.NullBooleanField(db_column='Potency', blank=True, null=True) # Field name made lowercase.
    flow = models.NullBooleanField(db_column='Flow', blank=True, null=True) # Field name made lowercase.
    cou = models.NullBooleanField(db_column='Cou', blank=True, null=True) # Field name made lowercase.
    dayrpt = models.NullBooleanField(db_column='DayRpt', blank=True, null=True) # Field name made lowercase.
    monthrpt = models.NullBooleanField(db_column='MonthRpt', blank=True, null=True) # Field name made lowercase.
    quarterrpt = models.NullBooleanField(db_column='QuarterRpt', blank=True, null=True) # Field name made lowercase.
    ishavetag = models.NullBooleanField(db_column='IsHaveTag', blank=True, null=True) # Field name made lowercase.
    isdealwith = models.NullBooleanField(db_column='IsDealwith', blank=True, null=True) # Field name made lowercase.
    checkman = models.CharField(db_column='CheckMan', max_length=50, blank=True) # Field name made lowercase.
    checktime = models.DateTimeField(db_column='CheckTime', blank=True, null=True) # Field name made lowercase.
    factman = models.CharField(db_column='FactMan', max_length=50, blank=True) # Field name made lowercase.
    factwritetime = models.DateTimeField(db_column='FactWriteTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PublicVerifyOne'

class TPublicverifytwo(models.Model):
    verifyid = models.IntegerField(db_column='VerifyID') # Field name made lowercase.
    isviolatesetparam = models.NullBooleanField(db_column='IsViolateSetParam', blank=True, null=True) # Field name made lowercase.
    waterishave = models.NullBooleanField(db_column='WaterIsHave', blank=True, null=True) # Field name made lowercase.
    airishave = models.NullBooleanField(db_column='AirIsHave', blank=True, null=True) # Field name made lowercase.
    runrate = models.DecimalField(db_column='RunRate', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    transfersrate = models.DecimalField(db_column='TransfersRate', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=1000, blank=True) # Field name made lowercase.
    watersetid = models.IntegerField(db_column='WaterSetID', blank=True, null=True) # Field name made lowercase.
    airparamsetid = models.IntegerField(db_column='AirParamSetID', blank=True, null=True) # Field name made lowercase.
    years = models.IntegerField(db_column='Years', blank=True, null=True) # Field name made lowercase.
    isseason = models.SmallIntegerField(db_column='IsSeason', blank=True, null=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_PublicVerifyTwo'

class TQualityctl(models.Model):
    qualitycrlid = models.IntegerField(db_column='QualityCrlID') # Field name made lowercase.
    titleid = models.ForeignKey('TQualitytitle', db_column='TitleID', blank=True, null=True) # Field name made lowercase.
    itemid = models.ForeignKey('TRunitem', db_column='ItemID', blank=True, null=True) # Field name made lowercase.
    statusid = models.NullBooleanField(db_column='StatusID', blank=True, null=True) # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_QualityCtl'

class TQualitytitle(models.Model):
    titleid = models.IntegerField(db_column='TitleID') # Field name made lowercase.
    titlecontent = models.CharField(db_column='TitleContent', max_length=1000) # Field name made lowercase.
    titletime = models.DateTimeField(db_column='TitleTime') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID', blank=True, null=True) # Field name made lowercase.
    ipaddress = models.TextField(db_column='IPAddress', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_QualityTitle'

class TReagentitem(models.Model):
    readentindex = models.IntegerField(db_column='ReadentIndex') # Field name made lowercase.
    reagentname = models.CharField(db_column='ReagentName', max_length=500, blank=True) # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3, blank=True) # Field name made lowercase.
    manufacturerid = models.IntegerField(db_column='ManufacturerID', blank=True, null=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ReagentItem'

class TReagentreplacing(models.Model):
    replacingindex = models.IntegerField(db_column='ReplacingIndex') # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True) # Field name made lowercase.
    replacetime = models.DateTimeField(db_column='ReplaceTime', blank=True, null=True) # Field name made lowercase.
    standardvalue = models.DecimalField(db_column='StandardValue', max_digits=10, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    precision = models.DecimalField(db_column='Precision', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    interferecomp = models.CharField(db_column='InterfereComp', max_length=1000, blank=True) # Field name made lowercase.
    examparmid = models.IntegerField(db_column='ExamParmID', blank=True, null=True) # Field name made lowercase.
    readentindex = models.BigIntegerField(db_column='ReadentIndex', blank=True, null=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ReagentReplacing'

class TRecordcation(models.Model):
    cationid = models.BigIntegerField(db_column='CationID') # Field name made lowercase.
    tableid = models.IntegerField(db_column='TableID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID', blank=True, null=True) # Field name made lowercase.
    writeperson = models.TextField(db_column='WritePerson', blank=True) # Field name made lowercase.
    writetime = models.DateTimeField(db_column='WriteTime', blank=True, null=True) # Field name made lowercase.
    checkperson = models.TextField(db_column='CheckPerson', blank=True) # Field name made lowercase.
    checktime = models.DateTimeField(db_column='CheckTime', blank=True, null=True) # Field name made lowercase.
    bcomplete = models.NullBooleanField(db_column='bComplete', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RecordCation'

class TRectifydemand(models.Model):
    rectifydemandid = models.TextField(db_column='RectifyDemandID') # Field name made lowercase.
    superviseconclusionid = models.BigIntegerField(db_column='SuperviseConclusionID', blank=True, null=True) # Field name made lowercase.
    conclusionid = models.BigIntegerField(db_column='ConclusionID', blank=True, null=True) # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    years = models.IntegerField(db_column='Years', blank=True, null=True) # Field name made lowercase.
    isseason = models.SmallIntegerField(db_column='IsSeason', blank=True, null=True) # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=60, blank=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True) # Field name made lowercase.
    invalidbegtime = models.DateTimeField(db_column='InvalidBegTime', blank=True, null=True) # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True) # Field name made lowercase. This field type is a guess.
    finishtimelimit = models.DateTimeField(db_column='FinishTimelimit', blank=True, null=True) # Field name made lowercase.
    iscomparison = models.NullBooleanField(db_column='IsComparison', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RectifyDemand'

class TRectifymonitorresult(models.Model):
    rectifyresultid = models.IntegerField(db_column='RectifyResultID') # Field name made lowercase.
    rectifyrecordid = models.TextField(db_column='RectifyRecordID') # Field name made lowercase.
    comparisonerror = models.TextField(db_column='ComparisonError', blank=True) # Field name made lowercase.
    iseligible = models.NullBooleanField(db_column='IsEligible') # Field name made lowercase.
    comparisonunit = models.TextField(db_column='ComparisonUnit', blank=True) # Field name made lowercase.
    comparisontime = models.DateTimeField(db_column='ComparisonTime', blank=True, null=True) # Field name made lowercase.
    comparisonnum = models.TextField(db_column='ComparisonNum', blank=True) # Field name made lowercase.
    reporturl = models.TextField(db_column='ReportUrl', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RectifyMonitorResult'

class TRectifyrecord(models.Model):
    rectifyrecordid = models.TextField(db_column='RectifyRecordID') # Field name made lowercase.
    rectifydemandid = models.TextField(db_column='RectifyDemandID') # Field name made lowercase.
    paramcode = models.CharField(db_column='ParamCode', max_length=3, blank=True) # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True) # Field name made lowercase. This field type is a guess.
    addtime = models.DateTimeField(db_column='AddTime', blank=True, null=True) # Field name made lowercase.
    adduser = models.CharField(db_column='AddUser', max_length=50, blank=True) # Field name made lowercase.
    ischeckout = models.NullBooleanField(db_column='IsCheckOut', blank=True, null=True) # Field name made lowercase.
    addtype = models.SmallIntegerField(db_column='AddType', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RectifyRecord'

class TRepairfault(models.Model):
    repairid = models.CharField(db_column='RepairID', max_length=20) # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    person = models.CharField(db_column='Person', max_length=30, blank=True) # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True) # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20, blank=True) # Field name made lowercase.
    repairperson = models.CharField(db_column='RepairPerson', max_length=30, blank=True) # Field name made lowercase.
    wperson = models.CharField(db_column='WPerson', max_length=30, blank=True) # Field name made lowercase.
    wtel = models.CharField(db_column='WTel', max_length=20, blank=True) # Field name made lowercase.
    wfax = models.CharField(db_column='WFax', max_length=10, blank=True) # Field name made lowercase.
    reorttime = models.DateTimeField(db_column='ReortTime', blank=True, null=True) # Field name made lowercase.
    rebacktime = models.DateTimeField(db_column='ReBackTime', blank=True, null=True) # Field name made lowercase.
    servicecost = models.DecimalField(db_column='ServiceCost', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    traffic = models.DecimalField(db_column='Traffic', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=400, blank=True) # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RepairFault'

class TReplacemon(models.Model):
    replacemonid = models.CharField(db_column='ReplaceMonID', max_length=20) # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    way = models.CharField(db_column='Way', max_length=10, blank=True) # Field name made lowercase.
    bakmachine = models.CharField(db_column='BakMachine', max_length=50, blank=True) # Field name made lowercase.
    bakmachinestarttime = models.DateTimeField(db_column='BakMachineStartTime', blank=True, null=True) # Field name made lowercase.
    bakmachinerpttime = models.DateTimeField(db_column='BakMachineRptTime', blank=True, null=True) # Field name made lowercase.
    bakmachineexamproject = models.CharField(db_column='BakMachineExamProject', max_length=20, blank=True) # Field name made lowercase.
    bakmachinefinishtime = models.DateTimeField(db_column='BakMachineFinishTime', blank=True, null=True) # Field name made lowercase.
    adjustperson = models.CharField(db_column='AdjustPerson', max_length=10, blank=True) # Field name made lowercase.
    adjustcase = models.CharField(db_column='AdjustCase', max_length=400, blank=True) # Field name made lowercase.
    adjustresult = models.CharField(db_column='AdjustResult', max_length=400, blank=True) # Field name made lowercase.
    artificialtime = models.DateTimeField(db_column='ArtificialTime', blank=True, null=True) # Field name made lowercase.
    samplingaddress = models.TextField(db_column='SamplingAddress', blank=True) # Field name made lowercase.
    recoverytime = models.DateTimeField(db_column='RecoveryTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ReplaceMon'

class TRequirement(models.Model):
    requireid = models.CharField(db_column='RequireID', max_length=18) # Field name made lowercase.
    demandsubject = models.TextField(db_column='DemandSubject', blank=True) # Field name made lowercase.
    prioritylevel = models.IntegerField(db_column='PriorityLevel', blank=True, null=True) # Field name made lowercase.
    submittime = models.DateTimeField(db_column='SubmitTime', blank=True, null=True) # Field name made lowercase.
    hopecompletetime = models.DateTimeField(db_column='HopeCompleteTime', blank=True, null=True) # Field name made lowercase.
    submitperson = models.CharField(db_column='SubmitPerson', max_length=50, blank=True) # Field name made lowercase.
    submituniti = models.CharField(db_column='SubmitUniti', max_length=100, blank=True) # Field name made lowercase.
    requirementexplain = models.TextField(db_column='RequirementExplain', blank=True) # Field name made lowercase. This field type is a guess.
    feasibility = models.TextField(db_column='Feasibility', blank=True) # Field name made lowercase. This field type is a guess.
    processresult = models.TextField(db_column='ProcessResult', blank=True) # Field name made lowercase. This field type is a guess.
    requirementstatus = models.CharField(db_column='RequirementStatus', max_length=1, blank=True) # Field name made lowercase.
    functionown = models.CharField(db_column='FunctionOwn', max_length=100, blank=True) # Field name made lowercase.
    processname = models.CharField(db_column='ProcessName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Requirement'

class TReviewconcentration(models.Model):
    reviewid = models.CharField(db_column='ReviewID', max_length=20) # Field name made lowercase.
    recodeid = models.ForeignKey(TAdjustrecord, db_column='RecodeID') # Field name made lowercase.
    concentration = models.DecimalField(db_column='Concentration', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    reviewsource = models.CharField(db_column='ReviewSource', max_length=200, blank=True) # Field name made lowercase.
    drug = models.TextField(db_column='Drug', blank=True) # Field name made lowercase.
    setperson = models.CharField(db_column='SetPerson', max_length=30, blank=True) # Field name made lowercase.
    testresult = models.DecimalField(db_column='TestResult', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    relativeerror = models.DecimalField(db_column='RelativeError', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    cconcentration = models.DecimalField(db_column='CConcentration', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    creviewsource = models.CharField(db_column='CReviewSource', max_length=200, blank=True) # Field name made lowercase.
    cdrug = models.TextField(db_column='CDrug', blank=True) # Field name made lowercase.
    csetperson = models.CharField(db_column='CSetPerson', max_length=30, blank=True) # Field name made lowercase.
    ctestresult = models.DecimalField(db_column='CTestResult', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    crelativeerror = models.DecimalField(db_column='CRelativeError', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    processcase = models.CharField(db_column='ProcessCase', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ReviewConcentration'

class TRoad(models.Model):
    roadid = models.IntegerField(db_column='RoadID') # Field name made lowercase.
    roadname = models.TextField(db_column='RoadName') # Field name made lowercase.
    long = models.TextField(blank=True)
    lat = models.TextField(db_column='Lat', blank=True) # Field name made lowercase.
    latlong = models.TextField(db_column='LatLong', blank=True) # Field name made lowercase. This field type is a guess.
    roadborder = models.TextField(db_column='RoadBorder', blank=True) # Field name made lowercase. This field type is a guess.
    namelatlong = models.TextField(db_column='NameLatLong', blank=True) # Field name made lowercase. This field type is a guess.
    isload = models.NullBooleanField(db_column='IsLoad', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Road'

class TRole(models.Model):
    roleid = models.IntegerField(db_column='RoleID') # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=50, blank=True) # Field name made lowercase.
    rolelevel = models.IntegerField(db_column='RoleLevel', blank=True, null=True) # Field name made lowercase.
    higherroleid = models.IntegerField(db_column='HigherRoleID', blank=True, null=True) # Field name made lowercase.
    specialname = models.TextField(db_column='SpecialName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Role'

class TRolefun(models.Model):
    funid = models.IntegerField(db_column='FunID') # Field name made lowercase.
    roleid = models.BigIntegerField(db_column='RoleID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RoleFun'

class TRunitem(models.Model):
    itemid = models.ForeignKey('self', db_column='ItemID') # Field name made lowercase.
    higheritemid = models.BigIntegerField(db_column='HigherItemID', blank=True, null=True) # Field name made lowercase.
    itemname = models.TextField(db_column='ItemName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RunItem'

class TRunlogbyuser(models.Model):
    logid = models.IntegerField(db_column='LogID') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID', blank=True, null=True) # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID', blank=True, null=True) # Field name made lowercase.
    abntime = models.DateTimeField(db_column='AbnTime', blank=True, null=True) # Field name made lowercase.
    macinfo = models.CharField(db_column='MacInfo', max_length=500, blank=True) # Field name made lowercase.
    loadinfo = models.TextField(db_column='LoadInfo', blank=True) # Field name made lowercase.
    fatherruninfo = models.CharField(db_column='FatherRunInfo', max_length=500, blank=True) # Field name made lowercase.
    automotruninfo = models.CharField(db_column='AutoMotRunInfo', max_length=500, blank=True) # Field name made lowercase.
    rtdper = models.DecimalField(db_column='RtdPer', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    minper = models.DecimalField(db_column='MinPer', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    hourper = models.DecimalField(db_column='HourPer', max_digits=10, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='UploadTime', blank=True, null=True) # Field name made lowercase.
    filename = models.TextField(db_column='FileName', blank=True) # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True) # Field name made lowercase.
    ischecked = models.NullBooleanField(db_column='IsChecked', blank=True, null=True) # Field name made lowercase.
    isreaded = models.NullBooleanField(db_column='IsReaded', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_RunLogByUser'

class TSavesource(models.Model):
    sourceid = models.IntegerField(db_column='SourceID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeID', blank=True, null=True) # Field name made lowercase.
    sourcename = models.TextField(db_column='SourceName', blank=True) # Field name made lowercase.
    havecount = models.IntegerField(db_column='HaveCount', blank=True, null=True) # Field name made lowercase.
    needcount = models.IntegerField(db_column='NeedCount', blank=True, null=True) # Field name made lowercase.
    suppliername = models.TextField(db_column='SupplierName', blank=True) # Field name made lowercase.
    cpersonname = models.TextField(db_column='CpersonName', blank=True) # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SaveSource'

class TScreenenum(models.Model):
    screenindex = models.IntegerField(db_column='ScreenIndex') # Field name made lowercase.
    screenname = models.CharField(db_column='ScreenName', max_length=200, blank=True) # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=14, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ScreenEnum'

class TSecondproduct(models.Model):
    productid = models.TextField(db_column='ProductID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    productname = models.TextField(db_column='ProductName', blank=True) # Field name made lowercase.
    chemistryname = models.TextField(db_column='ChemistryName', blank=True) # Field name made lowercase.
    casnumber = models.CharField(db_column='CASNumber', max_length=10, blank=True) # Field name made lowercase.
    fcount = models.DecimalField(db_column='Fcount', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    useway = models.TextField(db_column='UseWay', blank=True) # Field name made lowercase.
    stateindex = models.TextField(db_column='StateIndex', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SecondProduct'

class TServicerecord(models.Model):
    serviceid = models.CharField(db_column='ServiceID', max_length=20) # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    checker = models.CharField(db_column='Checker', max_length=10, blank=True) # Field name made lowercase.
    serviceperson = models.CharField(db_column='ServicePerson', max_length=30, blank=True) # Field name made lowercase.
    servicestarttime = models.DateTimeField(db_column='ServiceStartTime', blank=True, null=True) # Field name made lowercase.
    serviceendtime = models.DateTimeField(db_column='ServiceEndTime', blank=True, null=True) # Field name made lowercase.
    servicecase = models.CharField(db_column='ServiceCase', max_length=1000, blank=True) # Field name made lowercase.
    machinestate = models.CharField(db_column='MachineState', max_length=1000, blank=True) # Field name made lowercase.
    isadjust = models.NullBooleanField(db_column='IsAdjust', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ServiceRecord'

class TSetalarmdatatype(models.Model):
    alarmtypeid = models.IntegerField(db_column='AlarmTypeID') # Field name made lowercase.
    setalarmparamid = models.ForeignKey('TSetalarmparam', db_column='SetAlarmParamID') # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType') # Field name made lowercase.
    isnum = models.NullBooleanField(db_column='IsNum') # Field name made lowercase.
    alarmcou = models.IntegerField(db_column='AlarmCou', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SetAlarmDataType'

class TSetalarmparam(models.Model):
    setalarmparamid = models.TextField(db_column='SetAlarmParamID') # Field name made lowercase.
    examparmid = models.ForeignKey(TExamproject, db_column='ExamParmID') # Field name made lowercase.
    isalarm = models.NullBooleanField(db_column='IsAlarm') # Field name made lowercase.
    isfiltero2val = models.NullBooleanField(db_column='IsFilterO2Val', blank=True, null=True) # Field name made lowercase.
    iso2alarm = models.NullBooleanField(db_column='IsO2Alarm', blank=True, null=True) # Field name made lowercase.
    appendcontent = models.TextField(db_column='AppendContent', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SetAlarmParam'

class TSetalarmuser(models.Model):
    setalarmparamid = models.ForeignKey(TSetalarmparam, db_column='SetAlarmParamID') # Field name made lowercase.
    userid = models.ForeignKey('TUser', db_column='UserID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SetAlarmUser'

class TSetnvzs(models.Model):
    nvzsid = models.IntegerField(db_column='NvzsID') # Field name made lowercase.
    nvzsname = models.CharField(db_column='NVZsName', max_length=30) # Field name made lowercase.
    hourvalue = models.DecimalField(db_column='HourValue', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    dayvalue = models.DecimalField(db_column='DayValue', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SetNvzs'

class TSitenolaunchcause(models.Model):
    nolaunchcauseid = models.IntegerField(db_column='NoLaunchCauseID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    years = models.IntegerField(db_column='Years') # Field name made lowercase.
    cause = models.TextField(db_column='Cause') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SiteNoLaunchCause'

class TStandardrecord(models.Model):
    recordid = models.IntegerField(db_column='RecordID') # Field name made lowercase.
    rectifyrecordid = models.TextField(db_column='RectifyRecordID') # Field name made lowercase.
    moniday = models.DateTimeField(db_column='MoniDay', blank=True, null=True) # Field name made lowercase.
    standardvalue = models.DecimalField(db_column='StandardValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    machinevalue = models.DecimalField(db_column='MachineValue', max_digits=18, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    errorpersent = models.CharField(db_column='ErrorPersent', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_StandardRecord'

class TStatetype(models.Model):
    stateindex = models.TextField(db_column='StateIndex') # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_StateType'

class TStationkind(models.Model):
    kindid = models.IntegerField(db_column='KindID') # Field name made lowercase.
    kindname = models.CharField(db_column='KindName', max_length=30, blank=True) # Field name made lowercase.
    ismobile = models.NullBooleanField(db_column='IsMobile', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_StationKind'

class TStationoptlog(models.Model):
    optlogid = models.IntegerField(db_column='OptLogID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID', blank=True, null=True) # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime', blank=True, null=True) # Field name made lowercase.
    optid = models.CharField(db_column='OptID', max_length=8) # Field name made lowercase.
    logid = models.ForeignKey(TLogdict, db_column='LogID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_StationOptLog'

class TStatuschangerecord(models.Model):
    recordid = models.IntegerField(db_column='RecordID') # Field name made lowercase.
    examparmid = models.IntegerField(db_column='ExamParmID') # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime') # Field name made lowercase.
    isvalid = models.NullBooleanField(db_column='IsValid') # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime') # Field name made lowercase.
    changername = models.TextField(db_column='ChangerName', blank=True) # Field name made lowercase.
    pollutefactlogid = models.TextField(db_column='PolluteFactLogID', blank=True) # Field name made lowercase.
    rectifydemandid = models.TextField(db_column='RectifyDemandID', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_StatusChangeRecord'

class TStorway(models.Model):
    storwayid = models.IntegerField(db_column='StorWayID') # Field name made lowercase.
    storwayname = models.CharField(db_column='StorWayName', max_length=100) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_StorWay'

class TSubstanceclass(models.Model):
    classid = models.IntegerField(db_column='ClassID') # Field name made lowercase.
    classtypeid = models.ForeignKey(TClasstype, db_column='ClassTypeID') # Field name made lowercase.
    classname = models.TextField(db_column='ClassName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SubstanceClass'

class TSuperscale(models.Model):
    examid = models.IntegerField(db_column='ExamID') # Field name made lowercase.
    examparmid = models.ForeignKey(TExamproject, db_column='ExamParmID') # Field name made lowercase.
    levelid = models.IntegerField(db_column='LevelID', blank=True, null=True) # Field name made lowercase.
    standardvalue = models.FloatField(db_column='StandardValue', blank=True, null=True) # Field name made lowercase.
    standarddemo = models.CharField(db_column='StandardDemo', max_length=100, blank=True) # Field name made lowercase.
    isapply = models.NullBooleanField(db_column='IsApply', blank=True, null=True) # Field name made lowercase.
    maxvalue = models.FloatField(db_column='MaxValue', blank=True, null=True) # Field name made lowercase.
    datatype = models.TextField(db_column='DataType', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Superscale'

class TSuperviseconclusion(models.Model):
    superviseconclusionid = models.IntegerField(db_column='SuperviseConclusionID') # Field name made lowercase.
    verifyid = models.IntegerField(db_column='VerifyID', blank=True, null=True) # Field name made lowercase.
    gradetotallogid = models.BigIntegerField(db_column='GradeTotalLogID', blank=True, null=True) # Field name made lowercase.
    ischeckout = models.NullBooleanField(db_column='IsCheckOut', blank=True, null=True) # Field name made lowercase.
    isviolatesetparam = models.NullBooleanField(db_column='IsViolateSetParam', blank=True, null=True) # Field name made lowercase.
    signofftime = models.DateTimeField(db_column='SignOffTime', blank=True, null=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    years = models.IntegerField(db_column='Years', blank=True, null=True) # Field name made lowercase.
    isseason = models.SmallIntegerField(db_column='IsSeason', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SuperviseConclusion'

class TSystemnames(models.Model):
    systemid = models.CharField(db_column='SystemID', max_length=10) # Field name made lowercase.
    systemname = models.CharField(db_column='SystemName', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_SystemNames'

class TTabletype(models.Model):
    tableid = models.IntegerField(db_column='TableID') # Field name made lowercase.
    tablename = models.TextField(db_column='TableName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_TableType'

class TTagdict(models.Model):
    tagid = models.CharField(db_column='TagID', max_length=5) # Field name made lowercase.
    remark = models.TextField(db_column='Remark') # Field name made lowercase.
    isstation = models.NullBooleanField(db_column='IsStation') # Field name made lowercase.
    isplatform = models.NullBooleanField(db_column='IsPlatform') # Field name made lowercase.
    isvalid = models.NullBooleanField(db_column='IsValid') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_TagDict'

class TTenprojectitem(models.Model):
    itemid = models.IntegerField(db_column='ItemID') # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_TenProjectItem'

class TTenprojecttxtimage(models.Model):
    txtimageid = models.TextField(db_column='TxtImageID') # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=500, blank=True) # Field name made lowercase.
    savepath = models.CharField(db_column='SavePath', max_length=500, blank=True) # Field name made lowercase.
    txtcontent = models.TextField(db_column='TxtContent', blank=True) # Field name made lowercase. This field type is a guess.
    sortindex = models.IntegerField(db_column='SortIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_TenProjectTxtImage'

class TThreedefenseitem(models.Model):
    defenseid = models.BigIntegerField(db_column='DefenseID') # Field name made lowercase.
    defensename = models.CharField(db_column='DefenseName', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ThreeDefenseItem'

class TThreedefensetxtimage(models.Model):
    txtimageid = models.TextField(db_column='TxtImageID') # Field name made lowercase.
    defenseid = models.BigIntegerField(db_column='DefenseID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=500, blank=True) # Field name made lowercase.
    savepath = models.CharField(db_column='SavePath', max_length=500, blank=True) # Field name made lowercase.
    txtcontent = models.TextField(db_column='TxtContent', blank=True) # Field name made lowercase. This field type is a guess.
    sortindex = models.IntegerField(db_column='SortIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_ThreeDefenseTxtImage'

class TTrade(models.Model):
    tradeid = models.IntegerField(db_column='TradeID') # Field name made lowercase.
    highertradeid = models.BigIntegerField(db_column='HigherTradeID', blank=True, null=True) # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    tradedemo = models.CharField(db_column='TradeDemo', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Trade'

class TTransfers(models.Model):
    transfersid = models.IntegerField(db_column='TransfersID') # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Transfers'

class TTransport(models.Model):
    transportid = models.TextField(db_column='TransportID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID', blank=True, null=True) # Field name made lowercase.
    venturecode = models.TextField(db_column='VentureCode', blank=True) # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True) # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20, blank=True) # Field name made lowercase.
    endaddress = models.CharField(db_column='EndAddress', max_length=200, blank=True) # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True) # Field name made lowercase.
    revtime = models.DateTimeField(db_column='RevTime', blank=True, null=True) # Field name made lowercase.
    receivedcomp = models.CharField(db_column='ReceivedComp', max_length=200, blank=True) # Field name made lowercase.
    receivedman = models.CharField(db_column='ReceivedMan', max_length=20, blank=True) # Field name made lowercase.
    receivedmanphone = models.CharField(db_column='ReceivedManPhone', max_length=20, blank=True) # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=10, blank=True) # Field name made lowercase.
    recman = models.CharField(db_column='RecMan', max_length=20, blank=True) # Field name made lowercase.
    recmanphone = models.CharField(db_column='RecManPhone', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_Transport'

class TTransportbus(models.Model):
    platenumber = models.CharField(db_column='PlateNumber', max_length=10) # Field name made lowercase.
    chauffeur = models.CharField(db_column='Chauffeur', max_length=20, blank=True) # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True) # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex', blank=True, null=True) # Field name made lowercase.
    departid = models.IntegerField(db_column='DepartID', blank=True, null=True) # Field name made lowercase.
    bustype = models.CharField(db_column='BusType', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_TransportBus'

class TTransportway(models.Model):
    transportid = models.IntegerField(db_column='TransportID') # Field name made lowercase.
    transportname = models.TextField(db_column='TransportName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_TransportWay'

class TUser(models.Model):
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    roleid = models.ForeignKey(TRole, db_column='RoleID', blank=True, null=True) # Field name made lowercase.
    username = models.TextField(db_column='UserName', blank=True) # Field name made lowercase.
    userpwd = models.TextField(db_column='UserPwd', blank=True) # Field name made lowercase.
    realname = models.CharField(db_column='RealName', max_length=30, blank=True) # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    enabled = models.NullBooleanField(db_column='Enabled', blank=True, null=True) # Field name made lowercase.
    mobilenum = models.TextField(db_column='MobileNum', blank=True) # Field name made lowercase.
    islogin = models.NullBooleanField(db_column='IsLogin', blank=True, null=True) # Field name made lowercase.
    regtime = models.DateTimeField(db_column='RegTime', blank=True, null=True) # Field name made lowercase.
    firstlogintime = models.DateTimeField(db_column='FirstLoginTime', blank=True, null=True) # Field name made lowercase.
    lastlogintime = models.DateTimeField(db_column='LastLoginTime', blank=True, null=True) # Field name made lowercase.
    logintimes = models.IntegerField(db_column='LoginTimes', blank=True, null=True) # Field name made lowercase.
    createrid = models.ForeignKey('self', db_column='CreaterID', blank=True, null=True) # Field name made lowercase.
    areaid = models.ForeignKey(TAdminarea, db_column='AreaID', blank=True, null=True) # Field name made lowercase.
    dutyid = models.ForeignKey(TDuty, db_column='DutyID', blank=True, null=True) # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True) # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    sex = models.NullBooleanField(db_column='Sex', blank=True, null=True) # Field name made lowercase.
    isinner = models.NullBooleanField(db_column='IsInner', blank=True, null=True) # Field name made lowercase.
    isdeleted = models.NullBooleanField(db_column='IsDeleted') # Field name made lowercase.
    departid = models.IntegerField(db_column='DepartID', blank=True, null=True) # Field name made lowercase.
    areaids = models.IntegerField(db_column='AreaIDs', blank=True, null=True) # Field name made lowercase.
    isacceptdelaymessage = models.NullBooleanField(db_column='IsAcceptDelayMessage', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_User'

class TUseraccesslog(models.Model):
    logid = models.IntegerField(db_column='LogID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    httpurl = models.TextField(db_column='httpUrl') # Field name made lowercase.
    accessip = models.TextField(db_column='AccessIP', blank=True) # Field name made lowercase.
    accesstime = models.DateTimeField(db_column='AccessTime') # Field name made lowercase.
    menuid = models.IntegerField(db_column='MenuID', blank=True, null=True) # Field name made lowercase.
    otherdem = models.CharField(db_column='OtherDem', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserAccessLog'

class TUseractlog(models.Model):
    logid = models.TextField(db_column='LogID') # Field name made lowercase.
    userid = models.ForeignKey(TUser, db_column='UserID') # Field name made lowercase.
    acttime = models.DateTimeField(db_column='ActTime') # Field name made lowercase.
    event = models.TextField(db_column='Event', blank=True) # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    clientip = models.TextField(db_column='ClientIP', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserActLog'

class TUsercdc(models.Model):
    tid = models.ForeignKey('self', db_column='tid', primary_key=True)
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterID', blank=True, null=True) # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True) # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID', blank=True, null=True) # Field name made lowercase.
    username = models.TextField(db_column='UserName', blank=True) # Field name made lowercase.
    userpwd = models.TextField(db_column='UserPwd', blank=True) # Field name made lowercase.
    realname = models.CharField(db_column='RealName', max_length=30, blank=True) # Field name made lowercase.
    sex = models.NullBooleanField(db_column='Sex', blank=True, null=True) # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    mobilenum = models.TextField(db_column='MobileNum', blank=True) # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True) # Field name made lowercase.
    enabled = models.NullBooleanField(db_column='Enabled', blank=True, null=True) # Field name made lowercase.
    islogin = models.NullBooleanField(db_column='IsLogin', blank=True, null=True) # Field name made lowercase.
    regtime = models.DateTimeField(db_column='RegTime', blank=True, null=True) # Field name made lowercase.
    firstlogintime = models.DateTimeField(db_column='FirstLoginTime', blank=True, null=True) # Field name made lowercase.
    lastlogintime = models.DateTimeField(db_column='LastLoginTime', blank=True, null=True) # Field name made lowercase.
    logintimes = models.IntegerField(db_column='LoginTimes', blank=True, null=True) # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    isinner = models.NullBooleanField(db_column='IsInner', blank=True, null=True) # Field name made lowercase.
    isdeleted = models.NullBooleanField(db_column='IsDeleted', blank=True, null=True) # Field name made lowercase.
    dutyid = models.IntegerField(db_column='DutyID', blank=True, null=True) # Field name made lowercase.
    departid = models.IntegerField(db_column='DepartID', blank=True, null=True) # Field name made lowercase.
    opttype = models.SmallIntegerField(db_column='OptType', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserCDC'

class TUsercert(models.Model):
    userid = models.ForeignKey(TUser, db_column='UserID') # Field name made lowercase.
    serialnumber = models.TextField(db_column='SerialNumber') # Field name made lowercase.
    rawdata = models.BinaryField(db_column='RawData', blank=True, null=True) # Field name made lowercase.
    certstate = models.SmallIntegerField(db_column='CertState', blank=True, null=True) # Field name made lowercase.
    opttime = models.DateTimeField(db_column='OptTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserCert'

class TUsercomp(models.Model):
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    isused = models.NullBooleanField(db_column='IsUsed', blank=True, null=True) # Field name made lowercase.
    isreciveemail = models.NullBooleanField(db_column='IsReciveEmail', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserComp'

class TUseromp(models.Model):
    funuserid = models.IntegerField(db_column='FunUserID') # Field name made lowercase.
    funid = models.ForeignKey(TFunc, db_column='FunID', blank=True, null=True) # Field name made lowercase.
    userid = models.ForeignKey(TUser, db_column='UserID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserOmp'

class TUseroosconfig(models.Model):
    configid = models.IntegerField(db_column='ConfigID') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID') # Field name made lowercase. This field type is a guess.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    paramcode = models.TextField(db_column='ParamCode') # Field name made lowercase.
    timetype = models.SmallIntegerField(db_column='TimeType') # Field name made lowercase.
    datatype = models.TextField(db_column='DataType', blank=True) # Field name made lowercase.
    oospercent = models.TextField(db_column='OosPercent') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserOosConfig'

class TUseroptlog(models.Model):
    optlogid = models.IntegerField(db_column='OptLogID') # Field name made lowercase.
    userid = models.ForeignKey(TUser, db_column='UserID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime') # Field name made lowercase.
    computeraddress = models.TextField(db_column='ComputerAddress') # Field name made lowercase.
    logremark = models.TextField(db_column='LogRemark', blank=True) # Field name made lowercase.
    excepttreatlog = models.CharField(db_column='ExceptTreatLog', max_length=1000, blank=True) # Field name made lowercase.
    serviceday = models.DateTimeField(db_column='ServiceDay', blank=True, null=True) # Field name made lowercase.
    ortherwork = models.CharField(db_column='OrtherWork', max_length=1000, blank=True) # Field name made lowercase.
    changesupplies = models.CharField(db_column='ChangeSupplies', max_length=1000, blank=True) # Field name made lowercase.
    leavetime = models.DateTimeField(db_column='LeaveTime', blank=True, null=True) # Field name made lowercase.
    timespend = models.FloatField(db_column='TimeSpend', blank=True, null=True) # Field name made lowercase.
    isdownwrite = models.NullBooleanField(db_column='IsDownWrite', blank=True, null=True) # Field name made lowercase.
    remak = models.CharField(db_column='Remak', max_length=2000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserOptLog'

class TUseroptsyslog(models.Model):
    optlogid = models.IntegerField(db_column='OptLogID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True) # Field name made lowercase.
    opttime = models.DateTimeField(db_column='OptTime', blank=True, null=True) # Field name made lowercase.
    optcontent = models.CharField(db_column='OptContent', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserOptSysLog'

class TUserrole(models.Model):
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserRole'

class TUserstation(models.Model):
    userid = models.ForeignKey(TUser, db_column='UserID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    isreciveemail = models.NullBooleanField(db_column='IsReciveEmail', blank=True, null=True) # Field name made lowercase.
    paramlimit = models.TextField(db_column='ParamLimit', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserStation'

class TUsersyslog(models.Model):
    syslogid = models.TextField(db_column='SysLogID') # Field name made lowercase.
    userid = models.ForeignKey(TUser, db_column='UserID') # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime') # Field name made lowercase.
    computeraddress = models.TextField(db_column='ComputerAddress') # Field name made lowercase.
    logremark = models.TextField(db_column='LogRemark') # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_UserSysLog'

class TVentureparam(models.Model):
    venturecode = models.TextField(db_column='VentureCode') # Field name made lowercase.
    marktypeid = models.ForeignKey(TDangermarktype, db_column='MarkTypeID', blank=True, null=True) # Field name made lowercase.
    stateindex = models.ForeignKey(TStatetype, db_column='StateIndex', blank=True, null=True) # Field name made lowercase.
    gbcode = models.CharField(db_column='GBCode', max_length=50, blank=True) # Field name made lowercase.
    monitorway = models.TextField(db_column='MonitorWay', blank=True) # Field name made lowercase. This field type is a guess.
    casnumber = models.CharField(db_column='CASNumber', max_length=50, blank=True) # Field name made lowercase.
    venturename = models.CharField(db_column='VentureName', max_length=50, blank=True) # Field name made lowercase.
    chemname = models.CharField(db_column='ChemName', max_length=100, blank=True) # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=50, blank=True) # Field name made lowercase.
    orthername = models.TextField(db_column='OrtherName', blank=True) # Field name made lowercase.
    endangerdemo = models.TextField(db_column='EndangerDemo', blank=True) # Field name made lowercase. This field type is a guess.
    formula = models.TextField(db_column='Formula', blank=True) # Field name made lowercase. This field type is a guess.
    weight = models.FloatField(db_column='Weight', blank=True, null=True) # Field name made lowercase.
    meltingpoint = models.TextField(db_column='MeltingPoint', blank=True) # Field name made lowercase. This field type is a guess.
    density = models.TextField(db_column='Density', blank=True) # Field name made lowercase. This field type is a guess.
    shape = models.TextField(db_column='Shape', blank=True) # Field name made lowercase. This field type is a guess.
    boilingpoint = models.TextField(db_column='BoilingPoint', blank=True) # Field name made lowercase. This field type is a guess.
    solubility = models.TextField(db_column='Solubility', blank=True) # Field name made lowercase. This field type is a guess.
    isstable = models.NullBooleanField(db_column='IsStable', blank=True, null=True) # Field name made lowercase.
    functions = models.TextField(db_column='Functions', blank=True) # Field name made lowercase. This field type is a guess.
    laboratorymethod = models.TextField(db_column='LaboratoryMethod', blank=True) # Field name made lowercase. This field type is a guess.
    estandards = models.TextField(db_column='EStandards', blank=True) # Field name made lowercase. This field type is a guess.
    disposalmethods = models.TextField(db_column='DisposalMethods', blank=True) # Field name made lowercase. This field type is a guess.
    demo = models.TextField(db_column='Demo', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_VentureParam'

class TVenturepollutekind(models.Model):
    typeindex = models.IntegerField(db_column='TypeIndex') # Field name made lowercase.
    sourceindex = models.TextField(db_column='SourceIndex') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_VenturePolluteKind'

class TVenturerelative(models.Model):
    relativeid = models.TextField(db_column='RelativeID') # Field name made lowercase.
    sourceindex = models.TextField(db_column='SourceIndex', blank=True) # Field name made lowercase.
    venturecode = models.TextField(db_column='VentureCode', blank=True) # Field name made lowercase.
    reporttime = models.DateTimeField(db_column='ReportTime') # Field name made lowercase.
    nowstorage = models.DecimalField(db_column='NowStorage', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    maxstorage = models.DecimalField(db_column='MaxStorage', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    minstorage = models.DecimalField(db_column='MinStorage', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=10, blank=True) # Field name made lowercase.
    storagetype = models.CharField(db_column='StorageType', max_length=200, blank=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=500, blank=True) # Field name made lowercase.
    stateindex = models.ForeignKey(TStatetype, db_column='StateIndex', blank=True, null=True) # Field name made lowercase.
    isincresse = models.NullBooleanField(db_column='IsIncresse', blank=True, null=True) # Field name made lowercase.
    volumes = models.CharField(db_column='Volumes', max_length=10, blank=True) # Field name made lowercase.
    causedemo = models.CharField(db_column='CauseDemo', max_length=2000, blank=True) # Field name made lowercase.
    reportman = models.CharField(db_column='ReportMan', max_length=50, blank=True) # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=50, blank=True) # Field name made lowercase.
    islast = models.NullBooleanField(db_column='IsLast', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_VentureRelative'

class TVenturerisk(models.Model):
    sourceindex = models.TextField(db_column='SourceIndex') # Field name made lowercase.
    venturecode = models.TextField(db_column='VentureCode') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_VentureRisk'

class TVenturesource(models.Model):
    sourceindex = models.TextField(db_column='SourceIndex') # Field name made lowercase.
    venturecell = models.CharField(db_column='VentureCell', max_length=100, blank=True) # Field name made lowercase.
    storageaddress = models.CharField(db_column='StorageAddress', max_length=200, blank=True) # Field name made lowercase.
    long = models.TextField(db_column='Long', blank=True) # Field name made lowercase.
    lat = models.TextField(db_column='Lat', blank=True) # Field name made lowercase.
    juryest = models.CharField(db_column='JuryEst', max_length=1000, blank=True) # Field name made lowercase.
    demo = models.CharField(db_column='Demo', max_length=500, blank=True) # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_VentureSource'

class TVideoset(models.Model):
    stationid = models.ForeignKey(TAllstation, db_column='StationID') # Field name made lowercase.
    ipordomain = models.TextField(db_column='IPOrDomain', blank=True) # Field name made lowercase.
    jpgaddress = models.TextField(db_column='JpgAddress', blank=True) # Field name made lowercase.
    videocodingid = models.CharField(db_column='VideoCodingID', max_length=20, blank=True) # Field name made lowercase.
    chunnelid = models.TextField(db_column='ChunnelID', blank=True) # Field name made lowercase.
    localport = models.IntegerField(db_column='LocalPort', blank=True, null=True) # Field name made lowercase.
    streamip = models.TextField(db_column='StreamIP', blank=True) # Field name made lowercase.
    streamserverport = models.IntegerField(db_column='StreamServerPort', blank=True, null=True) # Field name made lowercase.
    videofileurl = models.CharField(db_column='VideoFileUrl', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_VideoSet'

class TWateranalyzes(models.Model):
    analyzesid = models.IntegerField(db_column='AnalyzesID') # Field name made lowercase.
    stationid = models.ForeignKey(TAllstation, db_column='StationID', blank=True, null=True) # Field name made lowercase.
    paramcode = models.ForeignKey(TDataparam, db_column='ParamCode', blank=True, null=True) # Field name made lowercase.
    sampletime = models.DateTimeField(db_column='SampleTime', blank=True, null=True) # Field name made lowercase.
    taketime = models.DateTimeField(db_column='TakeTime', blank=True, null=True) # Field name made lowercase.
    takeman = models.TextField(db_column='TakeMan', blank=True) # Field name made lowercase.
    analyzestime = models.DateTimeField(db_column='AnalyzesTime', blank=True, null=True) # Field name made lowercase.
    analyzesman = models.TextField(db_column='AnalyzesMan', blank=True) # Field name made lowercase.
    actualvalue = models.DecimalField(db_column='ActualValue', max_digits=18, decimal_places=3, blank=True, null=True) # Field name made lowercase.
    verifiesman = models.TextField(db_column='VerifiesMan', blank=True) # Field name made lowercase.
    filltime = models.DateTimeField(db_column='FillTime', blank=True, null=True) # Field name made lowercase.
    sampleremark = models.CharField(db_column='SampleRemark', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterAnalyzes'

class TWatercase(models.Model):
    watercaseid = models.IntegerField(db_column='WaterCaseID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    outwherecode = models.CharField(db_column='OutWhereCode', max_length=10) # Field name made lowercase.
    carrier = models.TextField(db_column='Carrier', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterCase'

class TWaterdistributed(models.Model):
    distributedid = models.IntegerField(db_column='DistributedID') # Field name made lowercase.
    compid = models.BigIntegerField(db_column='CompID') # Field name made lowercase.
    functionid = models.IntegerField(db_column='FunctionID', blank=True, null=True) # Field name made lowercase.
    protectid = models.IntegerField(db_column='ProtectID', blank=True, null=True) # Field name made lowercase.
    targetname = models.TextField(db_column='TargetName', blank=True) # Field name made lowercase.
    counts = models.IntegerField(db_column='Counts', blank=True, null=True) # Field name made lowercase.
    longitude = models.TextField(db_column='Longitude', blank=True) # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True) # Field name made lowercase.
    distance = models.FloatField(db_column='Distance', blank=True, null=True) # Field name made lowercase.
    sevicerange = models.TextField(db_column='SeviceRange', blank=True) # Field name made lowercase.
    cpersonname = models.TextField(db_column='CpersonName', blank=True) # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterDistributed'

class TWaterfunction(models.Model):
    functionid = models.IntegerField(db_column='FunctionID') # Field name made lowercase.
    functionname = models.TextField(db_column='FunctionName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterFunction'

class TWaterkeytype(models.Model):
    typeid = models.IntegerField(db_column='TypeID') # Field name made lowercase.
    typename = models.TextField(db_column='TypeName', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterKeyType'

class TWaterparamset(models.Model):
    watersetid = models.IntegerField(db_column='WaterSetID') # Field name made lowercase.
    wscvalue = models.TextField(db_column='wscValue', blank=True) # Field name made lowercase.
    wscdemo = models.CharField(db_column='wscDemo', max_length=200, blank=True) # Field name made lowercase.
    wppvalue = models.TextField(db_column='wppValue', blank=True) # Field name made lowercase.
    wppdemo = models.CharField(db_column='wppDemo', max_length=200, blank=True) # Field name made lowercase.
    wrpvalue = models.TextField(db_column='wrpValue', blank=True) # Field name made lowercase.
    wrpdemo = models.CharField(db_column='wrpDemo', max_length=200, blank=True) # Field name made lowercase.
    wepvalue = models.TextField(db_column='wepValue', blank=True) # Field name made lowercase.
    wepdemo = models.CharField(db_column='wepDemo', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterParamSet'

class TWaterprotect(models.Model):
    protectid = models.IntegerField(db_column='ProtectID') # Field name made lowercase.
    protectname = models.TextField(db_column='ProtectName') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterProtect'

class TWatershedkeys(models.Model):
    watershedid = models.IntegerField(db_column='WaterShedID') # Field name made lowercase.
    keyprojectindex = models.ForeignKey(TKeyprojects, db_column='KeyProjectIndex') # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_WaterShedKeys'

class TWatershed(models.Model):
    watershedid = models.IntegerField(db_column='WaterShedID') # Field name made lowercase.
    higherwaterid = models.BigIntegerField(db_column='HigherWaterID', blank=True, null=True) # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    hourvalue = models.DecimalField(db_column='HourValue', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    dayvalue = models.DecimalField(db_column='DayValue', max_digits=9, decimal_places=0, blank=True, null=True) # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True) # Field name made lowercase.
    long = models.TextField(db_column='Long', blank=True) # Field name made lowercase.
    lat = models.TextField(db_column='Lat', blank=True) # Field name made lowercase.
    speed = models.DecimalField(db_column='Speed', max_digits=10, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    longlats = models.TextField(db_column='LongLats', blank=True) # Field name made lowercase. This field type is a guess.
    directionindex = models.TextField(db_column='DirectionIndex', blank=True) # Field name made lowercase.
    isload = models.NullBooleanField(db_column='IsLoad', blank=True, null=True) # Field name made lowercase.
    namelnglat = models.TextField(db_column='NameLngLat', blank=True) # Field name made lowercase. This field type is a guess.
    fonttype = models.IntegerField(db_column='FontType', blank=True, null=True) # Field name made lowercase.
    waterborder = models.TextField(db_column='WaterBorder', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'T_Watershed'

class TWorkedtechnical(models.Model):
    workedtechnicalid = models.IntegerField(db_column='workedTechnicalID') # Field name made lowercase.
    workedtechnical = models.TextField(db_column='workedTechnical', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_workedTechnical'

