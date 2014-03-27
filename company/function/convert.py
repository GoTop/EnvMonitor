#coding=utf-8
from __future__ import unicode_literals
import os
from django.core.exceptions import ObjectDoesNotExist
from EnvMonitor import settings
from company.function.excel import excel_table_by_index
from company.function.string import convert_district

__author__ = 'GoTop'

from report.models import DataParam
from company.models import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')

def sort_district(station):
    district = station.t_admin_area.area_name
    sort_order = None
    if district == '右江区':
        sort_order = 1
    elif district == '田阳':
        sort_order = 2
    elif district == '田东':
        sort_order = 3
    elif district == '平果':
        sort_order = 4
    elif district == '德保':
        sort_order = 5
    elif district == '靖西':
        sort_order = 6
    elif district == '那坡':
        sort_order = 7
    elif district == '凌云':
        sort_order = 8
    elif district == '乐业':
        sort_order = 9
    elif district == '田林':
        sort_order = 10
    elif district == '隆林':
        sort_order = 11
    elif district == '西林':
        sort_order = 12
    return sort_order

def get_station_from_DB_baise():
    all_t_station = T_All_station.objects.using('DB_baise').all().order_by('t_admin_area')
    #all_t_station = sorted(all_t_station,key = sort_district)
    return all_t_station


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
        new_station = Station.objects.create(station_id=t_station.station_id,
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
            NationSuprevise.objects.create(mn=mn, year='2014', type=type)


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
    list = excel_table_by_index(file_path=file_path, by_index=0, colname_row=2, data_start_row=3)
    for row in list:
        # A:国控重点污染源
        # B:非国控，但列入国控建设项目范围内的
        # C:城镇污水处理厂
        # D:国家级和自治区级工业园区集中污水处理厂
        # E:地市级重点监管企业
        # F:非国控重金属污染源企业
        # AF:国控重金属污染源企业
        company_type = None
        if row['污染源单位（业主）属性'] == 'C':
            company_type = 'water_plant'

        #row['县区'] = convert_district(row['县区'])
        #创建或更新企业信息
        if company_type is not None:
            new_company, company_created = Company.objects.get_or_create(name=row['污染源单位（业主）'],
                                                                         organ_code=row['法人代码'],
                                                                         district=row['县区'],
                                                                         trade=company_type

            )
        else:
            new_company, company_created = Company.objects.get_or_create(name=row['污染源单位（业主）'],
                                                                         organ_code=row['法人代码'],
                                                                         district=row['县区'],
            )

        manufacturer, manufacturer_created = Manufacturer.objects.get_or_create(remark=row['监控设备厂家'])

        if manufacturer:
            try:
                #同一台重金属设备可能按两台算
                station = Station.objects.get(station_id=int(row['MN号']))
            except ObjectDoesNotExist:
                station = None

            if station:
                #station_type 只有两种
                station_type = None
                if row['设备类型'] == 'A':
                    station_type = 'water'
                elif row['设备类型'] == 'B':
                    station_type = 'gas'

                in_or_out = None
                if row['进口/排放口'] == '排放口':
                    in_or_out = 'out'
                elif row['进口/排放口'] == '进口':
                    in_or_out = 'in'
                #更新station的信息,因为之前从百色平台导入时未录入
                station.type = station_type
                station.in_or_out = in_or_out
                station.save(update_fields=['type', 'in_or_out'])

                #设置new_company的station的信息
                new_company.station_set.add(station)

                #创建或更新国控信息
                if row['2014国控名单'] == '是':
                    nation_sup_type = None
                    if station_type == 'water':
                        nation_sup_type = 'water'
                    elif station_type == 'gas':
                        nation_sup_type = 'gas'

                    #如何是污水处理厂的，则将nation_sup_type改为water_plant
                    if company_type == 'water_plant':
                        nation_sup_type = 'water_plant'
                    if row['污染源单位（业主）属性'] == 'F' or row['污染源单位（业主）属性'] == 'AF':
                        nation_sup_type = 'metal'
                    #获取或更新国控信息
                    NationSuprevise.objects.get_or_create(station=station, year='2014', type=nation_sup_type)

                param_remark_list = row['监控因子'].split("、")
                for param_remark in param_remark_list:
                    #DataParam表中有('CODcr','氨氮','PH','SO2','NOx','六价铬','总锰','总铅','总镉','砷')
                    #DataParam表中有COD对应的是CODcr
                    if param_remark == 'COD':
                        param_remark = 'CODcr'
                    #DataParam表中有没有'水中油'
                    if param_remark == '水中油':
                        continue
                    data_param = DataParam.objects.get(param_remark=param_remark)
                    if data_param:
                        #创建或更新检测仪信息
                        equipment, equipment_created = Equipment.objects.get_or_create(station=station,
                                                                                       data_param=data_param,
                                                                                       manufacturer=manufacturer)
                        #设置station的equipment的信息
                        if equipment:
                            station.equipment_set.add(equipment)
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
        new_manufacturer, created = Manufacturer.objects.get_or_create(id=t_manufacturer.manufacturer_id,
                                                                       remark=t_manufacturer.remark,
                                                                       contact_person=t_manufacturer.link_man,
                                                                       phone=t_manufacturer.phone,
                                                                       is_have_run_ipmp=t_manufacturer.is_have_run_ipmp

        )

