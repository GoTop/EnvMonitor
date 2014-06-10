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


a = {u'2012\u5e74\u662f\u5426\u5f00\u5c55\u793e\u4f1a\u5316\u8fd0\u884c\u5e76\u83b7\u5f97\u81ea\u6cbb\u533a\u8d22\u653f\u8865\u52a9': u'\u5426',
  u'2014\u56fd\u63a7\u540d\u5355': '',
  u'MN\u53f7': 45007760008901.0,
  u'\u53bf\u533a': u'\u7530\u4e1c',
  u'\u56fd\u63a7\u6e90\n\u5e74\u4efd': 2011.0,
  u'\u5730\u5e02': u'\u767e\u8272',
  u'\u5907\u6ce8': '',
  u'\u5e8f\u53f7': 30.0,
  u'\u662f\u5426\u4e3a2013\n\u65b0\u589e\u5bf9\u8c61': u'\u662f',
  u'\u662f\u5426\u5b63\u8282\u6027\u751f\u4ea7\u4f01\u4e1a': u'\u5426',
  u'\u662f\u5426\u8054\u7f51': u'\u662f',
  u'\u662f\u5426\u9a8c\u6536': u'\u5426',
  u'\u6c61\u67d3\u6e90\u5355\u4f4d\uff08\u4e1a\u4e3b\uff09': u'\u5e7f\u897f\u7530\u9633\u534e\u7f8e\u7eb8\u4e1a\u6709\u9650\u516c\u53f8',
  u'\u6c61\u67d3\u6e90\u5355\u4f4d\uff08\u4e1a\u4e3b\uff09\u5c5e\u6027': u'A',
  u'\u6cd5\u4eba\u4ee3\u7801': u'79683267-X',
  u'\u76d1\u63a7\u56e0\u5b50': u'SO2\u3001NOx',
  u'\u76d1\u63a7\u8bbe\u5907\u5382\u5bb6': u'\u5e7f\u5dde\u6797\u534e',
  u'\u81ea\u52a8\u76d1\u63a7\u8bbe\u5907\u540d\u79f0': u'\u5e7f\u897f\u7530\u9633\u534e\u7f8e\u7eb8\u4e1a\u6709\u9650\u516c\u53f8\u5e9f\u6c14\u6392\u653e\u53e3\u76d1\u63a7\u8bbe\u5907',
  u'\u8bbe\u5907\u7c7b\u578b': u'B',
  u'\u8fdb\u53e3/\u6392\u653e\u53e3': u'\u6392\u653e\u53e3',
  u'\u9884\u8ba1\u751f\u4ea7\u65f6\u957f\uff08\u5b63\u8282\u6027\u4f01\u4e1a\uff09': 12.0},
#print a.decode('gbk')
#print uni_prt('utf-8')
#print uni_prt(a, 'utf8')
#dicta = {u'\u4e2d\u6587': u'\u4ec0\u4e48', u'\u54c8\u54c8': u'\u4e1c\u897f'}

#dictb = unicode_to_show(dicta, 'utf8')
#print dicta
#print dictb
print uni_prt(a)

s = "u[42000] [Microsoft][SQL Native Client][SQL Server]\xb1\xed 'AbnormalData' \xd6\xd0\xb5\xc4\xc1\xd0 'DataType' \xb5\xc4\xc0\xe0\xd0\xcd\xb2\xbb\xc4\xdc\xd3\xc3\xd7\xf7\xcb\xf7\xd2\xfd\xd6\xd0\xb5\xc4\xbc\xfc\xc1\xd0\xa1\xa3 (1919) (SQLExecDirectW); [42000] [Microsoft][SQL Native Client][SQL Server]\xce\xde\xb7\xa8\xb4\xb4\xbd\xa8\xd4\xbc\xca\xf8\xa1\xa3\xc7\xeb\xb2\xce\xd4\xc4\xc7\xb0\xc3\xe6\xb5\xc4\xb4\xed\xce\xf3\xcf\xfb\xcf\xa2\xa1\xa3 (1750)"

print s.decode('gbk')




