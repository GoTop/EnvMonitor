from __future__ import unicode_literals
# coding=utf-8
import datetime
from company.db_baise_models import T_All_station
from company.function.standard import get_param_code, get_station_standard

__author__ = 'GoTop'

from django.db import connections
import time, datetime


def dict_fetch_all(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def get_monitor_value(mn, date, param_name, data_type, type):
    '''
    获取废水监测点位mn的date当天指定类型data_type（平均值Avg，或累计值Cou）
    和指定监测因子param_name的小时或日数据（由day_or_hour(day或hour)设置）
    '''
    param_code = get_param_code(param_name)

    # 根据day_or_hour选择数据库中的日数据表或者小时数据表
    if type == 'day':
        table_name = 'Day_' + mn
        #strptime() 函数根据指定的格式把一个时间字符串解析为时间元组
        datetime_tuple = time.strptime(date, "%Y%m%d")
        # time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定
        date = time.strftime("%Y/%m/%d %H:%M:%S", datetime_tuple)
    elif type == 'hour':
        table_name = 'Hour_' + mn
        #strptime() 函数根据指定的格式把一个时间字符串解析为时间元组
        datetime_tuple = time.strptime(date, "%Y/%m/%d %H:%M:%S")
        # time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定
        date = time.strftime("%Y/%m/%d %H:%M:%S", datetime_tuple)
    param = (table_name, mn, param_code, data_type, date)
    cursor = connections['DB_baise'].cursor()

    #因为在DB_baise数据库里，每个监测点位的日数据表名称都不一样（类似Day_45007760002801）
    #所以只能用构造SQL语句的方式进行查询
    query = '''SELECT * FROM %s
                WHERE StationID = '%s'
                AND ParamCode = '%s'
                AND DataType = '%s'
                AND DataTime = '%s' ''' % param

    cursor.execute(query)
    dict = dict_fetch_all(cursor)
    #row = cursor.fetchall()
    return round(dict[0]['dValue'], 2)


def get_water_day_data_func(mn, date, type):
    '''
    获取废水监测点位mn的date当天的小时或日数据（COD和NH的平均值，累计排放量，pH值和流量）
    小时或日数据（由day_or_hour(day或hour)设置）
    '''
    CODcr_Avg_value = get_monitor_value(mn, date, param_name='CODcr', data_type='Avg', type=type)
    CODcr_Cou_value = get_monitor_value(mn, date, param_name='CODcr', data_type='Cou', type=type)

    NH_Avg_value = get_monitor_value(mn, date, param_name='NH', data_type='Avg', type=type)
    NH_Cou_value = get_monitor_value(mn, date, param_name='NH', data_type='Cou', type=type)

    pH_Avg_day_value = get_monitor_value(mn, date, param_name='pH', data_type='Avg', type=type)
    volume_of_water_Cou_value = get_monitor_value(mn, date, param_name='volume_of_water',
                                                  data_type='Cou', type=type)
    daily_report_value = {'CODcr_Avg': CODcr_Avg_value,
                          'CODcr_Cou': CODcr_Cou_value,
                          'NH_Avg': NH_Avg_value,
                          'NH_Cou': NH_Cou_value,
                          'pH_Avg': pH_Avg_day_value,
                          'volume_of_water_Cou': volume_of_water_Cou_value,
    }

    # 获取排污标准
    CODcr_standard_dict = get_station_standard(mn=mn, param_name='CODcr')
    NH_standard_dict = get_station_standard(mn=mn, param_name='NH')

    standard_dict = {}
    if CODcr_standard_dict:
        daily_report_value['CODcr_standard'] = CODcr_standard_dict['standard_max']

        #如果CODcr的值超标，这设置一个字段为True
        if daily_report_value['CODcr_Avg'] > CODcr_standard_dict['standard_max'] \
                or daily_report_value['CODcr_Avg'] < CODcr_standard_dict['standard_min']:
            daily_report_value['CODcr_abnormal'] = True
    else:
        daily_report_value['CODcr_standard'] = '-'

    if NH_standard_dict:
        daily_report_value['NH_standard'] = NH_standard_dict['standard_max']

        #如果NH的值超标，这设置一个字段为True
        if daily_report_value['NH_Avg'] > NH_standard_dict['standard_max'] \
                or daily_report_value['NH_Avg'] < NH_standard_dict['standard_min']:
            daily_report_value['NH_abnormal'] = True
    else:
        daily_report_value['NH_standard'] = '-'

    return daily_report_value


def get_gas_day_data_func(mn, date, type):
    '''
    获取气监测点位mn的date当天的小时或日数据（SO2和NOx的平均值，累计排放量，流量）
    小时或日数据（由day_or_hour(day或hour)设置）
    '''

    # 能代替重复代码的一段代码，暂时先不用
    # report_value = {}
    # param_name_list = {'CODcr', 'NH'}
    # for param_name in param_name_list:
    # data_type_list = {'Avg', 'Cou'}
    #     for data_type in data_type_list:
    #         value = get_monitor_value(mn, date, param_name=param_name, data_type=data_type, type=type)
    #         key = param_name + '_' + data_type
    #         report_value[key] =  value


    SO2_Avg_value = get_monitor_value(mn, date, param_name='SO2', data_type='Avg', type=type)
    SO2_Cou_value = get_monitor_value(mn, date, param_name='SO2', data_type='Cou', type=type)

    NOx_Avg_value = get_monitor_value(mn, date, param_name='NOx', data_type='Avg', type=type)
    NOx_Cou_value = get_monitor_value(mn, date, param_name='NOx', data_type='Cou', type=type)

    volume_of_gas_Cou_value = get_monitor_value(mn, date, param_name='volume_of_gas',
                                                data_type='Cou', type=type)
    daily_report_value = {'SO2_Avg': SO2_Avg_value,
                          'SO2_Cou': SO2_Cou_value,
                          'NOx_Avg': NOx_Avg_value,
                          'NOx_Cou': NOx_Cou_value,
                          'volume_of_gas_Cou': volume_of_gas_Cou_value,
    }

    #获取排污标准
    SO2_standard_dict = get_station_standard(mn=mn, param_name='SO2')
    NOx_standard_dict = get_station_standard(mn=mn, param_name='NOx')

    standard_dict = {}
    if SO2_standard_dict:
        daily_report_value['SO2_standard'] = SO2_standard_dict['standard_max']

        #如果CODcr的值超标，这设置一个字段为True
        if daily_report_value['SO2_Avg'] > SO2_standard_dict['standard_max'] \
                or daily_report_value['SO2_Avg'] < SO2_standard_dict['standard_min']:
            daily_report_value['SO2_abnormal'] = True
    else:
        daily_report_value['SO2_standard'] = '-'

    if NOx_standard_dict:
        daily_report_value['NOx_standard'] = NOx_standard_dict['standard_max']

        #如果NH的值超标，这设置一个字段为True
        if daily_report_value['NOx_Avg'] > NOx_standard_dict['standard_max'] \
                or daily_report_value['NOx_Avg'] < NOx_standard_dict['standard_min']:
            daily_report_value['NOx_abnormal'] = True
    else:
        daily_report_value['NOx_standard'] = '-'
    return daily_report_value


def get_daily_report_func(mn, date, type):
    '''
    获取企业mn每日的日数据，以便按报表显示

    '''
    t_station = T_All_station.objects.using('DB_baise').get(pk=mn)

    # 判断该检测点位是水还是气
    #t_station_kind为监测类型编码，32为水，35为气
    if t_station.t_station_kind.kind_id == 32:
        daily_report_value = get_water_day_data_func(mn, date, type='day')

        # #获取排污标准的通用方法，暂时不用
        # param_name_list = {'CODcr', 'NH'}
        # for param_name in param_name_list:
        #     param_standard_dict = get_station_standard(mn=mn, param_name=param_name)
        #     if param_standard_dict:
        #         #当param_name为CODcr时，param_name_string就是CODcr_standard
        #         param_name_standard = param_name + '_standard'
        #         daily_report_value[param_name_standard] = param_standard_dict['standard_max']
        #
        #         #如果CODcr的值超标，这设置一个字段为True
        #         param_name_Avg = param_name + '_Avg'
        #         if daily_report_value[param_name_Avg] > param_standard_dict['standard_max'] \
        #                 or daily_report_value[param_name_Avg] < param_standard_dict['standard_min']:
        #             param_name_abnormal = param_name + '_abnormal'
        #             daily_report_value[param_name_abnormal] = True

    elif t_station.t_station_kind.kind_id == 35:
        daily_report_value = get_gas_day_data_func(mn, date, type='day')

    daily_report_value['station_name'] = t_station.station_name
    return daily_report_value

    #daily_report_list.append(daily_report_value)


def get_water_hour_data_report_func(mn, date):
    """
    获取废水监控点位mn的一天内的小时数据
    """
    struct_time = time.strptime(date, "%Y%m%d")

    # strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")

    datetime_string = time.strftime("%Y/%m/%d %H:%M:%S", datetime_object.timetuple())

    report_list = []
    for x in range(24):
        report_row = {}
        report_row = get_water_day_data_func(mn, datetime_string, type='hour')
        report_row['monitor_date'] = datetime_string
        report_list.append(report_row)

        datetime_object = datetime_object + datetime.timedelta(hours=1)
        datetime_string = time.strftime("%Y/%m/%d %H:%M:%S", datetime_object.timetuple())

    return report_list


def get_range_monitor_value(mn, start_date_object, end_date_object, param_name, data_type, type):
    '''
    一个简便功能函数，可以方便地获取监测点位mn的date的多个因子和数据类型的小时或日数据

    param_name_list：监控因子列表
    data_type_list：数据类型列表：Avg或Cou
    type(day或hour):小时或日数据

    return：返回的数组中，key为类似COD_Avg这样的格式
    '''

    # 根据type选择数据库中的日数据表或者小时数据表
    #格式化start_date和end_date
    if type == 'day':
        table_name = 'Day_' + mn
    elif type == 'hour':
        table_name = 'Hour_' + mn

    start_date_string = datetime.datetime.strftime(start_date_object, '%Y/%m/%d %H:%M:%S')
    end_date_string = datetime.datetime.strftime(end_date_object, '%Y/%m/%d %H:%M:%S')

    report_value = {}
    report_hour_value = {}

    #todo
    param_code = get_param_code(param_name)
    param = (table_name, mn, param_code, data_type, start_date_string, end_date_string)
    cursor = connections['DB_baise'].cursor()

    #因为在DB_baise数据库里，每个监测点位的日数据表名称都不一样（类似Day_45007760002801）
    #所以只能用构造SQL语句的方式进行查询
    query = '''SELECT * FROM %s
                WHERE StationID = '%s'
                AND ParamCode = '%s'
                AND DataType = '%s'
                AND DataTime >= '%s'
                AND DataTime <= '%s'
            ''' % param

    cursor.execute(query)
    dict = dict_fetch_all(cursor)

    #生成COD_Avg，pH_Cou 之类的key名
    key = param_name + '_' + data_type
    report_value[key] = dict

    #row = cursor.fetchall()
    #return round(dict[0]['dValue'], 2)

    # for x in range(24):
    #     datetime_object = datetime_object + datetime.timedelta(hours=1)
    #     datetime_string = time.strftime("%Y/%m/%d %H:%M:%S", datetime_object.timetuple())
    #     value = get_monitor_value(mn, datetime_string, param_name, data_type, type)
    #     key = param_name + '_' + data_type
    #     report_hour_value[key] = value
    #     report_value[x] = report_hour_value

    return report_value
