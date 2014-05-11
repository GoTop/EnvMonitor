# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from company.models import T_All_station
from report.function.report import get_station_standard, get_water_data_func, get_gas_data_func

import datetime

# Create your views here.
def water_daily_report_view(request, date):
    mn_list = ['45007760002801', '45007760003001']

    #strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")
    daily_report_list = []
    for mn in mn_list:
        daily_report_value = {}
        daily_report_value = get_water_data_func(mn, date, type='day')

        t_station = T_All_station.objects.using('DB_baise').get(pk=mn)
        daily_report_value['station_name'] = t_station.station_name
        daily_report_list.append(daily_report_value)
    return render_to_response('water_daily_report.html',
                              {'datetime': datetime_object,
                               'type': '日',
                               'daily_report_list': daily_report_list})


def gas_daily_report_view(request, date):
    mn_list = ['45007760002007', '45007760002601']

    #strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")
    daily_report_list = []
    for mn in mn_list:
        daily_report_value = {}
        daily_report_value = get_gas_data_func(mn, date, type='day')

        t_station = T_All_station.objects.using('DB_baise').get(pk=mn)
        daily_report_value['station_name'] = t_station.station_name

        daily_report_list.append(daily_report_value)
    return render_to_response('gas_daily_report.html',
                              {'datetime': datetime_object,
                               'type': '日',
                               'daily_report_list': daily_report_list})

#TODO
def company_hour_report_view(request, mn, date):

    #strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")
    hour_report_list = []

    daily_report_value = get_water_data_func(mn, date, type='hour')
    t_station = T_All_station.objects.using('DB_baise').get(pk=mn)
    #daily_report_value['station_name'] = t_station.station_name.decode('gbk', 'ignore').encode('utf8')
    daily_report_value['station_name'] = t_station.station_name
    #.encode('utf-8')

    CODcr_standard_dict = get_station_standard(mn=mn, param_name='CODcr')
    NH_standard_dict = get_station_standard(mn=mn, param_name='NH')

    standard_dict = {}
    if CODcr_standard_dict:
        daily_report_value['CODcr_standard'] = CODcr_standard_dict['standard_max']

        #如果CODcr的值超标，这设置一个字段为True
        if daily_report_value['CODcr_Avg'] > CODcr_standard_dict['standard_max'] \
                or daily_report_value['CODcr_Avg'] < CODcr_standard_dict['standard_min']:
            daily_report_value['CODcr_abnormal'] = True
    if NH_standard_dict:
        daily_report_value['NH_standard'] = NH_standard_dict['standard_max']

        #如果NH的值超标，这设置一个字段为True
        if daily_report_value['NH_Avg'] > NH_standard_dict['standard_max'] \
                or daily_report_value['NH_Avg'] < NH_standard_dict['standard_min']:
            daily_report_value['NH_abnormal'] = True

        hour_report_list.append(daily_report_value)
    return render_to_response('water_daily_report.html',
                              {'datetime': datetime_object, 'daily_report_list': hour_report_list})

