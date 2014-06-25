#coding=utf-8
from django.conf.urls import patterns, include, url

from company.views import CompanyList, StationList

from company.models import Company, Station

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EnvMonitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^company/test', 'company.views.test'),
    url(r'^company/init_database', 'company.views.init_database'),
    url(r'^company/get_station_info', 'company.views.get_station_info'),
    url(r'^company/get_station_from_db_baise_view', 'company.views.get_station_from_DB_baise_view'),
    url(r'^company/standard_info', 'company.views.get_standard'),
    url(r'^report/water_daily_report/(?P<date>\d{8})/$', 'report.views.water_daily_report_view'),
    url(r'^report/gas_daily_report/(?P<date>\d{8})/$', 'report.views.gas_daily_report_view'),
    url(r'^report/(?P<mn>\d{14})/(?P<date>\d{8})/$', 'report.views.company_water_day_report_view'),
    url(r'^report/get_abnormal_data/(?P<mn>\d{14})/(?P<date_string>\d{8})/$', 'report.views.get_abnormal_data_view'),
)

urlpatterns += patterns('',
    url(r'^company/$', CompanyList.as_view()),
)

urlpatterns += patterns('',
    url(r'^station/$', StationList.as_view()),
)


