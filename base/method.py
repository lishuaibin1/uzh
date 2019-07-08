# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 17:22
# @Author  : Mr.Li

import requests
from utils.operationExcel import *
from utils.operationJson import *
from utils.excel_line import *
from page.uzh import *


excel1 = OperationExcel()
def checkHeader(row, f1, f2):
    """
    检测请求头
    :param f1:请求头
    :param f2:请求头
    4,5是拆分URL后关键部分的索引
    要给封装post方法请求头加上参数
    """
    url = excel1.get_url(row=row)
    url = url.split('/')
    if url['4'] == 'sdfsfsdfasf':
        return f1
    elif url['5'] == 'dsfwfdfssd':
        return f2

# def post(self,row,data):
# 	try:
# 		r=requests.post(
# 			url=self.excel.getUrl(row=row),
# 			data=data,
# 			headers=checkHeader(
# 				row=row,
# 				f1=getHeadersValue(),
# 				f2=getHeadersInfo()),
# 				timeout=6)
# 		return r
# 	except Exception as e:
# 		raise  RuntimeError('接口请求发生未知的错误')

class Method:

    def __init__(self):
        #self.operationJson1 = OperationJson()
        self.excel = OperationExcel()
        self.excel_line = ExcelLine()

    # def post(self, row):
    #     """对于请求参数不变封装的方法"""
    #     try:
    #         r = requests.post(url=self.excel.get_url(row=row),
    #                           data=self.operationJson.getRequestData(row=row),
    #                           timeout=6)
    #         return r
    #     except Exception as e:
    #         raise RuntimeError('接口请求发生未知错误')

    def post(self, row, data):
        """对于变化的请求参数封装的方法，data参数直接调用setSo()方法，传参"""
        try:
            r = requests.post(url=self.excel.get_url(row=row),
                              data=data,
                              timeout=6)
            return r

        except Exception as e:
            raise RuntimeError('接口请求发生未知错误')

    def get(self, url):
        r = requests.get(url=url, headers=getHeadersValue())
        return r