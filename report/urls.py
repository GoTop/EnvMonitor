# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [

    #所有废水排放企业的date日报表
    url(r'^water_daily_report/(?P<date>\d{8})/$', views.water_daily_report_view),

    #所有废气排放企业的date日报表
    url(r'^gas_daily_report/(?P<date>\d{8})/$', views.gas_daily_report_view),

    #废水监控点位的date日报表
    url(r'^(?P<mn>\d{14})/(?P<date>\d{8})/$', views.company_water_day_report_view, name='station_day_report_url'),

    #监控点位的某一段时间内的报表报表（可以通过table_type设置显示显示小时数据还是日数据）
    # http://127.0.0.1:8000/report/station_data/day/45007760002007/20140101000000/20140131000000
    url(r'^station_data/(?P<table_type>(day|hour))/(?P<mn>\d{14})/(?P<start_date_string>\d{14})/(?P<end_date_string>\d{14})/$',
        views.station_data_view, name='station_data_url'),


    #获取某一时间段内，超标的具体时间和数值
    # http://127.0.0.1:8000/report/get_abnormal_data/45007760002007/20140302000000/20140302230000/
    url(r'^get_abnormal_data/(?P<mn>\d{14})/(?P<start_date_string>\d{14})/(?P<end_date_string>\d{14})/$',
        views.get_abnormal_data_view, name='get_abnormal_data'),

    #统计指定监控点位mn从start_date至end_date，指定监控因子列表中的param_name_list，
    #和数据类型data_type（ZsAvg）的超标数
    url(r'^count_abnormal_data/(?P<mn>\d{14})/(?P<start_date_string>\d{14})/(?P<end_date_string>\d{14})/$',
        views.count_abnormal_data_view, name='count_abnormal_data'),

    #统计指定监控点位mn_list从start_date至end_date，指定监控因子列表中的param_name_list，
    #和数据类型data_type（ZsAvg）的超标数
    # 127.0.0.1:8000/report/count_multi_abnormal_data/day/20140201000000/20140301000000/
    url(
        r'^count_multi_abnormal_data/(?P<start_date_string>\d{14})/(?P<end_date_string>\d{14})/(?P<table_type>(day|hour))$',
        views.count_multi_abnormal_data_view),
]