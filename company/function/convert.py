#coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

from company.models import Company, Station
from company.db_baise_models import *
import xlrd
from xlwt import Workbook

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_company_info_func():
    """
    从DB_balse数据库的T_Compinfo表中读取监测点位的信息，
    保存到EnvMonitor数据库Company的表中
    """
    all_t_company = T_Compinfo.objects.all()
    for t_company in all_t_company:
        new_company = Company(name=t_company.station_name,
                              tel=t_company.tel,
                              organ_code=t_company.organcode,
                              fax=t_company.fax,
                              post_code=t_company.postcode,
                              law_person=t_company.lawperson,
                              email=t_company.email,
                              setup_time=t_company.setuptime,
                              contact=t_company.contactman,
                              address=t_company.address
        )

        new_company.save()
        return all_t_company


def get_station_info_func():
    """
    从DB_balse数据库的T_Allstation表中读取监测点位的信息，
    保存到EnvMonitor数据库的Station表中
    """

    all_t_station = T_All_station.objects.using('DB_baise').all()
    for t_station in all_t_station:
        t_station.station_name = t_station.station_name

        kind_id = t_station.kind_id
        if t_station.kind_id == 32:
            type = 'water'
        elif t_station.kind_id == 35:
            type = 'gas'
        else:
            type = 'no'
        new_station = Station.objects.create(mn=t_station.station_id,
                                             name=t_station.station_name,
                                             type=type,
        )
    return all_t_station


def update_station():
    """
    从excle表中读取监测点位的信息，进行更新
    """
    file = 'D:/TDDOWNLOAD/2013年第4季度百色市重点监控企业自动监测数据有效性审核情况表（MN号）(1).xls'
    list = excel_table_by_index(file=file, colname_index=0, by_index=0)
    for row in list:
        mn = row['MN号']
        if row['是否14年国控'] == '是':
            type = None
            if row['水或气'] == '水':
                type = 'water'
            elif row['水或气'] == '气':
                type = 'gas'
            elif row['水或气'] == '重金属':
                type = 'gas'
            elif row['水或气'] == '污水处理厂':
                type = 'wastewater_treatment_plant'
            SpecialSuprevision.objects.create(mn=mn, year='2014', type=type)


def excel_table_by_index(file='file.xls', colname_index=0, by_index=0):
    """
    根据索引获取Excel表格中的数据
    参数:file：Excel文件路径
        colname_index：表头列名所在行的索引
        by_index：表的索引
    """
    data = xlrd.open_workbook(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  #行数
    ncols = table.ncols  #列数
    col_names = table.row_values(colname_index)  #某一行数据
    list = []
    for row_num in range(1, nrows):

        row = table.row_values(row_num)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[col_names[i]] = row[i]
            list.append(app)
    return list






