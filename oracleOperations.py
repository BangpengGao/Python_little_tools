# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-03-13 11:02:33
# @Last Modified by:   Phill
# @Last Modified time: 2019-03-13 11:44:14

import numpy as np
import cx_Oracle as oracle

def connectOracle(userName,passWord,dataBaseIp,dataBasePort=None,dataBaseName):
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
    if dataBaseName:
        connectStatement += dataBaseName
    else:
        print("dataBaseName is Null!")
        return "dataBaseName is Null!"
    try:
        db = oracle.connect(connectStatement)
    except Exception as e:
        print(e)
        return e
    cursor = db.cursor()
    return (db,cursor)

def selectOracle(cursor,sql):
    try:
        cursor.execute(sql)
        return np.array(cursor.fetchall())
    except Exception as e:
        print(e)
        return e

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