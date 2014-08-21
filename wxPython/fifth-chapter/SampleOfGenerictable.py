# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-17 16:48:52
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
使用这通用的表来显示阵容
"""


import wx
import wx.grid
import generictable


data = (("Bob", "Dernier"), ("Ryne", "Sandberg"),
        ("Gary", "Matthews"), ("Leon", "Durham"),
        ("Keith", "Moreland"), ("Ron", "Cey"),
        ("Jody", "Davis"), ("Larry", "Bowa"),
        ("Rick", "Sutcliffe"))

colLabels = ("Last", "First")
rowLabels = ("CF", "2B", "LF", "1B", "RF", "3B", "C", "SS", "P")


class SimpleGrid(wx.grid.Grid):

    """
    docstring for SimpleGrid
    """

    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        tableBase = generictable.GenericTable(data, rowLabels,
                                              colLabels)
        self.SetTable(tableBase)


class TestFrame(wx.Frame):

    """
    """

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid",
                          size=(275, 275))
        grid = SimpleGrid(self)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()


# This is the end
