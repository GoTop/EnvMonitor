# coding=utf-8
from __future__ import unicode_literals
__author__ = 'GoTop'

from company.models import T_All_station,T_Exam_project, T_Superscale

def get_standard_func(mn):

    station = T_All_station.objects.using('DB_baise').get(pk=mn)

    exam_project_list = T_Exam_project.objects.using('DB_baise').filter(station_id=mn)
    for exam_project in  exam_project_list:
        return exam_project.t_superscale_set.all()
    #for t_superscale in exam_project.t_superscale_set:






