# -*- coding: utf-8 -*-
__author__ = 'GoTop'
__date__ = '2013-09-04 10:51:00'

import sys
import pyodbc
import datetime

class SqlServerDB:

    def __init__(self,host,port,user,password,db,charset="utf8"):
        '''
        初妈化数据库连接
        '''
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.charset = charset

        try:
            str_conn = 'DRIVER={SQL Server};SERVER=' + self.host + ';PORT='+ self.port + ';DATABASE=' + self.db + ';UID=' + self.user + ';PWD=' + self.password + ''
            self.conn = pyodbc.connect(str_conn,unicode_results=True)
            self.cur = self.conn.cursor()
        except:
            print("SqlServer Connect Error")
            sys.exit()

    def query(self,sql):
        '''
        执行SQL语句
        '''
        try:
            n = self.cur.execute(sql)
            return n
        except:
            print("Mysql Query Error")
            sys.exit()

    def queryRow(self,sql):
        '''
        根据SQL执行，返回单行字典
        @return disct
        '''
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def queryAll(self,sql):
        '''
        根据SQL执行获取，返回列表
        @return list
        '''
        result = self.cur.execute(sql)
        desc = self.cur.description
        d = []
        for row in result:
            _d = {}
            for i in range(0,len(row)):
                _d[desc[i][0]] = row[i]
                d.append(_d)
        return d

    def insert(self,table_name,data):
        '''
        插入数据库
        @param table_name string 数据表名称
        @param data list 数据列表
        '''
        for key in data:
            data[key] = "'"+str(data[key])+"'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"

        return self.cur.query(real_sql)


    def getLastInsertId(self):
        '''
        获取最后插入的ID
        @return int
        '''
        return self.cur.lastrowid

    def rowcount(self):
        '''
        获取行数
        '''
        return self.cur.rowcount

    def commit(self):
        '''
        提交
        '''
        self.conn.commit()

    def close(self):
        '''
        关闭数据库连接句柄
        '''
        self.cur.close()
        self.conn.close()
