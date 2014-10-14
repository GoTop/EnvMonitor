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




    url(r'^get_abnormal_data/(?P<mn>\d{14})/(?P<date_string>\d{8})/$',
        views.get_abnormal_data_view),

    url(r'^count_abnormal_data/(?P<mn>\d{14})/(?P<start_date_string>\d{14})/(?P<end_date_string>\d{14})/$',
        views.count_abnormal_data_view),

    url(r'^count_multi_abnormal_data/(?P<start_date_string>\d{14})/(?P<end_date_string>\d{14})/$',
        views.count_multi_abnormal_data_view),


]