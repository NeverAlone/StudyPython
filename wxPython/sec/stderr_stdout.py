# -*- coding: utf-8 -*-

"""
    重定向
"""


import wx
import sys


class Frame(wx.Frame):
    """docstring for Frame"""
    def __init__(self, parent, id, title):
        print "Frame.__init__"
        wx.Frame.__init__(self, parent, id, title)


class App(wx.App):
    """docstring for App"""

    def __init__(self, redirect=True, filename=None):
        print "App.__init__"
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print "App.OnInit"   # 输出到stdout
        self.frame = Frame(parent=None, id=-1, title='Startup')  # 创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print>>sys.stderr, "A pretend error message"  # 输出到ststderr
        return True

    def OnExit(self):
        print "OnExit"

if __name__ == '__main__':
    # app = App(redirect=False)  # 文本重定向从这里开始
    app = App(True, "output.txt")  # 所有的应用程序创建后的输出重定向到名为output的文件中
    print "before MainLoop"
    app.MainLoop()  # 进入主事件循环
    print "after MainLoop"


# This is the end
