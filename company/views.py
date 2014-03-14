# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from function.standard import *
from function.db import SqlServerDB
import pyodbc
from company.function.convert import *
from report.function.report import *


class CompanyList(ListView):
    model = Company


class StationList(ListView):
    model = Station


# Create your views here.
def test(request):
    #list = update_station()

    get_data_param_table()
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


