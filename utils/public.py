# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:09
# @Author  : Mr.Li

import os

def data_dir(data='data', filename=None):
    """
    :param data: 所在文件夹名称
    :param filename: 文件名称
    :return: 文件路径
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), data, filename)
