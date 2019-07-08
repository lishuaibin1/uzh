# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 11:27
# @Author  : Mr.Li

import requests
import json


data = {'phone':'13572597243', 'password':'000000'}

def getHeadersValue():
    """获取请求头"""
    headers = {'Authorization': 'Bearer ' + sdff()}
    print(headers)
    return headers

def sdff():
    r = requests.post(url='http://test.api.uzh.cn/site/user-login',
                      data=data)
    print(r.json()['data']['token'])
    return r.json()['data']['token']


def sdf():
    r = requests.get(url='http://test.api.uzh.cn/order/receiving-order?page=1&per-page=50',
                     headers=getHeadersValue())
    print(r.text)
sdf()