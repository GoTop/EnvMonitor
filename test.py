__author__ = 'GoTop'

code_list = ('ascii',
             'big5',
             'big5hkscs',
             'cp037',
             'cp424',
             'cp437',
             'cp500',
             'cp720',
             'cp737',
             'cp775',
             'cp850',
             'cp852',
             'cp855',
             'cp856',
             'cp857',
             'cp858',
             'cp860',
             'cp861',
             'cp862',
             'cp863',
             'cp864',
             'cp865',
             'cp866',
             'cp869',
             'cp874',
             'cp875',
             'cp932',
             'cp949',
             'cp950',
             'cp1006',
             'cp1026',
             'cp1140',
             'cp1250',
             'cp1251',
             'cp1252',
             'cp1253',
             'cp1254',
             'cp1255',
             'cp1256',
             'cp1257',
             'cp1258',
             'euc_jp',
             'euc_jis_2004',
             'euc_jisx0213',
             'euc_kr',
             'gb2312',
             'gbk',
             'gb18030',
             'hz',
             'iso2022_jp',
             'iso2022_jp_1',
             'iso2022_jp_2',
             'iso2022_jp_2004',
             'iso2022_jp_3',
             'iso2022_jp_ext',
             'iso2022_kr',
             'latin_1',
             'iso8859_2',
             'iso8859_3',
             'iso8859_4',
             'iso8859_5',
             'iso8859_6',
             'iso8859_7',
             'iso8859_8',
             'iso8859_9',
             'iso8859_10',
             'iso8859_13',
             'iso8859_14',
             'iso8859_15',
             'iso8859_16',
             'johab',
             'koi8_r',
             'koi8_u',
             'mac_cyrillic',
             'mac_greek',
             'mac_iceland',
             'mac_latin2',
             'mac_roman',
             'mac_turkish',
             'ptcp154',
             'shift_jis',
             'shift_jis_2004',
             'shift_jisx0213',
             'utf_32',
             'utf_32_be',
             'utf_32_le',
             'utf_16',
             'utf_16_be',
             'utf_16_le',
             'utf_7',
             'utf_8',
             'utf_8_sig',
)

# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf_8')
#text = '''[23000] [Microsoft][SQL Native Client][SQL Server]\xb2\xbb\xc4\xdc\xbd\xab\xd6\xb5 NULL \xb2\xe5\xc8\xeb\xc1\xd0 'company_id'\xa3\xac\xb1\xed 'EnvMonitor.dbo.Station'\xa3\xbb\xc1\xd0\xb2\xbb\xd4\xca\xd0\xed\xd3\xd0\xbf\xd5\xd6\xb5\xa1\xa3INSERT \xca\xa7\xb0\xdc\xa1\xa3 (515) (SQLExecDirectW); [01000] [Microsoft][SQL Native Client][SQL Server]\xd3\xef\xbe\xe4\xd2\xd1\xd6\xd5\xd6\xb9\xa1\xa3 (3621)'''

text = '\xb2\xbb\xc4\xdc\xbd\xab\xd6\xb5'
#text.decode('utf_8')
print text

for code in code_list:
    for code_2 in code_list:
        try:
            text.decode(code).encode(code_2)
            print text
        except Exception, data:
            print Exception, ":", data  # for b in a:
#     print b




