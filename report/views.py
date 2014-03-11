from django.shortcuts import render
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from report.function.report import *

# Create your views here.
def daily_report_view(request,date):
    date

    mn_list = ['45007760002801']
    daily_report_list = daily_report_func(mn_list, date)
    return render_to_response('daily_report.html', {'daily_report_list': daily_report_list})