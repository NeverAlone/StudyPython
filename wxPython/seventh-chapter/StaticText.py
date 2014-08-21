# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-18 17:59:29
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
如何使用静态文本的一个基本例子
"""


import wx


class StaticTextFrame(wx.Frame):

    """docstring for StaticTextFrame"""

    def __init__(self):
        super(StaticTextFrame, self).__init__(None, -1, 'Static Text Example',
                                              size=(400, 300))

        panel = wx.Panel(self, -1)

        wx.StaticText(panel, -1, "This is an example of static text",
                     (100, 10))

        rev = wx.StaticText(panel, -1, "Static Text With Reversed Colors",
                           (100, 30))

        rev.SetForegroundColour('White')

        rev.SetBackgroundColour('Black')

        center = wx.StaticText(panel, -1, "align center",
                              (100, 50), (160, -1), wx.ALIGN_CENTER)
        center.SetForegroundColour('White')
        center.SetBackgroundColour('Black')

        right = wx.StaticText(panel, -1, "align right",
                             (100, 70), (160, -1), wx.ALIGN_RIGHT)
        right.SetForegroundColour("White")
        right.SetBackgroundColour("Black")

        strings = "You can also change the font."
        text = wx.StaticText(panel, -1, strings, (20, 100))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)

        wx.StaticText(panel, -1, "Your text\ncan be split\n"
                      "over multiple lines\n\neven blank ones", (20, 150))

        wx.StaticText(panel, -1, "Multi-lines text\ncan also\n"
                      "be right aligned\n\neven with a blank", (220, 150),
                      style=wx.ALIGN_RIGHT)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = StaticTextFrame()
    frame.Show()
    app.MainLoop()

# This is the end
