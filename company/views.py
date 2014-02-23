from django.shortcuts import render, render_to_response
from function.db import SqlServerDB
import pyodbc
from company.function.convert import *

# Create your views here.
def test_db(request):
#     db = SqlServerDB(host='127.0.0.1', port='1433', user='sa', password='the305', db='EnvMonitor', charset="utf8")
#     sql = '''
# CREATE TABLE Company(
#     company_id    int             IDENTITY(1,1),
#     Name          nvarchar(50)    NOT NULL,
#     Tel           varchar(12)     NULL,
#     OrganCode     varchar(20)     NULL,
#     Fax           varchar(12)     NULL,
#     Postcode      varchar(6)      NULL,
#     LawPerson     nvarchar(10)    NULL,
#     Email         varchar(50)     NULL,
#     SetUpTime     datetime        NULL,
#     LinkMan       nvarchar(10)    NULL,
#     Address       nvarchar(80)    NULL,
# )
# '''
#     resuslt = db.query(sql)
#     rowcount = db.rowcount()

    cnxn = pyodbc.connect(DRIVER='{SQL Native Client}',SERVER='localhost',DATABASE='EnvMonitor',UID='bi',PWD='the305')
    cursor = cnxn.cursor()
    cursor.execute("select company_id from Company")
    row = cursor.fetchall()
    if row:
        print row

    return render_to_response('article_list.html', {'error_message': row})


def get_station_info(request):
    """

    :param request:
    """

    all_t_station = get_station_info_func()
    return render_to_response('article_list.html', {'row': all_t_station })

