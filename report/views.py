# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render, render_to_response
from report.function.report import *
from company.db_baise_models import *
import datetime

# Create your views here.
def water_daily_report_view(request, date):
    mn_list = ['45007760002801', '45007760003001']

    #strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")
    daily_report_list = []
    for mn in mn_list:
        daily_report_value = water_daily_report_func(mn, date)
        t_station = T_All_station.objects.using('DB_baise').get(pk=mn)
        #daily_report_value['station_name'] = t_station.station_name.decode('gbk', 'ignore').encode('utf8')
        daily_report_value['station_name'] = t_station.station_name
        daily_report_list.append(daily_report_value)
    return render_to_response('daily_report.html', {'datetime': datetime_object, 'daily_report_list': daily_report_list})