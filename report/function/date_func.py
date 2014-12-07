# coding=utf-8
from __future__ import unicode_literals
import datetime

__author__ = 'GoTop'

#以下函数暂时未用


def strtodatetime(datestr, format):
    """
    将字符串转换成datetime类型
    """
    return datetime.datetime.strptime(datestr, format)



def datetostr(date):
    """
    时间转换成字符串,格式为2008-08-02
    """
    return str(date)[0:10]



def datediff(beginDate, endDate):
    """
    两个日期相隔多少天，例：2008-10-03和2008-10-01是相隔两天
    :param beginDate:
    :param endDate:
    """
    format = "%Y-%m-%d"
    bd = strtodatetime(beginDate, format)
    ed = strtodatetime(endDate, format)
    oneday = datetime.timedelta(days=1)
    count = 0

    while bd != ed:
        ed = ed - oneday
        count += 1
    return count


def getDays(beginDate, endDate):
    """
    #获取两个时间段的所有时间,返回list
    :param beginDate:
    :param endDate:
    """
    format = "%Y-%m-%d"
    bd = strtodatetime(beginDate, format)
    ed = strtodatetime(endDate, format)
    oneday = datetime.timedelta(days=1)
    num = datediff(beginDate, endDate) + 1
    li = []
    for i in range(0, num):
        li.append(datetostr(ed))
        ed = ed - oneday
    return li

def time_range_hour(beginDatetime, endDatetime):
    """
    #获取两个时间段的所有时间,返回list
    :param beginDate:
    :param endDate:
    """
    format = "%Y-%m-%d"
    bd = strtodatetime(beginDatetime, format)
    ed = strtodatetime(endDatetime, format)
    oneday = datetime.timedelta(hours=1)
    num = datediff(beginDatetime, endDatetime) + 1
    li = []
    for i in range(0, num):
        li.append(datetostr(ed))
        ed = ed - oneday
    return li

def get_time_range_list(start_datetime_object, stop_datetime_object, step, format=None):
    """
    Write your own generator which works like range and takes a time-object
    (which comes from your DB if I understand you correctly) as start and stop (exclusively)

    http://stackoverflow.com/questions/20832272/adjust-start-and-end-range-for-time-list-in-python
    """
    t = start_datetime_object
    li = []
    while t <= stop_datetime_object:
        #如果设置了format，就返回format后的时间字符串
        #入股偶没有设置，则返回datetime object
        if format:
            li.append(datetime.datetime.strftime(t, format).decode('utf-8'))
        else:
            li.append(t)
        t += step
    return li