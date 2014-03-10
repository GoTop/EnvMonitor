# coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

from company.models import T_All_station, T_Exam_project, T_Superscale, T_Data_param


def get_standard_func(mn):
    station = T_All_station.objects.using('DB_baise').get(pk=mn)
    t_exam_project_set = station.t_exam_project_set

    t_exam_project_set = T_Exam_project.objects.using('DB_baise').filter(station_id=mn).filter()

    all_standard = []
    for t_exam_project in t_exam_project_set:
        standard_info = {}
        #监控因子信息
        t_data_param = t_exam_project.param_code

        #标准信息，ph会有两个标准，一个是6，一个是9
        if t_data_param.param_remark == 'pH':
            t_superscale_set = t_exam_project.t_superscale_set.all()
            standard_max = t_superscale_set[0].standard_value
            standard_min = t_superscale_set[1].standard_value
        else:
            #COD的标准信息只有一个，60
            t_superscale_set = t_exam_project.t_superscale_set.all()
            for t_superscale in t_superscale_set:
                standard_max = t_superscale.standard_value
                standard_min = 0

        standard_info = {
            'param_remark': t_data_param.param_remark,
            'standard_max': standard_max,
            'standard_min': standard_min,
        }

        all_standard.append(standard_info)

    return (station, all_standard)








