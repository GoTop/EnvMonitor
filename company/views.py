# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from company.function.string import sort_company_by_district
from function.standard import *
from function.db import SqlServerDB
import pyodbc
from company.function.convert import *
from report.function.report import *


class CompanyList(ListView):
    model = Company
    queryset = sorted(Company.objects.all(), key=sort_company_by_district)
    template_name = 'company/company_list.html'


class StationList(ListView):
    model = Station
    template_name = 'company/station_list.html'


# Create your views here.
def test(request):
    #list = update_station()

    list = get_company_from_excel()
    return render_to_response('article_list.html', {'list': list})


def get_station_info(request):
    """
    从DB_balse数据库的T_Allstation表中读取监测点位的信息，
    保存到EnvMonitor数据库的Station表中
    """
    all_t_station = get_station_info_func()
    return render_to_response('article_list.html', {'row': all_t_station})


def get_standard(request):
    mn = '45007760002801'
    (station, all_standard_info) = get_standard_func(mn=mn)
    return render_to_response('standard_info.html', {'station': station,
                                                     'all_standard_info': all_standard_info
    })


def init_database(request):
    #将T_DataParam表从DB_baise数据库中的数据复制到EnvMonitor数据库的DataParam表中
    get_data_param_table()
    #将T_Manufacturer表从DB_baise数据库中的数据复制到EnvMonitor数据库的Manufacturer表中
    get_manufacturer_table()

    get_station_info_func()

    return render_to_response('result.html', {'text': 'success!'})


def get_station_from_DB_baise_view(request):
    station_list = get_station_from_DB_baise()
    return render_to_response('all_station.html', {'station_list': station_list})
