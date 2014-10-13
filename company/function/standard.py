# coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

from company.models import T_All_station, T_Exam_project, T_Superscale, T_Data_param

def get_param_code(param_name):
    """
    根据param_name返回ParamCode
    :param param_name:
    :return:
    """
    ParamCode = ''
    if param_name == 'CODcr':
        ParamCode = 'Z02'
    elif param_name == 'NH':
        ParamCode = 'Z05'
    elif param_name == 'pH':
        ParamCode = 'Z60'
    elif param_name == 'SO2':
        ParamCode = 'ZB2'
    elif param_name == 'NOx':
        ParamCode = 'ZB3'
    elif param_name == 'O2':
        #氧气含量
        ParamCode = 'ZB4'
    elif param_name == 'volume_of_water':
        ParamCode = 'Z91'
    elif param_name == 'volume_of_gas':
        ParamCode = 'Z92'
    return ParamCode

# def get_standard_func(mn):
#
#     """
#     获取监控点位mn的监测因子的标准
#     :param mn:
#     :return:
#     """
#     station = T_All_station.objects.using('DB_baise').get(pk=mn)
#     t_exam_project_set = station.t_exam_project_set
#
#     t_exam_project_set = T_Exam_project.objects.using('DB_baise').filter(station_id=mn)
#
#     all_standard = []
#     for t_exam_project in t_exam_project_set:
#         standard_info = {}
#         standard_max = None
#         standard_min = None
#         #监控因子信息
#         t_data_param = t_exam_project.param_code
#         #对应的标准
#         t_superscale_set = t_exam_project.t_superscale_set.all()
#         if t_superscale_set.exists():
#             #标准信息，ph会有两个标准，一个是6，一个是9
#             if t_data_param.param_remark == 'pH':
#                 standard_max = t_superscale_set[0].standard_value
#                 standard_min = t_superscale_set[1].standard_value
#             else:
#                 #COD的标准信息只有一个，60
#                 for t_superscale in t_superscale_set:
#                     standard_max = t_superscale.standard_value
#                     standard_min = 0
#         else:
#             continue
#
#         standard_info = {
#             'param_remark': t_data_param.param_remark,
#             'standard_max': standard_max,
#             'standard_min': standard_min,
#         }
#
#         all_standard.append(standard_info)
#
#     return (station, all_standard)


def get_station_standard(mn, param_name):
    """
    根据监测点位的mn，获取指定的监控因子param_name对应的标准值
    """
    param_code = get_param_code(param_name)
    t_superscale_list = T_Superscale.objects.using('DB_baise').filter(
        t_exam_project__t_data_param__param_code=param_code,
        t_exam_project__t_all_station__station_id=mn).all()
    standard = {}
    if t_superscale_list.exists():
        if t_superscale_list.count() == 1:
            standard['standard_max'] = t_superscale_list[0].standard_value
            standard['standard_min'] = 0
        elif t_superscale_list.count() == 2:
            standard['standard_max'] = t_superscale_list[0].standard_value
            standard['standard_min'] = t_superscale_list[1].standard_value

        standard['text'] = str(standard['standard_min']) + '-' + str(standard['standard_max'])
        standard['param_name'] = param_name
        standard['param_code'] = param_code
    else:
        standard = None

    return standard


#TODO 未完成
def get_all_station_standard(mn):
    """
    根据监测点位的mn，获取其所有的标准值
    """
    t_superscale_list = T_Superscale.objects.using('DB_baise').filter(
        t_exam_project__t_all_station__station_id=mn).all()



