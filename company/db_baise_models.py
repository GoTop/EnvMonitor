#coding=utf8
__author__ = 'GoTop'
from django.db import models
from para_models import *


class T_Data_param(models.Model):
    """
    监测参数字典
    """
    param_code = models.CharField(db_column='ParamCode', max_length=3, primary_key=True)
    standard_code = models.TextField(db_column='StandardCode', blank=True)
    param_remark = models.TextField(db_column='ParamRemark', blank=True)
    param_kind = models.IntegerField(db_column='ParamKind', blank=True, null=True)
    order_id = models.IntegerField(db_column='OrderID', blank=True, null=True)
    param_unit = models.TextField(db_column='ParamUnit', blank=True)
    data_precision = models.IntegerField(db_column='DataPrecision', blank=True, null=True)
    is_have_cou = models.NullBooleanField(db_column='IsHaveCou')
    standard_values = models.TextField(db_column='StandardValues', blank=True)
    app_value = models.DecimalField(db_column='AppValue', max_digits=18, decimal_places=5, blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'T_DataParam'


class T_Admin_area(models.Model):
    area_id = models.IntegerField(db_column='AreaID', primary_key=True)
    higherareaid = models.IntegerField(db_column='HigherAreaID', blank=True, null=True)
    area_name = models.TextField(db_column='AreaName')
    client_x = models.TextField(db_column='ClientX', blank=True)
    client_y = models.TextField(db_column='ClientY', blank=True)
    zoom_level = models.IntegerField(db_column='ZoomLevel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_AdminArea'


class T_Comp_info(models.Model):
    comp_id = models.IntegerField(db_column='CompID', primary_key=True)
    comp_name = models.CharField(db_column='CompName', max_length=100)
    tel = models.TextField(db_column='Tel', blank=True)
    fax = models.TextField(db_column='Fax', blank=True)
    post_code = models.TextField(db_column='Postcode', blank=True)
    law_person = models.CharField(db_column='LawPerson', max_length=20, blank=True)
    email = models.TextField(db_column='Email', blank=True)
    setup_time = models.DateTimeField(db_column='SetUpTime', blank=True, null=True)
    link_man = models.CharField(db_column='LinkMan', max_length=20, blank=True)
    address = models.CharField(db_column='Address', max_length=160, blank=True)
    longitude = models.TextField(blank=True)
    latitude = models.TextField(blank=True)
    hs_ename = models.CharField(db_column='HsEName', max_length=40, blank=True)
    reg_type = models.CharField(db_column='RegType', max_length=40, blank=True)
    sew_fac_cou = models.IntegerField(db_column='SewFacCou', blank=True, null=True)
    sfexploit_va = models.DecimalField(db_column='SFexploitVa', max_digits=9, decimal_places=0, blank=True,
                                       null=True)
    dispose_ability = models.DecimalField(db_column='DisposeAbility', max_digits=9, decimal_places=0, blank=True,
                                          null=True)
    tlfac_cou = models.IntegerField(db_column='TLFacCou', blank=True, null=True)
    idnkiln_cou = models.IntegerField(db_column='IdnkilnCou', blank=True, null=True)
    tlfac_cap = models.TextField(db_column='TLFacCap', blank=True)
    last_year_fine_money = models.DecimalField(db_column='LastYearFineMoney', max_digits=9, decimal_places=0,
                                               blank=True,
                                               null=True)
    last_year_pay_money = models.DecimalField(db_column='LastYearPayMoney', max_digits=9, decimal_places=0, blank=True,
                                              null=True)
    waste_emission_id = models.TextField(db_column='WasteEmissionID', blank=True)
    issuing_time = models.DateTimeField(db_column='IssuingTime', blank=True, null=True)
    add_time = models.DateTimeField(db_column='AddTime')
    user_id = models.IntegerField(db_column='UserID')
    area_id = models.IntegerField(db_column='AreaID', blank=True, null=True)
    short_name = models.CharField(db_column='ShortName', max_length=200, blank=True)
    tel_code_id = models.IntegerField(db_column='TelCodeID', blank=True, null=True)
    trade_id = models.TextField(db_column='TradeID', blank=True)
    country_attribute = models.TextField(db_column='CountryAttribute', blank=True)
    water_shed_id = models.IntegerField(db_column='WaterShedID', blank=True, null=True)
    pollute_level_index = models.IntegerField(db_column='PolluteLevelIndex', blank=True,
                                              null=True)
    is_facility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True)
    organ_code = models.TextField(db_column='OrganCode', blank=True)
    build_time = models.DateTimeField(db_column='BuildTime', blank=True, null=True)
    factory_area = models.DecimalField(db_column='FactoryArea', max_digits=10, decimal_places=2, blank=True,
                                       null=True)
    law_person_mum = models.TextField(db_column='LawPersonMum', blank=True)
    site_url = models.TextField(db_column='SiteUrl', blank=True)
    comp_properties = models.CharField(db_column='CompProperties', max_length=500,
                                       blank=True)
    linkman_phone = models.TextField(db_column='LinkManPhone', blank=True)
    contact_man = models.CharField(db_column='ContactMan', max_length=10, blank=True)
    contact_man_phone = models.TextField(db_column='ContactManPhone', blank=True)
    industry_park_name = models.CharField(db_column='IndustryParkName', max_length=200,
                                          blank=True)
    is_have_jury_project = models.NullBooleanField(db_column='IsHaveJuryProject', blank=True,
                                                   null=True)
    is_gb_judge = models.NullBooleanField(db_column='IsGBJudge', blank=True, null=True)
    is_occur_jury = models.NullBooleanField(db_column='IsOccurJury', blank=True,
                                            null=True)
    jury_demo = models.CharField(db_column='JuryDemo', max_length=1000, blank=True)
    kiln_type = models.TextField(db_column='kilnType', blank=True)
    kiln_have_decoke = models.NullBooleanField(db_column='KilnHaveDecoke', blank=True,
                                               null=True)
    kiln_is_run = models.NullBooleanField(db_column='KilnIsRun', blank=True, null=True)
    kiln_coal = models.DecimalField(db_column='KilnCoal', max_digits=18, decimal_places=6, blank=True,
                                    null=True)
    boiler_cou = models.IntegerField(db_column='BoilerCou', blank=True, null=True)
    boiler_ton = models.DecimalField(db_column='BoilerTon', max_digits=18, decimal_places=6, blank=True,
                                     null=True)
    boiler_type = models.TextField(db_column='BoilerType', blank=True)
    boiler_have_decoke = models.NullBooleanField(db_column='BoilerHaveDecoke', blank=True,
                                                 null=True)
    boiler_is_run = models.NullBooleanField(db_column='BoilerIsRun', blank=True,
                                            null=True)
    boiler_coal = models.DecimalField(db_column='BoilerCoal', max_digits=18, decimal_places=6, blank=True,
                                      null=True)
    img_save_path = models.CharField(db_column='ImgSavePath', max_length=500, blank=True)
    demo = models.TextField(db_column='Demo', blank=True)
    out_where_code = models.CharField(db_column='OutWhereCode', max_length=10, blank=True)
    function_id = models.IntegerField(db_column='FunctionID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CompInfo'


class T_All_station(models.Model):
    station_id = models.TextField(db_column='StationID', primary_key=True)

    #监测类型编码，32为水，35为气
    t_station_kind = models.ForeignKey('T_Station_kind', db_column='KindID', blank=True, null=True)
    #所属流域
    t_water_shed = models.ForeignKey('T_Water_shed', db_column='WaterShedID', blank=True, null=True)
    #关注程度编码
    t_attend_degree = models.ForeignKey('T_Attend_degree', db_column='AttendID', blank=True, null=True)
    #数采仪厂家
    t_transfers = models.ForeignKey('T_Transfers', db_column='TransfersID', blank=True, null=True)
    t_admin_area = models.ForeignKey(T_Admin_area, db_column='AreaID', blank=True, null=True)
    station_name = models.TextField(db_column='StationName', blank=True)
    t_trade = models.ForeignKey('T_Trade', db_column='TradeID', blank=True, null=True)
    order_id = models.IntegerField(db_column='OrderID', blank=True, null=True)
    #是否在线
    ionline = models.IntegerField(db_column='IOnline', blank=True, null=True)
    #企业标识
    comp_id = models.IntegerField(db_column='CompID', blank=True, null=True)
    short_name = models.CharField(db_column='ShortName', max_length=60, blank=True)
    mn_pwd = models.TextField(db_column='MNPwd', blank=True)
    standard_demo = models.TextField(db_column='StandardDemo', blank=True)
    higher_out_id = models.TextField(db_column='HigherOutID', blank=True)
    is_facility = models.NullBooleanField(db_column='IsFacility', blank=True, null=True)
    is_emergency = models.NullBooleanField(db_column='IsEmergency', blank=True, null=True)
    is_show = models.NullBooleanField(db_column='IsShow', blank=True, null=True)
    longitude = models.TextField(db_column='Longitude', blank=True)
    latitude = models.TextField(db_column='Latitude', blank=True)
    is_import_export = models.IntegerField(db_column='IsImportexport', blank=True,
                                           null=True)
    param_codes = models.TextField(db_column='ParamCodes', blank=True)
    pollute_level_index = models.IntegerField(db_column='PolluteLevelIndex', blank=True,
                                              null=True)
    long_warp = models.DecimalField(db_column='LongWarp', max_digits=12, decimal_places=9, blank=True,
                                    null=True)
    lat_warp = models.DecimalField(db_column='LatWarp', max_digits=12, decimal_places=9, blank=True,
                                   null=True)
    is_country_control = models.NullBooleanField(db_column='IsCountryControl', blank=True,
                                                 null=True)
    is_1015building = models.NullBooleanField(db_column='Is1015Building', blank=True,
                                              null=True)
    is_pass_accept = models.NullBooleanField(db_column='IsPassAccept', blank=True,
                                             null=True)
    pass_accept_time = models.DateTimeField(db_column='PassAcceptTime', blank=True,
                                            null=True)
    state_year = models.TextField(db_column='StateYear', blank=True)

    class Meta:
        managed = False
        db_table = 'T_AllStation'


class T_Exam_project(models.Model):
    '''
    监测项目
    '''
    exam_parm_id = models.IntegerField(db_column='ExamParmID', primary_key=True)
    t_all_station = models.ForeignKey(T_All_station, db_column='StationID')
    t_data_param = models.ForeignKey(T_Data_param, db_column='ParamCode', blank=True,
                                     null=True)
    t_manufacturer = models.ForeignKey('T_Manufacturer', db_column='ManufacturerID', blank=True,
                                       null=True)
    #仪器最小检出限
    low_limit_value = models.DecimalField(db_column='LowLimitValue', max_digits=18, decimal_places=4, blank=True,
                                          null=True)
    #仪器最高检出限
    high_limit_value = models.DecimalField(db_column='HighLimitValue', max_digits=18, decimal_places=4,
                                           blank=True, null=True)
    data_precision = models.IntegerField(db_column='DataPrecision', blank=True,
                                         null=True)
    param_unit = models.TextField(db_column='ParamUnit', blank=True)
    k_unit = models.DecimalField(db_column='kUnit', max_digits=8, decimal_places=2, blank=True,
                                 null=True)
    is_send = models.NullBooleanField(db_column='IsSend', blank=True, null=True)
    total_unit = models.TextField(db_column='TotalUnit', blank=True)
    sort_id = models.IntegerField(db_column='SortID', blank=True, null=True)
    is_used = models.NullBooleanField(db_column='IsUsed', blank=True, null=True)
    asc_id = models.NullBooleanField(db_column='AscID', blank=True, null=True)
    analyse_id = models.SmallIntegerField(db_column='AnalyseID', blank=True,
                                          null=True)
    model = models.TextField(db_column='Model', blank=True)
    number = models.TextField(db_column='Number', blank=True)
    minimum_level = models.DecimalField(db_column='MinimumLevel', max_digits=18, decimal_places=4, blank=True,
                                        null=True)
    error_max_value = models.DecimalField(db_column='ErrorMaxValue', max_digits=10, decimal_places=4, blank=True,
                                          null=True)
    error_min_value = models.DecimalField(db_column='ErrorMinValue', max_digits=10, decimal_places=4, blank=True,
                                          null=True)
    is_enable = models.NullBooleanField(db_column='IsEnable', blank=True,
                                        null=True)
    d_min_limit = models.DecimalField(db_column='dMinLimit', max_digits=18, decimal_places=6, blank=True,
                                      null=True)
    d_max_limit = models.DecimalField(db_column='dMaxLimit', max_digits=18, decimal_places=6, blank=True,
                                      null=True)
    is_main = models.NullBooleanField(db_column='IsMain', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_ExamProject'


class T_Superscale(models.Model):
    """
    执行标准范围设定
    """
    exam_id = models.IntegerField(db_column='ExamID', primary_key=True)
    t_exam_project = models.ForeignKey(T_Exam_project, db_column='ExamParmID')
    level_id = models.IntegerField(db_column='LevelID', blank=True, null=True)
    standard_value = models.FloatField(db_column='StandardValue', blank=True,
                                       null=True)
    standard_demo = models.CharField(db_column='StandardDemo', max_length=100,
                                     blank=True)
    is_apply = models.NullBooleanField(db_column='IsApply', blank=True, null=True)
    max_value = models.FloatField(db_column='MaxValue', blank=True, null=True)
    s = models.TextField(db_column='DataType', blank=True)

    class Meta:
        managed = False
        db_table = 'T_Superscale'

class T_Datatype(models.Model):
    data_type = models.TextField(db_column='DataType') # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'T_DataType'


