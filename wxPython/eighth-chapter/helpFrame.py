# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-20 09:12:38
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
Help Frame
"""


import wx


class HelpFrame(wx.Frame):

    """docstring for HelpFrame"""

    def __init__(self):
        pre = wx.PreFrame()  # 预构建对象
        pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
        pre.Create(None, -1, "Help Context", size=(300, 100),
                   style=wx.DEFAULT_FRAME_STYLE ^
                  (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))  # 创建框架
        self.PostCreate(pre)  # 底层C++指针的传递


if __name__ == '__main__':
    app = wx.PySimpleApp()
    HelpFrame().Show()
    app.MainLoop()

# This is the end
