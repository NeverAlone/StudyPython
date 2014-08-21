# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-17 18:49:27
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
AbstractModel
用于更新视图的一个自定义的模型
"""


class AbstractModel(object):

    """
    docStrings for AbstractModel
    """

    def __init__(self):
        self.listeners = []

    def addListener(self, listenerFunc):
        self.listeners.append(listenerFunc)

    def removeListener(self, listenerFunc):
        self.listeners.remove(listenerFunc)

    def update(self):
        for eachFunc in self.listeners:
            eachFunc(self)  # This is the end

# This is the end
