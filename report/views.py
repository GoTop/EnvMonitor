# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from company.function.standard import get_station_standard
from company.models import T_All_station, Station
import report.function.report_func as report_func
import report.function.abnormal_func as abnormal_func

import datetime

# Create your views here.
def water_daily_report_view(request, date):
    """
    所有废水排放点位的当天日数据报表

    """

    mn_list = ['45007760002801', '45007760003001']

    # strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")
    daily_report_list = []
    for mn in mn_list:
        # daily_report_value = {}
        # daily_report_value = get_water_data_func(mn, date, type='day')
        #
        # t_station = T_All_station.objects.using('DB_baise').get(pk=mn)
        # daily_report_value['station_name'] = t_station.station_name

        daily_report_row = report_func.get_daily_report_func(mn, date, type='day')

        daily_report_list.append(daily_report_row)
    return render_to_response('water_daily_report.html',
                              {'datetime': datetime_object,
                               'type': '日',
                               'daily_report_list': daily_report_list})


def gas_daily_report_view(request, date):
    '''
    所有废气排放点位的当天日数据报表
    '''
    mn_list = ['45007760002007', '45007760002601']

    # strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")
    daily_report_list = []
    for mn in mn_list:
        # daily_report_value = {}
        # daily_report_value = get_gas_data_func(mn, date, type='day')
        #
        # t_station = T_All_station.objects.using('DB_baise').get(pk=mn)
        # daily_report_value['station_name'] = t_station.station_name

        daily_report_row = report_func.get_daily_report_func(mn, date, type='day')

        daily_report_list.append(daily_report_row)
    return render_to_response('gas_daily_report.html',
                              {'datetime': datetime_object,
                               'type': '日',
                               'daily_report_list': daily_report_list})


# TODO
def company_water_day_report_view(request, mn, date):
    """
    获取监控点位mn在date当天24小时的小时数据，显示日报表
    """
    # strptime将格式字符串转换为datetime对象
    datetime_object = datetime.datetime.strptime(date, "%Y%m%d")
    report_list = []

    t_station = T_All_station.objects.using('DB_baise').get(pk=mn)

    report_list = report_func.get_water_hour_data_report_func(mn, date)

    return render_to_response('water_day_report.html',
                              {'station_name': t_station.station_name,
                               'datetime': datetime_object,
                               'type': '小时',
                               'report_list': report_list}
    )


def get_abnormal_data_view(request, mn, start_date_string, end_date_string):
    """
    获取指定mn的监控点位在start_date_string, end_date_string之间的异常在线监控数据
    :param request:
    :param mn:
    :param start_date_string:类似20140101000000
    :param end_date_string:
    :return:
    """
    # 根据监控点位的类型选择监控因子
    t_station = Station.objects.get(station_id=mn)
    if t_station.type == '废水':
        param_name_list = ['CODcr', 'NH']
        data_type = 'Avg'
    elif t_station.type == '废气':
        param_name_list = ['SO2', 'NOx']
        data_type = 'ZsAvg'

    report_list = []
    for param_name in param_name_list:
        abnormal_data_list = abnormal_func.get_abnormal_data(mn, start_date_string,
                                                             end_date_string,
                                                             param_name,
                                                             data_type)
        standard = get_station_standard(mn, param_name)
        if standard:
            standard_text = standard['text']
        else:
            standard_text = '-'

        report_dict = {'param_name': param_name,
                       'abnormal_data_list': abnormal_data_list,
                       'standard_text': standard_text}
        report_list.append(report_dict)

    # strptime将格式字符串转换为datetime对象
    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    return render_to_response('get_abmornal_date_result.html',
                              {'station_name': t_station.name,
                               'start_datetime': start_date_object,
                               'end_datetime': end_date_object,
                               'type': '小时',
                               'report_list': report_list}
    )


def count_abnormal_data_view(request, mn, start_date_string, end_date_string):
    """
    统计指定监控点位mn从start_date至end_date，指定监控因子列表中的param_name_list，
    和数据类型data_type（ZsAvg）的超标数
    """
    t_station = Station.objects.get(station_id=mn)
    if t_station.type == '废水':
        param_name_list = ['CODcr', 'NH']
        data_type = 'Avg'
    elif t_station.type == '废气':
        param_name_list = ['SO2', 'NOx']
        data_type = 'ZsAvg'

    for param_name in param_name_list:
        monitor_data_num_dict = abnormal_func.count_abnormal_data(mn, start_date_string,
                                                                  end_date_string,
                                                                  param_name,
                                                                  data_type)

        start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
        end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    return render_to_response('count_abnormal_data.html',
                              {'mn': mn,
                               'station_name': t_station.name,
                               'start_date_object': start_date_object,
                               'end_date_object': end_date_object,
                               'start_date_string': start_date_string,
                               'end_date_string': end_date_string,
                               'type': '小时',
                               'monitor_data_num_dict': monitor_data_num_dict}
    )


def count_multi_abnormal_data_view(request, start_date_string, end_date_string):
    """
    统计指定监控点位mn_list从start_date至end_date，指定监控因子列表中的param_name_list，
    和数据类型data_type（ZsAvg）的超标数
    """

    mn_list = ['45007760002801', '45007760003001', '45007760002007']

    multi_report_list = []

    for mn in mn_list:
        monitor_data_num_dict = {}
        t_station = Station.objects.get(station_id=mn)

        if t_station.type == '废水':
            param_name_list = ['CODcr', 'NH']
            data_type = 'Avg'
        elif t_station.type == '废气':
            param_name_list = ['SO2', 'NOx']
            data_type = 'ZsAvg'

        report_list = []
        for param_name in param_name_list:
            abnormal_data_dict = abnormal_func.count_abnormal_data(mn, start_date_string,
                                                                   end_date_string,
                                                                   param_name,
                                                                   data_type)

            report_dict = {'station_name': t_station.name,
                           'param_name': param_name,
                           'abnormal_data_dict': abnormal_data_dict,
                           'mn': mn}
            report_list.append(report_dict)

            # monitor_data_num_dict["station_name"] = t_station.name
            # monitor_data_num_dict_list.append(monitor_data_num_dict)
        multi_report_list.append(report_list)
    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    return render_to_response('count_multi_abnormal_data.html',
                              {'start_date_object': start_date_object,
                               'end_date_object': end_date_object,
                               'start_date_string': start_date_string,
                               'end_date_string': end_date_string,
                               'type': '小时',
                               'multi_report_list': multi_report_list}
    )

