# -*- coding: utf-8 -*-
"""
Created on Mon May  7 09:30:00 2018

@author: lidh
#ERP分析-最大利益模型
"""
import numpy as np
def _EQ(p_array,C,P,S,Q):
    Co=C-S
    Cu=P-C
    nrows=p_array.shape[0]
    profit=0
    for i in range(nrows):
        if Q>p_array[i,0]:
            profit=profit+(Cu*p_array[i,0]-Co*(Q-p_array[i,0]))*p_array[i,1]
        else:
            profit=profit+Cu*Q*p_array[i,1]
    return profit
def gx_max_profit(p_array,C,P,S):
    res=[];
    for i in p_array[:,0]:
        t=_EQ(p_array,C,P,S,i)
        res.append([i,t])
    return np.array(res)
