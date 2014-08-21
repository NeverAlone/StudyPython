# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-18 18:36:40
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
wx.TextCtrl的单行例子
"""


import wx


class TextFrame(wx.Frame):

    """docstring for TextFrame"""

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Text Entry Example",
                          size=(300, 100))
        panel = wx.Panel(self, -1)
        basicLabel = wx.StaticText(panel, -1, "Basic Control:")
        basicText = wx.TextCtrl(panel, -1, "I've entered some text!",
                                size=(175, -1))
        basicText.SetInsertionPoint(0)
        pwdLabel = wx.StaticText(panel, -1, "Password:")
        pwdText = wx.TextCtrl(panel, -1, "password",
                              size=(175, -1), style=wx.TE_PASSWORD)
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basicLabel, basicText, pwdLabel, pwdText])
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()

# This is the end
