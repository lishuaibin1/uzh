# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 14:20
# @Author  : Mr.Li

class ExcelLine:
    caseID = 0
    URL = 2
    Data = 3
    Expect = 4
    Result = 5

    def getCaseID(self):
        """获取caseID列"""
        return ExcelLine.caseID

    def getURL(self):
        """获取URL列"""
        return ExcelLine.URL

    def getData(self):
        """获取请求参数列"""
        return ExcelLine.Data

    def getExpect(self):
        """获取期望结果列"""
        return ExcelLine.Expect

    def getResult(self):
        """获取实际结果列"""
        return ExcelLine.Result

