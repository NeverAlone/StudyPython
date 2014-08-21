# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-20 08:28:58
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
第八章 基本框架
"""


import wx


class SubclassFrame(wx.Frame):

    """docstring for SubclassFrame"""

    def __init__(self):
        super(SubclassFrame, self).__init__(None, -1, "Frame Subclass",
                                            style=wx.FRAME_NO_TASKBAR |
                                            wx.DEFAULT_FRAME_STYLE,
                                            size=(300, 300))

        panel = wx.Panel(self, -1)
        button = wx.Button(panel, -1, "Close Me", pos=(15, 15))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = SubclassFrame()
    frame.Show()
    app.MainLoop()

# This is the end
