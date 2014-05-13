#coding=utf-8
#from __future__ import unicode_literals

__author__ = 'GoTop'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


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


a = {'district': u'\u53f3\u6c5f\u533a',
 'name': u'\u84dd\u661f\u5316\u5de5\u65b0\u6750\u6599\u80a1\u4efd\u6709\u9650\u516c\u53f8\u5e7f\u897f\u5206\u516c\u53f8',
 'organ_code': u'66480398-1',
 'trade': None},

#print a.decode('gbk')
#print uni_prt('utf-8')
#print uni_prt(a, 'utf8')
#dicta = {u'\u4e2d\u6587': u'\u4ec0\u4e48', u'\u54c8\u54c8': u'\u4e1c\u897f'}

#dictb = unicode_to_show(dicta, 'utf8')
#print dicta
#print dictb
print uni_prt(a)








