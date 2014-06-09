# coding=utf-8
from __future__ import unicode_literals
from company.function.standard import is_abnormal
from report.function.report import get_monitor_value


__author__ = 'GoTop'


def get_abnormal_date(mn, date):
    abnormal_data = {}
    data_type = 'Avg'
    param_name_list = ['CODcr', 'NH', 'pH']
    data_type_list = ['Avg']
    #获取小时均值数据
    type = 'hour'
    abnormal_data_list = get_monitor_value(mn, date, param_name_list, data_type_list, type)

    # abnormal_data['CODcr_Avg'] = get_monitor_value(mn, date, param_name='CODcr', data_type=data_type, type=type)
    # abnormal_data['NH_Avg'] = get_monitor_value(mn, date, param_name='NH', data_type=data_type, type=type)
    # abnormal_data['pH_Avg'] = get_monitor_value(mn, date, param_name='pH', data_type=data_type, type=type)

    for value, param_name in abnormal_data_list:
        if(is_abnormal(mn, value, param_name)):
            abnormal_data_list = AbnormalData(mn=mn, date_time=date, date_type='Avg',
                                                original_value=value)
    return abnormal_data_list

def get_save_abnormal_date():
    abnormal_data = get_abnormal_date()
    abnormal_data_object = AbnormalData(mn=mn, date_time=date_time, date_type=date_type, original_value=original_value)
