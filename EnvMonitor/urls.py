#coding=utf-8
from django.conf.urls import patterns, include, url

from company.views import CompanyList, StationList

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'EnvMonitor.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'company/', include('company.urls')),
                       url(r'report/', include('report.urls')),

                       url(r'testapp/', include('testapp.urls')),

                       url(r'^selectable/', include('selectable.urls')),

)

urlpatterns += patterns('',
                        url(r'^station/$', StationList.as_view()),
)


