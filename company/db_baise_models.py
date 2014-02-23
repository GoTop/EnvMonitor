__author__ = 'GoTop'
from django.db import models
from para_models import *


class TAdminarea(models.Model):
    areaid = models.IntegerField(db_column='AreaID')  # Field name made lowercase.
    higherareaid = models.IntegerField(db_column='HigherAreaID', blank=True, null=True)  # Field name made lowercase.
    areaname = models.TextField(db_column='AreaName')  # Field name made lowercase.
    clientx = models.TextField(db_column='ClientX', blank=True)  # Field name made lowercase.
    clienty = models.TextField(db_column='ClientY', blank=True)  # Field name made lowercase.
    zoomlevel = models.IntegerField(db_column='ZoomLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_AdminArea'


class T_Compinfo(models.Model):
    compid = models.IntegerField(db_column='CompID')  # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=100)  # Field name made lowercase.
    tel = models.TextField(db_column='Tel', blank=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True)  # Field name made lowercase.
    postcode = models.TextField(db_column='Postcode', blank=True)  # Field name made lowercase.
    lawperson = models.CharField(db_column='LawPerson', max_length=20, blank=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True)  # Field name made lowercase.
    setuptime = models.DateTimeField(db_column='SetUpTime', blank=True, null=True)  # Field name made lowercase.
    linkman = models.CharField(db_column='LinkMan', max_length=20, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=160, blank=True)  # Field name made lowercase.
    longitude = models.TextField(blank=True)
    latitude = models.TextField(blank=True)
    hsename = models.CharField(db_column='HsEName', max_length=40, blank=True)  # Field name made lowercase.
    regtype = models.CharField(db_column='RegType', max_length=40, blank=True)  # Field name made lowercase.
    sewfaccou = models.IntegerField(db_column='SewFacCou', blank=True, null=True)  # Field name made lowercase.
    sfexploitva = models.DecimalField(db_column='SFexploitVa', max_digits=9, decimal_places=0, blank=True,
                                      null=True)  # Field name made lowercase.
    disposeability = models.DecimalField(db_column='DisposeAbility', max_digits=9, decimal_places=0, blank=True,
                                         null=True)  # Field name made lowercase.
    tlfaccou = models.IntegerField(db_column='TLFacCou', blank=True, null=True)  # Field name made lowercase.
    idnkilncou = models.IntegerField(db_column='IdnkilnCou', blank=True, null=True)  # Field name made lowercase.
    tlfaccap = models.TextField(db_column='TLFacCap', blank=True)  # Field name made lowercase.
    lastyearfinemoney = models.DecimalField(db_column='LastYearFineMoney', max_digits=9, decimal_places=0, blank=True,
                                            null=True)  # Field name made lowercase.
    lastyearpaymoney = models.DecimalField(db_column='LastYearPayMoney', max_digits=9, decimal_places=0, blank=True,
                                           null=True)  # Field name made lowercase.
    wasteemissionid = models.TextField(db_column='WasteEmissionID', blank=True)  # Field name made lowercase.
    issuingtime = models.DateTimeField(db_column='IssuingTime', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200, blank=True)  # Field name made lowercase.
    telcodeid = models.IntegerField(db_column='TelCodeID', blank=True, null=True)  # Field name made lowercase.
    tradeid = models.TextField(db_column='TradeID', blank=True)  # Field name made lowercase.
    countryattribute = models.TextField(db_column='CountryAttribute', blank=True)  # Field name made lowercase.
    watershedid = models.IntegerField(db_column='WaterShedID', blank=True, null=True)  # Field name made lowercase.
    pollutelevelindex = models.IntegerField(db_column='PolluteLevelIndex', blank=True,
                                            null=True)  # Field name made lowercase.
    isfacility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True)  # Field name made lowercase.
    organcode = models.TextField(db_column='OrganCode', blank=True)  # Field name made lowercase.
    buildtime = models.DateTimeField(db_column='BuildTime', blank=True, null=True)  # Field name made lowercase.
    factoryarea = models.DecimalField(db_column='FactoryArea', max_digits=10, decimal_places=2, blank=True,
                                      null=True)  # Field name made lowercase.
    lawpersonmum = models.TextField(db_column='LawPersonMum', blank=True)  # Field name made lowercase.
    siteurl = models.TextField(db_column='SiteUrl', blank=True)  # Field name made lowercase.
    compproperties = models.CharField(db_column='CompProperties', max_length=500,
                                      blank=True)  # Field name made lowercase.
    linkmanphone = models.TextField(db_column='LinkManPhone', blank=True)  # Field name made lowercase.
    contactman = models.CharField(db_column='ContactMan', max_length=10, blank=True)  # Field name made lowercase.
    contactmanphone = models.TextField(db_column='ContactManPhone', blank=True)  # Field name made lowercase.
    industryparkname = models.CharField(db_column='IndustryParkName', max_length=200,
                                        blank=True)  # Field name made lowercase.
    ishavejuryproject = models.NullBooleanField(db_column='IsHaveJuryProject', blank=True,
                                                null=True)  # Field name made lowercase.
    isgbjudge = models.NullBooleanField(db_column='IsGBJudge', blank=True, null=True)  # Field name made lowercase.
    isoccurjury = models.NullBooleanField(db_column='IsOccurJury', blank=True, null=True)  # Field name made lowercase.
    jurydemo = models.CharField(db_column='JuryDemo', max_length=1000, blank=True)  # Field name made lowercase.
    kilntype = models.TextField(db_column='kilnType', blank=True)  # Field name made lowercase.
    kilnhavedecoke = models.NullBooleanField(db_column='KilnHaveDecoke', blank=True,
                                             null=True)  # Field name made lowercase.
    kilnisrun = models.NullBooleanField(db_column='KilnIsRun', blank=True, null=True)  # Field name made lowercase.
    kilncoal = models.DecimalField(db_column='KilnCoal', max_digits=18, decimal_places=6, blank=True,
                                   null=True)  # Field name made lowercase.
    boilercou = models.IntegerField(db_column='BoilerCou', blank=True, null=True)  # Field name made lowercase.
    boilerton = models.DecimalField(db_column='BoilerTon', max_digits=18, decimal_places=6, blank=True,
                                    null=True)  # Field name made lowercase.
    boilertype = models.TextField(db_column='BoilerType', blank=True)  # Field name made lowercase.
    boilerhavedecoke = models.NullBooleanField(db_column='BoilerHaveDecoke', blank=True,
                                               null=True)  # Field name made lowercase.
    boilerisrun = models.NullBooleanField(db_column='BoilerIsRun', blank=True, null=True)  # Field name made lowercase.
    boilercoal = models.DecimalField(db_column='BoilerCoal', max_digits=18, decimal_places=6, blank=True,
                                     null=True)  # Field name made lowercase.
    imgsavepath = models.CharField(db_column='ImgSavePath', max_length=500, blank=True)  # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True)  # Field name made lowercase. This field type is a guess.
    outwherecode = models.CharField(db_column='OutWhereCode', max_length=10, blank=True)  # Field name made lowercase.
    functionid = models.IntegerField(db_column='FunctionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CompInfo'


class T_AllStation(models.Model):
    station_id = models.TextField(db_column='StationID')  # Field name made lowercase.
    kindid = models.ForeignKey('TStationkind', db_column='KindID', blank=True, null=True)  # Field name made lowercase.
    watershedid = models.ForeignKey('TWatershed', db_column='WaterShedID', blank=True,
                                    null=True)  # Field name made lowercase.
    attendid = models.ForeignKey('TAttenddegree', db_column='AttendID', blank=True,
                                 null=True)  # Field name made lowercase.
    transfersid = models.ForeignKey('TTransfers', db_column='TransfersID', blank=True,
                                    null=True)  # Field name made lowercase.
    area_id = models.ForeignKey(TAdminarea, db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    station_name = models.TextField(db_column='StationName', blank=True)  # Field name made lowercase.
    tradeid = models.ForeignKey('TTrade', db_column='TradeID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    ionline = models.IntegerField(db_column='IOnline', blank=True, null=True)  # Field name made lowercase.
    comp_id = models.IntegerField(db_column='CompID', blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=60, blank=True)  # Field name made lowercase.
    mnpwd = models.TextField(db_column='MNPwd', blank=True)  # Field name made lowercase.
    standarddemo = models.TextField(db_column='StandardDemo', blank=True)  # Field name made lowercase.
    higheroutid = models.TextField(db_column='HigherOutID', blank=True)  # Field name made lowercase.
    isfacility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True)  # Field name made lowercase.
    isemergency = models.NullBooleanField(db_column='IsEmergency', blank=True, null=True)  # Field name made lowercase.
    isshow = models.NullBooleanField(db_column='IsShow', blank=True, null=True)  # Field name made lowercase.
    longitude = models.TextField(db_column='Longitude', blank=True)  # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True)  # Field name made lowercase.
    isimportexport = models.IntegerField(db_column='IsImportexport', blank=True,
                                         null=True)  # Field name made lowercase.
    paramcodes = models.TextField(db_column='ParamCodes', blank=True)  # Field name made lowercase.
    pollutelevelindex = models.IntegerField(db_column='PolluteLevelIndex', blank=True,
                                            null=True)  # Field name made lowercase.
    longwarp = models.DecimalField(db_column='LongWarp', max_digits=12, decimal_places=9, blank=True,
                                   null=True)  # Field name made lowercase.
    latwarp = models.DecimalField(db_column='LatWarp', max_digits=12, decimal_places=9, blank=True,
                                  null=True)  # Field name made lowercase.
    iscountrycontrol = models.NullBooleanField(db_column='IsCountryControl', blank=True,
                                               null=True)  # Field name made lowercase.
    is1015building = models.NullBooleanField(db_column='Is1015Building', blank=True,
                                             null=True)  # Field name made lowercase.
    ispassaccept = models.NullBooleanField(db_column='IsPassAccept', blank=True,
                                           null=True)  # Field name made lowercase.
    passaccepttime = models.DateTimeField(db_column='PassAcceptTime', blank=True,
                                          null=True)  # Field name made lowercase.
    stateyear = models.TextField(db_column='StateYear', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_AllStation'

