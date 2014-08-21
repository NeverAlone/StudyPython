# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-17 19:48:08
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
对模型例子进行单元测试的一个范例
"""


import unittest
import HowModelsWork
import wx


class TestExample(unittest.TestCase):  # 申明一个TestCase

    """docstring for TestExample"""

    def setUp(self):  # 为每个测试所做的配置
        self.app = wx.PySimpleApp()
        self.frame = HowModelsWork.ModelExample(parent=None, id=-1)

    def tearDown(self):  # 测试之后的清除工作
        self.frame.Destory()

    def testModel(self):  # 声明一个测试R
        self.frame.OnBarbey(None)
        self.assertEqual("Barney", self.frame.model.frist,
                         msg="First is wrong")
        self.assertEqual("Rubble", self.frame.model.last)


def suite():  # 创建一个TestSuite
    suite = unittest(TestExample, 'test')
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
# This is the end
