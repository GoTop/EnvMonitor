# coding=utf-8
from django.conf.urls import url, include
from . import views


urlpatterns = [

    #所有废水排放企业的date日报表
    url(r'^selectable_form/$', views.selectable_form),
    url(r'^smart_selects_form/$', views.smart_selects_form),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^selectable/', include('selectable.urls')),
]