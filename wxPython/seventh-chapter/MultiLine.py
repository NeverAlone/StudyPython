# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-19 07:31:19
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
创建一个多行文本控件
"""


import wx


class TextFrame(wx.Frame):

    """docstring for TextFrame"""

    def __init__(self):
        super(TextFrame, self).__init__(None, -1, "Text Entry Example",
                                        size=(300, 250))
        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1, 'Multi-line')
        multiText = wx.TextCtrl(panel, -1,
                                "Here is a long line of text set"
                                " on the control.\n\n"
                                "See that is wrapped,and that this line"
                                " is after a blank",
                                size=(200, 100),
                                style=wx.TE_MULTILINE)  # 创建一个文本控件
        multiText.SetInsertionPoint(0)  # 设置插入点

        richLabel = wx.StaticText(panel, -1, 'Rich Text')
        richText = wx.TextCtrl(panel, -1, "if supported by native control,"
                               "This is reversed, and this is a different font",
                               size=(200, 100),
                               style=wx.TE_MULTILINE | wx.TE_RICH2)
        # 创建富文本控件
        richText.SetInsertionPoint(0)
        richText.SetStyle(44, 52, wx.TextAttr("White", "Black"))
        points = richText.GetFont().GetPointSize()
        f = wx.Font(points + 3, wx.ROMAN, wx.ITALIC, wx.BOLD, True)
        # 创建一个字体
        richText.SetStyle(0, 82, wx.TextAttr("Blue", wx.NullColour, f))
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText, richLabel, richText])
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()




# This is the end
