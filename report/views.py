# coding=utf-8
from __future__ import unicode_literals

import datetime

from django.shortcuts import render_to_response

from company.function.standard import get_station_standard
from company.models import T_All_station, Station
from report.function import date_func
from report.function import monitor_value
from report.function.date_func import get_time_range_list
from report.function.monitor_value import get_range_monitor_value
import report.function.report_func as report_func
import report.function.abnormal_func as abnormal_func



# Create your views here.
from report.function.utility import merge


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

        daily_report_row = report_func.get_daily_report_func(mn, date, table_type='day')

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
                               'table_type': '小时',
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


def count_multi_abnormal_data_view(request, start_date_string, end_date_string, table_type):
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

        # 单个监控点位的统计数据
        report_list = []
        for param_name in param_name_list:
            abnormal_data_dict = abnormal_func.count_abnormal_data(mn, start_date_string,
                                                                   end_date_string,
                                                                   param_name,
                                                                   data_type,
                                                                   table_type)

            report_dict = {'station_name': t_station.name,
                           'param_name': param_name,
                           'abnormal_data_dict': abnormal_data_dict,
                           'mn': mn}
            report_list.append(report_dict)

            # monitor_data_num_dict["station_name"] = t_station.name
            # monitor_data_num_dict_list.append(monitor_data_num_dict)
        # 多个监控点位的统计数据
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


def station_data_view(request, mn, start_date_string, end_date_string, table_type):
    """
    获取mn监控点位从start_date_string, end_date_string的table_type表（日数据或者小时数据）中的监控数据
    :param request:
    :param mn:
    :param start_date_string:
    :param end_date_string:
    :param table_type:
    """
    multi_report_list = []
    monitor_data_num_dict = {}
    t_station = Station.objects.get(station_id=mn)

    # param_name的定义在get_param_code(param_name)函数中查看
    if t_station.type == '废水':
        param_name_list = ['CODcr', 'NH']
        data_type_list = ['Avg', 'Cou']
        volume_param_name = 'volume_of_water'
        volume_data_type = 'Cou'
    elif t_station.type == '废气':
        param_name_list = ['SO2', 'NOx']
        data_type_list = ['ZsAvg', 'Cou']
        volume_param_name = 'volume_of_gas'
        volume_data_type = 'Cou'


    # 单个监控点位的统计数据
    report_list = []

    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    step = datetime.timedelta(hours=24)
    time_range_list = date_func.get_time_range_list(start_date_object, end_date_object, step, format='%Y%m%d%H%M%S')

    # 如果使用 report_table = report_table.fromkeys(time_range_list, {})
    # 会导致每一个report_table的item的值均指向使用相同存储空间，导致对任意一个item的赋值，就是对所有item赋值的
    report_table = {k: {} for k in time_range_list}

    # 获取监控因子数据
    for param_name in param_name_list:
        for data_type in data_type_list:
            # todo 2014-12-1 改用每次获取一个监控因子监控数据，组合为报表中一行数据的方法
            monitor_data_list = monitor_value.get_range_monitor_value(mn, start_date_object, end_date_object,
                                                                      param_name, data_type, table_type)

            key = param_name + '_' + data_type

            report_row = {}
            for time in time_range_list:

                report_single_param = {key: '-'}
                report_row.update(report_single_param)
                report_table[time].update(report_row)

                for monitor_data in monitor_data_list:
                    monitor_data_datetime = monitor_data['DataTime'].strftime("%Y%m%d%H%M%S")
                    if time == monitor_data_datetime:
                        report_single_param = {key: monitor_data['dValue']}
                        report_row.update(report_single_param)
                        report_table[time].update(report_row)
                        break

    monitor_data_list = monitor_value.get_range_monitor_value(mn, start_date_object, end_date_object,
                                                              volume_param_name, volume_data_type, table_type)

    interval_second = 3600 * 24

    start_date_object = datetime.datetime.strptime(start_date_string, "%Y%m%d%H%M%S")
    end_date_object = datetime.datetime.strptime(end_date_string, "%Y%m%d%H%M%S")

    # 获取流量数据
    volume_data_table = get_format_monitor_data(mn, volume_param_name, volume_data_type, table_type,
                                                start_date_object, end_date_object, interval_second)

    report_table = merge(report_table, volume_data_table)
    report_table1 = sorted(report_table.items(), key=lambda x: x[0])

    standard = {}
    for param_name in param_name_list:
        standard.update({param_name: get_station_standard(mn, param_name)})

    if table_type == 'hour':
        type = '小时'
    elif table_type == 'day':
        type = '日'
    return render_to_response('station_data_report.html',
                              {'station_name': t_station.name,
                               'start_date_object': start_date_object,
                               'end_date_object': end_date_object,
                               'start_date_string': start_date_string,
                               'end_date_string': end_date_string,
                               'type': type,
                               'report_table': report_table1,
                               'standard': standard}
    )


def get_format_monitor_data(mn, param_name, data_type, table_type, start_date_object, end_date_object,
                            interval_second):
    """
    将获取数据库中一个时间段指定监控因子，指定数据类型的监控数据做成一个函数
    :param mn:
    :param param_name:
    :param data_type:
    :param table_type:
    :param start_date_object:
    :param end_date_object:
    :param interval_second:
    :return:
    """
    step = datetime.timedelta(seconds=interval_second)
    time_range_list = date_func.get_time_range_list(start_date_object, end_date_object, step, format='%Y%m%d%H%M%S')

    # 如果使用 report_table = report_table.fromkeys(time_range_list, {})
    # 会导致每一个report_table的item的值均指向使用相同存储空间，导致对任意一个item的赋值，就是对所有item赋值的
    report_table = {k: {} for k in time_range_list}

    # 获取监控因子数据
    # todo 2014-12-1 改用每次获取一个监控因子监控数据，组合为报表中一行数据的方法
    monitor_data_list = monitor_value.get_range_monitor_value(mn, start_date_object, end_date_object,
                                                              param_name, data_type, table_type)

    key = param_name + '_' + data_type

    report_row = {}
    for time in time_range_list:

        report_single_param = {key: '-'}
        report_row.update(report_single_param)
        report_table[time].update(report_row)

        for monitor_data in monitor_data_list:
            monitor_data_datetime = monitor_data['DataTime'].strftime("%Y%m%d%H%M%S")
            if time == monitor_data_datetime:
                report_single_param = {key: monitor_data['dValue']}
                report_row.update(report_single_param)
                report_table[time].update(report_row)
                break
    return report_table

