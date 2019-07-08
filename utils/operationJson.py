# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:09
# @Author  : Mr.Li

import json
from utils.public import *
from utils.operationExcel import *

class OperationJson:

    def __init__(self):
        self.excel = OperationExcel()

    def getReadJson(self):
        with open(data_dir(filename='requestData.json'), encoding='utf-8') as f:
            data = json.load(f)
            return data

    def getRequestData(self, row):
        """获取请求参数"""
        return self.getReadJson()[self.excel.get_data(row=row)]

