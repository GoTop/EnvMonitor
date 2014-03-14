# coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

import xlrd
from xlwt import Workbook


def excel_table_by_index(file='file.xls', colname_index=0, by_index=0):
    """
    根据索引获取Excel表格中的数据
    参数:file：Excel文件路径
        colname_index：表头列名所在行的索引
        by_index：表的索引
    """
    data = xlrd.open_workbook(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  #行数
    ncols = table.ncols  #列数
    col_names = table.row_values(colname_index)  #某一行数据
    list = []
    for row_num in range(1, nrows):

        row = table.row_values(row_num)
        if row:
            app = {}
            for i in range(len(col_names)):
                app[col_names[i]] = row[i]
            list.append(app)
    return list