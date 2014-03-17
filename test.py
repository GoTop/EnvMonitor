#coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def uni_prt(a, encoding=None):
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


a = {'对方答复': 111}

dict_result =  [u'\u5e8f\u53f7', u'\u5730\u5e02', u'\u53bf\u533a', u'\u81ea\u52a8\u76d1\u63a7\u8bbe\u5907\u540d\u79f0', u'\u8fdb\u53e3/\u6392\u653e\u53e3', u'\u8bbe\u5907\u7c7b\u578b', u'\u662f\u5426\u8054\u7f51', u'\u662f\u5426\u9a8c\u6536', u'MN\u53f7', u'\u6c61\u67d3\u6e90\u5355\u4f4d\uff08\u4e1a\u4e3b\uff09', u'\u6cd5\u4eba\u4ee3\u7801', u'\u6c61\u67d3\u6e90\u5355\u4f4d\uff08\u4e1a\u4e3b\uff09\u5c5e\u6027', u'\u76d1\u63a7\u56e0\u5b50', u'\u76d1\u63a7\u8bbe\u5907\u5382\u5bb6', u'\u662f\u5426\u5b63\u8282\u6027\u751f\u4ea7\u4f01\u4e1a', u'\u9884\u8ba1\u751f\u4ea7\u65f6\u957f\uff08\u5b63\u8282\u6027\u4f01\u4e1a\uff09', u'2012\u5e74\u662f\u5426\u5f00\u5c55\u793e\u4f1a\u5316\u8fd0\u884c\u5e76\u83b7\u5f97\u81ea\u6cbb\u533a\u8d22\u653f\u8865\u52a9', u'\u662f\u5426\u4e3a2013\u65b0\u589e\u5bf9\u8c61', u'\u56fd\u63a7\u6e90\u5e74\u4efd']
print uni_prt(dict_result, 'utf8')






