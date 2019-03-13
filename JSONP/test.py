# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:01:38 2018

@author: Lidh
"""
import numpy as np
import xlrd
import uuid
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import matplotlib.pyplot as plt
from util import gx_network
def predict(x_data,url_base):
    network=gx_network.GX_network()
    network.load_network(url_base)
    return network.predict(x_data)
def train_two(x_data,y_data,base_dir):
    network=gx_network.GX_network()
    network.load_network(base_dir)
    loss=network.train(x_data,y_data,2)
    network.save_network(base_dir)
    return loss
def train_one(x_data,y_data,base_dir,learn_rate,layers,train_epoches,fun,greedy):
    x_data=np.array(x_data)
    y_data=np.array(y_data)
    structs={'input_ps':x_data[0].size,'learn_rate':learn_rate,"fun":fun,"layers":layers}
    network=gx_network.GX_network()
    network.createNetwork(structs,1)
    loss = 0
    if greedy==0:
        loss=network.train(x_data,y_data,train_epoches,True)
    else:
        loss=network.train(x_data,y_data,-1,True)
    network.save_network(base_dir)
    return loss

def getModelPath():
    path = os.getcwd()
    path = path + "\\model\\"+str(uuid.uuid4())
    if not os.path.exists(path):
        os.makedirs(path)
    return path+"\\model"

def getJson(data):
    x_data=np.array(data['x_data'])
    mode=data['mode']
    if mode=='train_one':
        base_dir=getModelPath()
        y_data=np.array(data['y_data'])
        if len(y_data.shape)==1:
            y_data = np.transpose([y_data])
        learn_rate=float(data['learn_rate'])
        train_epoches=int(data['train_epoches'])
        layers=np.array(data['layers'])
        greedy = int(data["greedy"])
        fun=data['fun']
        print("layers=" + str(layers))
        print("fun = " + str(fun))
        res=train_one(x_data,y_data,base_dir,learn_rate,layers,train_epoches,fun,greedy)
        res={'result':res,"modelPath":base_dir}
        return res
    elif mode=='train_two':
        y_data=np.array(data['y_data'])
        train_epoches=int(data['train_epoches'])
        res=train_two(x_data,y_data,base_dir,train_epoches)
        res={'result':res}
        return res
    elif mode=='predict':
        base_dir=data["modelPath"]
        res=predict(x_data,base_dir)
        result=np.array(res[:,0]).astype(np.str)
        res={'result':list(result)}
        return res
    else:
        return {'result':'please set right mode!'}