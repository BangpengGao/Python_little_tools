# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-03-13 10:26:03
# @Last Modified by:   Phill
# @Last Modified time: 2019-03-13 10:46:39

import numpy as np
import pandas as pd

def readExcel(fileName,sheetName=None,indexs=None,headers=None):
    """
    Parameters:
    fileName
    sheetName
    indexs
    headers

    return:
    array format data
    """
    data = pd.read_excel(fileName,sheetName=sheetName,index=indexs,header=headers)
    return np.array(data)

def writeToExcel(data,fileName,indexs=None,headers=None):
    """
    Parameters:
    fileName
    sheetName
    indexs
    headers

    return
    None
    """
    data = pd.DataFrame(data)
    data.to_excel(fileName,index=indexs,header=headers)

def dictToList(data):
    """
    Parameter:
    data: dict

    return:
    list format data
    """
    res = []
    for key in data:
        if type(data[key]).__name__ == "list":
            da = data[key]
            da.insert(key)
            res.append(da)
            continue
        res.append([key,data[key]])
    return res

def readTxt(fileName,splitSymbol):
    """
    Parameters:
    fileName: file path and file name
    splitSymbol: split symbol

    return:
    list format data
    """
    res = []
    with open(fileName) as f:
        for line in f:
            lineData = line.split("\n")[0].split(splitSymbol)
            res.append(lineData)
    return res

def writeToTxt(fileName,data,splitSymbol,mode):
    """
    Parameters:
    fileName: file path and file name
    data: write data
    splitSymbol: split symbol
    mode: write mode, w is init and write, w+ is add
    """
    with open(fileName,mode) as f:
        for di in range(data):
            for i in range(len(di)-1):
                f.write(str(di[i]) + splitSymbol)
            f.write(str(di[-1]) + "\n")

