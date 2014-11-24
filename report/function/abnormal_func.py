# coding=utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
import company.function.standard as standard_func
from company.models import Station
import report.function.report_func as report_func
from report.models import AbnormalData
import time, datetime

__author__ = 'GoTop'


def is_abnormal(mn, value, param_name):
    """
    根据监测点位的mn和监控因子param_name的监测值value，判断数据是否异常
    """
    standard = standard_func.get_station_standard(mn, param_name)
    if standard:
        if value > standard['standard_max'] or value < standard['standard_min']:
            return True
        else:
            return False
    else:
        return False


def get_abnormal_data(mn, date_string, param_name_list):
    """
    获取指定监控点位mn，指定某一天的date的异常数据
    并保存到AbnormalData
    """
    data_type_list = ['ZsAvg']
    #获取小时均值数据
    type = 'hour'
    start_date_string = date_string + ' 00:00:00'
    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d %H:%M:%S")
    end_date_string = date_string + ' 23:59:59'
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d %H:%M:%S")

    monitor_data_dict = report_func.get_range_monitor_value(mn, start_date_object, end_date_object, param_name_list,
                                                            data_type_list, type)

    abnormal_data_list = []
    for param_name in param_name_list:
        for data_type in data_type_list:
            #生成COD_Avg，pH_Cou 之类的key名
            key = param_name + '_' + data_type
            for monitor_data in monitor_data_dict[key]:
                if (is_abnormal(mn, monitor_data['dValue'], param_name)):
                    t_station = Station.objects.get(station_id=mn)
                    abnormal_data, abnormal_data_created = AbnormalData.objects.get_or_create(mn=t_station,
                                                                                              data_time=monitor_data[
                                                                                                  'DataTime'],
                                                                                              data_type=monitor_data[
                                                                                                  'DataType'],
                                                                                              param_code=monitor_data[
                                                                                                  'ParamCode'],
                                                                                              original_value=
                                                                                              monitor_data[
                                                                                                  'dValue'])
                    if abnormal_data_created:
                        abnormal_data_list.append(abnormal_data)

    return abnormal_data_list


def count_abnormal_data(mn, start_date_string, end_date_string, param_name_list, data_type):
    """
    统计指定监控点位mn从start_date至end_date，指定监控因子列表中的param_name_list，
    和数据类型data_type（ZsAvg）的超标数
    """
    #获取小时均值数据
    type = 'hour'
    data_type_list = [data_type]
    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    monitor_data_dict = report_func.get_range_monitor_value(mn, start_date_object, end_date_object,
                                                            param_name_list, data_type_list, type)

    monitor_data_num_dict = {}
    for param_name in param_name_list:
        abnormal_data_num = 0
        #生成COD_Avg，pH_Cou 之类的key名
        key = param_name + '_' + data_type

        if key in monitor_data_dict.keys():
            #构造一个key名，类似COD_Avg_num，并赋值
            monitor_data_num_dict[key + '_total_num'] = len(monitor_data_dict[key])
            for monitor_data in monitor_data_dict[key]:
                if (is_abnormal(mn, monitor_data['dValue'], param_name)):
                    abnormal_data_num = abnormal_data_num + 1
            monitor_data_num_dict[key + '_abnormal_num'] = abnormal_data_num

    return monitor_data_num_dict


















