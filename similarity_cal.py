# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-04-25 09:43:35
# @Last Modified by:   Bangpeng Gao
# @Last Modified time: 2019-05-28 10:49:36

import numpy as np


def euclidean_distance(x, y):
    return np.sqrt(np.sum(np.square(x-y)))


def cos_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))


def pearson_similarity(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_ = x-x_mean
    y_ = y-y_mean
    return (np.sum((x_)*(y_)))/(np.sqrt(np.sum(pow(x_,2)))*np.sqrt(np.sum(pow(y_,2))))


if __name__ == '__main__':
    x = np.array([1,2,3,4,5,6])
    y = np.array([1,2,3,4,5,6])
    print(euclidean_distance(x, y))
    print(cos_similarity(x, y))
    print(pearson_similarity(x,y))