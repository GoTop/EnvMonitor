# coding=utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
import company.function.standard as standard_func
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


def get_abnormal_data(mn, date_string):
    """
    获取指定监控点位mn，指定日期date的异常数据
    并保存到AbnormalData
    """
    abnormal_data = {}
    data_type = 'Avg'
    param_name_list = ['CODcr', 'NH', 'pH']
    data_type_list = ['Avg']
    #获取小时均值数据
    type = 'hour'
    start_date_string = date_string + ' 00:00:00'
    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d %H:%M:%S")
    end_date_string = date_string + ' 23:59:59'
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d %H:%M:%S")

    monitor_data_dict = report_func.get_range_monitor_value(mn, start_date_object, end_date_object, param_name_list,
                                                             data_type_list, type)

    # abnormal_data['CODcr_Avg'] = get_monitor_value(mn, date, param_name='CODcr', data_type=data_type, type=type)
    # abnormal_data['NH_Avg'] = get_monitor_value(mn, date, param_name='NH', data_type=data_type, type=type)
    # abnormal_data['pH_Avg'] = get_monitor_value(mn, date, param_name='pH', data_type=data_type, type=type)

    for param_name in param_name_list:
        for data_type in data_type_list:
            #生成COD_Avg，pH_Cou 之类的key名
            key = param_name + '_' + data_type
            for abnormal_data in monitor_data_dict[key]:
                if (is_abnormal(mn, abnormal_data['dValue'], param_name)):
                    abnormal_data_list = AbnormalData(mn=mn, date_time=abnormal_data['DataTime'],
                                                      date_type=abnormal_data['DataType'],
                                                      original_value=abnormal_data['dValue'])
    #return abnormal_data_list


def get_save_abnormal_data(mn, date, ):
    abnormal_data_list = get_abnormal_data()
    for abnormal_data in abnormal_data_list:
        abnormal_data_object = AbnormalData(mn=mn, date_time=date, date_type='Avg', original_value=original_value)
