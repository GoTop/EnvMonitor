__author__ = 'GoTop'
from django.db import connections
import time

#
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def daily_report_func(mn_list, date):
    timeArray = time.strptime(date, "%Y%m%d")
    date = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)

    for mn in mn_list:
        table_name = 'Day_' + mn
        param = (table_name, mn, 'Z02', date,)
        cursor = connections['DB_baise'].cursor()

        query = '''SELECT * FROM %s
                    WHERE StationID = '%s'
                    AND
                    ParamCode = '%s'
                    AND
                    DataType = 'Cou'
                    AND
                    DataTime = '%s' ''' % param

        cursor.execute(query)
        dict = dictfetchall(cursor)
        #row = cursor.fetchall()
        return dict