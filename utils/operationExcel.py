# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:06
# @Author  : Mr.Li

import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_line import *

class OperationExcel(ExcelLine):

    def getExcel(self):
        db = xlrd.open_workbook(data_dir('data', 'data.xls'))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        """获取Excel行数"""
        return self.getExcel().nrows

    def get_row_line(self, row, line):
        """
        :param row: 行
        :param line: 列
        :return: 获取单元格的内容
        """
        return self.getExcel().cell_value(row, line)

    def get_url(self, row):
        """获取请求地址"""
        return self.get_row_line(row, self.getURL())

    def get_data(self, row):
        """获取请求参数"""
        return self.get_row_line(row, self.getData())

    def get_Expect(self, row):
        """获取期望结果"""
        return self.get_row_line(row, self.getExpect())

    def get_result(self, row):
        """获取实际结果"""
        return self.get_row_line(row, self.getResult())

    def writeResult(self, row, content):
        """测试结果写到文件中"""
        work = xlrd.open_workbook(data_dir('data', 'data.xls'))     # 获取到Excel文档
        old_content = copy(work)            # 复制Excel文档
        ws = old_content.get_sheet(0)       # sheet为零
        ws.write(row, self.getResult(), content)       # 写入内容传参(row=行,self.getResult()=列,content=要写入的内容)
        old_content.save(data_dir('data', 'data.xls'))  # 保存到Data.xls中

    def getSuccess(self):
        """获取成功的用例数"""
        pass_count = []
        for i in range(1, self.get_rows()):
            if self.get_result(i) == 'pass':
                pass_count.append(i)
        return len(pass_count)

    def getFail(self):
        return ((self.get_rows()-1)-self.getSuccess())

    def run_pass_rate(self):
        """测试结果通过率"""
        # return str(int(self.getSuccess()/(self.get_rows()-1))*100)+'%'
        rate = '100%'
        if self.getFail() == 0:
            return rate
        elif self.getFail() != 0:
            rate = str(int(self.getSuccess()/(self.get_rows()-1)*100))+'%'
            return rate
