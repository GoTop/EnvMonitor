# coding=utf-8
from __future__ import unicode_literals
from django.utils import timezone
from company.function.standard import get_param_code
import time, datetime
from django.db import connections
from date_func import get_time_range_list

__author__ = 'GoTop'


def dict_fetch_all(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def get_single_monitor_value(mn, date, param_name, data_type, table_type):
    """
    获取废水监测点位mn的date当天指定类型data_type（平均值Avg，或累计值Cou）
    和指定监测因子param_name的小时或日数据（由table_type(day或hour)设置）

    只返回一个单独的数值

    如果是获取日数据，date的格式必须是 "%Y%m%d"
    :param mn:
    :param date:
    :param param_name: param_name的定义在get_param_code(param_name)函数中查看
    :param data_type:
    :param table_type:
    如果是获取小时数据，date的格式必须是 "%Y/%m/%d %H:%M:%S"
    """
    param_code = get_param_code(param_name)

    # 根据day_or_hour选择数据库中的日数据表或者小时数据表
    if table_type == 'day':
        table_name = 'Day_' + mn
        # strptime() 函数根据指定的格式把一个时间字符串解析为时间元组
        datetime_tuple = time.strptime(date, "%Y%m%d")
        # time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定
        date = time.strftime("%Y/%m/%d %H:%M:%S", datetime_tuple)
    elif table_type == 'hour':
        table_name = 'Hour_' + mn
        # strptime() 函数根据指定的格式把一个时间字符串解析为时间元组
        datetime_tuple = time.strptime(date, "%Y/%m/%d %H:%M:%S")
        # time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定
        date = time.strftime("%Y/%m/%d %H:%M:%S", datetime_tuple)
    param = (table_name, mn, param_code, data_type, date)
    cursor = connections['DB_baise'].cursor()

    # 因为在DB_baise数据库里，每个监测点位的日数据表名称都不一样（类似Day_45007760002801）
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


def get_range_monitor_value(mn, start_date_object, end_date_object, param_name, data_type, table_type):
    '''
    一个简便功能函数，可以方便地获取监测点位mn的date的多个因子和数据类型的小时或日数据

    param_name_list：监控因子列表
    data_type：数据类型列表：Avg,ZsAvg,Min,Max,ZsMin,ZsMax,Cou
    table_type(day或hour):根据该参数选择小时或日数据的表

    return：返回的数组中，key为类似COD_Avg这样的格式
    '''

    # 根据type选择数据库中的日数据表或者小时数据表
    # 格式化start_date和end_date
    if table_type == 'day':
        table_name = 'Day_' + mn
    elif table_type == 'hour':
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
    return dict


def get_format_monitor_data(mn, param_name, data_type, table_type, start_date_object, end_date_object,
                            interval_second):
    """
    将获取数据库中一个时间段指定监控因子，指定数据类型的监控数据做成一个函数
    :param mn:
    :param param_name:
    :param data_type:
    :param table_type:
    :param start_date_object:
    :param end_date_object:
    :param interval_second:
    :return:
    """
    step = datetime.timedelta(seconds=interval_second)
    time_range_list = get_time_range_list(start_date_object, end_date_object, step)

    # 如果使用 report_table = report_table.fromkeys(time_range_list, {})
    # 会导致每一个report_table的item的值均指向使用相同存储空间，导致对任意一个item的赋值，就是对所有item赋值的
    report_table = {k: {} for k in time_range_list}

    # 获取监控因子数据
    # 改用每次获取一个监控因子某一时间段的所有监控数据，组合为报表中一行数据的方法
    monitor_data_list = get_range_monitor_value(mn, start_date_object, end_date_object,
                                                param_name, data_type, table_type)

    key = param_name + '_' + data_type

    report_row = {}
    for time in time_range_list:

        report_single_param = {key: '-'}
        report_row.update(report_single_param)
        report_table[time].update(report_row)

        for monitor_data in monitor_data_list:
            monitor_data_datetime = monitor_data['DataTime'].replace(tzinfo=None)
            #.strftime("%Y%m%d%H%M%S")
            if time == monitor_data_datetime:
                report_single_param = {key: monitor_data['dValue']}
                report_row.update(report_single_param)
                report_table[time].update(report_row)
                break
    return report_table
