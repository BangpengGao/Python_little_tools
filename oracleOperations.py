# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-03-13 11:02:33
# @Last Modified by:   Phill
# @Last Modified time: 2019-05-28 10:37:18

import numpy as np
import cx_Oracle as oracle

def connectOracle(userName,passWord,dataBaseIp,serviceName,dataBasePort=None):
    connectStatement = ""
    if userName:
        connectStatement = userName + "/"
    else:
        print("userName is Null!")
        return "userName is Null!"
    if passWord:
        connectStatement += passWord + "@"
    if dataBaseIp:
        connectStatement += dataBaseIp
    else:
        print("dataBaseIp is Null!")
        return "dataBaseIp is Null!"
    if dataBasePort:
        connectStatement += ":" + dataBasePort + "/"
    if serviceName:
        connectStatement += serviceName
    else:
        print("serviceName is Null!")
        return "serviceName is Null!"
    print(connectStatement)
    try:
        db = oracle.connect(connectStatement)
        cursor = db.cursor()
        return (db,cursor)
    except Exception as e:
        print(e)
        return 0

def selectOracle(cursor,sql):
    try:
        cursor.execute(sql)
        return np.array(cursor.fetchall())
    except Exception as e:
        print(e)
        return 0

def updateOrInsertOracle(cursor,sql):
    try:
        cursor.execute(sql)
        cursor.commit()
        return 1
    except Exception as e:
        print(e)
        return 0

def close(db,cursor):
    cursor.commit()
    cursor.close()
    db.close()




