# coding=utf-8
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from function.standard import *
from function.db import SqlServerDB
import pyodbc
from company.function.convert import *


class CompanyList(ListView):
    model = Company


class StationList(ListView):
    model = Station


# Create your views here.
def test_db(request):
    #     db = SqlServerDB(host='127.0.0.1', port='1433', user='sa', password='the305', db='EnvMonitor', charset="utf8")
    #     sql = '''
    # CREATE TABLE Company(
    #     company_id    int             IDENTITY(1,1),
    #     Name          nvarchar(50)    NOT NULL,
    #     Tel           varchar(12)     NULL,
    #     OrganCode     varchar(20)     NULL,
    #     Fax           varchar(12)     NULL,
    #     Postcode      varchar(6)      NULL,
    #     LawPerson     nvarchar(10)    NULL,
    #     Email         varchar(50)     NULL,
    #     SetUpTime     datetime        NULL,
    #     LinkMan       nvarchar(10)    NULL,
    #     Address       nvarchar(80)    NULL,
    # )
    # '''
    #     resuslt = db.query(sql)
    #     rowcount = db.rowcount()

    # cnxn = pyodbc.connect(DRIVER='{SQL Native Client}', SERVER='localhost', DATABASE='EnvMonitor', UID='sa',
    #                       PWD='the305')
    # cursor = cnxn.cursor()
    # cursor.execute('''INSERT INTO [EnvMonitor].[dbo].[Station]
    #        ([mn]
    #        ,[type]
    #        ,[company_id]
    #        ,[name]
    #        ,[in_or_out]
    #        ,[maintain_company_id])
    #  VALUES
    #        (4500111111121,
    #        'water',
    #        NULL,
    #        '问问',
    #        'in',
    #        NULL)''')
    # row =  cursor.rowcount
    # cnxn.commit()

    # row = cursor.fetchall()
    # if row:
    #     print row
    row = 1

    new_station = Station(mn='8',
                          name='哈哈',
                          type='water',
    )

    name_uni = '什么中文的偶崩溃了'

    new_company = Company.objects.create(name=name_uni)

    #new_station.save()

    return render_to_response('article_list.html', {'error_message': new_company.name})


def get_station_info(request):
    """

    :param request:
    """

    all_t_station = get_station_info_func()
    return render_to_response('article_list.html', {'row': all_t_station})


def get_standard(request):
    mn = '45007760002801'
    t_superscale_list = get_standard_func(mn = mn)
    return render_to_response('article_list.html', {'row': t_superscale_list})


