# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-03-13 11:02:33
# @Last Modified by:   Phill
# @Last Modified time: 2019-03-14 09:11:09

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

def main():
    userName = "system"
    passWord = "manger"
    dataBaseIp = "192.168.0.185"
    dataBasePort = '1521'
    serviceName = "orcl"
    db,cursor = connectOracle(userName,passWord,dataBaseIp,serviceName,dataBasePort)
    print(selectOracle(cursor,"SELECT * from HELP WHERE 1=1"))

if __name__ == '__main__':
    main()