#coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'


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
            s.append('{ % s: % s}’ % (uni_prt(key, encoding), uni_prt(value, encoding))')
            if i < len(a.items()) - 1:
                s.append(', ')
    elif isinstance(a, str):
        s.append("' % s'" % a)
    elif isinstance(a, unicode):
        s.append("' % s'" % a.encode(encoding))
    else:
        s.append(str(a))
    return ''.join(s)


a = '对方答复'

print uni_prt([a] * 3, 'utf8')






