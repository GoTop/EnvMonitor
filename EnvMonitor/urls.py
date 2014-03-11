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
    url(r'^company/test_db', 'company.views.test_db'),
    url(r'^company/get_station_info', 'company.views.get_station_info'),
    url(r'^company/standard_info', 'company.views.get_standard'),
    url(r'^report/daily_report/(?P<date>\d{8})/$', 'report.views.daily_report_view'),
)

urlpatterns += patterns('',
    url(r'^company/$', CompanyList.as_view()),
)

urlpatterns += patterns('',
    url(r'^station/$', StationList.as_view()),
)


