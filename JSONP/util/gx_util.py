# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:01:38 2018

@author: Lidh
"""
import json
import sys
from urllib import parse
from urllib import request
def getData():
    f=request.urlopen(sys.argv[1])
    strs=f.read()
    return json.loads(strs.decode('utf-8'))
def saveData(data):
    datao=parse.urlencode(data).encode('utf-8')
    request0=request.Request(sys.argv[2],datao)
    res=request.urlopen(request0).read().decode('utf-8')
    print(res)
    return res
def calBinaryClassificationAccuracy(pre_y,real_y):
    count = 0
    for i in range(len(pre_y)):
        if pre_y[i] >= 0.5 and real_y[i] == 1:
            count += 1
        if pre_y[i] < 0.5 and real_y[i] == 0:
            count += 1
    return round(float(count/len(res)), 2)
