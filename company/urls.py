# coding=utf-8
from django.conf.urls import patterns, url
from . import views


urlpatterns = [

    url(r'^test', views.test),

    #初始化数据库
    url(r'^init_database', views.init_database),

    url(r'^get_station_info', views.get_station_info),

    url(r'^get_station_from_db_baise_view', views.get_station_from_DB_baise_view),

    url(r'^standard_info', views.get_standard),

]

urlpatterns += patterns('',
    url(r'^$', views.CompanyList.as_view()),
)