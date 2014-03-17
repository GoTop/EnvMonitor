#coding=utf-8
from __future__ import unicode_literals
import os
from EnvMonitor import settings
from company.function.excel import excel_table_by_index

__author__ = 'GoTop'

from report.models import DataParam
from company.models import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')


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


# def get_company_info_func():
#     """
#     从DB_balse数据库的T_Compinfo表中读取监测点位的信息，
#     保存到EnvMonitor数据库Company的表中
#     """
#     all_t_company = T_Comp_info.objects.using('DB_baise').all()
#     for t_company in all_t_company:
#         new_company = Company(name=t_company.station_name,
#                               tel=t_company.tel,
#                               organ_code=t_company.organcode,
#                               fax=t_company.fax,
#                               post_code=t_company.postcode,
#                               law_person=t_company.lawperson,
#                               email=t_company.email,
#                               setup_time=t_company.setuptime,
#                               contact=t_company.contactman,
#                               address=t_company.address
#         )
#
#         new_company.save()
#         return all_t_company


from company.db_baise_models import *


def get_special_suprevision_from_excel():
    """
    从excle表中读取监测点位是否属于国控的信息，进行更新
    """
    file_path = settings.IMPORT_PATH + '2013年第4季度百色市重点监控企业自动监测数据有效性审核情况表（MN号）.xls'
    file_path = unicode(file_path, 'utf8')
    list = excel_table_by_index(file_path=file_path, colname_index=0, by_index=0)
    for row in list:
        mn = row['MN号']
        if row['是否14年国控'] == '是':
            type = None
            if row['水或气'] == '水':
                type = 'water'
            elif row['水或气'] == '气':
                type = 'gas'
            elif row['水或气'] == '重金属':
                type = 'water'
            elif row['水或气'] == '污水处理厂':
                type = 'wastewater_treatment_plant'
            SpecialSuprevision.objects.create(mn=mn, year='2014', type=type)


def get_station_from_excel():
    file_path = settings.IMPORT_PATH + '2013年重点污染源自动监控设施社会化运行计划（百色）.xls'
    file_path = unicode(file_path, 'utf8')
    list = excel_table_by_index(file_path=file_path, colname_index=2, by_index=0)
    for row in list:
        if row['污染源单位（业主）属性'] == 'A':
            type = 'water'
        elif row['污染源单位（业主）属性'] == 'B':
            type = 'gas'
        elif row['污染源单位（业主）属性'] == 'C':
            type = 'wastewater_treatment_plant'
        elif row['污染源单位（业主）属性'] == 'E':
            type = 'landfills'
        elif row['污染源单位（业主）属性'] == 'F':
            type = 'metal'

        station_name = row['自动监控设备名称']
        new_station = Station.objects.create(mn=row['MN号'],
                                             name=station_name,
                                             type=type, )
    return list


def get_company_from_excel():
    """
    从excle表中读取企业、监测点位的信息，进行更新
    """

    file_path = settings.IMPORT_PATH + r"2013年重点污染源自动监控设施社会化运行计划（百色）.xls"

    #file_path = file_path.encode('utf8')
    #file_path = unicode(file_path, 'utf8')
    list = excel_table_by_index(file_path=file_path, by_index=0, colname_row=2, data_start_row=3)
    for row in list:
        company_type = None
        station_type = None
        if row['污染源单位（业主）属性'] == 'A':
            station_type = 'water'
        elif row['污染源单位（业主）属性'] == 'B':
            station_type = 'gas'
        elif row['污染源单位（业主）属性'] == 'C':
            company_type = 'wastewater_treatment_plant'
        elif row['污染源单位（业主）属性'] == 'E':
            company_type = 'landfills'
        elif row['污染源单位（业主）属性'] == 'F':
            company_type = 'landfills'
            station_type = 'metal'

        if company_type is not None:
            new_company = Company.objects.create(name=row['污染源单位（业主）'],
                                                 organ_code=row['法人代码'],
                                                 district=row['县区'],
                                                 trade=company_type

            )
        else:
            new_company = Company.objects.create(name=row['污染源单位（业主）'],
                                                 organ_code=row['法人代码'],
                                                 district=row['县区'],
            )

        if row['进口/排放口'] == '排放口':
            in_or_out = 'out'
        elif row['进口/排放口'] == '进口':
            in_or_out = 'in'

        manufacturer, manufacturer_created = Manufacturer.objects.get_or_create(remark=row['监控设备厂家'])
        if manufacturer:
            equipment, equipment_created = Equipment.objects.get_or_create(manufacturer=manufacturer)
        station = Station.objects.get(mn=row['MN号'])
        if station:
            station.objects.update(type=type, in_or_out=in_or_out)
            if equipment:
                station.equipment_set.add(equipment)
            new_company.station_set.add(station)

    return list


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


def get_manufacturer_table():
    """
    将T_Manufacturer表从DB_baise数据库中的数据复制到EnvMonitor数据库的Manufacturer表中
    """
    t_manufacturer_set = T_Manufacturer.objects.using('DB_baise').all()
    for t_manufacturer in t_manufacturer_set:
        new_manufacturer = Manufacturer(manufacturer_id=t_manufacturer.manufacturer_id,
                                        remark=t_manufacturer.remark,
                                        link_man=t_manufacturer.link_man,
                                        phone=t_manufacturer.phone,
                                        is_have_run_ipmp=t_manufacturer.is_have_run_ipmp

        )
        new_manufacturer.save()
