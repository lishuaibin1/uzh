# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 16:01
# @Author  : Mr.Li

import unittest
from base.method import Method
from page.uzh import *

class UzhLogin(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.excel = OperationExcel()


    def statusCode(self, r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['status'], 200)

    def test_001(self):
        """验证登录"""
        r = self.obj.post(1, data=setSo())
        writeToken(r.json()['data']['token'])
        self.statusCode(r=r)
        self.excel.writeResult(1, 'pass')

    def test_002(self):
        """验证获取待接单订单列表"""
        r = self.obj.get(url=self.excel.get_url(2))
        item_list = r.json()['data']["items"]
        list = []
        for dic in item_list:
            for key, value in dic.items():
                if key == 'id':
                    list.append(value)
                    writeOrderID(str(list))
        self.statusCode(r=r)
        self.excel.writeResult(2, 'pass')
        # list = []
        # for i in range(0, 2):
        #     orderID = r.json()['data']['items'][i]['id']
        #     list.append(orderID)
        # writeOrderID(json.dumps(list))

    def test_003(self):
        """验证访问所有的未接单的订单信息"""
        list = geturls()
        for i in list:
            r = self.obj.get(url=i)
            self.statusCode(r=r)
            self.excel.writeResult(3, 'pass')

    def test_004(self):
        """获取已接单订单"""
        r = self.obj.get(url=self.excel.get_url(4))
        # print(r.text)
        item_list = r.json()['data']["items"]
        list = []
        for dic in item_list:
            for key, value in dic.items():
                if key == 'id':
                    list.append(value)
                    writeOrderID(str(list))
        self.statusCode(r=r)
        self.excel.writeResult(4, 'pass')




if __name__ == '__main__':
    unittest.main(verbosity=2)
