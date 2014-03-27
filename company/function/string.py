# coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

#TODO 未完成
def unicode_to_show(object, encoding=None):
    '''
    将各种类型的数据中的unicode编码转换成正确的编码格式来显示
    '''
    import sys

    if not encoding:
        encoding = sys.getdefaultencoding()

    elif isinstance(object, list):
        result = []
        for i, k in enumerate(object):
            value = convert_to_unicode(k, encoding)
            result.append(value)
    elif isinstance(object, tuple):
        result = None
        object_list = list(object)
        object_list_uni = convert_to_unicode(object_list, encoding)
        result = tuple(object_list_uni)
    elif isinstance(object, dict):
        result = {}
        for i, k in enumerate(object.items()):
            key, value = k
            key = convert_to_unicode(key, encoding)
            value = convert_to_unicode(value, encoding)
            result[key] = value

    elif isinstance(object, str):
        result = object

    elif isinstance(object, unicode):
        result = object.encode(encoding)

    return result

def uni_prt(a, encoding=None):
    '''
    查看unicode格式的数据
    '''
    import sys

    s = []
    if not encoding:
        encoding = sys.getdefaultencoding()
    if isinstance(a, (list, tuple)):
        if isinstance(a, list):
            s.append('[')
        else:
            s.append('(')
        for i, k in enumerate(a):
            s.append(uni_prt(k, encoding))
            if i < len(a) - 1:
                s.append(', ')

        if isinstance(a, list):
            s.append(']')
        else:
            s.append(')')
    elif isinstance(a, dict):
        for i, k in enumerate(a.items()):
            key, value = k
            s.append('{%s: %s}' % (uni_prt(key, encoding), uni_prt(value, encoding)))
            if i < len(a.items()) - 1:
                s.append(', ')
    elif isinstance(a, str):
        s.append("' %s'" % a)
    elif isinstance(a, unicode):
        s.append("' %s'" % a.encode(encoding))
    else:
        s.append(str(a))
    return ''.join(s)



def sort_station_by_district(station):
    '''
    使用sorted()对station进行自定义排序时，自定义排序顺序
    '''
    district = station.t_admin_area.area_name
    sort_order = None
    if district == '右江区':
        sort_order = 1
    elif district == '田阳县':
        sort_order = 2
    elif district == '田东县':
        sort_order = 3
    elif district == '平果县':
        sort_order = 4
    elif district == '德保县':
        sort_order = 5
    elif district == '靖西县':
        sort_order = 6
    elif district == '那坡县':
        sort_order = 7
    elif district == '凌云县':
        sort_order = 8
    elif district == '乐业县':
        sort_order = 9
    elif district == '田林县':
        sort_order = 10
    elif district == '隆林县':
        sort_order = 11
    elif district == '西林县':
        sort_order = 12
    return sort_order

def sort_company_by_district(company):
    '''
    使用sorted()对company进行自定义排序时，自定义排序顺序
    '''
    district = company.district
    sort_order = None
    if district == '右江区':
        sort_order = 1
    elif district == '田阳':
        sort_order = 2
    elif district == '田东':
        sort_order = 3
    elif district == '平果':
        sort_order = 4
    elif district == '德保':
        sort_order = 5
    elif district == '靖西':
        sort_order = 6
    elif district == '那坡':
        sort_order = 7
    elif district == '凌云':
        sort_order = 8
    elif district == '乐业':
        sort_order = 9
    elif district == '田林':
        sort_order = 10
    elif district == '隆林':
        sort_order = 11
    elif district == '西林':
        sort_order = 12
    return sort_order

