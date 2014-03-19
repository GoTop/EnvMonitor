#coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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





a = str("[23000] [Microsoft][SQL Native Client][SQL Server]\xce\xa5\xb7\xb4\xc1\xcb UNIQUE KEY \xd4\xbc\xca\xf8 'UQ__Company__52D92AFC'\xa1\xa3\xb2\xbb\xc4\xdc\xd4\xda\xb6\xd4\xcf\xf3 'dbo.Company' \xd6\xd0\xb2\xe5\xc8\xeb\xd6\xd8\xb8\xb4\xbc\xfc\xa1\xa3 (2627) (SQLExecDirectW); [01000] [Microsoft][SQL Native Client][SQL Server]\xd3\xef\xbe\xe4\xd2\xd1\xd6\xd5\xd6\xb9\xa1\xa3 (3621)")


print a.decode('gbk')
print a.decode('utf-8')
#print uni_prt(a, 'utf8')
#dicta = {u'\u4e2d\u6587': u'\u4ec0\u4e48', u'\u54c8\u54c8': u'\u4e1c\u897f'}

#dictb = unicode_to_show(dicta, 'utf8')
#print dicta
#print dictb
print uni_prt(a, 'utf8')






