#coding=utf-8
from django.conf.urls import patterns, include, url

from company.views import CompanyList

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
)

urlpatterns += patterns('',
    url(r'^company/$', CompanyList.as_view()),
)