# -*- coding: utf-8 -*-
"""
    docstring for hello_wxPython.py
"""
import wx
# from wx import *  # wxPython模块的导入顺序

"""
# wxPython必须有一个 应用程序对象（application)
# 和 框架对象 （frame）
"""


class App(wx.App):  # 子类化wxPython应用程序类
    """docstring for  App"wx.App)__init__(self, arg):
        super( App,wx.App)_init__()
        self.arg = arg
    """

    def OnInit(self):  # 定义一个应用程序的初始化方法
        frame = wx.Frame(parent=None, title='Hello WxPython!')
        frame.Show()
        return True

app = App()  # 创建一个应用程序类的
app.MainLoop()  # 进入应用程序的主事件循环
