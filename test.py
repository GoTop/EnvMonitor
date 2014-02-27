#coding=gbk
__author__ = 'GoTop'


# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf_8')
text = '''
('23000', "[23000] [Microsoft][SQL Native Client][SQL Server]\xce\xa5\xb7\xb4\xc1\xcb PRIMARY KEY \xd4\xbc\xca\xf8 'PK__Station__30F848ED'\xa1\xa3\xb2\xbb\xc4\xdc\xd4\xda\xb6\xd4\xcf\xf3 'dbo.Station' \xd6\xd0\xb2\xe5\xc8\xeb\xd6\xd8\xb8\xb4\xbc\xfc\xa1\xa3 (2627) (SQLExecDirectW); [01000] [Microsoft][SQL Native Client][SQL Server]\xd3\xef\xbe\xe4\xd2\xd1\xd6\xd5\xd6\xb9\xa1\xa3 (3621)")
'''

#text = '\xb2\xbb\xc4\xdc\xbd\xab\xd6\xb5'
text = text.decode('gb2312')
#print text

# import sys
# reload(sys)
# sys.setdefaultencoding('gb2312')

# str = u'python视频培训班'
#
# dict2 = {1: 'python视频培训班', 2: '咨询010-68165761 QQ：1465376564'}
# for key in dict2:
#     print dict2[key]

string = '汉'
print string
print len(string)
print repr(string)
#string = string.decode('utf8').encode('gbk')
# print string
# print len(string)
# print repr(string)


uni = u'汉'
print uni
print len(uni)
print repr(uni)
print repr(uni.encode('gbk'))

print uni.encode('gbk')






