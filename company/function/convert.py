#coding=utf-8
from __future__ import unicode_literals
import os
from django.core.exceptions import ObjectDoesNotExist
import time
from django.db import connection

from EnvMonitor import settings
from company.function.excel import excel_table_by_index
from company.function.string import sort_station_by_district

__author__ = 'GoTop'

from report.models import DataParam
from company.para_models import T_Trade
from company.models import *
from company.db_baise_models import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_station_from_db_baise():
    all_t_station = T_All_station.objects.using('DB_baise').all()
    all_t_station = sorted(all_t_station, key=sort_station_by_district)
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
            station_type = 'water'
        elif kind_id == 35:
            station_type = 'gas'
        else:
            station_type = ''
        new_station = Station.objects.create(station_id=t_station.station_id,
                                             name=t_station.station_name,
                                             type=station_type,
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
    如果，T_All_station有的点位，excle中没有，则无法填写县区
    """

    # file_path = settings.IMPORT_PATH + r"2013年重点污染源自动监控设施社会化运行计划（百色）.xls"
    # list = excel_table_by_index(file_path=file_path, by_index=0, colname_row=2, data_start_row=3)

    file_path = settings.IMPORT_PATH + r"百色市2015年重点污染源自动监控设施社会化运行计划.xls"
    list = excel_table_by_index(file_path=file_path, by_index=0, colname_row=2, data_start_row=3)

    for row in list:
        mn = int(row['MN号'])

        #从DB_baise中获取station的trade行业信息
        try:
            t_station = T_All_station.objects.using('DB_baise').get(station_id=mn)
            station_trade = t_station.t_trade.remark
        except ObjectDoesNotExist:
            #如果遇到excle表中的企业，在T_All_station数据库中不存在，比如“广西百色那荷矿业有限责任公司”
            #则将其trade设置为其他
            station_trade = T_Trade.objects.using('DB_baise').get(pk=1).remark

        #row['污染源单位（业主）属性']的代码含义如下：
        # A:国控重点污染源
        # B:非国控，但列入国控建设项目范围内的
        # C:城镇污水处理厂
        # D:国家级和自治区级工业园区集中污水处理厂
        # E:地市级重点监管企业
        # F:非国控重金属污染源企业
        # AF:国控重金属污染源企业

        #row['县区'] = convert_district(row['县区'])
        #创建或更新企业信息

        try:
            company = Company.objects.get(name=row['污染源单位（业主）'])
        except ObjectDoesNotExist:
            company = Company(name=row['污染源单位（业主）'], organ_code=row['法人代码'],
                              district=row['县区'],
                              trade=station_trade)
            company.save()

        # new_company, company_created = Company.objects.get_or_create(name=row['污染源单位（业主）'],
        #                                                              defaults={
        #                                                                  'organ_code': row['法人代码'],
        #                                                                  'district': row['县区'],
        #                                                                  'trade': station_trade}
        # )

        #manufacturer, manufacturer_created = Manufacturer.objects.get_or_create(remark=row['监控设备厂家'])

        try:
            manufacturer = Manufacturer.objects.get(remark=row['监控设备厂家'])
        except ObjectDoesNotExist:
            manufacturer = Manufacturer(remark=row['监控设备厂家'])
            manufacturer.save()

        if manufacturer:
            #从EnvMonitor数据库station表中（该表数据来源于DB_baise数据库）获取信息
            try:
                station = Station.objects.get(station_id=mn)
            except ObjectDoesNotExist:
                station = None
        if station:
            #station_type 只有两种
            station_type = None
            if row['设备类型'] == 'A':
                station_type = '废水'
            elif row['设备类型'] == 'B':
                station_type = '废气'

            in_or_out = None
            if row['进口/排放口'] == '排放口':
                in_or_out = '排放口'
            elif row['进口/排放口'] == '进口':
                in_or_out = '进口'
            #更新station的信息,因为之前未从百色平台导入时未录入
            station.type = station_type
            station.in_or_out = in_or_out
            station.save(update_fields=['type', 'in_or_out'])

            #设置company的station的信息
            company.station_set.add(station)


            #创建或更新国控信息
            #暂时禁用
            # if row['2014国控名单'] == '是':
            #     nation_sup_type = None
            #     if station_type == '废水':
            #         nation_sup_type = '废水'
            #     elif station_type == '废气':
            #         nation_sup_type = '废气'
            #
            #     #果然station trade是以下类型，则修改相应的nation_sup_type
            #     if station_trade == '污水处理厂':
            #         nation_sup_type = '污水处理厂'
            #     if station_trade == '垃圾填埋厂':
            #         nation_sup_type = '垃圾填埋厂'
            #     if row['污染源单位（业主）属性'] == 'F' or row['污染源单位（业主）属性'] == 'AF':
            #         nation_sup_type = '重金属'
            #     #获取或更新国控信息
            #     NationSuprevise.objects.get_or_create(station=station, year='2014', type=nation_sup_type)

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
                    # equipment, equipment_created = Equipment.objects.get_or_create(station=station,
                    #                                                                data_param=data_param,
                    #                                                                manufacturer=manufacturer)

                    try:
                        equipment = Equipment.objects.get(station=station,
                                                          data_param=data_param,
                                                          manufacturer=manufacturer)
                    except ObjectDoesNotExist:
                        equipment = Equipment(station=station,
                                              data_param=data_param,
                                              manufacturer=manufacturer)
                        equipment.save()

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
        # new_manufacturer, created = Manufacturer.objects.get_or_create(id=t_manufacturer.manufacturer_id,
        #                                                                remark=t_manufacturer.remark,
        #                                                                contact_person=t_manufacturer.link_man,
        #                                                                phone=t_manufacturer.phone,
        #                                                                is_have_run_ipmp=t_manufacturer.is_have_run_ipmp
        #
        # )

        try:
            manufacturer = Manufacturer.objects.get(id=t_manufacturer.manufacturer_id,
                                                    remark=t_manufacturer.remark,
                                                    contact_person=t_manufacturer.link_man,
                                                    phone=t_manufacturer.phone,
                                                    is_have_run_ipmp=t_manufacturer.is_have_run_ipmp)
        except ObjectDoesNotExist:
            manufacturer = Manufacturer(id=t_manufacturer.manufacturer_id,
                                        remark=t_manufacturer.remark,
                                        contact_person=t_manufacturer.link_man,
                                        phone=t_manufacturer.phone,
                                        is_have_run_ipmp=t_manufacturer.is_have_run_ipmp)
            manufacturer.save()


