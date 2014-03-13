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
def test_db(request):
    standard_list = get_station_standard(mn='45007760002801', param_name='CODcr')
    for standard in standard_list:
        pass
    return render_to_response('article_list.html', {'result_tuple': standard_list.items()})


def get_station_info(request):
    """

    :param request:
    """
    all_t_station = get_station_info_func()
    return render_to_response('article_list.html', {'row': all_t_station})


def get_standard(request):
    mn = '45007760002801'
    (station, all_standard_info) = get_standard_func(mn=mn)
    return render_to_response('standard_info.html', {'station': station,
                                                     'all_standard_info': all_standard_info
    })


