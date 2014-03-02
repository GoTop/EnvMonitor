__author__ = 'GoTop'
from django.db import models
from para_models import *


class T_Adminarea(models.Model):
    area_id = models.IntegerField(db_column='AreaID', primary_key=True)  # Field name made lowercase.
    higherareaid = models.IntegerField(db_column='HigherAreaID', blank=True, null=True)  # Field name made lowercase.
    area_name = models.TextField(db_column='AreaName')  # Field name made lowercase.
    client_x = models.TextField(db_column='ClientX', blank=True)  # Field name made lowercase.
    client_y = models.TextField(db_column='ClientY', blank=True)  # Field name made lowercase.
    zoom_level = models.IntegerField(db_column='ZoomLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_AdminArea'


class T_Compinfo(models.Model):
    comp_id = models.IntegerField(db_column='CompID', primary_key=True)  # Field name made lowercase.
    comp_name = models.CharField(db_column='CompName', max_length=100)  # Field name made lowercase.
    tel = models.TextField(db_column='Tel', blank=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True)  # Field name made lowercase.
    post_code = models.TextField(db_column='Postcode', blank=True)  # Field name made lowercase.
    law_person = models.CharField(db_column='LawPerson', max_length=20, blank=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True)  # Field name made lowercase.
    setup_time = models.DateTimeField(db_column='SetUpTime', blank=True, null=True)  # Field name made lowercase.
    link_man = models.CharField(db_column='LinkMan', max_length=20, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=160, blank=True)  # Field name made lowercase.
    longitude = models.TextField(blank=True)
    latitude = models.TextField(blank=True)
    hs_ename = models.CharField(db_column='HsEName', max_length=40, blank=True)  # Field name made lowercase.
    reg_type = models.CharField(db_column='RegType', max_length=40, blank=True)  # Field name made lowercase.
    sew_fac_cou = models.IntegerField(db_column='SewFacCou', blank=True, null=True)  # Field name made lowercase.
    sfexploit_va = models.DecimalField(db_column='SFexploitVa', max_digits=9, decimal_places=0, blank=True,
                                      null=True)  # Field name made lowercase.
    dispose_ability = models.DecimalField(db_column='DisposeAbility', max_digits=9, decimal_places=0, blank=True,
                                         null=True)  # Field name made lowercase.
    tlfac_cou = models.IntegerField(db_column='TLFacCou', blank=True, null=True)  # Field name made lowercase.
    idnkiln_cou = models.IntegerField(db_column='IdnkilnCou', blank=True, null=True)  # Field name made lowercase.
    tlfac_cap = models.TextField(db_column='TLFacCap', blank=True)  # Field name made lowercase.
    last_year_fine_money = models.DecimalField(db_column='LastYearFineMoney', max_digits=9, decimal_places=0, blank=True,
                                            null=True)  # Field name made lowercase.
    last_year_pay_money = models.DecimalField(db_column='LastYearPayMoney', max_digits=9, decimal_places=0, blank=True,
                                           null=True)  # Field name made lowercase.
    waste_emission_id = models.TextField(db_column='WasteEmissionID', blank=True)  # Field name made lowercase.
    issuing_time = models.DateTimeField(db_column='IssuingTime', blank=True, null=True)  # Field name made lowercase.
    add_time = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    area_id = models.IntegerField(db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='ShortName', max_length=200, blank=True)  # Field name made lowercase.
    tel_code_id = models.IntegerField(db_column='TelCodeID', blank=True, null=True)  # Field name made lowercase.
    trade_id = models.TextField(db_column='TradeID', blank=True)  # Field name made lowercase.
    country_attribute = models.TextField(db_column='CountryAttribute', blank=True)  # Field name made lowercase.
    water_shed_id = models.IntegerField(db_column='WaterShedID', blank=True, null=True)  # Field name made lowercase.
    pollute_level_index = models.IntegerField(db_column='PolluteLevelIndex', blank=True,
                                            null=True)  # Field name made lowercase.
    is_facility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True)  # Field name made lowercase.
    organ_code = models.TextField(db_column='OrganCode', blank=True)  # Field name made lowercase.
    build_time = models.DateTimeField(db_column='BuildTime', blank=True, null=True)  # Field name made lowercase.
    factory_area = models.DecimalField(db_column='FactoryArea', max_digits=10, decimal_places=2, blank=True,
                                      null=True)  # Field name made lowercase.
    law_person_mum = models.TextField(db_column='LawPersonMum', blank=True)  # Field name made lowercase.
    site_url = models.TextField(db_column='SiteUrl', blank=True)  # Field name made lowercase.
    comp_properties = models.CharField(db_column='CompProperties', max_length=500,
                                      blank=True)  # Field name made lowercase.
    linkman_phone = models.TextField(db_column='LinkManPhone', blank=True)  # Field name made lowercase.
    contact_man = models.CharField(db_column='ContactMan', max_length=10, blank=True)  # Field name made lowercase.
    contact_man_phone = models.TextField(db_column='ContactManPhone', blank=True)  # Field name made lowercase.
    industry_park_name = models.CharField(db_column='IndustryParkName', max_length=200,
                                        blank=True)  # Field name made lowercase.
    is_have_jury_project = models.NullBooleanField(db_column='IsHaveJuryProject', blank=True,
                                                null=True)  # Field name made lowercase.
    is_gb_judge = models.NullBooleanField(db_column='IsGBJudge', blank=True, null=True)  # Field name made lowercase.
    is_occur_jury = models.NullBooleanField(db_column='IsOccurJury', blank=True, null=True)  # Field name made lowercase.
    jury_demo = models.CharField(db_column='JuryDemo', max_length=1000, blank=True)  # Field name made lowercase.
    kiln_type = models.TextField(db_column='kilnType', blank=True)  # Field name made lowercase.
    kiln_have_decoke = models.NullBooleanField(db_column='KilnHaveDecoke', blank=True,
                                             null=True)  # Field name made lowercase.
    kiln_is_run = models.NullBooleanField(db_column='KilnIsRun', blank=True, null=True)  # Field name made lowercase.
    kiln_coal = models.DecimalField(db_column='KilnCoal', max_digits=18, decimal_places=6, blank=True,
                                   null=True)  # Field name made lowercase.
    boiler_cou = models.IntegerField(db_column='BoilerCou', blank=True, null=True)  # Field name made lowercase.
    boiler_ton = models.DecimalField(db_column='BoilerTon', max_digits=18, decimal_places=6, blank=True,
                                    null=True)  # Field name made lowercase.
    boiler_type = models.TextField(db_column='BoilerType', blank=True)  # Field name made lowercase.
    boiler_have_decoke = models.NullBooleanField(db_column='BoilerHaveDecoke', blank=True,
                                               null=True)  # Field name made lowercase.
    boiler_is_run = models.NullBooleanField(db_column='BoilerIsRun', blank=True, null=True)  # Field name made lowercase.
    boiler_coal = models.DecimalField(db_column='BoilerCoal', max_digits=18, decimal_places=6, blank=True,
                                     null=True)  # Field name made lowercase.
    img_save_path = models.CharField(db_column='ImgSavePath', max_length=500, blank=True)  # Field name made lowercase.
    demo = models.TextField(db_column='Demo', blank=True)  # Field name made lowercase. This field type is a guess.
    out_where_code = models.CharField(db_column='OutWhereCode', max_length=10, blank=True)  # Field name made lowercase.
    function_id = models.IntegerField(db_column='FunctionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CompInfo'


class T_AllStation(models.Model):
    station_id = models.TextField(db_column='StationID', primary_key=True)  # Field name made lowercase.
    kind = models.ForeignKey('T_Station_kind', db_column='KindID', blank=True, null=True)  # Field name made lowercase.
    watershed_id = models.ForeignKey('T_Watershed', db_column='WaterShedID', blank=True,
                                     null=True)  # Field name made lowercase.
    attend_id = models.ForeignKey('T_Attend_degree', db_column='AttendID', blank=True,
                                  null=True)  # Field name made lowercase.
    transfers_id = models.ForeignKey('T_Transfers', db_column='TransfersID', blank=True,
                                     null=True)  # Field name made lowercase.
    area_id = models.ForeignKey(T_Adminarea, db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    station_name = models.TextField(db_column='StationName', blank=True)  # Field name made lowercase.
    trade_id = models.ForeignKey('T_Trade', db_column='TradeID', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    ionline = models.IntegerField(db_column='IOnline', blank=True, null=True)  # Field name made lowercase.
    comp_id = models.IntegerField(db_column='CompID', blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='ShortName', max_length=60, blank=True)  # Field name made lowercase.
    mn_pwd = models.TextField(db_column='MNPwd', blank=True)  # Field name made lowercase.
    standard_demo = models.TextField(db_column='StandardDemo', blank=True)  # Field name made lowercase.
    higher_out_id = models.TextField(db_column='HigherOutID', blank=True)  # Field name made lowercase.
    is_facility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True)  # Field name made lowercase.
    is_emergency = models.NullBooleanField(db_column='IsEmergency', blank=True, null=True)  # Field name made lowercase.
    is_show = models.NullBooleanField(db_column='IsShow', blank=True, null=True)  # Field name made lowercase.
    longitude = models.TextField(db_column='Longitude', blank=True)  # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude', blank=True)  # Field name made lowercase.
    is_import_export = models.IntegerField(db_column='IsImportexport', blank=True,
                                           null=True)  # Field name made lowercase.
    param_codes = models.TextField(db_column='ParamCodes', blank=True)  # Field name made lowercase.
    pollute_level_index = models.IntegerField(db_column='PolluteLevelIndex', blank=True,
                                              null=True)  # Field name made lowercase.
    long_warp = models.DecimalField(db_column='LongWarp', max_digits=12, decimal_places=9, blank=True,
                                   null=True)  # Field name made lowercase.
    lat_warp = models.DecimalField(db_column='LatWarp', max_digits=12, decimal_places=9, blank=True,
                                  null=True)  # Field name made lowercase.
    is_country_control = models.NullBooleanField(db_column='IsCountryControl', blank=True,
                                                 null=True)  # Field name made lowercase.
    is_1015building = models.NullBooleanField(db_column='Is1015Building', blank=True,
                                              null=True)  # Field name made lowercase.
    is_pass_accept = models.NullBooleanField(db_column='IsPassAccept', blank=True,
                                             null=True)  # Field name made lowercase.
    pass_accept_time = models.DateTimeField(db_column='PassAcceptTime', blank=True,
                                            null=True)  # Field name made lowercase.
    state_year = models.TextField(db_column='StateYear', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_AllStation'
