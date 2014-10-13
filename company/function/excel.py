# coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'

import xlrd
from xlwt import Workbook


def excel_table_by_index(file_path='file.xls', by_index=0, colname_row=0, data_start_row=1):
    """
    根据索引获取Excel表格中的数据
    参数:file：Excel文件路径
        colname_row：表头列名所在行的索引
        by_index：表的索引
        data_start_row: 数据开始的列
    """
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[by_index]
    nrows = table.nrows  #行数
    ncols = table.ncols  #列数
    col_names = table.row_values(colname_row)  #标题所在的列，从0开始计算
    list = []
    for row_num in range(data_start_row, nrows):
        row = table.row_values(row_num)
        if row:
            app = {}
            for i in range(len(col_names)):
                app[col_names[i]] = row[i]
            list.append(app)
    return list