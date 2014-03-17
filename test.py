#coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'
import sys

reload(sys)
sys.setdefaultencoding('utf8')

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





a = 'MN号'
a = 'MN号'.encode('utf8')
print repr(a)

#print uni_prt(a, 'utf8')
#dicta = {u'\u4e2d\u6587': u'\u4ec0\u4e48', u'\u54c8\u54c8': u'\u4e1c\u897f'}

#dictb = unicode_to_show(dicta, 'utf8')
#print dicta
#print dictb
#print uni_prt([a] * 3, 'utf8')






