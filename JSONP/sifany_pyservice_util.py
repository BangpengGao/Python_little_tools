# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:22:16 2018

@author: lidh
"""



from flask import Response

import json

def get_response(data):
    response = Response(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
    response.headers['Access-Control-Allow-Origin'] = '*',
    return response

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


