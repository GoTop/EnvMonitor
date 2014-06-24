# coding=utf-8
from __future__ import unicode_literals
from company.function.standard import get_station_standard
from report.function.report_func import get_monitor_value, get_monitor_value_func
from report.models import AbnormalData


__author__ = 'GoTop'

def is_abnormal(mn, value, param_name):
    """
    根据监测点位的mn和监控因子param_name的监测值value，判断数据是否异常
    """
    standard = get_station_standard(mn, param_name)
    if value > standard['standard_max'] or value < standard['standard_min']:
        return True
    else:
        return False

def get_abnormal_date(mn, date):
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
    abnormal_data_list = get_monitor_value_func(mn, date, param_name_list, data_type_list, type)

    # abnormal_data['CODcr_Avg'] = get_monitor_value(mn, date, param_name='CODcr', data_type=data_type, type=type)
    # abnormal_data['NH_Avg'] = get_monitor_value(mn, date, param_name='NH', data_type=data_type, type=type)
    # abnormal_data['pH_Avg'] = get_monitor_value(mn, date, param_name='pH', data_type=data_type, type=type)

    for abnormal_data in abnormal_data_list:
        for param_name, value in abnormal_data:
            if(is_abnormal(mn, value, param_name)):
                abnormal_data_list = AbnormalData(mn=mn, date_time=date, date_type='Avg',
                                                    original_value=value)
    return abnormal_data_list

def get_save_abnormal_date(mn, date, ):
    abnormal_data_list = get_abnormal_date()
    for abnormal_data in abnormal_data_list:
        abnormal_data_object = AbnormalData(mn=mn, date_time=date, date_type='Avg', original_value=original_value)
