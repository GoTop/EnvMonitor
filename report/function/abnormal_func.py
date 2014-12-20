# coding=utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
from django.core.exceptions import ObjectDoesNotExist
import company.function.standard as standard_func
from company.models import Station
from report.function import monitor_value
import report.function.report_func as report_func
from report.models import AbnormalData
import time, datetime

__author__ = 'GoTop'


def is_abnormal(mn, value, param_name):
    """
    根据监测点位的mn和监控因子param_name的监测值value，判断数据是否异常
    """
    standard = standard_func.get_station_standard(mn, param_name)
    if standard:
        if value > standard['standard_max'] or value < standard['standard_min']:
            return True
        else:
            return False
    else:
        return False


def is_abnormal_by_standard(value, standard_max, standard_min):
    """
    根据standard_max, standard_min,判断监测值value，判断数据是否异常
    """
    if value > standard_max or value < standard_min:
        return True
    else:
        return False


def get_abnormal_data(mn, start_date_string, end_date_string, param_name, data_type, table_type,
                      old_standard_info=None):
    """
    获取指定监控点位mn，指定某一段时间的date的异常超标数据
    并保存到AbnormalData
    """

    #data_type_list = ['ZsAvg']
    #获取小时均值数据
    #table_type = 'hour'

    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    #获取该时段的在线监控数值
    monitor_data_dict = monitor_value.get_range_monitor_value(mn, start_date_object, end_date_object, param_name,
                                                              data_type, table_type)

    abnormal_data_list = []

    standard = standard_func.get_station_standard(mn, param_name)

    #如果设置了旧标准
    if old_standard_info:
        #旧标准改为新标准的时间
        standard_change_date = datetime.datetime.strptime(old_standard_info['old_standard']['standard_change_date'],
                                                          "%Y%m%d")

    t_station = Station.objects.get(station_id=mn)

    #生成类似COD_Avg，pH_Cou 之类的key名
    key = param_name + '_' + data_type
    for monitor_data in monitor_data_dict:
        #如果当前的自动监控数据的时间早于“旧标准改为新标准的时间”，则使用旧标准
        if old_standard_info and monitor_data['DataTime'].replace(tzinfo=None) < standard_change_date:
            standard = {}
            standard['standard_max'] = old_standard_info['old_standard'][param_name]['standard_max']
            standard['standard_min'] = old_standard_info['old_standard'][param_name]['standard_min']

        if standard:
            if (is_abnormal_by_standard(monitor_data['dValue'], standard['standard_max'], standard['standard_min'])):
                # try:
                #     abnormal_data = AbnormalData.objects.get(mn=t_station,
                #                                              data_time=monitor_data[
                #                                                  'DataTime'],
                #                                              data_type=monitor_data[
                #                                                  'DataType'],
                #                                              param_code=monitor_data[
                #                                                  'ParamCode'])
                # except ObjectDoesNotExist:
                abnormal_data = AbnormalData(mn=t_station,
                                             data_time=monitor_data[
                                                 'DataTime'],
                                             data_type=monitor_data[
                                                 'DataType'],
                                             param_code=monitor_data[
                                                 'ParamCode'],
                                             original_value=monitor_data[
                                                 'dValue'])
                    #先不保存
                    #abnormal_data.save()

                #不能用abnormal_data_created来进行判断，因为如果之前已经查询过一次，第二次之后不会再生成数据
                if abnormal_data:
                    abnormal_data_list.append(abnormal_data)

    return abnormal_data_list


def count_abnormal_data(mn, start_date_string, end_date_string, param_name, data_type, table_type,
                        old_standard_info=None,
                        predict=False):
    """
    统计指定监控点位mn从start_date至end_date，指定监控因子param_name，
    和数据类型data_type（ZsAvg）的超标数

    predict: 是否根据不正常数据所占的比例，统计出在计划的天数内，在线数据的总数，达标数据数
    """
    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    monitor_data_dict = monitor_value.get_range_monitor_value(mn, start_date_object, end_date_object,
                                                              param_name, data_type, table_type)

    monitor_data_num_dict = {}
    abnormal_data_num = 0
    #生成COD_Avg，pH_Cou 之类的key名
    key = param_name + '_' + data_type

    standard = standard_func.get_station_standard(mn, param_name)

    #如果设置了旧标准
    if old_standard_info:
        #旧标准改为新标准的时间
        standard_change_date = datetime.datetime.strptime(old_standard_info['old_standard']['standard_change_date'],
                                                          "%Y%m%d")

    #构造一个key名，类似COD_Avg_num，并赋值
    total_num = len(monitor_data_dict)
    for monitor_data in monitor_data_dict:
        #如果当前的自动监控数据的时间早于“旧标准改为新标准的时间”，则使用旧标准
        if old_standard_info and monitor_data['DataTime'].replace(tzinfo=None) < standard_change_date:
            standard = {}
            standard['standard_max'] = old_standard_info['old_standard'][param_name]['standard_max']
            standard['standard_min'] = old_standard_info['old_standard'][param_name]['standard_min']

        if standard:
            if (is_abnormal_by_standard(monitor_data['dValue'], standard['standard_max'],
                                            standard['standard_min'])):
                abnormal_data_num = abnormal_data_num + 1
        else:
            abnormal_data_num = False


    #如果设置了需要预测未到来的天数内的自动监控数和有效数据个数：
    now = datetime.datetime.now()
    if predict and end_date_object < now:
        #计划统计的天数
        plan_count_days = (end_date_object - start_date_object).days
        #根据不正常数据所占的比例，统计出在计划的天数内，不正常数据的个数
        abnormal_data_num = plan_count_days * int(abnormal_data_num / total_num)

    monitor_data_num_dict[key + '_total_num'] = total_num
    monitor_data_num_dict[key + '_abnormal_num'] = abnormal_data_num
    monitor_data_num_dict[key + '_valid_num'] = total_num - abnormal_data_num

    return monitor_data_num_dict


















