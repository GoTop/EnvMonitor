#coding=utf-8
from __future__ import unicode_literals
__author__ = 'GoTop'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
text = '''
"[42S02] [Microsoft][SQL Native Client][SQL Server]\xb6\xd4\xcf\xf3\xc3\xfb  'T_AllStation' \xce\xde\xd0\xa7\xa1\xa3 (208) (SQLExecDirectW)"
'''
text = text.encode('gbk')
print text

# import sys
# reload(sys)
# sys.setdefaultencoding('gb2312')

# str = u'python��Ƶ��ѵ��'
#
# dict2 = {1: 'python��Ƶ��ѵ��', 2: '��ѯ010-68165761 QQ��1465376564'}
# for key in dict2:
#     print dict2[key]

# string = '汉'
# print string
# print len(string)
# print repr(string)
#string = string.decode('utf8').encode('gbk')
# print string
# print len(string)
# print repr(string)
uni = '汉'


print "---------------------------"
print uni
print len(uni)
print repr(uni)
print repr(uni.encode('utf-8'))

#print repr(uni.encode('gbk'))
 
  






