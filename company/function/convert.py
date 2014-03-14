#coding=utf-8
from __future__ import unicode_literals
from company.function.excel import excel_table_by_index

__author__ = 'GoTop'

from report.models import DataParam

from company.models import Company, Station
from company.db_baise_models import *


def get_company_info_func():
    """
    从DB_balse数据库的T_Compinfo表中读取监测点位的信息，
    保存到EnvMonitor数据库Company的表中
    """
    all_t_company = T_Comp_info.objects.all()
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

        kind_id = t_station.t_station_kind.kind_id
        if kind_id == 32:
            type = 'water'
        elif kind_id == 35:
            type = 'gas'
        else:
            type = ''
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


def get_data_param_table():
    """
    将T_DataParam表从DB_baise数据库中的数据复制到EnvMonitor数据库的DataParam表中
    """
    t_data_param_set = T_Data_param.objects.using('DB_baise').all()
    for t_data_param in t_data_param_set:
        new_data_param = DataParam(param_code=t_data_param.param_code,
                                   standard_code=t_data_param.standard_code,
                                   param_remark=t_data_param.param_remark,
                                   param_kind=t_data_param.param_kind,
                                   order_id=t_data_param.order_id,
                                   param_unit=t_data_param.param_unit,
                                   data_precision=t_data_param.data_precision,
                                   is_have_cou=t_data_param.is_have_cou,
                                   app_value=t_data_param.app_value
        )
        new_data_param.save()





