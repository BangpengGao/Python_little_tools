# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:22:16 2018

@author: lidh
"""



from flask import Flask,request
import sifany_pyservice_util as spu
app=Flask(__name__)
import test
import json

@app.route("/network",methods=["GET","POST"])
def gx_network():
    data = request.args;
    return "successCallback"+"("+json.dumps(test.getJson(eval(list(data)[1])))+")"#将结果以json形式返回，通过jsonp与前台交互
    # return spu.get_response(test.getJson(eval(list(data)[1])))

if __name__ == '__main__':
    app.run(processes=0,threaded=True,debug=False)