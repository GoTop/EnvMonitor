from __future__ import unicode_literals
# coding=utf-8
__author__ = 'GoTop'

from django.db import connections
import time

#
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def get_param_code(param_name):
    #根据param_name返回ParamCode
    ParamCode = ''
    if param_name == 'CODcr':
        ParamCode = 'Z02'
    elif param_name == 'NH':
        ParamCode = 'Z05'
    elif param_name == 'SO2':
        ParamCode = 'ZB2'
    elif param_name == 'NOx':
        ParamCode = 'ZB3'
    elif param_name == 'pH':
        ParamCode = 'Z60'
    elif param_name == 'volume_of_water':
        ParamCode = 'Z91'
    return ParamCode


def day_param_value(mn, date, param_name, data_type):
    param_code = get_param_code(param_name)
    timeArray = time.strptime(date, "%Y%m%d")
    date = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    table_name = 'Day_' + mn
    param = (table_name, mn, param_code, data_type, date)
    cursor = connections['DB_baise'].cursor()

    query = '''SELECT * FROM %s
                WHERE StationID = '%s'
                AND ParamCode = '%s'
                AND DataType = '%s'
                AND DataTime = '%s' ''' % param

    cursor.execute(query)
    dict = dictfetchall(cursor)
    #row = cursor.fetchall()
    return round(dict[0]['dValue'], 2)


def water_daily_report_func(mn, date):
    CODcr_Avg_day_value = day_param_value(mn, date, param_name='CODcr', data_type='Avg')
    CODcr_Cou_day_value = day_param_value(mn, date, param_name='CODcr', data_type='Cou')

    NH_Avg_day_value = day_param_value(mn, date, param_name='NH', data_type='Avg')
    NH_Cou_day_value = day_param_value(mn, date, param_name='NH', data_type='Cou')

    pH_Avg_day_value = day_param_value(mn, date, param_name='pH', data_type='Avg')
    volume_of_water_Cou_day_value = day_param_value(mn, date, param_name='volume_of_water', data_type='Cou')
    daily_report_value = {'CODcr_Avg': CODcr_Avg_day_value,
                          'CODcr_Cou': CODcr_Cou_day_value,
                          'NH_Avg': NH_Avg_day_value,
                          'NH_Cou': NH_Cou_day_value,
                          'pH_Avg': pH_Avg_day_value,
                          'volume_of_water_Cou': volume_of_water_Cou_day_value,
    }
    return daily_report_value


def COD_day_cou_value(mn, date):
    #strptime将格式字符串转换为datetime对象
    timeArray = time.strptime(date, "%Y%m%d")
    date = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    table_name = 'Day_' + mn
    param = (table_name, mn, 'Z02', date,)
    cursor = connections['DB_baise'].cursor()

    query = '''SELECT * FROM %s
                WHERE StationID = '%s'
                AND ParamCode = '%s'
                AND DataType = 'Cou'
                AND DataTime = '%s' ''' % param

    cursor.execute(query)
    dict = dictfetchall(cursor)
    #row = cursor.fetchall()
    return dict.dValue



