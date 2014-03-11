__author__ = 'GoTop'
from django.db import connections
import time


def daily_report_func(mn_list, date):
    date = time.strptime(date, "%Y-%m-%d 00:00:00")

    for mn in mn_list:
        Day_mn = 'Day' + mn
        param = {'Day_mn': Day_mn,
                 'mn': mn,
                 'date': date,
        }
        cursor = connections['DB_baise'].cursor()
        cursor.execute('''SELECT *
                            FROM %(Day_mn)s
                            WHERE StationID = %(mn)s
                            AND ParamCode = %(param_code)s
                            AND DataType = Cou
                            AND DataTime = %(date)s''',
                       param)
        row = cursor.fetchone()