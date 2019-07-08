# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 17:02
# @Author  : Mr.Li

from utils.operationJson import *
from utils.operationExcel import *
from utils.public import *
import json

OperationJson = OperationJson()
excel2 = OperationExcel()

def setSo(phone='13572597243', password='000000'):
    """对搜索的数据从新赋值,对请求参数关键字(变量部分)进行重新赋值"""
    dic1 = OperationJson.getRequestData(row=1)
    dic1['phone'] = phone
    dic1['password'] = password
    return dic1

def writeOrderID(content):
    """
    把上下关联的数据写到文件中
    :param content: 写入文件的内容
    :return: 
    """""
    with open(data_dir(filename='OrderID'), 'w') as f:
        f.write(content)

# def example():        # 示例
#     """
#     1.创建一个列表将获取的数据放到列表中，然后调用上面写入的方法(writePositionID())将数据写到文件中去（如果列表数据格式不多可以进行序列化和反序列化）
#     2.此方法一般在tests文件中，写在这里是为了更好的说明问题
#     """
#     list1 = []
#     for i in range(0, 15):
#         positionID = r.json()[data]
#         list1.append(positionID)
#     writePositionID(list1)

def writeToken(content):
    """把token写入文件"""
    with open(data_dir(filename='token'), 'w') as f:
        f.write(content)

def getToken():
    """获取写入文件的信息"""
    with open(data_dir(filename='token'), 'r') as f:
        return f.read()

def getOrderID():
    """获取写入文件的信息"""
    with open(data_dir(filename='OrderID'), 'r') as f:
        return json.loads(f.read())
        # return f.read()        # 另一种情况


# def setPositionInfo():
#     """
#     上下关联 如：
#     1.请求搜索
#     2.搜索成功，服务端返回了数据
#     3.拿到返回数据中的职位ID
#     4.然后把职位ID当做参数一样传到职位详情的请求参数中
#     """
#     dict1 = OperationJson.getRequestData(row=2)
#     dict1['positionId'] = getOrderID()
#     print(dict1)

def geturls():
    url = excel2.get_url(row=2)
    list = []
    for OrderID in getOrderID():
        url = 'http://test.api.uzh.cn/order/details?order_id={0}&source=snatch_order'.format(OrderID)
        list.append(url)
    return list

def getHeadersValue():
    """获取请求头"""

    headers = {'Authorization': 'Bearer ' + getToken()}
    # print(getToken())
    # print(headers)
    return headers

