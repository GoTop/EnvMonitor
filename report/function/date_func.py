from datetime import datetime

__author__ = 'GoTop'

#一下函数暂时未用


#4、将字符串转换成datetime类型
def strtodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)


#5、时间转换成字符串,格式为2008-08-02
def datetostr(date):
    return str(date)[0:10]


#6、两个日期相隔多少天，例：2008-10-03和2008-10-01是相隔两天
def datediff(beginDate, endDate):
    format = "%Y-%m-%d";
    bd = strtodatetime(beginDate, format)
    ed = strtodatetime(endDate, format)
    oneday = datetime.timedelta(days=1)
    count = 0
    while bd != ed:
        ed = ed - oneday
        count += 1
    return count


def getDays(beginDate, endDate):
    format = "%Y-%m-%d";
    bd = strtodatetime(beginDate, format)
    ed = strtodatetime(endDate, format)
    oneday = datetime.timedelta(days=1)
    num = datediff(beginDate, endDate) + 1
    li = []
    for i in range(0, num):
        li.append(datetostr(ed))
        ed = ed - oneday
    return li