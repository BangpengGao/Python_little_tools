# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-03-23 10:24:19
# @Last Modified by:   Phill
# @Last Modified time: 2019-03-23 10:24:47

import pymysql
import numpy as np

def getSqlConn(host,user,password,db):
    '''
    Parameters
    host:数据库地址
    user:用户名
    password:密码
    db:数据库名称

    return
    conn
    cursor
    '''
    conn= pymysql.connect(host=host,user=user,password=password,db=db)
    cursor = conn.cursor()
    return conn,cursor

def insertToDatabase(conn, cursor, sql):
    '''
    Parameters
    conn
    cursor
    sql:sql语句

    return
    data:sql语句结果，numpy.array格式
    '''
    try:
        res = cursor.execute(sql)
        conn.commit()
        if res > 0:
            print("-----SUCCESS-----")
            return 1
        print("-----Failed-----")
        return 0
    except Exception as e:
        print("-----Failed-----")
        print (e)
        return 0

def getDataUnionSQL(cursor,sql):
    '''
    Parameters
    cursor
    sql:sql语句

    return
    data:sql语句结果，numpy.array格式
    '''
    cursor.execute(sql)
    data=cursor.fetchall()
    return np.array(data)
